import pytest
from pySecureCryptos import encoderDecoders
import random
import secrets
import repeatTimes            

            



# function to test HexConvertor encode decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    stringFromByte = encoderDecoders.HexConvertor.encode(byte)

    byteAgain = encoderDecoders.HexConvertor.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"





if __name__ == "__main__":
    pass

