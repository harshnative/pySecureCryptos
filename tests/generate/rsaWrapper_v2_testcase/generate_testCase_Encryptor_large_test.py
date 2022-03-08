from Cryptodome import PublicKey
from pySecureCryptos import rsaWrapper_v2
import random
import secrets
import pickle


class GetKey:

    print("generating key")
    keyGenObj = rsaWrapper_v2.KeyGenerator()

    keyPublic = keyGenObj.get_publicKey_bytes()

    keyPrivate = keyGenObj.get_privateKey_bytes()

    keyPublic_str = keyGenObj.get_publicKey_string()

    keyPrivate_str = keyGenObj.get_privateKey_string()



# function to generate a random byte
def getRandomByte():
    byte = secrets.token_bytes(10000)

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

    fileName = "binFiles/rsaWrapper_v2_testcases_bin/Encryptor_large_byte_test_testCases.bin"

    number = 1

    outputList = []

    for i in range(number):

        randomByte = b""

        for j in range(1000):
            print(i , j)
            randomByte = randomByte + getRandomByte()

        genObj = rsaWrapper_v2.Encryptor(GetKey.keyPublic , GetKey.keyPrivate).encrypt_lbyte_yield(randomByte)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                enc_byte = ex.value
                break

        outputList.append([randomByte , GetKey.keyPublic , GetKey.keyPrivate , enc_byte])


    for i in range(number):

        randomByte = b""

        for j in range(1000):
            print(i , j)
            randomByte = randomByte + getRandomByte()

        genObj = rsaWrapper_v2.Encryptor(GetKey.keyPublic_str , GetKey.keyPrivate_str).encrypt_lbyte_yield(randomByte)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                enc_byte = ex.value
                break

        outputList.append([randomByte , GetKey.keyPublic , GetKey.keyPrivate , enc_byte])



    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")

















def main2():

    fileName = "binFiles/rsaWrapper_v2_testcases_bin/Encryptor_large_string_test_testCases.bin"

    number = 1

    outputList = []

    for i in range(number):

        randomString = ""

        for j in range(1000):
            print(i , j)
            randomString = randomString + getRandomString()

        genObj = rsaWrapper_v2.Encryptor(GetKey.keyPublic , GetKey.keyPrivate).encrypt_lstring_yield(randomString)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                enc_string = ex.value
                break

        outputList.append([randomString , GetKey.keyPublic , GetKey.keyPrivate , enc_string])






    for i in range(number):

        randomString = ""

        for j in range(1000):
            print(i , j)
            randomString = randomString + getRandomString()

        genObj = rsaWrapper_v2.Encryptor(GetKey.keyPublic_str , GetKey.keyPrivate_str).encrypt_lstring_yield(randomString)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                enc_string = ex.value
                break

        outputList.append([randomString , GetKey.keyPublic , GetKey.keyPrivate , enc_string])




    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")











if __name__ == "__main__":
    main()
    main2()

