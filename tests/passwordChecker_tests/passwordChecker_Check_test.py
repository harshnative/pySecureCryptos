import pytest
from pySecureCryptos import passwordChecker
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













@pytest.mark.parametrize("password_list" , [
       ["Hello world1" , ["hello"] , "low"] , 
       ["Hello world123" , ["hello"] , "medium"] , 
       ["Hello world123$" , ["hello"] , "high"] , 
       ["Thisisverystrongpassw%6rd12" , ["hello"] , "max"] ,
   ])
def test_main(password_list):
   
    if(password_list[2] == "low"):
        result = passwordChecker.Check.check_low(password_list[0] , password_list[1])

    elif(password_list[2] == "medium"):
        result = passwordChecker.Check.check_medium(password_list[0] , password_list[1])

    elif(password_list[2] == "high"):
        result = passwordChecker.Check.check_high(password_list[0] , password_list[1])

    elif(password_list[2] == "max"):
        result = passwordChecker.Check.check_max(password_list[0] , password_list[1])

    assert result == None , getAssetionMessage(locals() , "password does not match the security requirement")
        















if __name__ == "__main__":
    pass

