import pytest
from pySecureCryptos import encoderDecoders
import random
import secrets
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











            



# function to test Base64_32 yield encode with Base64_32 decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    byte = getRandomByte()

    genObj = encoderDecoders.Base64_32.encode_yield(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    byteAgain = encoderDecoders.Base64_32.decode(stringFromByte)

    assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")










# function to test Base64_32 encode with Base64_32 yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():

    byte = getRandomByte()

    stringFromByte = encoderDecoders.Base64_32.encode(byte)

    genObj = encoderDecoders.Base64_32.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")













# function to test Base64_32 yield encode with Base64_32 yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():

    byte = getRandomByte()

    genObj = encoderDecoders.Base64_32.encode_yield(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    genObj = encoderDecoders.Base64_32.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")









# function to check if the code is still compatible with the previous results
def test_compatible_1():

    fileName = "binFiles/encoderDecoder_testcases_bin/Base64_32_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.Base64_32.encode(byte)

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        byteAgain = encoderDecoders.Base64_32.decode(encodedByte)

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")











# function to check if the code is still compatible with the previous results
def test_compatible_2():

    fileName = "binFiles/encoderDecoder_testcases_bin/Base64_32_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        gen = encoderDecoders.Base64_32.encode_yield(byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringFromByte = ex.value
                break

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        byteAgain = encoderDecoders.Base64_32.decode(encodedByte)

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")















# function to check if the code is still compatible with the previous results
def test_compatible_3():

    fileName = "binFiles/encoderDecoder_testcases_bin/Base64_32_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.Base64_32.encode(byte)

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        gen = encoderDecoders.Base64_32.decode_yield(encodedByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteAgain = ex.value
                break

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")

















# function to check if the code is still compatible with the previous results
def test_compatible_4():

    fileName = "binFiles/encoderDecoder_testcases_bin/Base64_32_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        gen = encoderDecoders.Base64_32.encode_yield(byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringFromByte = ex.value
                break

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        gen = encoderDecoders.Base64_32.decode_yield(encodedByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteAgain = ex.value
                break

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")










if __name__ == "__main__":
    pass

