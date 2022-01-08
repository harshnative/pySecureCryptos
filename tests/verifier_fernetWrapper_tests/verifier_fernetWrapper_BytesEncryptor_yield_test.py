import pytest
from pySecureCryptos import verifier_fernetWrapper
import random
import repeatTimes            
import pickle
import secrets







# function to generate a random string
def getRandomString(minStringLen = 1 , maxStringLen = 10000):
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr



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











@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main():

    byte = getRandomByte()
    password = getRandomString(1 , 100)

    obj = verifier_fernetWrapper.BytesEncryptor(password)

    gen = obj.encrypt_yield(byte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encByte = ex.value
            break

    decByte = obj.decrypt(encByte)

    assert byte == decByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():
    

    byte = getRandomByte()
    password = getRandomString(1 , 100)

    obj = verifier_fernetWrapper.BytesEncryptor(password)

    encByte = obj.encrypt(byte)
    gen = obj.decrypt_yield(encByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decByte = ex.value
            break

    assert byte == decByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")





















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():
    

    byte = getRandomByte()
    password = getRandomString(1 , 100)

    obj = verifier_fernetWrapper.BytesEncryptor(password)

    gen = obj.encrypt_yield(byte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encByte = ex.value
            break

    gen = obj.decrypt_yield(encByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decByte = ex.value
            break

    assert byte == decByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")

















# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/verifier_fernetWrapper_testcases_bin/BytesEncryptor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , password , encByte in pickledList:

        decByte = verifier_fernetWrapper.BytesEncryptor(password).decrypt(encByte)

        assert byte == decByte , getAssetionMessage(locals() , "decrypted byte does not match the original byte")









# function to check if the code is still compatible with the previous results
def test_compatible_2():

    fileName = "binFiles/verifier_fernetWrapper_testcases_bin/BytesEncryptor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , password , encByte in pickledList:

        decByte = verifier_fernetWrapper.BytesEncryptor(password).decrypt_yield(encByte)

        while(True):
            try:
                next(decByte)
            except StopIteration as ex:
                decByte = ex.value
                break

        assert byte == decByte , getAssetionMessage(locals() , "decrypted byte does not match the original byte")






if __name__ == "__main__":
    pass

