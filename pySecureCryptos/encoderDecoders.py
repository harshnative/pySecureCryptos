import binascii
from numpy import base_repr
import string
import base64


#  _               _                 _                        _            _                  
# | |__    _   _  | |_    ___       | |_    ___         ___  | |_   _ __  (_)  _ __     __ _  
# | '_ \  | | | | | __|  / _ \      | __|  / _ \       / __| | __| | '__| | | | '_ \   / _` | 
# | |_) | | |_| | | |_  |  __/      | |_  | (_) |      \__ \ | |_  | |    | | | | | | | (_| | 
# |_.__/   \__, |  \__|  \___|       \__|  \___/       |___/  \__| |_|    |_| |_| |_|  \__, | 
#          |___/                                                                       |___/  

# class containing method to encode or decode any byte 
class Byte2String:

    # method to convert any byte into string
    @classmethod
    def encode(cls , byte : bytes) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))


        """
        ALGO - 
        convert each byte into int - result = int btw 0 to 255

        convert the int into string type. 

        make the int string 3 chars long means if the string is 49 convert to 049

        append to main string and return main string
        """

        string = ""

        for i in byte:
            i = str(int(i))
            i = ("0" * (3 - len(i))) + i 
            string = string + i

        return string

    # method to convert the output string from above method into byte again
    # returns a bytes type object
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        """
        ALGO - 

        traverse the string and slice the string into 3 chars long

        convert the string back to int

        pass the int list to bytes and return
        """

        intList = []

        for i in range(0 , len(string) , 3):
            toAppend = int(string[i : i + 3])
            intList.append(toAppend)

        return bytes(intList)














#        _            _                        _                  _               _           
#  ___  | |_   _ __  (_)  _ __     __ _       | |_    ___        | |__    _   _  | |_    ___  
# / __| | __| | '__| | | | '_ \   / _` |      | __|  / _ \       | '_ \  | | | | | __|  / _ \ 
# \__ \ | |_  | |    | | | | | | | (_| |      | |_  | (_) |      | |_) | | |_| | | |_  |  __/ 
# |___/  \__| |_|    |_| |_| |_|  \__, |       \__|  \___/       |_.__/   \__, |  \__|  \___| 
#                                 |___/                                   |___/               

class String2Byte:

    # method to convert string to byte
    # returns bytes
    @classmethod
    def encode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        """
        convert each char in string to corresponding ASCII value (int)

        convert this intList to bytes
        """
        intList = []

        for i in string:
            intList.append(ord(i))

        return bytes(intList)



    @classmethod
    def decode(cls , byte : bytes) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        string = ""

        for i in byte:
            i = chr(int(i))
            string = string + i

        return string

        





















#  _               _                 _                        _            _                  
# | |__    _   _  | |_    ___       | |_    ___         ___  | |_   _ __  (_)  _ __     __ _  
# | '_ \  | | | | | __|  / _ \      | __|  / _ \       / __| | __| | '__| | | | '_ \   / _` | 
# | |_) | | |_| | | |_  |  __/      | |_  | (_) |      \__ \ | |_  | |    | | | | | | | (_| | 
# |_.__/   \__, |  \__|  \___|       \__|  \___/       |___/  \__| |_|    |_| |_| |_|  \__, | 
#          |___/                                                                       |___/  


# class containing method to encode or decode any byte 
class Byte2String_yield:

    # method to convert any byte into string
    @classmethod
    def encode(cls , byte : bytes) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        """
        ALGO - 
        convert each byte into int - result = int btw 0 to 255

        convert the int into string type. 

        make the int string 3 chars long means if the string is 49 convert to 049

        append to main string and return main string
        """

        string = ""

        totalCount = len(byte)
        currentCount = 0

        for i in byte:
            i = str(int(i))
            i = ("0" * (3 - len(i))) + i 
            string = string + i

            currentCount = currentCount + 1
            yield currentCount , totalCount

        return string


    # method to convert the output string from above method into byte again
    # returns a bytes type object
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        """
        ALGO - 

        traverse the string and slice the string into 3 chars long

        convert the string back to int

        pass the int list to bytes and return
        """

        intList = []

        totalCount = len(string) // 3 + 1
        currentCount = 0

        for i in range(0 , len(string) , 3):
            toAppend = int(string[i : i + 3])
            intList.append(toAppend)

            currentCount = currentCount + 1
            yield currentCount , totalCount

        return bytes(intList)













#        _            _                        _                  _               _           
#  ___  | |_   _ __  (_)  _ __     __ _       | |_    ___        | |__    _   _  | |_    ___  
# / __| | __| | '__| | | | '_ \   / _` |      | __|  / _ \       | '_ \  | | | | | __|  / _ \ 
# \__ \ | |_  | |    | | | | | | | (_| |      | |_  | (_) |      | |_) | | |_| | | |_  |  __/ 
# |___/  \__| |_|    |_| |_| |_|  \__, |       \__|  \___/       |_.__/   \__, |  \__|  \___| 
#                                 |___/                                   |___/               


class String2Byte_yield:

    # method to convert string to byte
    # returns bytes
    @classmethod
    def encode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        """
        convert each char in string to corresponding ASCII value (int)

        convert this intList to bytes
        """
        intList = []

        totalCount = len(string)
        currentCount = 0

        for i in string:
            intList.append(ord(i))

            currentCount = currentCount + 1
            yield currentCount , totalCount

        return bytes(intList)


    @classmethod
    def decode(cls , byte : bytes) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        string = ""

        totalCount = len(byte)
        currentCount = 0

        for i in byte:
            i = chr(int(i))
            string = string + i

            currentCount = currentCount + 1
            yield currentCount , totalCount

        return string





















#  _                                                                       _                   
# | |__     ___  __  __        ___    ___    _ __   __   __   ___   _ __  | |_    ___    _ __  
# | '_ \   / _ \ \ \/ /       / __|  / _ \  | '_ \  \ \ / /  / _ \ | '__| | __|  / _ \  | '__| 
# | | | | |  __/  >  <       | (__  | (_) | | | | |  \ V /  |  __/ | |    | |_  | (_) | | |    
# |_| |_|  \___| /_/\_\       \___|  \___/  |_| |_|   \_/    \___| |_|     \__|  \___/  |_|    
                                                                                             



# convert byte to hex and vice versa
class HexConvertor:

    # encode byte into string
    # hexlify function returns hex in byte format , which needs to be encoded in string
    @classmethod
    def encode(cls , byte : bytes) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        return str(binascii.hexlify(byte) , "utf-8")


    # function to convert the encoded string into byte
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        return binascii.unhexlify(bytes(string , "utf-8"))



    # generator version
    # encode byte into string
    @classmethod
    def encode_yield(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        currentYield = 1
        totalYield = (lenByte // chunkSize) + 1

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(binascii.hexlify(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode_yield(cls , string : str , chunkSize : int = 1) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkSize = chunkSize * 1024 * 1024 * 2
        
        result = b""

        lenString = len(string)

        currentYield = 1
        totalYield = (lenString // chunkSize) + 1

        # decode each chunk
        for i in range(0 , lenString , chunkSize):
            byteFromString = binascii.unhexlify(bytes(string[i : i+chunkSize] , "utf-8"))
            result = result + byteFromString

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield
        return result 

    































#  _                            ____     __     _____                              _                
# | |__     __ _   ___    ___  |___ \   / /_   | ____|  _ __     ___    ___     __| |   ___   _ __  
# | '_ \   / _` | / __|  / _ \   __) | | '_ \  |  _|   | '_ \   / __|  / _ \   / _` |  / _ \ | '__| 
# | |_) | | (_| | \__ \ |  __/  / __/  | (_) | | |___  | | | | | (__  | (_) | | (_| | |  __/ | |    
# |_.__/   \__,_| |___/  \___| |_____|  \___/  |_____| |_| |_|  \___|  \___/   \__,_|  \___| |_|    
                                                                                                  




# convert byte to base 36 and vice versa
# class Base36Encoder:

#     # encode byte into string
#     @classmethod
#     def encode(cls , byte : bytes , chunkSize : int = 128) -> str:
        

#         # type checking the parameters
#         if(type(byte) != bytes):
#             raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

#         # type checking the parameters
#         if(type(chunkSize) != int):
#             raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


#         # convert chunk size into bytes
#         lenByte = len(byte)

#         result = ""

#         # encode each chunk
#         # output chunk size is twice the input chunk size
#         for i in range(0 , lenByte , chunkSize):
#             hex_from_byte = binascii.hexlify(byte[i : i+chunkSize])
#             decimal_from_hex = int(hex_from_byte , 16)
#             base36_from_decimal = base_repr(decimal_from_hex , 36)

#             result = result + base36_from_decimal + "-"

#         result = result[:-1]
#         return result 




#     # decode - convert encoded string back to byte
#     @classmethod
#     def decode(cls , string : str) -> bytes:

#         # type checking the parameters
#         if(type(string) != str):
#             raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


#         # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
#         chunkList = string.split("-")
        
#         result = b""

#         # decode each chunk
#         for i in chunkList:
#             decimal_from_base36 = int(i , 36)
#             hex_from_decimal = hex(decimal_from_base36)
#             byte_from_hex = binascii.unhexlify(hex_from_decimal[2:])

#             result = result + byte_from_hex

#         return result 



#     # generator version
#     # encode byte into string
#     @classmethod
#     def encode_yield(cls , byte : bytes , chunkSize : int = 128) -> str:
        

#         # type checking the parameters
#         if(type(byte) != bytes):
#             raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

#         # type checking the parameters
#         if(type(chunkSize) != int):
#             raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


#         # convert chunk size into bytes
#         lenByte = len(byte)

#         result = ""

#         currentYield = 1
#         totalYield = (lenByte // chunkSize) + 1

#         # encode each chunk
#         # output chunk size is twice the input chunk size
#         for i in range(0 , lenByte , chunkSize):
#             hex_from_byte = binascii.hexlify(byte[i : i+chunkSize])
#             decimal_from_hex = int(hex_from_byte , 16)
#             base36_from_decimal = base_repr(decimal_from_hex , 36)

#             result = result + base36_from_decimal + "-"

#             yield currentYield , totalYield
#             currentYield = currentYield + 1

#         if(currentYield <= totalYield):
#             yield totalYield , totalYield

#         result = result[:-1]
#         return result 



#     # generator verion
#     # decode - convert encoded string back to byte
#     @classmethod
#     def decode_yield(cls , string : str) -> bytes:

#         # type checking the parameters
#         if(type(string) != str):
#             raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


#         # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
#         chunkList = string.split("-")
        
#         result = b""

#         currentYield = 1
#         totalYield = len(chunkList)

#         # decode each chunk
#         for i in chunkList:
#             decimal_from_base36 = int(i , 36)
#             hex_from_decimal = hex(decimal_from_base36)
#             byte_from_hex = binascii.unhexlify(hex_from_decimal[2:])

#             result = result + byte_from_hex


#             yield currentYield , totalYield
#             currentYield = currentYield + 1

#         if(currentYield <= totalYield):
#             yield totalYield , totalYield
#         return result 

    




























#  ____                          ___     ___    _____                              _                
# | __ )    __ _   ___    ___   / _ \   / _ \  | ____|  _ __     ___    ___     __| |   ___   _ __  
# |  _ \   / _` | / __|  / _ \ | (_) | | | | | |  _|   | '_ \   / __|  / _ \   / _` |  / _ \ | '__| 
# | |_) | | (_| | \__ \ |  __/  \__, | | |_| | | |___  | | | | | (__  | (_) | | (_| | |  __/ | |    
# |____/   \__,_| |___/  \___|    /_/   \___/  |_____| |_| |_|  \___|  \___/   \__,_|  \___| |_|    
                                                                                                  


# # convert byte to base 90 and vice versa
# class Base90Encoder:


#     def __init__(self):
#         printableChars = list(string.printable[:-5])
#         printableChars.remove("'")
#         printableChars.remove('"')
#         printableChars.remove('\\')
#         printableChars.remove('`')
#         printableChars.remove(' ')

#         self.printableChars = printableChars

#         power_cache = []

#         for i in range(4096):
#             power_cache.append(90 ** i)

#         self.power_cache = power_cache



#     def _base90encoder(self , integer):
#         base90 = ""

#         while(integer >= 90):
#             rem = integer % 90
#             integer = integer // 90
#             base90 = base90 + self.printableChars[rem]

#         base90 = base90 + self.printableChars[integer]

#         return base90



#     def _base90decoder(self , base90):
#         finalint = 0

#         for index , char in enumerate(base90):

#             indexValue_valueArray = None

#             for i,j in enumerate(self.printableChars):
#                 if(j == char):
#                     indexValue_valueArray = i

            
#             finalint = finalint + (indexValue_valueArray * self.power_cache[index])
            
#         return finalint



#     # generator version
#     # encode byte into string
#     def encode_yield(self , byte : bytes) -> str:
        

#         # type checking the parameters
#         if(type(byte) != bytes):
#             raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

#         # convert chunk size into bytes
#         chunkSize = 2048
        
#         # convert chunk size into bytes
#         lenByte = len(byte)

#         result = ""

#         currentYield = 1
#         totalYield = (lenByte // chunkSize) + 1

#         # encode each chunk
#         # output chunk size is twice the input chunk size
#         for i in range(0 , lenByte , chunkSize):
#             hex_from_byte = binascii.hexlify(byte[i : i+chunkSize])
#             decimal_from_hex = int(hex_from_byte , 16)
#             base36_from_decimal = self._base90encoder(decimal_from_hex)

#             result = result + base36_from_decimal + " "

#             yield currentYield , totalYield
#             currentYield = currentYield + 1

#         if(currentYield <= totalYield):
#             yield totalYield , totalYield

#         result = result[:-1]
#         return result 


    


#     # generator verion
#     # decode - convert encoded string back to byte
#     def decode_yield(self , string : str) -> bytes:

#         # type checking the parameters
#         if(type(string) != str):
#             raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


#         # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
#         chunkList = string.split(" ")
        
#         result = b""

#         currentYield = 1
#         totalYield = len(chunkList)

#         # decode each chunk
#         for i in chunkList:
#             decimal_from_base36 = self._base90decoder(i)
#             hex_from_decimal = hex(decimal_from_base36)
#             byte_from_hex = binascii.unhexlify(hex_from_decimal[2:])

#             result = result + byte_from_hex


#             yield currentYield , totalYield
#             currentYield = currentYield + 1

#         if(currentYield <= totalYield):
#             yield totalYield , totalYield
#         return result 






#     # generator version
#     # encode byte into string
#     def encode(self , byte : bytes) -> str:
        

#         # type checking the parameters
#         if(type(byte) != bytes):
#             raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

#         # convert chunk size into bytes
#         chunkSize = 2048
        
#         # convert chunk size into bytes
#         lenByte = len(byte)

#         result = ""

#         # encode each chunk
#         # output chunk size is twice the input chunk size
#         for i in range(0 , lenByte , chunkSize):
#             hex_from_byte = binascii.hexlify(byte[i : i+chunkSize])
#             decimal_from_hex = int(hex_from_byte , 16)
#             base36_from_decimal = self._base90encoder(decimal_from_hex)

#             result = result + base36_from_decimal + " "

#         result = result[:-1]
#         return result 


    


#     # generator verion
#     # decode - convert encoded string back to byte
#     def decode(self , string : str) -> bytes:

#         # type checking the parameters
#         if(type(string) != str):
#             raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


#         # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
#         chunkList = string.split(" ")
        
#         result = b""

#         # decode each chunk
#         for i in chunkList:
#             decimal_from_base36 = self._base90decoder(i)
#             hex_from_decimal = hex(decimal_from_base36)
#             byte_from_hex = binascii.unhexlify(hex_from_decimal[2:])

#             result = result + byte_from_hex

#         return result 























#  ____                          __     _  _              __     _  _    
# | __ )    __ _   ___    ___   / /_   | || |            / /_   | || |   
# |  _ \   / _` | / __|  / _ \ | '_ \  | || |_          | '_ \  | || |_  
# | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|         | (_) | |__   _| 
# |____/   \__,_| |___/  \___|  \___/     |_|    _____   \___/     |_|   
#                                               |_____|                  


class Base64_64():
    # generator version
    # encode byte into string
    @classmethod
    def encode(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b64encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""


        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b64decode(bytes(i , "utf-8"))
            result = result + byteFromString

        return result



    # generator version
    # encode byte into string
    @classmethod
    def encode_yield(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        currentYield = 1
        totalYield = (lenByte // chunkSize) + 1

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b64encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode_yield(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""

        currentYield = 1
        totalYield = len(chunkList)

        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b64decode(bytes(i , "utf-8"))
            result = result + byteFromString

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield
        return result

    
























#  ____                          __     _  _             _    __    
# | __ )    __ _   ___    ___   / /_   | || |           / |  / /_   
# |  _ \   / _` | / __|  / _ \ | '_ \  | || |_          | | | '_ \  
# | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|         | | | (_) | 
# |____/   \__,_| |___/  \___|  \___/     |_|    _____  |_|  \___/  
#                                               |_____|             



class Base64_16():
    # generator version
    # encode byte into string
    @classmethod
    def encode(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b16encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""


        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b16decode(bytes(i , "utf-8"))
            result = result + byteFromString

        return result



    # generator version
    # encode byte into string
    @classmethod
    def encode_yield(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        currentYield = 1
        totalYield = (lenByte // chunkSize) + 1

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b16encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode_yield(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""

        currentYield = 1
        totalYield = len(chunkList)

        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b16decode(bytes(i , "utf-8"))
            result = result + byteFromString

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield
        return result

    











































#  ____                          __     _  _             _____   ____   
# | __ )    __ _   ___    ___   / /_   | || |           |___ /  |___ \  
# |  _ \   / _` | / __|  / _ \ | '_ \  | || |_            |_ \    __) | 
# | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|          ___) |  / __/  
# |____/   \__,_| |___/  \___|  \___/     |_|    _____  |____/  |_____| 
#                                               |_____|                 


class Base64_32():
    # generator version
    # encode byte into string
    @classmethod
    def encode(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b32encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""


        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b32decode(bytes(i , "utf-8"))
            result = result + byteFromString

        return result



    # generator version
    # encode byte into string
    @classmethod
    def encode_yield(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        currentYield = 1
        totalYield = (lenByte // chunkSize) + 1

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b32encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode_yield(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""

        currentYield = 1
        totalYield = len(chunkList)

        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b32decode(bytes(i , "utf-8"))
            result = result + byteFromString

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield
        return result




































#  ____                          __     _  _              ___    ____   
# | __ )    __ _   ___    ___   / /_   | || |            ( _ )  | ___|  
# |  _ \   / _` | / __|  / _ \ | '_ \  | || |_           / _ \  |___ \  
# | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|         | (_) |  ___) | 
# |____/   \__,_| |___/  \___|  \___/     |_|    _____   \___/  |____/  
#                                               |_____|                 


class Base64_85():
    # generator version
    # encode byte into string
    @classmethod
    def encode(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b85encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""


        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b85decode(bytes(i , "utf-8"))
            result = result + byteFromString

        return result



    # generator version
    # encode byte into string
    @classmethod
    def encode_yield(cls , byte : bytes , chunkSize : int = 1) -> str:
        

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size into bytes
        chunkSize = chunkSize * 1024 * 1024
        
        lenByte = len(byte)

        result = ""

        currentYield = 1
        totalYield = (lenByte // chunkSize) + 1

        # encode each chunk
        # output chunk size is twice the input chunk size
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(base64.b85encode(byte[i : i+chunkSize]) , "utf-8")
            result = result + stringFromByte + ":__:"

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield

        result = result[:-4]
        return result 


    # generator verion
    # decode - convert encoded string back to byte
    @classmethod
    def decode_yield(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))


        # convert chunk size into bytes , chunk before decoding is twice the size of decoded chunk
        chunkList = string.split(":__:")
        
        result = b""

        currentYield = 1
        totalYield = len(chunkList)

        # decode each chunk
        for i in chunkList:
            byteFromString = base64.b85decode(bytes(i , "utf-8"))
            result = result + byteFromString

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield
        return result

























#  ____         ____         ____                              ____   
# / ___|       |___ \       | __ )                    __   __ |___ \  
# \___ \         __) |      |  _ \        _____       \ \ / /   __) | 
#  ___) |       / __/       | |_) |      |_____|       \ V /   / __/  
# |____/       |_____|      |____/                      \_/   |_____| 
                                                                    
           

class String2Byte_v2:

    # method to convert string to byte using utf-8 encoding
    @classmethod
    def encode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        return bytes(string , "utf-8")


    # method to convert byte again to string using utf-8 encoding
    @classmethod
    def decode(cls , byte : bytes) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        return str(byte , "utf-8")


    # generator version of the encoder
    # chunk size in MB
    @classmethod
    def encode_yield(cls , string : str , chunkSize : int = 1) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        # convert chunk size to bytes
        chunkSize = chunkSize * 1024 * 1024
        
        result = b""

        lenString = len(string)

        currentYield = 1
        totalYield = (lenString // chunkSize) + 1

        # encode each chunk
        # chunk and encoded chunk are of same size
        for i in range(0 , lenString , chunkSize):
            byteFromString = bytes(string[i : i+chunkSize] , "utf-8")
            result = result + byteFromString

            yield currentYield , totalYield
            currentYield = currentYield + 1
        
        if(currentYield <= totalYield):
            yield totalYield , totalYield

        return result



    # generator version of the decoder
    @classmethod
    def decode_yield(cls , byte : bytes , chunkSize : int = 1) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))
        
        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size to bytes
        chunkSize = chunkSize * 1024 * 1024

        result = ""

        lenByte = len(byte)

        currentYield = 1
        totalYield = (lenByte // chunkSize) + 1

        # decode each chunk
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(byte[i : i+chunkSize] , "utf-8")
            result = result + stringFromByte

            yield currentYield , totalYield
            currentYield = currentYield + 1


        if(currentYield <= totalYield):
            yield totalYield , totalYield
        return result





















#  ____         ____         ____                              ____   
# | __ )       |___ \       / ___|                    __   __ |___ \  
# |  _ \         __) |      \___ \        _____       \ \ / /   __) | 
# | |_) |       / __/        ___) |      |_____|       \ V /   / __/  
# |____/       |_____|      |____/                      \_/   |_____| 
                                                                    


class Byte2String_v2:

    # method to convert byte to string
    # does not encode every type of byte
    @classmethod
    def encode(cls , byte : bytes) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        return str(byte , "utf-8")


    # method to convert the string back to byte
    @classmethod
    def decode(cls , string : str) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        return bytes(string , "utf-8")


    # generator version of the encoder
    # chunk size in MB
    @classmethod
    def encode_yield(cls , byte : bytes , chunkSize : int = 1) -> str:

        # type checking the parameters
        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))


        # convert chunk size to bytes from MB
        chunkSize = chunkSize * 1024 * 1024
        
        result = ""

        lenByte = len(byte)

        currentYield = 1
        totalYield = (lenByte // chunkSize) + 1

        # encode each chunk
        # the chunk and encoded chunk are of the same length
        for i in range(0 , lenByte , chunkSize):
            stringFromByte = str(byte[i : i+chunkSize] , "utf-8")
            result = result + stringFromByte

            yield currentYield , totalYield
            currentYield = currentYield + 1
        
        if(currentYield <= totalYield):
            yield totalYield , totalYield

        return result




    # generator version of the decoder
    @classmethod
    def decode_yield(cls , string : str , chunkSize : int = 1) -> bytes:

        # type checking the parameters
        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))
        
        # type checking the parameters
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        # chunk size to bytes to MB
        chunkSize = chunkSize * 1024 * 1024

        result = b""

        lenString = len(string)

        currentYield = 1
        totalYield = (lenString // chunkSize) + 1

        # decode each chunk
        for i in range(0 , lenString , chunkSize):
            stringFromByte = bytes(string[i : i+chunkSize] , "utf-8")
            result = result + stringFromByte

            yield currentYield , totalYield
            currentYield = currentYield + 1

        if(currentYield <= totalYield):
            yield totalYield , totalYield
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







#  _                  _                       _               _                 _                        _            _                  
# | |_    ___   ___  | |_                    | |__    _   _  | |_    ___       | |_    ___         ___  | |_   _ __  (_)  _ __     __ _  
# | __|  / _ \ / __| | __|       _____       | '_ \  | | | | | __|  / _ \      | __|  / _ \       / __| | __| | '__| | | | '_ \   / _` | 
# | |_  |  __/ \__ \ | |_       |_____|      | |_) | | |_| | | |_  |  __/      | |_  | (_) |      \__ \ | |_  | |    | | | | | | | (_| | 
#  \__|  \___| |___/  \__|                   |_.__/   \__, |  \__|  \___|       \__|  \___/       |___/  \__| |_|    |_| |_| |_|  \__, | 
#                                                     |___/                                                                       |___/  


# function to test the above class
def __test():
    myString = b"hello world"

    stringFromByte = Byte2String.encode(myString)

    print(stringFromByte , type(stringFromByte))

    byteAgain = Byte2String.decode(stringFromByte)

    print(byteAgain)


# function to test the above class
def __test2():


    # big object to encode decode 
    myByte = b"hello world" * 1000

    # creating the generator obj for the method
    generatorObj_encode = Byte2String_yield.encode(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    
    print("\n")

    # similarly for decode
    generatorObj_decode = Byte2String_yield.decode(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    if(byteAgain == myByte):
        print("\nok")
    else:
        print("\nerror")






























#  _                  _                             _            _                        _                  _               _           
# | |_    ___   ___  | |_                     ___  | |_   _ __  (_)  _ __     __ _       | |_    ___        | |__    _   _  | |_    ___  
# | __|  / _ \ / __| | __|       _____       / __| | __| | '__| | | | '_ \   / _` |      | __|  / _ \       | '_ \  | | | | | __|  / _ \ 
# | |_  |  __/ \__ \ | |_       |_____|      \__ \ | |_  | |    | | | | | | | (_| |      | |_  | (_) |      | |_) | | |_| | | |_  |  __/ 
#  \__|  \___| |___/  \__|                   |___/  \__| |_|    |_| |_| |_|  \__, |       \__|  \___/       |_.__/   \__, |  \__|  \___| 
#                                                                            |___/                                   |___/               


# function to test the above class
def __test3():
    myByte = "hello world"

    byteFromString = String2Byte.encode(myByte)

    print(byteFromString , type(byteFromString))

    stringAgain = String2Byte.decode(byteFromString)

    print(stringAgain)


# function to test the above class
def __test4():


    # big object to encode decode 
    myString = "hello world" * 1000

    # creating the generator obj for the method
    generatorObj_encode = String2Byte_yield.encode(myString)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            byteFromString = ex.value
            break

    
    # similarly for decode
    generatorObj_decode = String2Byte_yield.decode(byteFromString)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            stringAgain = ex.value
            break

    if(stringAgain == myString):
        print("\nok")
    else:
        print("\nerror")





















#  _                  _          _                                                                       _                   
# | |_    ___   ___  | |_       | |__     ___  __  __        ___    ___    _ __   __   __   ___   _ __  | |_    ___    _ __  
# | __|  / _ \ / __| | __|      | '_ \   / _ \ \ \/ /       / __|  / _ \  | '_ \  \ \ / /  / _ \ | '__| | __|  / _ \  | '__| 
# | |_  |  __/ \__ \ | |_       | | | | |  __/  >  <       | (__  | (_) | | | | |  \ V /  |  __/ | |    | |_  | (_) | | |    
#  \__|  \___| |___/  \__|      |_| |_|  \___| /_/\_\       \___|  \___/  |_| |_|   \_/    \___| |_|     \__|  \___/  |_|    
                                                                                                                           


def __test_HexConvertor():

    myByte = b"hello world"

    stringFromByte = HexConvertor.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = HexConvertor.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")




def __test_HexConvertor2():


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = HexConvertor.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = HexConvertor.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")

    























#  _                  _             ____                         _____    __     _____                              _                
# | |_    ___   ___  | |_          | __ )    __ _   ___    ___  |___ /   / /_   | ____|  _ __     ___    ___     __| |   ___   _ __  
# | __|  / _ \ / __| | __|  _____  |  _ \   / _` | / __|  / _ \   |_ \  | '_ \  |  _|   | '_ \   / __|  / _ \   / _` |  / _ \ | '__| 
# | |_  |  __/ \__ \ | |_  |_____| | |_) | | (_| | \__ \ |  __/  ___) | | (_) | | |___  | | | | | (__  | (_) | | (_| | |  __/ | |    
#  \__|  \___| |___/  \__|         |____/   \__,_| |___/  \___| |____/   \___/  |_____| |_| |_|  \___|  \___/   \__,_|  \___| |_|    
                                                                                                                                   


def __test_Base36Encoder():

    myByte = b"hello world"

    stringFromByte = Base36Encoder.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base36Encoder.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")




def __test_Base36Encoder2():


    # big object to encode decode 
    myByte = b"h" * 1024 * 1024

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base36Encoder.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base36Encoder.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")

    

















#  _                  _             ____                          ___     ___    _____                              _                
# | |_    ___   ___  | |_          | __ )    __ _   ___    ___   / _ \   / _ \  | ____|  _ __     ___    ___     __| |   ___   _ __  
# | __|  / _ \ / __| | __|         |  _ \   / _` | / __|  / _ \ | (_) | | | | | |  _|   | '_ \   / __|  / _ \   / _` |  / _ \ | '__| 
# | |_  |  __/ \__ \ | |_          | |_) | | (_| | \__ \ |  __/  \__, | | |_| | | |___  | | | | | (__  | (_) | | (_| | |  __/ | |    
#  \__|  \___| |___/  \__|  _____  |____/   \__,_| |___/  \___|    /_/   \___/  |_____| |_| |_|  \___|  \___/   \__,_|  \___| |_|    
#                          |_____|                                                                                                   


def __test_Base90Encoder():

    myByte = b"hello world"

    obj = Base90Encoder()

    stringFromByte = obj.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = obj.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")






def __test_Base90Encoder2():


    # big object to encode decode 
    myByte = b"h" * 1024 * 1024

    print("myByte len = " , len(myByte) , "\n")

    obj = Base90Encoder()

    # creating the generator obj for the method
    generatorObj_encode = obj.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = obj.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")




















#  _                  _                             _            ____    _               _                         ____   
# | |_    ___   ___  | |_                     ___  | |_   _ __  |___ \  | |__    _   _  | |_    ___       __   __ |___ \  
# | __|  / _ \ / __| | __|       _____       / __| | __| | '__|   __) | | '_ \  | | | | | __|  / _ \      \ \ / /   __) | 
# | |_  |  __/ \__ \ | |_       |_____|      \__ \ | |_  | |     / __/  | |_) | | |_| | | |_  |  __/       \ V /   / __/  
#  \__|  \___| |___/  \__|                   |___/  \__| |_|    |_____| |_.__/   \__, |  \__|  \___|        \_/   |_____| 
#                                                                                |___/                                    


def __test_string2bytev2():


    # big object to encode decode 
    myString = "hello world" * 1024 * 1024 * 8

    print("str len = " , len(myString) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = String2Byte_v2.encode_yield(myString)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            byteFromString = ex.value
            break

    print("byteFromString len = " , len(byteFromString) , "\n")
    
    # similarly for decode
    generatorObj_decode = String2Byte_v2.decode_yield(byteFromString)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            stringAgain = ex.value
            break

    print("stringAgain len = " , len(stringAgain) , "\n")

    if(stringAgain == myString):
        print("\nok")
    else:
        print("\nerror")







def __test_string2bytev2_2():


    # big object to encode decode 
    myString = "hello world"

    print("myString = " , myString)
    print("str len = " , len(myString) , "\n")

    # creating the generator obj for the method
    byteFromString = String2Byte_v2.encode(myString)

    print("byteFromString = " , byteFromString)
    print("byteFromString len = " , len(byteFromString) , "\n")
    
    # similarly for decode
    stringAgain = String2Byte_v2.decode(byteFromString)

    print("stringAgain = " , stringAgain)
    print("stringAgain len = " , len(stringAgain) , "\n")

    if(stringAgain == myString):
        print("\nok")
    else:
        print("\nerror")


























#  _                  _          _       ____                                    ____   
# | |_    ___   ___  | |_       | |__   |___ \   ___                    __   __ |___ \  
# | __|  / _ \ / __| | __|      | '_ \    __) | / __|       _____       \ \ / /   __) | 
# | |_  |  __/ \__ \ | |_       | |_) |  / __/  \__ \      |_____|       \ V /   / __/  
#  \__|  \___| |___/  \__|      |_.__/  |_____| |___/                     \_/   |_____| 
                                                                                      



def __test_byte2stringv2():


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 8

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Byte2String_v2.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Byte2String_v2.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")






def __test_byte2stringv2_2():


    # big object to encode decode 
    myByte = b"hello world"

    print("myByte = " , myByte)
    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    stringFromByte = Byte2String_v2.encode(myByte)

    print("stringFromByte = " , stringFromByte)
    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    byteAgain = Byte2String_v2.decode(stringFromByte)

    print("byteAgain = " , byteAgain)
    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")


















#  _                  _             ____                          __     _  _              __     _  _    
# | |_    ___   ___  | |_          | __ )    __ _   ___    ___   / /_   | || |            / /_   | || |   
# | __|  / _ \ / __| | __|         |  _ \   / _` | / __|  / _ \ | '_ \  | || |_          | '_ \  | || |_  
# | |_  |  __/ \__ \ | |_          | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|         | (_) | |__   _| 
#  \__|  \___| |___/  \__|  _____  |____/   \__,_| |___/  \___|  \___/     |_|    _____   \___/     |_|   
#                          |_____|                                               |_____|                  



def __test_Base64_64():

    myByte = b"hello world"

    stringFromByte = Base64_64.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_64.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")




def __test_Base64_64_2():


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_64.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_64.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")

    






















#  _                  _             ____                          __     _  _             _    __    
# | |_    ___   ___  | |_          | __ )    __ _   ___    ___   / /_   | || |           / |  / /_   
# | __|  / _ \ / __| | __|         |  _ \   / _` | / __|  / _ \ | '_ \  | || |_          | | | '_ \  
# | |_  |  __/ \__ \ | |_          | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|         | | | (_) | 
#  \__|  \___| |___/  \__|  _____  |____/   \__,_| |___/  \___|  \___/     |_|    _____  |_|  \___/  
#                          |_____|                                               |_____|             



def __test_Base64_16():

    myByte = b"hello world"

    stringFromByte = Base64_16.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_16.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")




def __test_Base64_16_2():


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_16.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_16.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")

    






















#  _                  _             ____                          __     _  _             _____   ____   
# | |_    ___   ___  | |_          | __ )    __ _   ___    ___   / /_   | || |           |___ /  |___ \  
# | __|  / _ \ / __| | __|         |  _ \   / _` | / __|  / _ \ | '_ \  | || |_            |_ \    __) | 
# | |_  |  __/ \__ \ | |_          | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|          ___) |  / __/  
#  \__|  \___| |___/  \__|  _____  |____/   \__,_| |___/  \___|  \___/     |_|    _____  |____/  |_____| 
#                          |_____|                                               |_____|                 


def __test_Base64_32():

    myByte = b"hello world"

    stringFromByte = Base64_32.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_32.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")




def __test_Base64_32_2():


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_32.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_32.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")

    


























#  _                  _             ____                          __     _  _              ___    ____   
# | |_    ___   ___  | |_          | __ )    __ _   ___    ___   / /_   | || |            ( _ )  | ___|  
# | __|  / _ \ / __| | __|         |  _ \   / _` | / __|  / _ \ | '_ \  | || |_           / _ \  |___ \  
# | |_  |  __/ \__ \ | |_          | |_) | | (_| | \__ \ |  __/ | (_) | |__   _|         | (_) |  ___) | 
#  \__|  \___| |___/  \__|  _____  |____/   \__,_| |___/  \___|  \___/     |_|    _____   \___/  |____/  
#                          |_____|                                               |_____|                 



def __test_Base64_85():

    myByte = b"hello world"

    stringFromByte = Base64_85.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_85.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")




def __test_Base64_85_2():


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_85.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_85.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")






















#                      _          
#  _ __ ___     __ _  (_)  _ __   
# | '_ ` _ \   / _` | | | | '_ \  
# | | | | | | | (_| | | | | | | | 
# |_| |_| |_|  \__,_| |_| |_| |_| 
                                


def __main():
    import time
    start = time.perf_counter()

    __test_Base64_85()
    # __test_Base64_85_2()
    # __test_Base90Encoder2()

    end = time.perf_counter()


    print(f"\n\n\nTime taken = {end - start}")






    
if __name__ == "__main__":
    # __test_string2bytev2()
    # __test()
    # __test_HexConvertor2()
    __main()


