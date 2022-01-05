import pytest
from pySecureCryptos import  verifier_onetimepadWrapper
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

    encString = verifier_onetimepadWrapper.StringEncryptor.encrypt(string , password)
    decString = verifier_onetimepadWrapper.StringEncryptor.decrypt(encString , password)

    assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")













# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/verifier_onetimepadWrapper_testcases_bin/StringEncryptor_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for string , password , encString in pickledList:

        decString = verifier_onetimepadWrapper.StringEncryptor.decrypt(encString , password)


        assert string == decString , getAssetionMessage(locals() , "decrypted string does not match the original string")









if __name__ == "__main__":
    pass

