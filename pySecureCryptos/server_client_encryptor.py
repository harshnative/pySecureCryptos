from Cryptodome.Signature import pss as Cipher_pss
from Cryptodome.PublicKey import RSA
from .encoderDecoders import *
from .hashers_v2 import *
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from typing import Union
import secrets
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256 as Cryptodome_SHA256







#  _                                                
# | | __   ___   _   _         __ _    ___   _ __   
# | |/ /  / _ \ | | | |       / _` |  / _ \ | '_ \  
# |   <  |  __/ | |_| |      | (_| | |  __/ | | | | 
# |_|\_\  \___|  \__, |       \__, |  \___| |_| |_| 
#                |___/        |___/                 





# key size , avgtime , max time , min time
# 1024 , 0.13045738699438517 , 0.41157023099367507 , 0.044456824980443344
# 2048 , 0.6016242760029854 , 1.5902376979938708 , 0.09847884299233556
# 3072 , 1.8595398340024984 , 3.205021528992802 , 0.6348795160010923
# 4096 , 4.65693292079086 , 10.478919560002396 , 0.7353818640112877
# 5120 , 11.271185925399186 , 20.71055350798997 , 4.2160446449997835
# 6144 , 22.94962278229941 , 41.116515233006794 , 4.3491839109919965

# method to generate RSA keys
# RSA key generation is expensive process , so keep size low on smaller machines
class KeyGenerator:

    # generate the key in constructor
    def __init__(self , size : int = 4096):

        # type checking the parameters
        if(type(size) != int):
            raise TypeError("size parameter expected to be of int type instead got {} type".format(type(size)))

        if(size % 256 != 0):
            raise ValueError("size parameter should be in multiple of 256 like 1028 , 2048 , 4096 etc")


        self.key = RSA.generate(size)

    # return the private key in byte
    def get_privateKey_bytes(self) -> bytes:
        private_key = self.key.export_key()
        return private_key

    # return private key in strings
    def get_privateKey_string(self) -> str:
        private_key = self.key.export_key()
        hexPrivateKey = HexConvertor.encode(private_key)
        return hexPrivateKey

    # return public key in bytes
    def get_publicKey_bytes(self) -> bytes:
        public_key = self.key.public_key().export_key()
        return public_key

    # return public key in strings
    def get_publicKey_string(self) -> str:
        public_key = self.key.public_key().export_key()
        hexpublicKey = HexConvertor.encode(public_key)
        return hexpublicKey


    

















#  _____                                         _                   
# | ____|  _ __     ___   _ __   _   _   _ __   | |_    ___    _ __  
# |  _|   | '_ \   / __| | '__| | | | | | '_ \  | __|  / _ \  | '__| 
# | |___  | | | | | (__  | |    | |_| | | |_) | | |_  | (_) | | |    
# |_____| |_| |_|  \___| |_|     \__, | | .__/   \__|  \___/  |_|    
#                                |___/  |_|                          


class Encryptor:


    # public key of receiver / client
    # private key of sender / server
    # chunk size in MB - for AES encryption
    def __init__(self , publicKey : Union[str , bytes] , privateKey : Union[str , bytes] , keySize : int = 4096 , chunkSize : int = 16):

        # type checking the parameters
        if(type(publicKey) not in (str , bytes)):
            raise TypeError("publicKey parameter expected to be of str or bytes type instead got {} type".format(type(publicKey)))

        if(type(privateKey) not in (str , bytes)):
            raise TypeError("privateKey parameter expected to be of str or bytes type instead got {} type".format(type(privateKey)))

        if(type(keySize) != int):
            raise TypeError(f"keySize parameter expected to be of {int} type or bytes type instead got {type(privateKey)} type")

        if(type(chunkSize) != int):
            raise TypeError(f"chunkSize parameter expected to be of {int} type or bytes type instead got {type(chunkSize)} type")



        # if the keys are in str format , convert them back to bytes
        if(type(publicKey) == str):
            publicKey = HexConvertor.decode(publicKey)
        if(type(privateKey) == str):
            privateKey = HexConvertor.decode(privateKey)

        # convert the keys to RSA type
        self.publicKey = RSA.import_key(publicKey)
        self.privateKey = RSA.import_key(privateKey)

        # init main encryptor decryptor module object
        self.cipherPublic = Cipher_PKCS1_v1_5.new(self.publicKey)
        self.cipherPrivate = Cipher_PKCS1_v1_5.new(self.privateKey)

        # random aes key
        self.aes_key = SHA256(secrets.token_bytes(256)).get_byte()
        self.enc_aes_key = self.cipherPublic.encrypt(self.aes_key)

        # aes chunk size
        self.aes_chunkSize = chunkSize * 1000 * 1000

        # aes mode
        self.mode = AES.MODE_EAX

        # cipher signature module object
        self.cipherSignature = Cipher_pss.new(self.privateKey)
        self.cipherSignatureVerify = Cipher_pss.new(self.publicKey)
















    

    # function to encrypt a byte object
    # generator function
    def encrypt_byte_yield(self , byte : bytes) -> bytes:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))
        
        result = b""

        hashObj = hashlib.sha256()

        len_byte = len(byte)

        currentCount = 0

        # number of chunks
        totalYield = (len_byte // self.aes_chunkSize) + 1


        # divide data in chunks and encrypt
        for i in range(0 , len_byte , self.aes_chunkSize):

            # divide
            chunk = byte[i : i+self.aes_chunkSize]

            # update hash
            hashObj.update(chunk)

            # encrypt
            cipher = AES.new(self.aes_key, AES.MODE_EAX)
            nonce = cipher.nonce

            ciphertext, tag = cipher.encrypt_and_digest(chunk)

            # add to result
            result = result + ciphertext + b":-helper:-" + tag + b":-helper:-" + nonce + b":-sce_aesWrapper-:"

            yield currentCount , totalYield
            currentCount = currentCount + 1

        result = result[:len(b":-sce_aesWrapper-:") * -1]

        # add encrypted key to result
        result = result + b":-encKey-:" + self.enc_aes_key

        crypto_hash_object = Cryptodome_SHA256.new(hashObj.digest())

        # add signature to result
        signature = self.cipherSignature.sign(crypto_hash_object)

        result = result + b":-signature-:" + signature

        if(currentCount <= totalYield):
            yield totalYield , totalYield

        return result
















    
    # function to decrypt the encrypted byte    
    def decrypt_byte_yield(self , enc_byte : bytes) -> bytes:

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise TypeError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))


        enc_byte , signature = enc_byte.split(b":-signature-:")

        enc_byte , encKey = enc_byte.split(b":-encKey-:")

        aes_key = self.cipherPrivate.decrypt(encKey , None)

        # split into chunks
        chunkList = enc_byte.split(b":-sce_aesWrapper-:")

        hashObj = hashlib.sha256()

        result = b""

        currentCount = 0

        # number of chunks
        totalYield = len(chunkList)


        # divide data in chunks and encrypt
        for i in chunkList:

            cipherText , tag , nonce = i.split(b":-helper:-")

            cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt(cipherText)

            try:
                cipher.verify(tag)
            except ValueError:
                raise ValueError("Key incorrect or message corrupted")

            result = result + plaintext

            hashObj.update(plaintext)


            yield currentCount , totalYield
            currentCount = currentCount + 1

        crypto_hash_object = Cryptodome_SHA256.new(hashObj.digest())

        try:
            self.cipherSignatureVerify.verify(crypto_hash_object, signature)
        except (ValueError, TypeError):
            raise ValueError("The signature is not authentic")
        

        if(currentCount <= totalYield):
            yield totalYield , totalYield

        return result






















    # function to encrypt a byte object
    def encrypt_byte(self , byte : bytes) -> bytes:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))
        
        result = b""

        hashObj = hashlib.sha256()

        len_byte = len(byte)

        # divide data in chunks and encrypt
        for i in range(0 , len_byte , self.aes_chunkSize):

            # divide
            chunk = byte[i : i+self.aes_chunkSize]

            # update hash
            hashObj.update(chunk)

            # encrypt
            cipher = AES.new(self.aes_key, AES.MODE_EAX)
            nonce = cipher.nonce

            ciphertext, tag = cipher.encrypt_and_digest(chunk)

            # add to result
            result = result + ciphertext + b":-helper:-" + tag + b":-helper:-" + nonce + b":-sce_aesWrapper-:"

        result = result[:len(b":-sce_aesWrapper-:") * -1]

        # add encrypted key to result
        result = result + b":-encKey-:" + self.enc_aes_key

        crypto_hash_object = Cryptodome_SHA256.new(hashObj.digest())

        # add signature to result
        signature = self.cipherSignature.sign(crypto_hash_object)

        result = result + b":-signature-:" + signature

        return result
















    
    # function to decrypt the encrypted byte    
    def decrypt_byte(self , enc_byte : bytes) -> bytes:

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise TypeError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))


        enc_byte , signature = enc_byte.split(b":-signature-:")

        enc_byte , encKey = enc_byte.split(b":-encKey-:")

        aes_key = self.cipherPrivate.decrypt(encKey , None)

        # split into chunks
        chunkList = enc_byte.split(b":-sce_aesWrapper-:")

        hashObj = hashlib.sha256()

        result = b""

        # divide data in chunks and encrypt
        for i in chunkList:

            cipherText , tag , nonce = i.split(b":-helper:-")

            cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt(cipherText)

            try:
                cipher.verify(tag)
            except ValueError:
                raise ValueError("Key incorrect or message corrupted")

            result = result + plaintext

            hashObj.update(plaintext)

        crypto_hash_object = Cryptodome_SHA256.new(hashObj.digest())

        try:
            self.cipherSignatureVerify.verify(crypto_hash_object, signature)
        except (ValueError, TypeError):
            raise ValueError("The signature is not authentic")

        return result



























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


    print("generating server key")

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()


    print("generating client key")

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()



    print("encrypting message server")
    encObj_server = Encryptor(publicKey_client , privateKey_server)

    serverMessageSize = 1000 * 1000 * 64
    myByte_server = b"h" * serverMessageSize

    print("serverMessageSize" , len(myByte_server))

    genObj = encObj_server.encrypt_byte_yield(myByte_server)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedByte_server = ex.value
            break
    print()

    print(f"encryptedByte_server len = {len(encryptedByte_server)}")




    print("encrypting message client")
    encObj_client = Encryptor(publicKey_server , privateKey_client)

    clientMessageSize = 1000 * 1000 * 64
    myByte_client = b"X" * clientMessageSize

    print("clientMessageSize" , len(myByte_client))

    genObj = encObj_client.encrypt_byte_yield(myByte_client)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedByte_client = ex.value
            break
    print()

    print(f"encryptedByte len = {len(encryptedByte_client)}")



    print("\n\n\n")

    print("client decrypting servers message")

    genObj = encObj_client.decrypt_byte_yield(encryptedByte_server)
    
    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedByte_client = ex.value
            break
    print()

    print(f"decryptedByte_client len = {len(decryptedByte_client)}")

    
    if(decryptedByte_client != myByte_server):
        print("\nerror")
    else:
        print("\nok")



    print("server decrypting clients message")

    genObj = encObj_server.decrypt_byte_yield(encryptedByte_client)
    
    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedByte_server = ex.value
            break
    print()

    print(f"decryptedByte_server len = {len(decryptedByte_server)}")

    
    if(decryptedByte_server != myByte_client):
        print("\nerror")
    else:
        print("\nok")










def __test_encryptor_byte():


    print("generating server key")

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()


    print("generating client key")

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()



    print("encrypting message server")
    encObj_server = Encryptor(publicKey_client , privateKey_server)

    myByte_server = b"hello world"


    encryptedByte_server = encObj_server.encrypt_byte(myByte_server)

    print(f"encryptedByte_server = {encryptedByte_server} , len = {len(encryptedByte_server)}")




    print("encrypting message client")
    encObj_client = Encryptor(publicKey_server , privateKey_client)

    myByte_client = b"hi there"


    encryptedByte_client = encObj_client.encrypt_byte(myByte_client)

    print(f"encryptedByte = {encryptedByte_client} , len = {len(encryptedByte_client)}")



    print("\n\n\n")

    print("client decrypting servers message")

    decryptedByte_client = encObj_client.decrypt_byte(encryptedByte_server)
    
    print(f"decryptedByte_client = {decryptedByte_client} , len = {len(decryptedByte_client)}")

    
    if(decryptedByte_client != myByte_server):
        print("\nerror")
    else:
        print("\nok")



    print("server decrypting clients message")

    decryptedByte_server = encObj_server.decrypt_byte(encryptedByte_client)
    
    print(f"decryptedByte_server = {decryptedByte_server} , len = {len(decryptedByte_server)}")

    
    if(decryptedByte_server != myByte_client):
        print("\nerror")
    else:
        print("\nok")








if __name__ == "__main__":
    __test_encryptor_byte_yield()
    # __test_encryptor_byte()