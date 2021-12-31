import pytest
from pySecureCryptos import encoderDecoders
import random
import repeatTimes            




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






# function to test String2Byte encode decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():
    

    string = getRandomString()

    byteFromString = encoderDecoders.String2Byte.encode(string)

    stringAgain = encoderDecoders.String2Byte.decode(byteFromString)

    assert string == stringAgain , "decoded string does not match the original string"





if __name__ == "__main__":
    pass

