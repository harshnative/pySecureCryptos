import pytest
from pySecureCryptos import encoderDecoders
import random
import secrets
import repeatTimes            



# function to test Byte2String_yield encode with Byte2String decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))
    genObj = encoderDecoders.Byte2String_yield.encode(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    byteAgain = encoderDecoders.Byte2String.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"



if __name__ == "__main__":
    pass

