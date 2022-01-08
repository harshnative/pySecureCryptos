from Cryptodome import PublicKey
from pySecureCryptos import rsaWrapper
import random
import secrets
import pickle


class GetKey:

    print("generating key")
    keyGenObj = rsaWrapper.KeyGenerator()

    keyPublic = keyGenObj.get_publicKey_bytes()

    keyPrivate = keyGenObj.get_privateKey_bytes()

    keyPublic_str = keyGenObj.get_publicKey_string()

    keyPrivate_str = keyGenObj.get_privateKey_string()



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

    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_byte_test_testCases.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()

        encByte = rsaWrapper.Encryptor(GetKey.keyPublic , GetKey.keyPrivate).encrypt_byte(byte)

        outputList.append([byte , GetKey.keyPublic , GetKey.keyPrivate , encByte])


    for i in range(number):
        print(i)

        byte = getRandomByte()

        encByte = rsaWrapper.Encryptor(GetKey.keyPublic_str , GetKey.keyPrivate_str).encrypt_byte(byte)

        outputList.append([byte , GetKey.keyPublic , GetKey.keyPrivate , encByte])


    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")















def main2():

    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_byte_yield_test_testCases.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()

        genObj = rsaWrapper.Encryptor(GetKey.keyPublic , GetKey.keyPrivate).encrypt_byte_yield(byte)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                encByte = ex.value
                break

        outputList.append([byte , GetKey.keyPublic , GetKey.keyPrivate , encByte])


    for i in range(number):
        print(i)

        byte = getRandomByte()

        genObj = rsaWrapper.Encryptor(GetKey.keyPublic_str , GetKey.keyPrivate_str).encrypt_byte_yield(byte)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                encByte = ex.value
                break

        outputList.append([byte , GetKey.keyPublic , GetKey.keyPrivate , encByte])


    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")









if __name__ == "__main__":
    main()
    main2()

