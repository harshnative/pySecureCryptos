import random
import string
import time
import secrets
from .encoderDecoders import *





class RandomString:

    @classmethod
    def generate(cls , size , seed = None , lowerCase = True , upperCase = True , nums = True , specialChars = True , space = False):

        if(type(size) != int):
            raise TypeError("size parameter expected to be of int type instead got {} type".format(type(size)))

        if(seed == None):
            seed = str(time.time())

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

        charList = []

        if(lowerCase):
            charList.extend(list(string.ascii_lowercase))
        
        if(upperCase):
            charList.extend(list(string.ascii_uppercase))
        
        if(nums):
            charList.extend(list(string.digits))

        if(specialChars):
            charList.extend(list("~`!@#$%^&*()_+-=|[]\:<>?;,./"))
        
        if(space):
            charList.append(" ")

        randomList = random.choices(charList , k=size)

        randomString = "".join(randomList)

        return randomString


    

    @classmethod
    def generate_secrets(cls , size = 256):
        
        randomByte = secrets.token_bytes(size)

        stringFromByte = HexConvertor.encode(randomByte)

        return stringFromByte







def __test_randomString():

    randomString = RandomString.generate(12)

    print(f"randomString = {randomString}")



def __test_randomString2():

    randomString = RandomString.generate_secrets()

    print(f"randomString = {randomString}")







if __name__ == "__main__":
    __test_randomString2()