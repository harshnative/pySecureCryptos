from Cryptodome import PublicKey
from pySecureCryptos import verifier_fernetWrapper_v2
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

    fileName = "binFiles/verifier_fernetWrapper_v2_testcases_bin/Encryptor_string_test_testCases.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        string = getRandomString()
        password = getRandomString(1 , 100)

        enc_string = verifier_fernetWrapper_v2.Encryptor(password).encrypt_string(string)

        outputList.append([string , password , enc_string])


    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")















def main2():

    fileName = "binFiles/verifier_fernetWrapper_v2_testcases_bin/Encryptor_string_yield_test_testCases.bin"

    number = 2

    outputList = []

    for i in range(number):
        print(i)

        string = getRandomString()
        password = getRandomString(1,100)

        genObj = verifier_fernetWrapper_v2.Encryptor(password).encrypt_string_yield(string)

        while(True):
            try:
                next(genObj)

            except StopIteration as ex:
                enc_string = ex.value
                break

        outputList.append([string , password , enc_string])



    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")









if __name__ == "__main__":
    main()
    main2()

