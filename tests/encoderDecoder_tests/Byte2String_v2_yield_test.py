import pytest
from pySecureCryptos import encoderDecoders
import random
import repeatTimes            


# function to generate a random byte
def getRandomByte():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    byte = bytes(randomStr , "utf-8")

    return byte




# function to test Byte2String_v2 yield encode with Byte2String_v2 decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():
    
    byte = getRandomByte()

    genObj = encoderDecoders.Byte2String_v2.encode_yield(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    byteAgain = encoderDecoders.Byte2String_v2.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"













# function to test Byte2String_v2 encode with Byte2String_v2 yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    byte = bytes(randomStr , "utf-8")

    stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)

    genObj = encoderDecoders.Byte2String_v2.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , "decoded byte does not match the original byte"









# function to test Byte2String_v2 yield encode with Byte2String_v2 yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    byte = bytes(randomStr , "utf-8")

    genObj = encoderDecoders.Byte2String_v2.encode_yield(byte)
    
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    genObj = encoderDecoders.Byte2String_v2.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , "decoded byte does not match the original byte"





if __name__ == "__main__":
    pass

