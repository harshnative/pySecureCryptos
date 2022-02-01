from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib
import base64
import multiprocessing
import os
import time
from .encoderDecoders import *
from .hashers_v2 import *












#  _                    
# | | __   ___   _   _  
# | |/ /  / _ \ | | | | 
# |   <  |  __/ | |_| | 
# |_|\_\  \___|  \__, | 
#                |___/  


class Keys:

    @classmethod
    def getKey(cls , password : str , iterations : int = 390000) -> bytes:

        # type checking the parameters
        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).digest()
        sha224_hashed_password_bytes = hashlib.sha224(password.encode("utf-8")).digest()

        # md5_hashed_password will act as a salt
        salt = md5_hashed_password
        
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
    def _encrypt_byte(cls , index , byte  , key , returnDict):

        # init fernet obj and encrypt data
        fernetObj = Fernet(key)
        encChunk = fernetObj.encrypt(byte)

        # add result to shared memory
        returnDict[index] = encChunk



    
    # method to encrypt a single chunk of data 
    @classmethod
    def _encrypt_byte_normal(cls , byte  , key):

        # init fernet obj and encrypt data
        fernetObj = Fernet(key)
        encChunk = fernetObj.encrypt(byte)

        # add result to shared memory
        return encChunk




















    # method to encrypt a large chunk of data
    # data will be encrypted using multiprocessing
    # key should be get from Keys.getKey(password) method
    # chunk size in MB , default is 8 MB. This value depends on your processing power. More the processing power, larger the chunk size should be
    @classmethod
    def main_encrypt_byte(cls , byte : bytes , key : bytes , chunkSize : int = 8) -> bytes:

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
            p = multiprocessing.Process(target=Encryptor._encrypt_byte, args=(index , i , key , return_dict , ))
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

        # generating checksum
        checksum = SHA512(byte).get_byte()

        encChecksum = cls._encrypt_byte_normal(checksum , key)

        result = result + b":vfw_v3_checksum:"  + encChecksum

        return result
















    # method to decrypt a single chunk of data 
    # return dict is the shared variable in multiprocessing
    @classmethod
    def _decrypt_byte(cls , index , enc_byte  , key , returnDict):

        # init fernet obj and decrypt data
        fernetObj = Fernet(key)
        decChunk = fernetObj.decrypt(enc_byte)

        # add result to shared memory
        returnDict[index] = decChunk




    
    # method to decrypt a single chunk of data 
    @classmethod
    def _decrypt_byte_normal(cls , enc_byte  , key):

        # init fernet obj and decrypt data
        fernetObj = Fernet(key)
        decChunk = fernetObj.decrypt(enc_byte)
        return decChunk






















    
    # method to decrypt a large chunk of data
    # data will be decrypted using multiprocessing
    @classmethod
    def main_decrypt_byte(cls , enc_byte : bytes , key : bytes) -> bytes:

        # init shared var
        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        enc_byte , checksum = enc_byte.split(b":vfw_v3_checksum:")

        # seperate chunks
        chunkList = enc_byte.split(b":~:~:")
        processes = []

        # init process of decryption for each chunk
        for index , i in enumerate(chunkList):
            p = multiprocessing.Process(target=Encryptor._decrypt_byte, args=(index , i , key , return_dict , ))
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

        
        # checksum match
        decChecksum = cls._decrypt_byte_normal(checksum , key)

        newChecksum = SHA512(result).get_byte()

        if(newChecksum != decChecksum):
            raise RuntimeError("decryption failed , checksum did not verify")

        return result





















    # method to encrypt a single chunk of data 
    # return dict is the shared variable in multiprocessing
    @classmethod
    def _encrypt_string(cls , index , string  , key , returnDict):

        # init fernet obj and encrypt data
        fernetObj = Fernet(key)

        byteFromString = String2Byte_v2.encode(string)
        encChunk = fernetObj.encrypt(byteFromString)
        stringFromByte = HexConvertor.encode(encChunk)

        # add result to shared memory
        returnDict[index] = stringFromByte




    # method to encrypt a single chunk of data 
    @classmethod
    def _encrypt_string_normal(cls , string  , key):

        # init fernet obj and encrypt data
        fernetObj = Fernet(key)

        byteFromString = String2Byte_v2.encode(string)
        encChunk = fernetObj.encrypt(byteFromString)
        stringFromByte = HexConvertor.encode(encChunk)

        return stringFromByte
































    # method to encrypt a large chunk of data
    # data will be encrypted using multiprocessing
    # key should be get from Keys.getKey(password) method
    # chunk size in MB , default is 8 MB. This value depends on your processing power. More the processing power, larger the chunk size should be
    # if the string as some chars which are outside the scope of utf-8 then , then use comp = True , it increases compatibility
    @classmethod
    def main_encrypt_string(cls , string : str , key : bytes , chunkSize : int = 4) -> bytes:

        if(type(string) != str):
            raise TypeError(f"string parameter expected to be {str} , instead got {type(string)}")

        if(type(key) != bytes):
            raise TypeError(f"key parameter expected to be {bytes} , instead got {type(key)}")

        if(type(chunkSize) != int):
            raise TypeError(f"chunkSize parameter expected to be {int} , instead got {type(chunkSize)}")

        if(chunkSize < 4):
            raise ValueError("chunk size should be greator than 4")


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
            raise MemoryError("Length of the string object passed is too long")


        # encrypt each chunk using multi processing
        for index , i in enumerate(chunkList):
            p = multiprocessing.Process(target=Encryptor._encrypt_string, args=(index , i , key , return_dict , ))
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


        # generating checksum
        checksum = SHA512(String2Byte_v2.encode(string)).get_string()

        encChecksum = cls._encrypt_string_normal(checksum , key)

        result = result + ":vfw_v3_checksum:"  + encChecksum

        return result





























    # method to decrypt a single chunk of data 
    # return dict is the shared variable in multiprocessing
    @classmethod
    def _decrypt_string(cls , index , enc_string  , key , returnDict):

        # init fernet obj and decrypt data
        fernetObj = Fernet(key)

        byteFromString = HexConvertor.decode(enc_string)
        decChunk = fernetObj.decrypt(byteFromString)
        stringFromByte = String2Byte_v2.decode(decChunk)

        # add result to shared memory
        returnDict[index] = stringFromByte





    # method to decrypt a single chunk of data 
    @classmethod
    def _decrypt_string_normal(cls , enc_string  , key):

        # init fernet obj and decrypt data
        fernetObj = Fernet(key)

        byteFromString = HexConvertor.decode(enc_string)
        decChunk = fernetObj.decrypt(byteFromString)
        stringFromByte = String2Byte_v2.decode(decChunk)

        return stringFromByte

























    
    # method to decrypt a large chunk of data
    # data will be decrypted using multiprocessing
    @classmethod
    def main_decrypt_string(cls , enc_string : str , key : bytes) -> str:

        # init shared var
        manager = multiprocessing.Manager()
        return_dict = manager.dict()

        enc_string , checksum = enc_string.split(":vfw_v3_checksum:")

        # seperate chunks
        chunkList = enc_string.split(":~:~:")
        processes = []

        # init process of decryption for each chunk
        for index , i in enumerate(chunkList):
            p = multiprocessing.Process(target=Encryptor._decrypt_string, args=(index , i , key , return_dict , ))
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

        # checksum match
        decChecksum = cls._decrypt_string_normal(checksum , key)

        newChecksum = SHA512(String2Byte_v2.encode(result)).get_string()

        if(newChecksum != decChecksum):
            raise RuntimeError("decryption failed , checksum did not verify")

        return result































    # function to read a file in chunks
    @classmethod
    def _read_in_chunks(cls , file_object, chunk_size=4096):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data



    # function to read a file in sepearte lines
    @classmethod
    def _read_in_lines(cls , file_object):
        while True:
            line = file_object.readline()
        
            # if line is empty
            # end of file is reached
            if not line:
                break
            yield line

































    # method to encrypt a large bytes file
    @classmethod
    def encrypt_file(cls , filepath : str , destinationPath : str , key : bytes) -> None:

        if(type(filepath) != str):
            raise TypeError(f"filename parameter expected to be {str} type instead got {type(filepath)} type.")

        if(type(destinationPath) != str):
            raise TypeError(f"destinationPath parameter expected to be {str} type instead got {type(destinationPath)} type.")

        if(type(key) != bytes):
            raise TypeError(f"key parameter expected to be {bytes} type instead got {type(key)} type.")

        cpuCount = os.cpu_count()

        # chunkSize in bytes
        chunkSize = 8 * cpuCount * 1024 * 1024

        # check if file path is correct
        fileCorrect = os.path.isfile(filepath)

        if(not(fileCorrect)):
            raise FileNotFoundError("no file was found at the path specified")

        # seperate file name and file path
        head, tail = os.path.split(filepath)

        destinationCorrect = os.path.isdir(destinationPath)

        if(not(destinationCorrect)):
            raise ("no dir was found at the path specified")

        # add name to dest path
        destinationPath = destinationPath + tail + ".enc"

        # get file size to calculate total yield
        fileSize = os.stat(filepath).st_size

        currentCount = 0
        totalYield = (fileSize // chunkSize) + 1

        # open file
        with open(filepath , "rb") as fil , open(destinationPath , "wb") as fil2:
            for data in cls._read_in_chunks(fil , chunkSize):

                # encrypt data chunk
                enc_data = cls.main_encrypt_byte(data , key)

                # write encrypted chunk to disk
                fil2.write(enc_data)
                fil2.write(b"\n")

                yield currentCount , totalYield
                currentCount = currentCount + 1


        # complete yield if not completed
        if(currentCount <= totalYield):
            yield totalYield , totalYield



































    # method to decrypt a large bytes file
    @classmethod
    def decrypt_file(cls , filepath : str , destinationPath : str , key : bytes) -> None:

        # function to yield number of lines
        def _count_generator(reader):
            b = reader(1024 * 1024 * 16)
            while b:
                yield b
                b = reader(1024 * 1024 * 16)

        if(type(filepath) != str):
            raise TypeError(f"filename parameter expected to be {str} type instead got {type(filepath)} type.")

        if(type(destinationPath) != str):
            raise TypeError(f"destinationPath parameter expected to be {str} type instead got {type(destinationPath)} type.")

        if(type(key) != bytes):
            raise TypeError(f"key parameter expected to be {bytes} type instead got {type(key)} type.")

        # check if file path is correct
        fileCorrect = os.path.isfile(filepath)

        if(not(fileCorrect)):
            raise FileNotFoundError("no file was found at the path specified")

        # seperate file name and file path
        head, tail = os.path.split(filepath)

        destinationCorrect = os.path.isdir(destinationPath)

        if(not(destinationCorrect)):
            raise ("no dir was found at the path specified")

        # add name to dest path without .enc extension
        destinationPath = destinationPath + tail[:-4]

        currentCount = 0

        # calculate number of lines in a file 
        with open(filepath, 'rb') as fp:
            c_generator = _count_generator(fp.raw.read)
            totalYield = sum(buffer.count(b'\n') for buffer in c_generator) + 1


        # open file
        with open(filepath , "rb") as fil , open(destinationPath , "wb") as fil2:
            for data in cls._read_in_lines(fil):

                # decrypt data chunk
                dec_data = cls.main_decrypt_byte(data , key)

                # write decrypted chunk to disk
                fil2.write(dec_data)

                yield currentCount , totalYield
                currentCount = currentCount + 1


        # complete yield if not completed
        if(currentCount <= totalYield):
            yield totalYield , totalYield


    




















































#  _                  _                       _               _                 
# | |_    ___   ___  | |_                    | |__    _   _  | |_    ___   ___  
# | __|  / _ \ / __| | __|       _____       | '_ \  | | | | | __|  / _ \ / __| 
# | |_  |  __/ \__ \ | |_       |_____|      | |_) | | |_| | | |_  |  __/ \__ \ 
#  \__|  \___| |___/  \__|                   |_.__/   \__, |  \__|  \___| |___/ 
#                                                     |___/                     


def __test_byte_main():

    print("starting")

    key = Keys.getKey("hello")

    n = 1024 * 1024 * 24
    toenc = b"h" * n

    start = time.perf_counter()

    enc = Encryptor.main_encrypt_byte(toenc , key)
    dec = Encryptor.main_decrypt_byte(enc , key)

    end = time.perf_counter()

    print(len(enc))
    print(len(dec))

    print(toenc == dec)


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , len(toenc) / 1024 / 1024))

































#  _                  _                        __   _   _         
# | |_    ___   ___  | |_                     / _| (_) | |   ___  
# | __|  / _ \ / __| | __|       _____       | |_  | | | |  / _ \ 
# | |_  |  __/ \__ \ | |_       |_____|      |  _| | | | | |  __/ 
#  \__|  \___| |___/  \__|                   |_|   |_| |_|  \___| 
                                                                



def __test_byte_file():

    print("starting")

    key = Keys.getKey("hello")

    fileName = "testVideo.mp4"

    filePath = f"/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/{fileName}"
    destPath = "/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/"
    
    filePath2 = f"/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/{fileName}.enc"
    destPath2 = "/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/dec/"

    start = time.perf_counter()

    enc_obj = Encryptor.encrypt_bfile(filePath , destPath , key)

    print()
    for i in enc_obj:
        print(f"\r{i}" , end = "")
    print()

    dec_obj = Encryptor.decrypt_bfile(filePath2 , destPath2 , key)

    print()
    for i in dec_obj:
        print(f"\r{i}" , end = "")
    print()

    end = time.perf_counter()


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , os.stat(filePath).st_size / 1024 / 1024))























#  _                  _                _            _                  
# | |_    ___   ___  | |_        ___  | |_   _ __  (_)  _ __     __ _  
# | __|  / _ \ / __| | __|      / __| | __| | '__| | | | '_ \   / _` | 
# | |_  |  __/ \__ \ | |_       \__ \ | |_  | |    | | | | | | | (_| | 
#  \__|  \___| |___/  \__|      |___/  \__| |_|    |_| |_| |_|  \__, | 
#                                                               |___/  


def __test_string_main():

    print("starting")

    key = Keys.getKey("hello")

    toenc = 'h' * (1024 * 1024 * 16)

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
    # __test_byte_main()
    # __test_byte_file()
    # __test_string_file()
    pass
