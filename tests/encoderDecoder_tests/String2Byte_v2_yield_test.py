import pytest
from pySecureCryptos import encoderDecoders
import random
import repeatTimes    
import pickle        





def getAssetionMessage(locals , message):
    locals_stored = locals
    
    result = str(message) + "\n\n\nFunction Vars Dump -\n"
    count = 1

    for name,val in locals_stored.items():
        result = result + f"\n\n{count}. {name} is {type(val)} = \n{val}\n"
        count = count + 1

    return result




# function to generate a random string
def getRandomString():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr
            






# function to test String2Byte_v2 encode with String2Byte_v2 decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():


    string = getRandomString()

    gen = encoderDecoders.String2Byte_v2.encode_yield(string)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            byteFromString = ex.value
            break

    stringAgain = encoderDecoders.String2Byte_v2.decode(byteFromString)

    assert string == stringAgain , getAssetionMessage(locals() , "decoded string does not match the original string")










# function to test String2Byte_v2 encode with String2Byte_v2 decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():

    string = getRandomString()

    byteFromString = encoderDecoders.String2Byte_v2.encode(string)

    gen = encoderDecoders.String2Byte_v2.decode_yield(byteFromString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            stringAgain = ex.value
            break

    assert string == stringAgain , getAssetionMessage(locals() , "decoded string does not match the original string")












# function to test String2Byte_v2 encode with String2Byte_v2 decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():

    string = getRandomString()

    gen = encoderDecoders.String2Byte_v2.encode_yield(string)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            byteFromString = ex.value
            break

    gen = encoderDecoders.String2Byte_v2.decode_yield(byteFromString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            stringAgain = ex.value
            break

    assert string == stringAgain , getAssetionMessage(locals() , "decoded string does not match the original string")













# function to check if the code is still compatible with the previous results
def test_compatible_1():

    fileName = "binFiles/encoderDecoder_testcases_bin/String2Byte_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , encodedString in pickledList:
    
        byteFromString = encoderDecoders.String2Byte_v2.encode(string)

        assert encodedString == byteFromString , getAssetionMessage(locals() , "encoded strings are different")

        stringAgain = encoderDecoders.String2Byte_v2.decode(encodedString)

        assert string == stringAgain , getAssetionMessage(locals() , "decoded string does not match the original string")











# function to check if the code is still compatible with the previous results
def test_compatible_2():

    fileName = "binFiles/encoderDecoder_testcases_bin/String2Byte_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , encodedString in pickledList:
    
        gen = encoderDecoders.String2Byte_v2.encode_yield(string)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteFromString = ex.value
                break

        assert encodedString == byteFromString , getAssetionMessage(locals() , "encoded strings are different")

        stringAgain = encoderDecoders.String2Byte_v2.decode(encodedString)

        assert string == stringAgain , getAssetionMessage(locals() , "decoded string does not match the original string")














# function to check if the code is still compatible with the previous results
def test_compatible_3():

    fileName = "binFiles/encoderDecoder_testcases_bin/String2Byte_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , encodedString in pickledList:
    
        byteFromString = encoderDecoders.String2Byte_v2.encode(string)

        assert encodedString == byteFromString , getAssetionMessage(locals() , "encoded strings are different")

        gen = encoderDecoders.String2Byte_v2.decode_yield(encodedString)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringAgain = ex.value
                break

        assert string == stringAgain , getAssetionMessage(locals() , "decoded string does not match the original string")
















# function to check if the code is still compatible with the previous results
def test_compatible_4():

    fileName = "binFiles/encoderDecoder_testcases_bin/String2Byte_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , encodedString in pickledList:
    
        gen = encoderDecoders.String2Byte_v2.encode_yield(string)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteFromString = ex.value
                break

        assert encodedString == byteFromString , getAssetionMessage(locals() , "encoded strings are different")

        gen = encoderDecoders.String2Byte_v2.decode_yield(encodedString)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringAgain = ex.value
                break

        assert string == stringAgain , getAssetionMessage(locals() , "decoded string does not match the original string")








if __name__ == "__main__":
    pass

