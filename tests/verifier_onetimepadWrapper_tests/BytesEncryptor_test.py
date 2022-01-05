import pytest
from pySecureCryptos import verifier_onetimepadWrapper
import random
import repeatTimes            
import pickle
import secrets




def getAssetionMessage(locals , message):
    locals_stored = locals

    result = str(message) + "\n\n\nFunction Vars Dump -\n"
    count = 1

    for name,val in locals_stored.items():
        result = result + f"\n\n{count}. {name} is {type(val)} = \n{val}\n"
        count = count + 1

    return result








# function to generate a random string
def getRandomString(minStringLen = 1 , maxStringLen = 10000):
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr




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

    encByte = verifier_onetimepadWrapper.BytesEncryptor.encrypt(byte , password , returnByteObject=True)
    encString = verifier_onetimepadWrapper.BytesEncryptor.encrypt(byte , password , returnByteObject=False)

    decByte = verifier_onetimepadWrapper.BytesEncryptor.decrypt_byte(encByte , password)
    decByte2 = verifier_onetimepadWrapper.BytesEncryptor.decrypt(encString , password)

    assert byte == decByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")
    assert byte == decByte2 , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")















# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/verifier_onetimepadWrapper_testcases_bin/BytesEncryptor_test_testCases_1.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , password , encByte in pickledList:

        decByte = verifier_onetimepadWrapper.BytesEncryptor.decrypt_byte(encByte , password)

        assert byte == decByte , getAssetionMessage(locals() , "decrypted byte does not match the original byte")














# function to check if the code is still compatible with the previous results
def test_compatible_2():

    fileName = "binFiles/verifier_onetimepadWrapper_testcases_bin/BytesEncryptor_test_testCases_2.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , password , encString in pickledList:

        decByte = verifier_onetimepadWrapper.BytesEncryptor.decrypt(encString , password)

        assert byte == decByte , getAssetionMessage(locals() , "decrypted byte does not match the original byte")





if __name__ == "__main__":
    pass

