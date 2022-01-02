import pytest
from pySecureCryptos import encoderDecoders
import random
import secrets
import repeatTimes          
import pickle  




# function to generate a random byte
def getRandomByte():
    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    return byte











            



# function to test HexConvertor yield encode with HexConvertor decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    byte = getRandomByte()

    genObj = encoderDecoders.HexConvertor.encode_yield(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    byteAgain = encoderDecoders.HexConvertor.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"










# function to test HexConvertor encode with HexConvertor yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():

    byte = getRandomByte()

    stringFromByte = encoderDecoders.HexConvertor.encode(byte)

    genObj = encoderDecoders.HexConvertor.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , "decoded byte does not match the original byte"













# function to test HexConvertor yield encode with HexConvertor yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():

    byte = getRandomByte()

    genObj = encoderDecoders.HexConvertor.encode_yield(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    genObj = encoderDecoders.HexConvertor.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , "decoded byte does not match the original byte"









# function to check if the code is still compatible with the previous results
def test_compatible_1():

    fileName = "binFiles/encoderDecoder_testcases_bin/HexConvertor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.HexConvertor.encode(byte)

        assert encodedByte == stringFromByte , "encoded bytes are different"

        byteAgain = encoderDecoders.HexConvertor.decode(encodedByte)

        assert byte == byteAgain , "decoded byte does not match the original byte"











# function to check if the code is still compatible with the previous results
def test_compatible_2():

    fileName = "binFiles/encoderDecoder_testcases_bin/HexConvertor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        gen = encoderDecoders.HexConvertor.encode_yield(byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringFromByte = ex.value
                break

        assert encodedByte == stringFromByte , "encoded bytes are different"

        byteAgain = encoderDecoders.HexConvertor.decode(encodedByte)

        assert byte == byteAgain , "decoded byte does not match the original byte"















# function to check if the code is still compatible with the previous results
def test_compatible_3():

    fileName = "binFiles/encoderDecoder_testcases_bin/HexConvertor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.HexConvertor.encode(byte)

        assert encodedByte == stringFromByte , "encoded bytes are different"

        gen = encoderDecoders.HexConvertor.decode_yield(encodedByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteAgain = ex.value
                break

        assert byte == byteAgain , "decoded byte does not match the original byte"

















# function to check if the code is still compatible with the previous results
def test_compatible_4():

    fileName = "binFiles/encoderDecoder_testcases_bin/HexConvertor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        gen = encoderDecoders.HexConvertor.encode_yield(byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringFromByte = ex.value
                break

        assert encodedByte == stringFromByte , "encoded bytes are different"

        gen = encoderDecoders.HexConvertor.decode_yield(encodedByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteAgain = ex.value
                break

        assert byte == byteAgain , "decoded byte does not match the original byte"










if __name__ == "__main__":
    pass

