import pytest
from pySecureCryptos import verifier_fernetWrapper
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







# function to generate a random string
def getRandomString(minStringLen = 1 , maxStringLen = 10000):
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():
    

    string = getRandomString()
    password = getRandomString(1 , 100)

    obj = verifier_fernetWrapper.StringEncryptor(password)

    if(random.random() > 0.5):
        gen = obj.encrypt_yield(string , returnString=True)
        
        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                encString = ex.value
                break

        decString = obj.decrypt_string(encString)

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")

    else:

        gen = obj.encrypt_yield(string , returnString=False)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                encByte = ex.value
                break

        decString = obj.decrypt_byte(encByte)

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")
















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():
    

    string = getRandomString()
    password = getRandomString(1 , 100)

    obj = verifier_fernetWrapper.StringEncryptor(password)

    if(random.random() > 0.5):
        encString = obj.encrypt(string , returnString=True)

        gen = obj.decrypt_string_yield(encString)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decString = ex.value
                break

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")

    else:

        encByte = obj.encrypt(string , returnString=False)

        gen = obj.decrypt_byte_yield(encByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decString = ex.value
                break

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")




















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_4():
    

    string = getRandomString()
    password = getRandomString(1 , 100)

    obj = verifier_fernetWrapper.StringEncryptor(password)

    if(random.random() > 0.5):
        gen = obj.encrypt_yield(string , returnString=True)
        
        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                encString = ex.value
                break

        gen = obj.decrypt_string_yield(encString)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decString = ex.value
                break

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")

    else:

        gen = obj.encrypt_yield(string , returnString=False)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                encByte = ex.value
                break

        gen = obj.decrypt_byte_yield(encByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decString = ex.value
                break

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")



















# function to check if the code is still compatible with the previous results
def test_compatible_returnString():

    fileName = "binFiles/verifier_fernetWrapper_testcases_bin/StringEncryptor_yield_test_testCases_1.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , password , encString in pickledList:

        decString = verifier_fernetWrapper.StringEncryptor(password).decrypt_string(encString)

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")






# function to check if the code is still compatible with the previous results
def test_compatible_returnString_2():

    fileName = "binFiles/verifier_fernetWrapper_testcases_bin/StringEncryptor_yield_test_testCases_1.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , password , encString in pickledList:

        gen = verifier_fernetWrapper.StringEncryptor(password).decrypt_string_yield(encString)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decString = ex.value
                break

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")




















# function to check if the code is still compatible with the previous results
def test_compatible_returnByte():

    fileName = "binFiles/verifier_fernetWrapper_testcases_bin/StringEncryptor_yield_test_testCases_2.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , password , encByte in pickledList:

        decString = verifier_fernetWrapper.StringEncryptor(password).decrypt_byte(encByte)

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")










# function to check if the code is still compatible with the previous results
def test_compatible_returnByte_2():

    fileName = "binFiles/verifier_fernetWrapper_testcases_bin/StringEncryptor_yield_test_testCases_2.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , password , encByte in pickledList:

        gen = verifier_fernetWrapper.StringEncryptor(password).decrypt_byte_yield(encByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decString = ex.value
                break

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")






if __name__ == "__main__":
    pass

