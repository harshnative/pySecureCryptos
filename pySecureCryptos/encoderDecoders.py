import binascii


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
    def encode(cls , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise ValueError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))


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
    def decode(cls , string):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))


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
    def encode(cls , string):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))


        """
        convert each char in string to corresponding ASCII value (int)

        convert this intList to bytes
        """
        intList = []

        for i in string:
            intList.append(ord(i))

        return bytes(intList)


    @classmethod
    def decode(cls , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise ValueError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

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
    def encode(cls , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise ValueError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

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
    def decode(cls , string):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

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
    def encode(cls , string):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

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
    def decode(cls , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise ValueError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        string = ""

        totalCount = len(byte)
        currentCount = 0

        for i in byte:
            i = chr(int(i))
            string = string + i

            currentCount = currentCount + 1
            yield currentCount , totalCount

        return string

















# convert byte to hex and vice versa
class HexConvertor:

    @classmethod
    def encode(cls , byte):

        # type checking the parameters
        if(type(byte) != bytes):
            raise ValueError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        return str(binascii.hexlify(byte) , "utf-8")

    @classmethod
    def decode(cls , string):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

        return binascii.unhexlify(bytes(string , "utf-8"))










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


    








    
if __name__ == "__main__":
    __test_HexConvertor()


