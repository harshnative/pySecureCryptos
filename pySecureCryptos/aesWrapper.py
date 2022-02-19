from Cryptodome.Cipher import AES
from .encoderDecoders import *
from .hashers_v2 import *





    










#                                               _                   
#   ___   _ __     ___   _ __   _   _   _ __   | |_    ___    _ __  
#  / _ \ | '_ \   / __| | '__| | | | | | '_ \  | __|  / _ \  | '__| 
# |  __/ | | | | | (__  | |    | |_| | | |_) | | |_  | (_) | | |    
#  \___| |_| |_|  \___| |_|     \__, | | .__/   \__|  \___/  |_|    
#                               |___/  |_|                          


class Encryptor:

    # chunk size in MB
    def __init__(self , password : str , chunkSize : int = 16):

        # type checking the parameters
        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))
  
 
        
        password_bytes = String2Byte_v2.encode(password)

        self.key = SHA256(password_bytes).get_byte()

        self.chunkSize = chunkSize * 1000 * 1000

        self.mode = AES.MODE_EAX





















    # function to encrypt a byte object
    # generator function
    def encrypt_byte_yield(self , byte : bytes) -> bytes:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))
        
        result = b""

        len_byte = len(byte)

        currentCount = 0

        # number of chunks
        totalYield = (len_byte // self.chunkSize) + 1


        # divide data in chunks and encrypt
        for i in range(0 , len_byte , self.chunkSize):
            chunk = byte[i : i+self.chunkSize]

            cipher = AES.new(self.key, AES.MODE_EAX)
            nonce = cipher.nonce

            ciphertext, tag = cipher.encrypt_and_digest(chunk)

            result = result + ciphertext + b":helper:" + tag + b":helper:" + nonce + b":-aesWrapper-:"

            yield currentCount , totalYield
            currentCount = currentCount + 1

        result = result[:len(b":-aesWrapper-:") * -1]

        if(currentCount <= totalYield):
            yield totalYield , totalYield

        return result


















    # function to decrypt the encrypted byte    
    def decrypt_byte_yield(self , enc_byte : bytes) -> bytes:

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise TypeError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))

        # split into chunks
        chunkList = enc_byte.split(b":-aesWrapper-:")

        result = b""

        currentCount = 0

        # number of chunks
        totalYield = len(chunkList)


        # divide data in chunks and encrypt
        for i in chunkList:

            cipherText , tag , nonce = i.split(b":helper:")

            cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt(cipherText)
            try:
                cipher.verify(tag)
            except ValueError:
                raise ValueError("Key incorrect or message corrupted")

            result = result + plaintext

            yield currentCount , totalYield
            currentCount = currentCount + 1

        if(currentCount <= totalYield):
            yield totalYield , totalYield

        return result













    # function to encrypt a byte object
    # generator function
    def encrypt_byte(self , byte : bytes) -> bytes:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))
        
        result = b""

        len_byte = len(byte)


        # divide data in chunks and encrypt
        for i in range(0 , len_byte , self.chunkSize):
            chunk = byte[i : i+self.chunkSize]

            cipher = AES.new(self.key, AES.MODE_EAX)
            nonce = cipher.nonce

            ciphertext, tag = cipher.encrypt_and_digest(chunk)

            result = result + ciphertext + b":helper:" + tag + b":helper:" + nonce + b":-aesWrapper-:"

        result = result[:len(b":-aesWrapper-:") * -1]

        return result


















    # function to decrypt the encrypted byte    
    def decrypt_byte(self , enc_byte : bytes) -> bytes:

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise TypeError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))

        # split into chunks
        chunkList = enc_byte.split(b":-aesWrapper-:")

        result = b""


        # divide data in chunks and encrypt
        for i in chunkList:

            cipherText , tag , nonce = i.split(b":helper:")

            cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt(cipherText)
            try:
                cipher.verify(tag)
            except ValueError:
                raise ValueError("Key incorrect or message corrupted")

            result = result + plaintext

        return result













    # function to encrypt a string object
    # generator function
    def encrypt_string_yield(self , string : str) -> str:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))
        
        result = ""

        len_string = len(string)

        currentCount = 0

        # number of chunks
        totalYield = (len_string // self.chunkSize) + 1


        # divide data in chunks and encrypt
        for i in range(0 , len_string , self.chunkSize):
            chunk = string[i : i+self.chunkSize]
            chunk = String2Byte_v2.encode(chunk)

            cipher = AES.new(self.key, AES.MODE_EAX)
            nonce = HexConvertor.encode(cipher.nonce)

            ciphertext , tag = cipher.encrypt_and_digest(chunk)

            ciphertext = HexConvertor.encode(ciphertext)
            tag = HexConvertor.encode(tag)

            result = result + ciphertext + ":helper:" + tag + ":helper:" + nonce + ":-aesWrapper-:"

            yield currentCount , totalYield
            currentCount = currentCount + 1

        result = result[:len(":-aesWrapper-:") * -1]

        if(currentCount <= totalYield):
            yield totalYield , totalYield

        return result


















    # function to decrypt the encrypted string    
    def decrypt_string_yield(self , enc_string : str) -> str:

        # type checking the parameters
        if(type(enc_string) != str):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        # split into chunks
        chunkList = enc_string.split(":-aesWrapper-:")

        result = ""

        currentCount = 0

        # number of chunks
        totalYield = len(chunkList)


        # divide data in chunks and encrypt
        for i in chunkList:

            cipherText , tag , nonce = i.split(":helper:")
            cipherText = HexConvertor.decode(cipherText)
            tag = HexConvertor.decode(tag)
            nonce = HexConvertor.decode(nonce)

            cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt(cipherText)

            plaintext = String2Byte_v2.decode(plaintext)
            try:
                cipher.verify(tag)
            except ValueError:
                raise ValueError("Key incorrect or message corrupted")

            result = result + plaintext

            yield currentCount , totalYield
            currentCount = currentCount + 1

        if(currentCount <= totalYield):
            yield totalYield , totalYield

        return result










    

    # function to encrypt a string object
    # generator function
    def encrypt_string(self , string : str) -> str:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))
        
        result = ""

        len_string = len(string)

        # divide data in chunks and encrypt
        for i in range(0 , len_string , self.chunkSize):
            chunk = string[i : i+self.chunkSize]
            chunk = String2Byte_v2.encode(chunk)

            cipher = AES.new(self.key, AES.MODE_EAX)
            nonce = HexConvertor.encode(cipher.nonce)

            ciphertext , tag = cipher.encrypt_and_digest(chunk)

            ciphertext = HexConvertor.encode(ciphertext)
            tag = HexConvertor.encode(tag)

            result = result + ciphertext + ":helper:" + tag + ":helper:" + nonce + ":-aesWrapper-:"

        result = result[:len(":-aesWrapper-:") * -1]


        return result


















    # function to decrypt the encrypted string    
    def decrypt_string(self , enc_string : str) -> str:

        # type checking the parameters
        if(type(enc_string) != str):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        # split into chunks
        chunkList = enc_string.split(":-aesWrapper-:")

        result = ""

        # divide data in chunks and encrypt
        for i in chunkList:

            cipherText , tag , nonce = i.split(":helper:")
            cipherText = HexConvertor.decode(cipherText)
            tag = HexConvertor.decode(tag)
            nonce = HexConvertor.decode(nonce)

            cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
            plaintext = cipher.decrypt(cipherText)

            plaintext = String2Byte_v2.decode(plaintext)
            try:
                cipher.verify(tag)
            except ValueError:
                raise ValueError("Key incorrect or message corrupted")

            result = result + plaintext

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

    password = "hello"

    
    print("making obj")
    encObj = Encryptor(password)

    myByte = b"h" * 1024 * 1024 * 128

    print(f"encrypting byte of len = {len(myByte)}")


    genObj = encObj.encrypt_byte_yield(myByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            # print("\r{} , {}".format(currentCount , totalYield) , end="")
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







def __test_encryptor_byte():

    password = "hello"

    print("making obj")
    encObj = Encryptor(password)

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


















#  _                  _                             _            _                  
# | |_    ___   ___  | |_                     ___  | |_   _ __  (_)  _ __     __ _  
# | __|  / _ \ / __| | __|       _____       / __| | __| | '__| | | | '_ \   / _` | 
# | |_  |  __/ \__ \ | |_       |_____|      \__ \ | |_  | |    | | | | | | | (_| | 
#  \__|  \___| |___/  \__|                   |___/  \__| |_|    |_| |_| |_|  \__, | 
#                                                                            |___/  


def __test_encryptor_string_yield():

    password = "hello"

    print("making obj")
    encObj = Encryptor(password)

    # 16 MB
    myString = "h" * 1024 * 1024 * 128

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


    
    



def __test_encryptor_string():

    password = "hello"

    print("making obj")
    encObj = Encryptor(password)

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


    














if __name__ == "__main__":
    # __test_encryptor_byte_yield()
    # __test_encryptor_byte_yield()
    # __test_encryptor_byte()
    # __test_encryptor_byte()
    __test_encryptor_string_yield()
    # __test_encryptor_string()