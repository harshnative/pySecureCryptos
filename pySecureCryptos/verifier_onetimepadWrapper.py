from .shuffler import Shuffler
import hashlib
import onetimepad
from .encoderDecoders import *
from .onetimepadWrapper import StringEncryptor as ow_stringEncryptor
from .onetimepadWrapper import BytesEncryptor as ow_bytesEncryptor
from typing import Union









#        _            _                                                             _                   
#  ___  | |_   _ __  (_)  _ __     __ _         ___   _ __     ___   _ __   _   _  | |_    ___    _ __  
# / __| | __| | '__| | | | '_ \   / _` |       / _ \ | '_ \   / __| | '__| | | | | | __|  / _ \  | '__| 
# \__ \ | |_  | |    | | | | | | | (_| |      |  __/ | | | | | (__  | |    | |_| | | |_  | (_) | | |    
# |___/  \__| |_|    |_| |_| |_|  \__, |       \___| |_| |_|  \___| |_|     \__, |  \__|  \___/  |_|    
#                                 |___/                                     |___/                       

class StringEncryptor:

    @classmethod
    def encrypt(cls , string : str , password : str) -> str:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        lenString = len(string)
        hashedLength = len(sha224_hashed_password_shuffled)

        # dividing the data into chunks of size hashedLength
        # each chunk will have its own encryption key
        # encryption key is generated from shuffling the sha224_hashed_password_shuffled again and again
        for i in range(0 , lenString , hashedLength):
            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            

    
        result = ""
        
        # encrypt each chunk using its corresponding key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        # this is mainly done to make message and key size same for onetimepad
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(string) , 2048):
            tempChunk = string[i : i + 2048]
            tempChunk_byte = String2Byte.encode(tempChunk)
            sha256_hash.update(tempChunk_byte)


        checksum = str(sha256_hash.hexdigest())
        # checksum will be 64 length

        enc_checksum = ow_stringEncryptor.encrypt(checksum , sha224_hashed_password_shuffled)
        result = result + ":checksum:" + enc_checksum

        return result









    @classmethod
    def decrypt(cls , enc_string : str , password : str) -> str:

        # type checking the parameters
        if(type(enc_string) != str):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        enc_string , checksum = enc_string.split(":checksum:")

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        # dividing the data into chunk of size hashedLength2
        # as returned from the encryptor is of twice the original size
        # i.e encrypted message is twice the size of message. not dependent on the size of key in actaul
        # and getting the corresponding chunk keys
        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

        result = ""
        
        # encrypt each chunk using corresponding key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

        # verifying the decryption
        dec_checksum = ow_stringEncryptor.decrypt(checksum , sha224_hashed_password_shuffled)

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(result) , 2048):
            tempChunk = result[i : i + 2048]
            tempChunk_byte = String2Byte.encode(tempChunk)
            sha256_hash.update(tempChunk_byte)

        new_checksum = str(sha256_hash.hexdigest())
        # checksum will be 64 length

        if(new_checksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")


        return result

    



























#          _          _       _              _            _                                             
#  _   _  (_)   ___  | |   __| |       ___  | |_   _ __  (_)  _ __     __ _         ___   _ __     ___  
# | | | | | |  / _ \ | |  / _` |      / __| | __| | '__| | | | '_ \   / _` |       / _ \ | '_ \   / __| 
# | |_| | | | |  __/ | | | (_| |      \__ \ | |_  | |    | | | | | | | (_| |      |  __/ | | | | | (__  
#  \__, | |_|  \___| |_|  \__,_|      |___/  \__| |_|    |_| |_| |_|  \__, |       \___| |_| |_|  \___| 
#  |___/                                                              |___/                             


class StringEncryptor_yield:

    @classmethod
    def encrypt(cls , string : str , password : str) -> str:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        lenString = len(string)
        hashedLength = len(sha224_hashed_password_shuffled)

        totalYields = int(lenString // hashedLength) * 2 + 1 + int((lenString // 2048) + 1)
        currentYield = 0

        for i in range(0 , lenString , hashedLength):
            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            
            yield currentYield , totalYields

            currentYield = currentYield + 1

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

            yield currentYield , totalYields

            currentYield = currentYield + 1

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(string) , 2048):
            tempChunk = string[i : i + 2048]
            tempChunk_byte = String2Byte.encode(tempChunk)
            sha256_hash.update(tempChunk_byte)

            yield currentYield , totalYields
            currentYield = currentYield + 1


        checksum = str(sha256_hash.hexdigest())
        # checksum will be 64 length

        enc_checksum = ow_stringEncryptor.encrypt(checksum , sha224_hashed_password_shuffled)
        result = result + ":checksum:" + enc_checksum

        return result











    @classmethod
    def decrypt(cls , enc_string : str , password : str) -> str:

        # type checking the parameters
        if(type(enc_string) != str):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        enc_string , checksum = enc_string.split(":checksum:")

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        totalYields = int(lenString // hashedLength2) * 2 + 1 + int((lenString // 2) // 2048) + 1
        currentYield = 0

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

            yield currentYield , totalYields

            currentYield = currentYield + 1


        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

            yield currentYield , totalYields

            currentYield = currentYield + 1

        # verifying the decryption
        dec_checksum = ow_stringEncryptor.decrypt(checksum , sha224_hashed_password_shuffled)

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(result) , 2048):
            tempChunk = result[i : i + 2048]
            tempChunk_byte = String2Byte.encode(tempChunk)
            sha256_hash.update(tempChunk_byte)

            yield currentYield , totalYields
            currentYield = currentYield + 1


        new_checksum = str(sha256_hash.hexdigest())
        # checksum will be 64 length

        if(new_checksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")


        return result

    





























#  _               _                                            
# | |__    _   _  | |_    ___   ___         ___   _ __     ___  
# | '_ \  | | | | | __|  / _ \ / __|       / _ \ | '_ \   / __| 
# | |_) | | |_| | | |_  |  __/ \__ \      |  __/ | | | | | (__  
# |_.__/   \__, |  \__|  \___| |___/       \___| |_| |_|  \___| 
#          |___/                                                


class BytesEncryptor:

    @classmethod
    def encrypt(cls , byteObject : bytes , password : str , returnByteObject : bool = True) -> Union[str , bytes]:

        # type checking the parameters
        if((type(byteObject) != bytes) and (type(byteObject) != bytearray)):
            raise TypeError("byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(byteObject)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        string = Byte2String.encode(byteObject)

        lenString = len(string)
        hashedLength = len(sha224_hashed_password_shuffled)

        for i in range(0 , lenString , hashedLength):
            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

        if(returnByteObject):
            result = String2Byte.encode(result)

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(byteObject) , 2048):
            tempChunk = byteObject[i : i + 2048]
            sha256_hash.update(tempChunk)


        if(returnByteObject):
            checksum = sha256_hash.digest()
            # checksum will be 64 length

            enc_checksum = ow_bytesEncryptor.encrypt(checksum , sha224_hashed_password_shuffled)
            result = result + b":checksum:" + enc_checksum

        else:
            checksum = str(sha256_hash.hexdigest())
            # checksum will be 64 length

            enc_checksum = ow_stringEncryptor.encrypt(checksum , sha224_hashed_password_shuffled)
            result = result + ":checksum:" + enc_checksum

        return result












    @classmethod
    def decrypt(cls , enc_string : str , password : str) -> bytes:

        # type checking the parameters
        if((type(enc_string) != str)):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type. If you returned byte type from encrytor for BytesEncryptor , then use decrypt_byte method".format(type(enc_string)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        enc_string , checksum = enc_string.split(":checksum:")

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

        result = Byte2String.decode(result)

        # verifying the decryption
        dec_checksum = ow_stringEncryptor.decrypt(checksum , sha224_hashed_password_shuffled)

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(result) , 2048):
            tempChunk = result[i : i + 2048]
            sha256_hash.update(tempChunk)


        new_checksum = str(sha256_hash.hexdigest())
        # checksum will be 64 length

        if(new_checksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")


        return result










    @classmethod
    def decrypt_byte(cls , enc_byteObject : bytes , password : str) -> bytes:

        # type checking the parameters
        if((type(enc_byteObject) != bytes) and (type(enc_byteObject) != bytearray)):
            raise TypeError("enc_byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(enc_byteObject)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        enc_byteObject , checksum = enc_byteObject.split(b":checksum:")

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        enc_string = String2Byte.decode(enc_byteObject)

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

        result = Byte2String.decode(result)

        # verifying the decryption
        dec_checksum = ow_bytesEncryptor.decrypt_byte(checksum , sha224_hashed_password_shuffled)

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(result) , 2048):
            tempChunk = result[i : i + 2048]
            sha256_hash.update(tempChunk)


        new_checksum = sha256_hash.digest()
        # checksum will be 64 length

        if(new_checksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")


        return result




























#          _          _       _        _               _                                            
#  _   _  (_)   ___  | |   __| |      | |__    _   _  | |_    ___   ___         ___   _ __     ___  
# | | | | | |  / _ \ | |  / _` |      | '_ \  | | | | | __|  / _ \ / __|       / _ \ | '_ \   / __| 
# | |_| | | | |  __/ | | | (_| |      | |_) | | |_| | | |_  |  __/ \__ \      |  __/ | | | | | (__  
#  \__, | |_|  \___| |_|  \__,_|      |_.__/   \__, |  \__|  \___| |___/       \___| |_| |_|  \___| 
#  |___/                                       |___/                                                


class BytesEncryptor_yield:

    @classmethod
    def encrypt(cls , byteObject : bytes , password : str , returnByteObject : bool = True) -> Union[str , bytes]:

        # type checking the parameters
        if((type(byteObject) != bytes) and (type(byteObject) != bytearray)):
            raise TypeError("byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(byteObject)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)

        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        lenString = int(len(byteObject)*3)
        hashedLength = len(sha224_hashed_password_shuffled)
        
        if(returnByteObject):
            totalYields = int(len(byteObject)) + (int(lenString // hashedLength) * 2 + 1) + int(lenString * 2) + int(len(byteObject) // 2048) + 1
        else:
            totalYields = int(len(byteObject)) + (int(lenString // hashedLength) * 2 + 1) + int(len(byteObject) // 2048) + 1
        
        currentYield = 0

        genObj_b2s_encode = Byte2String_yield.encode(byteObject)

        while(True):
            try:
                _ , _ = next(genObj_b2s_encode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                string = ex.value
                break

        lenString = len(string)

        for i in range(0 , lenString , hashedLength):


            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            
            yield currentYield , totalYields

            currentYield = currentYield + 1

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

            yield currentYield , totalYields

            currentYield = currentYield + 1

        if(returnByteObject):
            genObj_s2b_encode = String2Byte_yield.encode(result)

            while(True):
                try:
                    _ , _ = next(genObj_s2b_encode)
                    yield currentYield , totalYields
                    currentYield = currentYield + 1

                except StopIteration as ex:
                    result = ex.value
                    break

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(byteObject) , 2048):
            tempChunk = byteObject[i : i + 2048]
            sha256_hash.update(tempChunk)

            yield currentYield , totalYields
            currentYield = currentYield + 1


        if(returnByteObject):
            checksum = sha256_hash.digest()
            # checksum will be 64 length

            enc_checksum = ow_bytesEncryptor.encrypt(checksum , sha224_hashed_password_shuffled)
            result = result + b":checksum:" + enc_checksum

        else:
            checksum = str(sha256_hash.hexdigest())
            # checksum will be 64 length

            enc_checksum = ow_stringEncryptor.encrypt(checksum , sha224_hashed_password_shuffled)
            result = result + ":checksum:" + enc_checksum

        return result









    @classmethod
    def decrypt(cls , enc_string : str , password : str) -> bytes:

        # type checking the parameters
        if((type(enc_string) != str)):
            raise TypeError("enc_string parameter expected to be of str type instead got {} type. If you returned byte type from encrytor for BytesEncryptor , then use decrypt_byte method".format(type(enc_string)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        enc_string , checksum = enc_string.split(":checksum:")
        
        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        totalYields = (int(lenString // hashedLength2) * 2 + 1) + int(lenString // 2 // 3) + int((lenString // 2) // 2048) + 1
        
        currentYield = 0

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 
            
            yield currentYield , totalYields

            currentYield = currentYield + 1



        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

            yield currentYield , totalYields

            currentYield = currentYield + 1

        genObj_b2s_decode = Byte2String_yield.decode(result)

        while(True):
            try:
                _ , _ = next(genObj_b2s_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                result = ex.value
                break

        # verifying the decryption
        dec_checksum = ow_stringEncryptor.decrypt(checksum , sha224_hashed_password_shuffled)

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(result) , 2048):
            tempChunk = result[i : i + 2048]
            sha256_hash.update(tempChunk)

            yield currentYield , totalYields
            currentYield = currentYield + 1


        new_checksum = str(sha256_hash.hexdigest())
        # checksum will be 64 length

        if(new_checksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")


        return result











    @classmethod
    def decrypt_byte(cls , enc_byteObject : bytes , password : str) -> bytes:

        # type checking the parameters
        if((type(enc_byteObject) != bytes) and (type(enc_byteObject) != bytearray)):
            raise TypeError("enc_byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(enc_byteObject)))

        if(type(password) != str):
            raise TypeError("password parameter expected to be of str type instead got {} type".format(type(password)))

        enc_byteObject , checksum = enc_byteObject.split(b":checksum:")
        
        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        len_enc_byteObject = len(enc_byteObject)

        totalYields = len_enc_byteObject + (int(len_enc_byteObject // hashedLength2) * 2 + 1) + int(len_enc_byteObject // 3 // 2) + int(((len_enc_byteObject // 3) // 2048) + 1)
        currentYield = 0

        genObj_s2b_decode = String2Byte_yield.decode(enc_byteObject)

        while(True):
            try:
                _ , _ = next(genObj_s2b_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                enc_string = ex.value
                break

        lenString = len(enc_string)

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 
            
            yield currentYield , totalYields

            currentYield = currentYield + 1

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

            yield currentYield , totalYields

            currentYield = currentYield + 1

        genObj_b2s_decode = Byte2String_yield.decode(result)

        while(True):
            try:
                _ , _ = next(genObj_b2s_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                result = ex.value
                break

        # verifying the decryption
        dec_checksum = ow_bytesEncryptor.decrypt_byte(checksum , sha224_hashed_password_shuffled)

        sha256_hash = hashlib.sha256()

        for i in range(0 , len(result) , 2048):
            tempChunk = result[i : i + 2048]
            sha256_hash.update(tempChunk)

            yield currentYield , totalYields
            currentYield = currentYield + 1


        new_checksum = sha256_hash.digest()
        # checksum will be 64 length

        if(new_checksum != dec_checksum):
            raise RuntimeError("decryption failed , checksum did not verify")


        return result

































#  _                  _                             _            _                                             
# | |_    ___   ___  | |_                     ___  | |_   _ __  (_)  _ __     __ _         ___   _ __     ___  
# | __|  / _ \ / __| | __|       _____       / __| | __| | '__| | | | '_ \   / _` |       / _ \ | '_ \   / __| 
# | |_  |  __/ \__ \ | |_       |_____|      \__ \ | |_  | |    | | | | | | | (_| |      |  __/ | | | | | (__  
#  \__|  \___| |___/  \__|                   |___/  \__| |_|    |_| |_| |_|  \__, |       \___| |_| |_|  \___| 
#                                                                            |___/                             


def __test_stringEncrytor():
    string = "hello world"
    encryptedString = StringEncryptor.encrypt(string , "hello")
    decryptedString = StringEncryptor.decrypt(encryptedString , "hello")

    print("string = " , string)
    print("encryptedString = " , encryptedString)
    print("decryptedString = " , decryptedString)

    if(string == decryptedString):
        print("ok")
    else:
        print("error")










def __test_stringEncrytor2():
    string = "hello world" * 1123
    genObj_encrypt = StringEncryptor_yield.encrypt(string , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end="")
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    genObj_decrypt = StringEncryptor_yield.decrypt(encryptedString , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end="")
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    if(string == decryptedString):
        print("\nok")
    else:
        print("\nerror")



















#  _                  _                       _               _                                            
# | |_    ___   ___  | |_                    | |__    _   _  | |_    ___   ___         ___   _ __     ___  
# | __|  / _ \ / __| | __|       _____       | '_ \  | | | | | __|  / _ \ / __|       / _ \ | '_ \   / __| 
# | |_  |  __/ \__ \ | |_       |_____|      | |_) | | |_| | | |_  |  __/ \__ \      |  __/ | | | | | (__  
#  \__|  \___| |___/  \__|                   |_.__/   \__, |  \__|  \___| |___/       \___| |_| |_|  \___| 
#                                                     |___/                                                



def __test_byteEncrytor():
    byteObject = b"hello world"
    encryptedString = BytesEncryptor.encrypt(byteObject , "hello" , returnByteObject=False)
    decryptedByte = BytesEncryptor.decrypt(encryptedString , "hello")

    if(byteObject == decryptedByte):
        print("ok")
    else:
        print("error")

    print("\n\ntest 2\n\n")


    byteObject = b"hello world"
    
    # we will get bytes object from the encryptor function , say you are storing this on a blob storage
    encryptedByte = BytesEncryptor.encrypt(byteObject , "hello" , returnByteObject=True)
    decryptedByte = BytesEncryptor.decrypt_byte(encryptedByte , "hello")


    if(byteObject == decryptedByte):
        print("ok")
    else:
        print("error")










def __test_byteEncrytor2():
    byteObject = b"hello world" * 1123

    genObj_encrypt = BytesEncryptor_yield.encrypt(byteObject , "hello" , returnByteObject=False)

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    genObj_decrypt = BytesEncryptor_yield.decrypt(encryptedString , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    if(byteObject == decryptedByte):
        print("\nok")
    else:
        print("\nerror")




    print("\n\ntest 2\n\n")


    byteObject = b"hello world" * 1123

    genObj_encrypt = BytesEncryptor_yield.encrypt(byteObject , "hello" , returnByteObject=True)

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    genObj_decrypt = BytesEncryptor_yield.decrypt_byte(encryptedByte , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    if(byteObject == decryptedByte):
        print("\nok")
    else:
        print("\nerror")

























if __name__ == "__main__":
    __test_byteEncrytor2()
    # __test_stringEncrytor2()