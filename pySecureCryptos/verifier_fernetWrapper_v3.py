from typing import Type
import numba
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
import base64
import multiprocessing
import os
import time
import encoderDecoders













#  _                    
# | | __   ___   _   _  
# | |/ /  / _ \ | | | | 
# |   <  |  __/ | |_| | 
# |_|\_\  \___|  \__, | 
#                |___/  


class Keys:

    @classmethod
    def getKey(cls , password , iterations=390000):

        # type checking the parameters
        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # converting sha224_hashed_password to bytes to make it usable in kdf 
        sha224_hashed_password_bytes = bytes(sha224_hashed_password , "utf-8")

        # md5_hashed_password will act as a salt
        salt = bytes(md5_hashed_password , "utf-8")
        
        # deriving fernet key from the password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=iterations,
        )

        key = base64.urlsafe_b64encode(kdf.derive(sha224_hashed_password_bytes))

        return key























#                                               _                   
#   ___   _ __     ___   _ __   _   _   _ __   | |_    ___    _ __  
#  / _ \ | '_ \   / __| | '__| | | | | | '_ \  | __|  / _ \  | '__| 
# |  __/ | | | | | (__  | |    | |_| | | |_) | | |_  | (_) | | |    
#  \___| |_| |_|  \___| |_|     \__, | | .__/   \__|  \___/  |_|    
#                               |___/  |_|                          


class Encryptor:


    # method to encrypt a single chunk of data 
    # return dict is the shared variable in multiprocessing
    @classmethod
    def __encrypt_byte(cls , index , byte  , key , returnDict):

        # init fernet obj and encrypt data
        fernetObj = Fernet(key)
        encChunk = fernetObj.encrypt(byte)

        # add result to shared memory
        returnDict[index] = encChunk









    # method to encrypt a large chunk of data
    # data will be encrypted using multiprocessing
    # key should be get from Keys.getKey(password) method
    # chunk size in MB , default is 8 MB. This value depends on your processing power. More the processing power, larger the chunk size should be
    @classmethod
    def main_encrypt_byte(cls , byte , key , chunkSize = 8):

        if(type(byte) != bytes):
            raise TypeError(f"byte parameter expected to be {bytes} , instead got {type(byte)}")

        if(type(key) != bytes):
            raise TypeError(f"key parameter expected to be {bytes} , instead got {type(key)}")

        if(type(chunkSize) != int):
            raise TypeError(f"chunkSize parameter expected to be {int} , instead got {type(chunkSize)}")



        # init shared variable
        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        len_byte = len(byte)

        # chunk size in bytes
        chunkSize = 1024 * 1024 * chunkSize

        chunkList = []
        processes = []

        # divide data into chunks
        for i in range(0 , len_byte , chunkSize):
            chunk = byte[i : i + chunkSize]
            chunkList.append(chunk)

        len_chunkList = len(chunkList)

        # if the number os chunks exceed 128 , then abort the process as processing large number of chunks at onces may lead to memory overflow
        if(len_chunkList > 128):
            raise MemoryError("Length of the byte object passed is too long")


        # encrypt each chunk using multi processing
        for index , i in enumerate(chunkList):
            p = multiprocessing.Process(target=Encryptor.__encrypt_byte, args=(index , i , key , return_dict , ))
            processes.append(p)
            p.start()

        # wait for all the encryption to finish
        for process in processes:
            process.join()

        result = b""

        # join the encrypted chunk in correct order
        for i in range(len_chunkList):

            # get encrypted chunk of index i from shared dict
            enc_chunk = return_dict.get(i , None)

            if(enc_chunk == None):
                raise RuntimeError("Encryption cannot be completed using multiprocessing")
            
            result = result + enc_chunk + b":~:~:"

        result = result[:-5]

        return result





    # method to decrypt a single chunk of data 
    # return dict is the shared variable in multiprocessing
    @classmethod
    def __decrypt_byte(cls , index , enc_byte  , key , returnDict):

        # init fernet obj and decrypt data
        fernetObj = Fernet(key)
        decChunk = fernetObj.decrypt(enc_byte)

        # add result to shared memory
        returnDict[index] = decChunk





    
    # method to decrypt a large chunk of data
    # data will be decrypted using multiprocessing
    @classmethod
    def main_decrypt_byte(cls , enc_byte , key):

        # init shared var
        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        # seperate chunks
        chunkList = enc_byte.split(b":~:~:")
        processes = []

        # init process of decryption for each chunk
        for index , i in enumerate(chunkList):
            p = multiprocessing.Process(target=Encryptor.__decrypt_byte, args=(index , i , key , return_dict , ))
            processes.append(p)
            p.start()

        # wait for all decryption processes to finish
        for process in processes:
            process.join()

        result = b""

        # join the chunks in correct order
        for i in range(len(chunkList)):
            dec_chunk = return_dict.get(i , None)

            if(dec_chunk == None):
                raise RuntimeError("Decryption cannot be completed using multiprocessing")
            
            result = result + dec_chunk

        return result






    # method to encrypt a single chunk of data 
    # return dict is the shared variable in multiprocessing
    @classmethod
    def __encrypt_string(cls , index , string  , key , returnDict):

        # init fernet obj and encrypt data
        fernetObj = Fernet(key)

        byteFromString = encoderDecoders.String2Byte.encode(string)
        encChunk = fernetObj.encrypt(byteFromString)
        stringFromByte = encoderDecoders.HexConvertor.encode(encChunk)

        # add result to shared memory
        returnDict[index] = stringFromByte









    # method to encrypt a large chunk of data
    # data will be encrypted using multiprocessing
    # key should be get from Keys.getKey(password) method
    # chunk size in MB , default is 8 MB. This value depends on your processing power. More the processing power, larger the chunk size should be
    @classmethod
    def main_encrypt_string(cls , string , key , chunkSize = 1):

        if(type(string) != str):
            raise TypeError(f"string parameter expected to be {str} , instead got {type(string)}")

        if(type(key) != bytes):
            raise TypeError(f"key parameter expected to be {bytes} , instead got {type(key)}")

        if(type(chunkSize) != int):
            raise TypeError(f"chunkSize parameter expected to be {int} , instead got {type(chunkSize)}")



        # init shared variable
        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        len_string = len(string)

        # chunk size in bytes
        chunkSize = 1024 * 1024 * chunkSize

        chunkList = []
        processes = []

        # divide data into chunks
        for i in range(0 , len_string , chunkSize):
            chunk = string[i : i + chunkSize]
            chunkList.append(chunk)

        len_chunkList = len(chunkList)

        # if the number os chunks exceed 128 , then abort the process as processing large number of chunks at onces may lead to memory overflow
        if(len_chunkList > 128):
            raise MemoryError("Length of the byte object passed is too long")


        # encrypt each chunk using multi processing
        for index , i in enumerate(chunkList):
            p = multiprocessing.Process(target=Encryptor.__encrypt_string, args=(index , i , key , return_dict , ))
            processes.append(p)
            p.start()

        # wait for all the encryption to finish
        for process in processes:
            process.join()

        result = ""

        # join the encrypted chunk in correct order
        for i in range(len_chunkList):

            # get encrypted chunk of index i from shared dict
            enc_chunk = return_dict.get(i , None)

            if(enc_chunk == None):
                raise RuntimeError("Encryption cannot be completed using multiprocessing")
            
            result = result + enc_chunk + ":~:~:"

        result = result[:-5]

        return result





    # method to decrypt a single chunk of data 
    # return dict is the shared variable in multiprocessing
    @classmethod
    def __decrypt_string(cls , index , enc_string  , key , returnDict):

        # init fernet obj and decrypt data
        fernetObj = Fernet(key)

        byteFromString = encoderDecoders.HexConvertor.decode(enc_string)
        decChunk = fernetObj.decrypt(byteFromString)
        stringFromByte = encoderDecoders.String2Byte.decode(decChunk)

        # add result to shared memory
        returnDict[index] = stringFromByte





    
    # method to decrypt a large chunk of data
    # data will be decrypted using multiprocessing
    @classmethod
    def main_decrypt_string(cls , enc_string , key):

        # init shared var
        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        # seperate chunks
        chunkList = enc_string.split(":~:~:")
        processes = []

        # init process of decryption for each chunk
        for index , i in enumerate(chunkList):
            p = multiprocessing.Process(target=Encryptor.__decrypt_string, args=(index , i , key , return_dict , ))
            processes.append(p)
            p.start()

        # wait for all decryption processes to finish
        for process in processes:
            process.join()

        result = ""

        # join the chunks in correct order
        for i in range(len(chunkList)):
            dec_chunk = return_dict.get(i , None)

            if(dec_chunk == None):
                raise RuntimeError("decryption cannot be completed using multiprocessing")
            
            result = result + dec_chunk

        return result





















def __test_byte_main():

    print("starting")

    key = Keys.getKey("hello")

    toenc = b"h" * (1024 * 1024 * 24)

    start = time.perf_counter()

    enc = Encryptor.main_encrypt_byte(toenc , key)
    dec = Encryptor.main_decrypt_byte(enc , key)

    end = time.perf_counter()

    print(len(enc))
    print(len(dec))

    print(toenc == dec)


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , len(toenc) / 1024 / 1024))



















def __test_string_main():

    print("starting")

    key = Keys.getKey("hello")

    toenc = "h" * (1024 * 1024 * 4)

    start = time.perf_counter()

    enc = Encryptor.main_encrypt_string(toenc , key)
    dec = Encryptor.main_decrypt_string(enc , key)

    end = time.perf_counter()

    print(len(enc))
    print(len(dec))

    print(toenc == dec)


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , len(toenc) / 1024 / 1024))








if __name__ == "__main__":
    __test_string_main()
    pass