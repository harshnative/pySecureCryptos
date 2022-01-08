import pytest
from pySecureCryptos import encoderDecoders
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
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    byte = bytes(randomStr , "utf-8")

    return byte




# function to test Byte2String_v2 yield encode with Byte2String_v2 decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():
    
    byte = getRandomByte()

    genObj = encoderDecoders.Byte2String_v2.encode_yield(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    byteAgain = encoderDecoders.Byte2String_v2.decode(stringFromByte)

    assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")













# function to test Byte2String_v2 encode with Byte2String_v2 yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():


    byte = getRandomByte()

    stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)

    genObj = encoderDecoders.Byte2String_v2.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")









# function to test Byte2String_v2 yield encode with Byte2String_v2 yield decode
@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():
    

    byte = getRandomByte()

    genObj = encoderDecoders.Byte2String_v2.encode_yield(byte)
    
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    genObj = encoderDecoders.Byte2String_v2.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")










# function to check if the code is still compatible with the previous results
def test_compatible_1():

    fileName = "binFiles/encoderDecoder_testcases_bin/Byte2String_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        byteAgain = encoderDecoders.Byte2String_v2.decode(encodedByte)

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")











# function to check if the code is still compatible with the previous results
def test_compatible_2():

    fileName = "binFiles/encoderDecoder_testcases_bin/Byte2String_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        gen = encoderDecoders.Byte2String_v2.encode_yield(byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringFromByte = ex.value
                break

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        byteAgain = encoderDecoders.Byte2String_v2.decode(encodedByte)

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")















# function to check if the code is still compatible with the previous results
def test_compatible_3():

    fileName = "binFiles/encoderDecoder_testcases_bin/Byte2String_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        gen = encoderDecoders.Byte2String_v2.decode_yield(encodedByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteAgain = ex.value
                break

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")

















# function to check if the code is still compatible with the previous results
def test_compatible_4():

    fileName = "binFiles/encoderDecoder_testcases_bin/Byte2String_v2_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , encodedByte in pickledList:
    
        gen = encoderDecoders.Byte2String_v2.encode_yield(byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringFromByte = ex.value
                break

        assert encodedByte == stringFromByte , getAssetionMessage(locals() , "encoded bytes are different")

        gen = encoderDecoders.Byte2String_v2.decode_yield(encodedByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                byteAgain = ex.value
                break

        assert byte == byteAgain , getAssetionMessage(locals() , "decoded byte does not match the original byte")






if __name__ == "__main__":
    pass

