import pytest
from pySecureCryptos import encoderDecoders
import random
import repeatTimes            

            



# function to test String2Byte_yield encode with String2Byte_yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    string = randomStr

    gen = encoderDecoders.String2Byte_yield.encode(string)

    while(True):
        try:
            next(gen)
        except Exception as ex:
            byteFromString = ex.value
            break

    gen = encoderDecoders.String2Byte_yield.decode(byteFromString)

    while(True):
        try:
            next(gen)
        except Exception as ex:
            stringAgain = ex.value
            break

    assert string == stringAgain , "decoded string does not match the original string"





if __name__ == "__main__":
    pass

