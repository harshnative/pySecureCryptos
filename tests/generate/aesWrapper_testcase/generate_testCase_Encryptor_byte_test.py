from Cryptodome import PublicKey
from pySecureCryptos import aesWrapper
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

    fileName = "binFiles/aesWrapper_testcases_bin/Encryptor_byte_test_testCases.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()
        password = getRandomString(1 , 100)

        encByte = aesWrapper.Encryptor(password).encrypt_byte(byte)

        outputList.append([byte , password , encByte])



    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")















def main2():

    fileName = "binFiles/aesWrapper_testcases_bin/Encryptor_byte_yield_test_testCases.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()
        password = getRandomString(1 , 100)

        genObj = aesWrapper.Encryptor(password).encrypt_byte_yield(byte)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                encByte = ex.value
                break

        outputList.append([byte , password , encByte])


    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")









if __name__ == "__main__":
    main()
    main2()

