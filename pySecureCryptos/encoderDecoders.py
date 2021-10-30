# class containing method to encode or decode any byte 
class ByteEncoderDecoder:

    # method to convert any byte into string
    @classmethod
    def encodeByte2String(cls , byte):

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
    # returns a bytearray type object
    @classmethod
    def decodeString2Byte_for_encodeByte2String(cls , string):

        """
        ALGO - 

        traverse the string and slice the string into 3 chars long

        convert the string back to int

        pass the int list to bytearray and return
        """

        intList = []

        for i in range(0 , len(string) , 3):
            toAppend = int(string[i : i + 3])
            intList.append(toAppend)

        return bytearray(intList)


    # method to convert string to byte
    # returns bytearray
    @classmethod
    def encodeString2Byte(cls , string):

        """
        convert each char in string to corresponding ASCII value (int)

        convert this intList to byteArray
        """
        intList = []

        for i in string:
            intList.append(ord(i))

        return bytearray(intList)


    @classmethod
    def decodeByte2String_for_encodeString2Byte(cls , byte):
        string = ""

        for i in byte:
            i = chr(int(i))
            string = string + i

        return string

        



# function to test the above class
def __test():

    import secrets
    import random 
    import time

    from colored import fg
    blueColor = fg('blue')
    greenColor = fg('green')
    redColor = fg('red')
    yellowColor = fg('yellow')
    whiteColor = fg('white')

    def testEncodeByte2String(howMany):
        avgTime = 0
        error = 0
        errorList = []

        for k in range(howMany):

            print(f"\ron {k} / {howMany}" , end = "")

            byteLength = random.randint(0 , 100000)

            randomByte = secrets.token_bytes(byteLength)

            start = time.time()
            encodedString = ByteEncoderDecoder.encodeByte2String(randomByte)
            decodedString = ByteEncoderDecoder.decodeString2Byte_for_encodeByte2String(encodedString)
            end = time.time()

            avgTime = avgTime + (((end - start) / byteLength) * 1000)

            if(decodedString != randomByte):
                error = error + 1 
                errorList.append([randomByte , decodedString])

        avgTime = avgTime / howMany

        return error , errorList , avgTime


    print("\n\n")

    # testing determinant function 
    print(whiteColor + "Testing encodeByte2String_simple")

    error , errorList , avgTime = testEncodeByte2String(1000)

    print()

    if(error == 0):
        print(blueColor + "avg time taken by testEncodeByte2String function per encode decode cycle per 1000 chars = {}".format(avgTime))
        print(greenColor + "testEncodeByte2String function test passed")
    else:
        print(redColor + "testEncodeByte2String function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))



    def testEncodeString2Byte(howMany):
        avgTime = 0
        error = 0
        errorList = []

        for k in range(howMany):

            print(f"\ron {k} / {howMany}" , end = "")

            stringPool = []

            for i in range(0 , 256):
                stringPool.append(chr(i))

            stringLength = random.randint(1 , 100000)

            randomString = ""
            for i in range(stringLength):
                randomString = randomString + random.choice(stringPool)

            start = time.time()
            encodedByte = ByteEncoderDecoder.encodeString2Byte(randomString)
            decodedString = ByteEncoderDecoder.decodeByte2String_for_encodeString2Byte(encodedByte)
            end = time.time()

            avgTime = avgTime + (((end - start) / stringLength) * 1000)

            if(decodedString != randomString):
                error = error + 1 
                errorList.append([randomString , decodedString])

        avgTime = avgTime / howMany

        return error , errorList , avgTime


    print("\n\n")

    # testing determinant function 
    print(whiteColor + "on testEncodeString2Byte")

    error , errorList , avgTime = testEncodeString2Byte(1000)

    print()

    if(error == 0):
        print(blueColor + "avg time taken by testEncodeString2Byte function per encode decode cycle per 1000 chars = {}".format(avgTime))
        print(greenColor + "testEncodeString2Byte function test passed")
    else:
        print(redColor + "testEncodeString2Byte function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))





if __name__ == "__main__":

    __test()
    # pass


