import pytest
from pySecureCryptos import encoderDecoders
import random
import repeatTimes            


# function to test Byte2String_v2 encode decode
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

    byte = bytes(randomStr , "utf-8")

    stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)

    byteAgain = encoderDecoders.Byte2String_v2.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"





if __name__ == "__main__":
    pass

