import pytest
from pySecureCryptos import hashers_v2
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
def getRandomString():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr



















# function to check if the code is still compatible with the previous results
def test_compatible():

    fileName = "binFiles/hashers_v2_testcases_bin/md5_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    for byte , hashed_byte , hashed_byte_yield , hashed_string , hashed_string_yield in pickledList:
    
        new_hashed_byte = hashers_v2.MD5(byte).get_byte()

        assert new_hashed_byte == hashed_byte , getAssetionMessage(locals() , "hashed bytes does not match") 


        genObj = hashers_v2.MD5(byte).get_byte_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                new_hashed_byte_yield = ex.value
                break

        assert new_hashed_byte_yield == hashed_byte_yield , getAssetionMessage(locals() , "hashed bytes does not match") 

        new_hashed_string = hashers_v2.MD5(byte).get_string()

        assert new_hashed_string == hashed_string , getAssetionMessage(locals() , "hashed string does not match") 


        genObj = hashers_v2.MD5(byte).get_string_yield()
        
        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                new_hashed_string_yield = ex.value
                break

        assert new_hashed_string_yield == hashed_string_yield , getAssetionMessage(locals() , "hashed string does not match") 




if __name__ == "__main__":
    pass

