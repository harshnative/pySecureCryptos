import secrets
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import encoderDecoders
import hashers
import time
import verifier_fernetWrapper_v3




#  _                                                
# | | __   ___   _   _         __ _    ___   _ __   
# | |/ /  / _ \ | | | |       / _` |  / _ \ | '_ \  
# |   <  |  __/ | |_| |      | (_| | |  __/ | | | | 
# |_|\_\  \___|  \__, |       \__, |  \___| |_| |_| 
#                |___/        |___/                 


# method to generate RSA keys
# RSA key generation is expensive process , so keep size low on smaller machines
class KeyGenerator:

    # generate the key in constructor
    def __init__(self , size = 4096):

        # type checking the parameters
        if(type(size) != int):
            raise TypeError("size parameter expected to be of int type instead got {} type".format(type(size)))

        if(size % 256 != 0):
            raise ValueError("size parameter should be in multiple of 256 like 1028 , 2048 , 4096 etc")


        self.key = RSA.generate(size)

    # return the private key in byte
    def get_privateKey_bytes(self):
        private_key = self.key.export_key()
        return private_key

    # return private key in strings
    def get_privateKey_string(self):
        private_key = self.key.export_key()
        hexPrivateKey = encoderDecoders.HexConvertor.encode(private_key)
        return hexPrivateKey

    # return public key in bytes
    def get_publicKey_bytes(self):
        public_key = self.key.public_key().export_key()
        return public_key

    # return public key in strings
    def get_publicKey_string(self):
        public_key = self.key.public_key().export_key()
        hexpublicKey = encoderDecoders.HexConvertor.encode(public_key)
        return hexpublicKey


    










#                                               _                   
#   ___   _ __     ___   _ __   _   _   _ __   | |_    ___    _ __  
#  / _ \ | '_ \   / __| | '__| | | | | | '_ \  | __|  / _ \  | '__| 
# |  __/ | | | | | (__  | |    | |_| | | |_) | | |_  | (_) | | |    
#  \___| |_| |_|  \___| |_|     \__, | | .__/   \__|  \___/  |_|    
#                               |___/  |_|                          


class Encryptor:

    def __init__(self , publicKey , privateKey , keySize = 4096):

        # type checking the parameters
        if((type(publicKey) != str) and (type(publicKey) != bytes)):
            raise TypeError("publicKey parameter expected to be of str or bytes type instead got {} type".format(type(publicKey)))

        # type checking the parameters
        if((type(privateKey) != str) and (type(privateKey) != bytes)):
            raise TypeError("privateKey parameter expected to be of str or bytes type instead got {} type".format(type(privateKey)))
        
        # if the keys are in str format , convert them back to bytes
        if(type(publicKey) == str):
            publicKey = encoderDecoders.HexConvertor.decode(publicKey)
        if(type(privateKey) == str):
            privateKey = encoderDecoders.HexConvertor.decode(privateKey)

        # convert the keys to RSA type
        self.publicKey = RSA.import_key(publicKey)
        self.privateKey = RSA.import_key(privateKey)

        # init main encryptor decryptor module object
        self.cipherPublic = Cipher_PKCS1_v1_5.new(self.publicKey)
        self.cipherPrivate = Cipher_PKCS1_v1_5.new(self.privateKey)

        # chunk size
        self.chunkSize = keySize // 12

        # fernet password
        self.fernet_pass_byte = secrets.token_bytes(512)
        self.fernet_pass_string = encoderDecoders.HexConvertor.encode(self.fernet_pass_byte)
        
        # fernet key
        self.fernetKey = verifier_fernetWrapper_v3.Keys.getKey(self.fernet_pass_string)
        
        # encrypted fernet password
        self.enc_pass_byte = self.encrypt_byte(self.fernet_pass_byte)
        self.enc_pass_string = self.encrypt_string(self.fernet_pass_string)






    # function to encrypt a byte object
    # generator function
    def encrypt_byte_yield(self , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))
        
        chunkList = []
        len_byte = len(byte)

        currentCount = 1

        # number of chunks * 2 + checksum yield
        totalYield = (((len_byte // self.chunkSize) + 1) * 2) + (((len_byte // 2048) + 1) * 2)


        # divide data in chunks
        for i in range(0 , len_byte , self.chunkSize):
            chunkList.append(byte[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        
        result = b""

        # encrypt each chunk and join
        for i in chunkList:
            encChunk = self.cipherPublic.encrypt(i)
            result = result + encChunk + b":~:~:"

            yield currentCount , totalYield
            currentCount = currentCount + 1


        result = result[:-5]

        # get checksum
        genObj = hashers.SHA256(byte).get_byte_yield()

        while(True):
            try:
                _ , _ = next(genObj)

                yield currentCount , totalYield
                currentCount = currentCount + 1

            except StopIteration as ex:
                checksum = ex.value
                break
        
        # encrypt checksum
        encChecksum = self.cipherPublic.encrypt(checksum)

        # add checksum to result
        result = result + b":rsa_v2_checksum:" + encChecksum


        # complete the yield progress
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result
















    # function to decrypt the encrypted byte    
    def decrypt_byte_yield(self , enc_byte):

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise TypeError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))

        # seperate checksum
        enc_byte , checksum = enc_byte.split(b":rsa_v2_checksum:")

        # split into chunks
        chunkList = enc_byte.split(b":~:~:")

        currentCount = 1

        # number of chunks  + checksum yield
        totalYield = len(chunkList) + ((((len(chunkList) * self.chunkSize) // 2048) + 1) * 2)

        result = b""

        # decrypt each chunk and add to result
        for i in chunkList:
            dec_chunk = self.cipherPrivate.decrypt(i , None)
            result = result + dec_chunk

            yield currentCount , totalYield
            currentCount = currentCount + 1


        # get checksum of decrypted byte
        genObj = hashers.SHA256(result).get_byte_yield()

        while(True):
            try:
                _ , _ = next(genObj)

                yield currentCount , totalYield
                currentCount = currentCount + 1

            except StopIteration as ex:
                newChecksum = ex.value
                break

        # decrypt original checksum
        dec_checksum = self.cipherPrivate.decrypt(checksum , None)

        # check if original checksum and checksum from decrypted byte match or not
        if(newChecksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")

        # complete the yield progress
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result



















    # function to encrypt a string object
    # generator function
    def encrypt_string_yield(self , string):

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))
        
        
        chunkList = []
        len_string = len(string)

        currentCount = 1

        # number of chunks * 2 + checksum yield
        totalYield = (((len_string // self.chunkSize) + 1) * 2) + (((len_string // 2048) + 1) * 2)

        # divide data in chunks
        for i in range(0 , len_string , self.chunkSize):
            chunkList.append(string[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        byteFromString = b""
        
        result = ""

        # encrypt each chunk and join
        for i in chunkList:

            # convert the string chunk to bytes to encrypt
            i_byte = encoderDecoders.String2Byte.encode(i)

            # encrypt chunk
            encChunk = self.cipherPublic.encrypt(i_byte)

            # convertor encrypted chunk to bytes again
            encChunk_string = encoderDecoders.HexConvertor.encode(encChunk)

            result = result + encChunk_string + ":~:~:"
            byteFromString = byteFromString + i_byte

            yield currentCount , totalYield
            currentCount = currentCount + 1

        result = result[:-5]

        # get checksum
        genObj = hashers.SHA256(byteFromString).get_byte_yield()

        while(True):
            try:
                _ , _ = next(genObj)

                yield currentCount , totalYield
                currentCount = currentCount + 1

            except StopIteration as ex:
                checksum = ex.value
                break
        
        # encrypt checksum
        encChecksum = self.cipherPublic.encrypt(checksum)

        encChecksum_string = encoderDecoders.HexConvertor.encode(encChecksum)

        # add checksum to result
        result = result + ":rsa_v2_checksum:" + encChecksum_string

        # complete the yield progress
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result



    


















    # function to decrypt encrypted string
    def decrypt_string_yield(self , enc_string):

        # type checking the parameters
        if(type(enc_string) != str):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        # seperate checksum
        enc_string , checksum = enc_string.split(":rsa_v2_checksum:")

        # split into chunks
        chunkList = enc_string.split(":~:~:")

        currentCount = 1

        # number of chunks  + checksum yield
        totalYield = len(chunkList) + ((((len(chunkList) * self.chunkSize) // 2048) + 1) * 2)

        result = ""
        byteFromString = b""

        # decrypt each chunk and add to result
        for i in chunkList:
            
            # convert string chunk to byte
            chunk_byte = encoderDecoders.HexConvertor.decode(i)
            dec_chunk = self.cipherPrivate.decrypt(chunk_byte , None)

            # convert decrypted chunk back to string
            dec_chunk_string = encoderDecoders.String2Byte.decode(dec_chunk)

            result = result + dec_chunk_string
            byteFromString = byteFromString + dec_chunk

            yield currentCount , totalYield
            currentCount = currentCount + 1


        # get checksum of decrypted byte
        genObj = hashers.SHA256(byteFromString).get_byte_yield()

        while(True):
            try:
                _ , _ = next(genObj)

                yield currentCount , totalYield
                currentCount = currentCount + 1

            except StopIteration as ex:
                newChecksum = ex.value
                break
        
        # original checksum to byte
        checksum = encoderDecoders.HexConvertor.decode(checksum)

        # decrypt original checksum
        dec_checksum = self.cipherPrivate.decrypt(checksum , None)

        # check if original checksum and checksum from decrypted byte match or not
        if(newChecksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")

        # complete the yield progress
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result





    















    # function to encrypt a large byte object using multiprocessing
    # uses a 512 bit key fernet encryption and then attaches that key to result using rsa encryption
    # chunkSize in MB
    def encrypt_lbyte_yield(self , large_byte , chunkSize = 8):

        # type checking the parameters
        if(type(large_byte) != bytes):
            raise TypeError("large_byte parameter expected to be of bytes type instead got {} type".format(type(large_byte)))

        lenByte = len(large_byte)

        # chunk size in bytes
        bytes_chunkSize = chunkSize * 1024 * 1024


        # calc total yield
        currentCount = 0
        totalYield = (lenByte // bytes_chunkSize) + 1

        result = b""

        # encrypt each chunk using fernet
        for i in range(0 , lenByte , bytes_chunkSize):
            chunk = large_byte[i: i + bytes_chunkSize]
            enc_chunk = verifier_fernetWrapper_v3.Encryptor.main_encrypt_byte(chunk , self.fernetKey , chunkSize)
            
            result = result + enc_chunk + b"$~$~$"

            yield currentCount , totalYield
            currentCount = currentCount + 1

        result = result[:-5]


        # attack the enc fernet key to result
        result = result + b":rsa_v2_encKey:" + self.enc_pass_byte

        # complete yield if not
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result
















    # method to decyprt the byte encrypted using multi processing
    def decrypt_lbyte_yield(self , large_byte):

        # type checking the parameters
        if(type(large_byte) != bytes):
            raise TypeError("large_byte parameter expected to be of bytes type instead got {} type".format(type(large_byte)))

        # seperate fernet key and byte data
        large_byte , fernetPass = large_byte.split(b":rsa_v2_encKey:")

        # decrypt the fernet key and convert it to string
        dec_fernetPass = self.decrypt_byte(fernetPass)
        fernetPass_string = encoderDecoders.HexConvertor.encode(dec_fernetPass)
        
        # set fernet key as obj 
        fernetKey = verifier_fernetWrapper_v3.Keys.getKey(fernetPass_string)

        chunkList = large_byte.split(b"$~$~$")

        # calc total yield
        currentCount = 0
        totalYield = len(chunkList)

        result = b""

        # decrypt each chunk using fernet wrapper
        for i in chunkList:
            dec_chunk = verifier_fernetWrapper_v3.Encryptor.main_decrypt_byte(i , fernetKey)
            
            result = result + dec_chunk

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # complete yield if not
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result

















    # function to encrypt a large string object using multiprocessing
    # chunkSize size in MB
    def encrypt_lstring_yield(self , large_string , chunkSize = 4):

        # type checking the parameters
        if(type(large_string) != str):
            raise TypeError("large_string parameter expected to be of str type instead got {} type".format(type(large_string)))

        len_string = len(large_string)
        
        # chunk size in bytes
        bytes_chunkSize = chunkSize * 1024 * 1024
        
        # calc total yield
        currentCount = 0
        totalYield = (len_string // bytes_chunkSize) + 1

        result = ""

        # decrypt each chunk using fernet wrapper v3 
        for i in range(0 , len_string , bytes_chunkSize):
            chunk = large_string[i: i + bytes_chunkSize]
            enc_chunk = verifier_fernetWrapper_v3.Encryptor.main_encrypt_string(chunk , self.fernetKey , chunkSize)
            
            result = result + enc_chunk + "$~$~$"

            yield currentCount , totalYield
            currentCount = currentCount + 1

        result = result[:-5]


        # add encrypted fernet key to end
        result = result + ":rsa_v2_encKey:" + self.enc_pass_string


        # complete yield if not
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result















    # function to decrypt a large string object using multi processing
    def decrypt_lstring_yield(self , large_string):

        # type checking the parameters
        if(type(large_string) != str):
            raise TypeError("large_string parameter expected to be of str type instead got {} type".format(type(large_string)))

        # seperate out fernet key
        large_string , fernetPass = large_string.split(":rsa_v2_encKey:")

        # decrypt key and set as obj
        dec_fernetPass = self.decrypt_string(fernetPass)
        fernetKey = verifier_fernetWrapper_v3.Keys.getKey(dec_fernetPass)

        chunkList = large_string.split("$~$~$")

        # calc total yield
        currentCount = 0
        totalYield = len(chunkList)

        result = ""

        # decrypt each chunk
        for i in chunkList:
            dec_chunk = verifier_fernetWrapper_v3.Encryptor.main_decrypt_string(i , fernetKey)
            
            result = result + dec_chunk

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # complete yield if not 
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return result



    














    # function to encrypt a byte object
    def encrypt_byte(self , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))
        
        chunkList = []
        len_byte = len(byte)

        # divide data in chunks
        for i in range(0 , len_byte , self.chunkSize):
            chunkList.append(byte[i : i+self.chunkSize])
        
        result = b""

        # encrypt each chunk and join
        for i in chunkList:
            encChunk = self.cipherPublic.encrypt(i)
            result = result + encChunk + b":~:~:"

        result = result[:-5]

        # get checksum
        checksum = hashers.SHA256(byte).get_byte()
        
        # encrypt checksum
        encChecksum = self.cipherPublic.encrypt(checksum)

        # add checksum to result
        result = result + b":rsa_v2_checksum:" + encChecksum

        return result
















    # function to decrypt the encrypted byte    
    def decrypt_byte(self , enc_byte):

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise TypeError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))

        # seperate checksum
        enc_byte , checksum = enc_byte.split(b":rsa_v2_checksum:")

        # split into chunks
        chunkList = enc_byte.split(b":~:~:")

        result = b""

        # decrypt each chunk and add to result
        for i in chunkList:
            dec_chunk = self.cipherPrivate.decrypt(i , None)
            result = result + dec_chunk

        # get checksum of decrypted byte
        newChecksum = hashers.SHA256(result).get_byte()

        # decrypt original checksum
        dec_checksum = self.cipherPrivate.decrypt(checksum , None)

        # check if original checksum and checksum from decrypted byte match or not
        if(newChecksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")

        return result


















    # function to encrypt a string object
    def encrypt_string(self , string):

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))
        
        
        chunkList = []
        len_string = len(string)

        # divide data in chunks
        for i in range(0 , len_string , self.chunkSize):
            chunkList.append(string[i : i+self.chunkSize])

        byteFromString = b""
        
        result = ""

        # encrypt each chunk and join
        for i in chunkList:

            # convert the string chunk to bytes to encrypt
            i_byte = encoderDecoders.String2Byte.encode(i)

            # encrypt chunk
            encChunk = self.cipherPublic.encrypt(i_byte)

            # convertor encrypted chunk to bytes again
            encChunk_string = encoderDecoders.HexConvertor.encode(encChunk)

            result = result + encChunk_string + ":~:~:"
            byteFromString = byteFromString + i_byte

        result = result[:-5]

        # get checksum
        checksum = hashers.SHA256(byteFromString).get_byte()

        # encrypt checksum
        encChecksum = self.cipherPublic.encrypt(checksum)

        encChecksum_string = encoderDecoders.HexConvertor.encode(encChecksum)

        # add checksum to result
        result = result + ":rsa_v2_checksum:" + encChecksum_string

        return result



















    
    def decrypt_string(self , enc_string):

        # type checking the parameters
        if(type(enc_string) != str):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        # seperate checksum
        enc_string , checksum = enc_string.split(":rsa_v2_checksum:")

        # split into chunks
        chunkList = enc_string.split(":~:~:")

        result = ""
        byteFromString = b""

        # decrypt each chunk and add to result
        for i in chunkList:
            
            # convert string chunk to byte
            chunk_byte = encoderDecoders.HexConvertor.decode(i)
            dec_chunk = self.cipherPrivate.decrypt(chunk_byte , None)

            # convert decrypted chunk back to string
            dec_chunk_string = encoderDecoders.String2Byte.decode(dec_chunk)

            result = result + dec_chunk_string
            byteFromString = byteFromString + dec_chunk

        # get checksum of decrypted byte
        newChecksum = hashers.SHA256(byteFromString).get_byte()
        
        # original checksum to byte
        checksum = encoderDecoders.HexConvertor.decode(checksum)

        # decrypt original checksum
        dec_checksum = self.cipherPrivate.decrypt(checksum , None)

        # check if original checksum and checksum from decrypted byte match or not
        if(newChecksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")

        return result









































#  _                  _                       _                                                
# | |_    ___   ___  | |_                    | | __   ___   _   _         __ _    ___   _ __   
# | __|  / _ \ / __| | __|       _____       | |/ /  / _ \ | | | |       / _` |  / _ \ | '_ \  
# | |_  |  __/ \__ \ | |_       |_____|      |   <  |  __/ | |_| |      | (_| | |  __/ | | | | 
#  \__|  \___| |___/  \__|                   |_|\_\  \___|  \__, |       \__, |  \___| |_| |_| 
#                                                           |___/        |___/                 


def __test_keyGen():

    keyGenObj = KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_string = keyGenObj.get_privateKey_string()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_string = keyGenObj.get_publicKey_string()

    print(f"\nprivateKey_bytes len = {len(privateKey_bytes)}")
    print(f"\nprivateKey_string len = {len(privateKey_string)}")
    print(f"\npublicKey_bytes len = {len(publicKey_bytes)}")
    print(f"\npublicKey_string len = {len(publicKey_string)}")














def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()












#  _                  _                       _               _           
# | |_    ___   ___  | |_                    | |__    _   _  | |_    ___  
# | __|  / _ \ / __| | __|       _____       | '_ \  | | | | | __|  / _ \ 
# | |_  |  __/ \__ \ | |_       |_____|      | |_) | | |_| | | |_  |  __/ 
#  \__|  \___| |___/  \__|                   |_.__/   \__, |  \__|  \___| 
#                                                     |___/               


def __test_encryptor_byte_yield():

    print("generating key")
    keyGenObj = KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_string = keyGenObj.get_privateKey_string()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_string = keyGenObj.get_publicKey_string()

    print("making obj")
    encObj = Encryptor(publicKey_bytes , privateKey_bytes)

    myByte = b"hello world" * 12345

    print(f"encrypting byte of len = {len(myByte)}")


    genObj = encObj.encrypt_byte_yield(myByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    print(f"encryptedByte len = {len(encryptedByte)}")

    
    genObj = encObj.decrypt_byte_yield(encryptedByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    print(f"decryptedByte len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")


    # test with string keys
    print("making obj")
    encObj = Encryptor(publicKey_string , privateKey_string)
    
    genObj = encObj.decrypt_byte_yield(encryptedByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    print(f"decryptedByte len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")

    print("done")
    








def __test_encryptor_byte():

    print("generating key")
    keyGenObj = KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_string = keyGenObj.get_privateKey_string()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_string = keyGenObj.get_publicKey_string()

    print("making obj")
    encObj = Encryptor(publicKey_bytes , privateKey_bytes)

    myByte = b"hello world"

    print(f"encrypting byte of len = {len(myByte)}")


    encryptedByte = encObj.encrypt_byte(myByte)

    print(f"encryptedByte = {encryptedByte} len = {len(encryptedByte)}")

    
    decryptedByte = encObj.decrypt_byte(encryptedByte)

    print(f"decryptedByte = {decryptedByte} len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")


    # test with string keys
    print("making obj")
    encObj = Encryptor(publicKey_string , privateKey_string)
    
    decryptedByte = encObj.decrypt_byte(encryptedByte)

    print(f"decryptedByte = {decryptedByte} len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")

    print("done")
















#  _                  _                             _            _                  
# | |_    ___   ___  | |_                     ___  | |_   _ __  (_)  _ __     __ _  
# | __|  / _ \ / __| | __|       _____       / __| | __| | '__| | | | '_ \   / _` | 
# | |_  |  __/ \__ \ | |_       |_____|      \__ \ | |_  | |    | | | | | | | (_| | 
#  \__|  \___| |___/  \__|                   |___/  \__| |_|    |_| |_| |_|  \__, | 
#                                                                            |___/  


def __test_encryptor_string_yield():

    print("generating key")
    keyGenObj = KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_string = keyGenObj.get_privateKey_string()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_string = keyGenObj.get_publicKey_string()

    print("making obj")
    encObj = Encryptor(publicKey_bytes , privateKey_bytes)

    myString = "hello world" * 12345

    print(f"encrypting string of len = {len(myString)}")


    genObj = encObj.encrypt_string_yield(myString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    print(f"encryptedString len = {len(encryptedString)}")

    
    genObj = encObj.decrypt_string_yield(encryptedString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print(f"decryptedString len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")


    
    # testing with string key 
    print("making obj")

    encObj = Encryptor(publicKey_string , privateKey_string)
    genObj = encObj.decrypt_string_yield(encryptedString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print(f"decryptedString len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")

    print("done")
    















def __test_encryptor_string():

    print("generating key")
    keyGenObj = KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_string = keyGenObj.get_privateKey_string()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_string = keyGenObj.get_publicKey_string()

    print("making obj")
    encObj = Encryptor(publicKey_bytes , privateKey_bytes)

    myString = "hello world"

    print(f"encrypting string of len = {len(myString)}")


    encryptedString = encObj.encrypt_string(myString)

    print(f"encryptedString = {encryptedString} len = {len(encryptedString)}")

    
    decryptedString = encObj.decrypt_string(encryptedString)

    print(f"decryptedString = {decryptedString} len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")


    
    # testing with string key 
    print("making obj")

    encObj = Encryptor(publicKey_string , privateKey_string)
    decryptedString = encObj.decrypt_string(encryptedString)

    print(f"decryptedString = {decryptedString} len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")

    print("done")
    




def __test_time_byte():

    print("starting")

    keyGenObj = KeyGenerator()

    publicKey = keyGenObj.get_publicKey_bytes()
    privateKey = keyGenObj.get_privateKey_string()

    enc_obj = Encryptor(publicKey , privateKey)

    n = 1024 * 1024 // 2
    toenc = b"h" * n

    start = time.perf_counter()

    enc = enc_obj.encrypt_byte(toenc)
    # dec = Encryptor.main_decrypt_byte(enc , key)

    end = time.perf_counter()

    print(len(enc))
    # print(len(dec))

    # print(toenc == dec)


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , len(toenc) / 1024 / 1024))




















#  _                  _                       _                                              _         _  
# | |_    ___   ___  | |_                    | |   __ _   _ __    __ _    ___         ___   | |__     (_) 
# | __|  / _ \ / __| | __|       _____       | |  / _` | | '__|  / _` |  / _ \       / _ \  | '_ \    | | 
# | |_  |  __/ \__ \ | |_       |_____|      | | | (_| | | |    | (_| | |  __/      | (_) | | |_) |   | | 
#  \__|  \___| |___/  \__|                   |_|  \__,_| |_|     \__, |  \___|       \___/  |_.__/   _/ | 
#                                                                |___/                              |__/  


def __test_encrypt_lByte():

    print("generating key")
    keyGenObj = KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_string = keyGenObj.get_privateKey_string()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_string = keyGenObj.get_publicKey_string()

    print("making obj")
    encObj = Encryptor(publicKey_bytes , privateKey_bytes)

    # 64 Mb of data
    myByte = b"h" * 1024 * 1024 * 64

    print(f"encrypting byte of len = {len(myByte)}")


    genObj = encObj.encrypt_lbyte_yield(myByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    print(f"encryptedByte len = {len(encryptedByte)}")

    
    genObj = encObj.decrypt_lbyte_yield(encryptedByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    print(f"decryptedByte len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")


    # test with string keys
    print("making obj")
    encObj = Encryptor(publicKey_string , privateKey_string)
    
    genObj = encObj.decrypt_lbyte_yield(encryptedByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    print(f"decryptedByte len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")

    print("done")
    










def __test_encryptor_lstring():

    print("generating key")
    keyGenObj = KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_string = keyGenObj.get_privateKey_string()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_string = keyGenObj.get_publicKey_string()

    print("making obj")
    encObj = Encryptor(publicKey_bytes , privateKey_bytes)

    # 48 mb of data
    myString = "h" * 1024 * 1024 * 48

    print(f"encrypting string of len = {len(myString)}")


    genObj = encObj.encrypt_lstring_yield(myString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    print(f"encryptedString len = {len(encryptedString)}")

    
    genObj = encObj.decrypt_lstring_yield(encryptedString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print(f"decryptedString len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")


    
    # testing with string key 
    print("making obj")

    encObj = Encryptor(publicKey_string , privateKey_string)
    genObj = encObj.decrypt_lstring_yield(encryptedString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print(f"decryptedString len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")

    print("done")








if __name__ == "__main__":
    # __test_encryptor_byte_yield()
    # __test_encryptor_string_yield()
    # __test_encryptor_byte()
    # __test_encryptor_string()
    # __test_time_byte()
    # __test_encrypt_lByte()
    __test_encryptor_lstring()