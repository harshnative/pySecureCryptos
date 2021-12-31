import pytest
from pySecureCryptos import encoderDecoders
import secrets
import random
import repeatTimes            



# function to test Byte2String encode decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    stringFromByte = encoderDecoders.Byte2String.encode(byte)

    byteAgain = encoderDecoders.Byte2String.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"





if __name__ == "__main__":
    pass
