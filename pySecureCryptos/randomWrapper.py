import random
import string
import time






class RandomString:

    @classmethod
    def generate(cls , size , seed = None , lowerCase = True , upperCase = True , nums = True , specialChars = True , space = False):

        if(type(size) != int):
            raise ValueError("size parameter expected to be of int type instead got {} type".format(type(size)))

        if(seed == None):
            seed = str(time.time())

        if(type(seed) != str):
            raise ValueError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

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







def __test_randomString():

    randomString = RandomString.generate(12)

    print(f"randomString = {randomString}")






if __name__ == "__main__":
    __test_randomString()