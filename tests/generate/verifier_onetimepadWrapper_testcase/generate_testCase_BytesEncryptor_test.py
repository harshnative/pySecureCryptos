from pySecureCryptos import verifier_onetimepadWrapper
import random
import secrets
import pickle





# function to generate a random byte
def getRandomByte():
    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    return byte

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

    fileName = "binFiles/verifier_onetimepadWrapper_testcases_bin/BytesEncryptor_test_testCases_1.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()
        password = getRandomString(1 , 100)

        encByte = verifier_onetimepadWrapper.BytesEncryptor.encrypt(byte , password , returnByteObject=True)
        outputList.append([byte , password , encByte])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")












def main2():

    fileName = "binFiles/verifier_onetimepadWrapper_testcases_bin/BytesEncryptor_test_testCases_2.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()
        password = getRandomString(1 , 100)

        encString = verifier_onetimepadWrapper.BytesEncryptor.encrypt(byte , password , returnByteObject=False)
        outputList.append([byte , password , encString])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")






if __name__ == "__main__":
    main()
    main2()
