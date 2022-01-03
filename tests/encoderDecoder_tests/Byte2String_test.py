import pytest
from pySecureCryptos import encoderDecoders
import secrets
import random
import repeatTimes            
import pickle






def getAssetionMessage(locals , message):
    locals_stored = locals
    
    result = str(message) + "\n\n\nFunction Vars Dump -\n"
    count = 1

    for name,val in locals_stored.items():
        result = result + f"\n\n{count}. {name} is {type(val)} = \n{val}\n"
        count = count + 1

    return result








# function to generate a random byte
def getRandomByte():
    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    return byte







# function to test Byte2String encode decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    byte = getRandomByte()

    stringFromByte = encoderDecoders.Byte2String.encode(byte)

    byteAgain = encoderDecoders.Byte2String.decode(stringFromByte)

    assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")








# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/encoderDecoder_testcases_bin/Byte2String_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.Byte2String.encode(byte)

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        byteAgain = encoderDecoders.Byte2String.decode(encodedByte)

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")




if __name__ == "__main__":
    pass
