from pySecureCryptos import onetimepadWrapper
import random
import secrets
import pickle


# function to generate a random string
def getRandomString(minStringLen = 1 , maxStringLen = 10000):
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr






def main():

    fileName = "binFiles/onetimepadWrapper_testcases_bin/StringEncryptor_yield_test_testCases.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        string = getRandomString()
        password = getRandomString(1 , 100)

        gen = onetimepadWrapper.StringEncryptor_yield.encrypt(string , password)
        
        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                encString = ex.value
                break
        
        outputList.append([string , password , encString])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")





if __name__ == "__main__":
    main()
