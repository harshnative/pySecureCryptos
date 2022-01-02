import pytest
from pySecureCryptos import encoderDecoders
import random
import repeatTimes     
import pickle

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





# function to test Byte2String_v2 encode decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    byte = getRandomByte()

    stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)

    byteAgain = encoderDecoders.Byte2String_v2.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"












# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/encoderDecoder_testcases_bin/Byte2String_v2_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)

        assert encodedByte == stringFromByte , "encoded bytes are different"

        byteAgain = encoderDecoders.Byte2String_v2.decode(encodedByte)

        assert byte == byteAgain , "decoded byte does not match the original byte"




if __name__ == "__main__":
    pass

