from shuffler import Shuffler
import hashlib
import encoderDecoders
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



class StringEncryptor:

    def __init__(self , password , iterations=390000):

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

        # init fernet object
        self.fernetObj = Fernet(key)

        self.chunkSize = 256
        self.chunkSize__outputSize = 440
        self.chunkSize__inputSize = {}
        self.__getInputSize()


    def __getInputSize(self , max=256):

        for i in range(max+1):
            outputSize = self.__getOutputSize(i)
            self.chunkSize__inputSize[outputSize] = i



    def __getOutputSize(self , inputSize):
        string = "h" * inputSize

        string_byte = bytes(string , "utf-8")

        enc_byte = self.fernetObj.encrypt(string_byte)

        return len(enc_byte)








    # method to encrypt a string
    # returns encrypted string if returnString = True
    # else returns a byte object
    def encrypt_yield(self , string , returnString = True):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(len(string) == 0):
            raise ValueError("empty string passed")

        currentYield = 1
        len_string = len(string)

        # calculating total yield
        # if the returnString is True - String2Byte_yield will yield a total of len_string times + number of chunks the data is divided into two times , one for dividing and one for ecrypting + yield times of Byte2String_yield function - depends on the output size of the encryptor (general outputs of the normal chunk + output of the chunk which as less size)
        # else String2Byte_yield will yield a total of len_string times + number of chunks the data is divided into two times , one for dividing and one for ecrypting
        if(returnString):
            totalYields = int(len_string) + ((int(len_string // self.chunkSize)+1)*2) + int(((self.chunkSize__outputSize) * (len_string // self.chunkSize)) + self.__getOutputSize(len_string % self.chunkSize))
        else:
            totalYields = int(len_string) + ((int(len_string // self.chunkSize)+1)*2)

        # generator object of string 2 byte encoder
        # need to convert the string passed into byte to be able to encrypt by the fernet
        genObj_s2b_encode = encoderDecoders.String2Byte_yield.encode(string)

        # yield the process variables and get the result
        while(True):
            try:
                _ , _ = next(genObj_s2b_encode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                byteFromString = ex.value
                break


        len_byteFromString = len(byteFromString)

        # dividing data into chunks
        chunkList = []

        for i in range(0 , len_byteFromString , self.chunkSize):
            if((i+self.chunkSize) < len_byteFromString):
                chunkList.append(byteFromString[i : i + self.chunkSize]) 
            else:
                chunkList.append(byteFromString[i : ])

            yield currentYield , totalYields
            currentYield = currentYield + 1
        
        # if the return required is of string type 
        if(returnString):

            result = ""

            # encrypt each chunk using fernet and convert the byte back to string
            for i in chunkList:
                encrypted_byte = self.fernetObj.encrypt(i)

                yield currentYield , totalYields
                currentYield = currentYield + 1

                genObj_b2s_encode = encoderDecoders.Byte2String_yield.encode(encrypted_byte)

                while(True):
                    try:
                        _ , _ = next(genObj_b2s_encode)
                        yield currentYield , totalYields
                        currentYield = currentYield + 1

                    except StopIteration as ex:
                        stringFromByte = ex.value
                        break

                result = result + stringFromByte + ":~:~:"
        
        else:
            result = b""

            # encrypt each chunk using fernet
            for i in chunkList:
                encrypted_byte = self.fernetObj.encrypt(i)

                yield currentYield , totalYields
                currentYield = currentYield + 1

                result = result + encrypted_byte + b":~:~:"

        return result[:-5]












    # method to decrypt a string
    # returns decrypted string
    def decrypt_string_yield(self , enc_string):

        # type checking the parameters
        if(type(enc_string) != str):
            raise ValueError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        currentYield = 1
        len_string = len(enc_string)
        len_byteFromString = len_string // 3

        chunkList = enc_string.split(":~:~:")


        # calculating total yield
        # Byte2String yields len_byteFromString + number of chunks the data is divided into + yield of the String 2 byte decode function - 256 * total chunks + last chunk input size
        totalYields = int(len_byteFromString) + len(chunkList) + (256 * len(chunkList)) + (self.chunkSize__inputSize.get(len(chunkList[-1]) // 3))

        result = b""

        for i in chunkList:
            # generator object of byte 2 string decoder
            # need to convert back the string to byte - (byte to string was made in encryptor function)
            genObj_b2s_encode = encoderDecoders.Byte2String_yield.decode(i)

            # yield the process variables and get the result
            while(True):
                try:
                    _ , _ = next(genObj_b2s_encode)
                    yield currentYield , totalYields
                    currentYield = currentYield + 1

                except StopIteration as ex:
                    encbyte_From_encString = ex.value
                    break

            decrypted_byte = self.fernetObj.decrypt(encbyte_From_encString)
            result = result + decrypted_byte

            yield currentYield , totalYields
            currentYield = currentYield + 1


        # convert the byte object returned from fernet back to string
        genObj_s2b_decode  = encoderDecoders.String2Byte_yield.decode(result)

        while(True):
            try:
                _ , _ = next(genObj_s2b_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                stringFromByte = ex.value
                break

        return stringFromByte

    












    # method to decrypt a string
    # returns decrypted string
    # else returns a byte object
    def decrypt_byte_yield(self , enc_byte):

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise ValueError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))

        currentYield = 1
        len_enc_byte = len(enc_byte)

        chunkList = enc_byte.split(b":~:~:")

        # calculating total yield
        # number of chunks the data is divided into + yield of the String 2 byte decode function - 256 * total chunks + last chunk input size
        totalYields = len(chunkList) + (256 * len(chunkList)) + self.chunkSize__inputSize.get(len(chunkList[-1]))

        result = b""

        for i in chunkList:
            decrypted_byte = self.fernetObj.decrypt(i)
            result = result + decrypted_byte

            yield currentYield , totalYields
            currentYield = currentYield + 1


        # convert the byte object returned from fernet back to string
        genObj_s2b_decode  = encoderDecoders.String2Byte_yield.decode(result)

        while(True):
            try:
                _ , _ = next(genObj_s2b_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                stringFromByte = ex.value
                break

        return stringFromByte

















    # method to encrypt a string
    # returns encrypted string if returnString = True
    # else returns a byte object
    def encrypt(self , string , returnString = True):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(len(string) == 0):
            raise ValueError("empty string passed")

        # need to convert the string passed into byte to be able to encrypt by the fernet
        byteFromString = encoderDecoders.String2Byte.encode(string)

        len_byteFromString = len(byteFromString)

        # dividing data into chunks
        chunkList = []

        for i in range(0 , len_byteFromString , self.chunkSize):
            if((i+self.chunkSize) < len_byteFromString):
                chunkList.append(byteFromString[i : i + self.chunkSize]) 
            else:
                chunkList.append(byteFromString[i : ])

        
        # if the return required is of string type 
        if(returnString):

            result = ""

            # encrypt each chunk using fernet and convert the byte back to string
            for i in chunkList:
                encrypted_byte = self.fernetObj.encrypt(i)

                stringFromByte = encoderDecoders.Byte2String.encode(encrypted_byte)

                result = result + stringFromByte + ":~:~:"
        
        else:
            result = b""

            # encrypt each chunk using fernet
            for i in chunkList:
                encrypted_byte = self.fernetObj.encrypt(i)

                result = result + encrypted_byte + b":~:~:"

        return result[:-5]






























class BytesEncryptor:

    def __init__(self , password , iterations=390000):

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

        # init fernet object
        self.fernetObj = Fernet(key)

        self.chunkSize = 256
        self.chunkSize__outputSize = 440
        self.chunkSize__inputSize = {}
        self.__getInputSize()


    def __getInputSize(self , max=256):

        for i in range(max+1):
            outputSize = self.__getOutputSize(i)
            self.chunkSize__inputSize[outputSize] = i



    def __getOutputSize(self , inputSize):
        byte = b"h" * inputSize

        enc_byte = self.fernetObj.encrypt(byte)

        return len(enc_byte)








    # method to encrypt a string
    # returns a encrypted byte object
    def encrypt_yield(self , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise ValueError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        if(len(byte) == 0):
            raise ValueError("empty byte passed")

        currentYield = 1
        len_byte = len(byte)

        # calculating total yield
        # number of chunks the data is divided into two times , one for dividing and one for ecrypting 
        totalYields = (int(len_byte // self.chunkSize)+1)*2 

        # dividing data into chunks
        chunkList = []

        for i in range(0 , len_byte , self.chunkSize):
            if((i+self.chunkSize) < len_byte):
                chunkList.append(byte[i : i + self.chunkSize]) 
            else:
                chunkList.append(byte[i : ])

            yield currentYield , totalYields
            currentYield = currentYield + 1
        
        result = b""

        # encrypt each chunk using fernet
        for i in chunkList:
            encrypted_byte = self.fernetObj.encrypt(i)

            yield currentYield , totalYields
            currentYield = currentYield + 1

            result = result + encrypted_byte + b":~:~:"

        return result[:-5]











    # method to decrypt a byte
    # returns a bytes object
    def decrypt_yield(self , enc_byte):

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise ValueError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))

        currentYield = 1

        chunkList = enc_byte.split(b":~:~:")

        # calculating total yield
        # number of chunks the data is divided into 
        totalYields = len(chunkList)

        result = b""

        for i in chunkList:
            decrypted_byte = self.fernetObj.decrypt(i)
            result = result + decrypted_byte

            yield currentYield , totalYields
            currentYield = currentYield + 1

        return result
















    # method to encrypt a string
    # returns a encrypted byte object
    def encrypt(self , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise ValueError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        if(len(byte) == 0):
            raise ValueError("empty byte passed")

        currentYield = 1
        len_byte = len(byte)

        # dividing data into chunks
        chunkList = []

        for i in range(0 , len_byte , self.chunkSize):
            if((i+self.chunkSize) < len_byte):
                chunkList.append(byte[i : i + self.chunkSize]) 
            else:
                chunkList.append(byte[i : ])

        result = b""

        # encrypt each chunk using fernet
        for i in chunkList:
            encrypted_byte = self.fernetObj.encrypt(i)

            result = result + encrypted_byte + b":~:~:"

        return result[:-5]











    # method to decrypt a byte
    # returns a bytes object
    def decrypt(self , enc_byte):

        # type checking the parameters
        if(type(enc_byte) != bytes):
            raise ValueError("enc_byte parameter expected to be of bytes type instead got {} type".format(type(enc_byte)))

        currentYield = 1

        chunkList = enc_byte.split(b":~:~:")

        result = b""

        for i in chunkList:
            decrypted_byte = self.fernetObj.decrypt(i)
            result = result + decrypted_byte

        return result
    



























def __test():

    obj = StringEncryptor("hello world")

    myString = "my name is john"

    print("\nlen myString string = {}\n".format(len(myString)))

    encryptedString = obj.encrypt(myString , True)

    print("\nencrypted string = {}\n".format(encryptedString))

    decryptedString = obj.decrypt_string(encryptedString)

    print("\ndecrypted string = {}\n".format(decryptedString))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")







def __test1():

    obj = StringEncryptor("hello world")

    myString = "my name is john"

    print("\nlen myString string = {}\n".format(len(myString)))

    encryptedByte = obj.encrypt(myString , False)

    print("\n encryptedByte = {}\n".format(encryptedByte))

    decryptedString = obj.decrypt_byte(encryptedByte)

    print("\n decryptedString = {}\n".format(decryptedString))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")








def __test2():

    obj = StringEncryptor("hello world")

    myString = "my name is john" * 1123

    print("\nlen myString string = {}\n".format(len(myString)))

    objGen_encryptor = obj.encrypt_yield(myString , True)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_encryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    print("\nlen encrypted string = {}\n".format(len(encryptedString)))

    objGen_decryptor = obj.decrypt_string_yield(encryptedString)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_decryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print("\nlen decryptedString = {}\n".format(len(decryptedString)))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")








def __test3():

    obj = StringEncryptor("hello world")

    myString = "my name is john" * 1123

    print("\nlen myString string = {}\n".format(len(myString)))

    objGen_encryptor = obj.encrypt_yield(myString , False)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_encryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    print("\nlen encryptedByte = {}\n".format(len(encryptedByte)))

    objGen_decryptor = obj.decrypt_byte_yield(encryptedByte)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_decryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print("\nlen decryptedString = {}\n".format(len(decryptedString)))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")









def __test4():

    obj = ByteEncryptor("hello world")

    myByte = b"my name is john" * 11233

    print("\nlen myByte = {}\n".format(len(myByte)))

    objGen_encryptor = obj.encrypt_yield(myByte)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_encryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    print("\nlen encrypted byte = {}\n".format(len(encryptedByte)))

    objGen_decryptor = obj.decrypt_yield(encryptedByte)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_decryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    print("\nlen decryptedByte = {}\n".format(len(decryptedByte)))

    if(decryptedByte == myByte):
        print("\nok")
    else:
        print("\nerror")











def __test5():

    obj = ByteEncryptor("hello world")

    myByte = b"my name is john"

    print("\nlen myByte = {}\n".format(len(myByte)))

    encryptedByte = obj.encrypt(myByte)

    print("\nencryptedByte = {}\n".format(encryptedByte))

    decryptedByte = obj.decrypt(encryptedByte)

    print("\ndecryptedByte = {}\n".format(decryptedByte))

    if(decryptedByte == myByte):
        print("\nok")
    else:
        print("\nerror")



if __name__ == "__main__":
    __test5()
