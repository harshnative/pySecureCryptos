import pytest
from pySecureCryptos import  onetimepadWrapper
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
def test_main():
    

    string = getRandomString()
    password = getRandomString(1 , 100)

    gen = onetimepadWrapper.StringEncryptor_yield.encrypt(string , password)
    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encString = ex.value
            break

    decString = onetimepadWrapper.StringEncryptor.decrypt(encString , password)

    assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")











@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_2():
    

    string = getRandomString()
    password = getRandomString(1 , 100)

    encString = onetimepadWrapper.StringEncryptor.encrypt(string , password)
    
    gen = onetimepadWrapper.StringEncryptor_yield.decrypt(encString , password)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decString = ex.value
            break

    assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_main_3():
    

    string = getRandomString()
    password = getRandomString(1 , 100)

    gen = onetimepadWrapper.StringEncryptor_yield.encrypt(string , password)
    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encString = ex.value
            break

    gen = onetimepadWrapper.StringEncryptor_yield.decrypt(encString , password)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decString = ex.value
            break

    assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")











# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/onetimepadWrapper_testcases_bin/StringEncryptor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , password , encString in pickledList:

        decString = onetimepadWrapper.StringEncryptor.decrypt(encString , password)


        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")
















# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/onetimepadWrapper_testcases_bin/StringEncryptor_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , password , encString in pickledList:

        gen = onetimepadWrapper.StringEncryptor_yield.decrypt(encString , password)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decString = ex.value
                break

        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")







if __name__ == "__main__":
    pass

