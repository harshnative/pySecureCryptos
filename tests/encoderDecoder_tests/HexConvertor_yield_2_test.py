import pytest
from pySecureCryptos import encoderDecoders
import random
import secrets
import repeatTimes            

            



# function to test HexConvertor encode with HexConvertor yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    stringFromByte = encoderDecoders.HexConvertor.encode(byte)

    genObj = encoderDecoders.HexConvertor.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , "decoded byte does not match the original byte"





if __name__ == "__main__":
    pass

