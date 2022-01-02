import pytest
from pySecureCryptos import encoderDecoders
import random
import repeatTimes            
import pickle



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






# function to test String2Byte_v2 encode decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():
    

    string = getRandomString()

    byteFromString = encoderDecoders.String2Byte_v2.encode(string)

    stringAgain = encoderDecoders.String2Byte_v2.decode(byteFromString)

    assert string == stringAgain , "decoded string does not match the original string"














# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/encoderDecoder_testcases_bin/String2Byte_v2_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , encodedString in pickledList:
    
        byteFromString = encoderDecoders.String2Byte_v2.encode(string)

        assert encodedString == byteFromString , "encoded strings are different"

        stringAgain = encoderDecoders.String2Byte_v2.decode(encodedString)

        assert string == stringAgain , "decoded string does not match the original string"










if __name__ == "__main__":
    pass

