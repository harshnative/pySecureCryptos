from pySecureCryptos import hashers_v2
import random
import secrets
import pickle





# function to generate a random byte
def getRandomByte(minByteLen = 1 , maxByteLen = 1000):

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

    fileName = "binFiles/hashers_v2_testcases_bin/sha256_test_testCases.bin"

    number = 5

    outputList = []

    for i in range(number):
        print(i)
        
        byte = getRandomByte(10000 , 100000)

        hashed_byte = hashers_v2.SHA256(byte).get_byte()

        genObj = hashers_v2.SHA256(byte).get_byte_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                hashed_byte_yield = ex.value
                break


        hashed_string = hashers_v2.SHA256(byte).get_string()

        genObj = hashers_v2.SHA256(byte).get_string_yield()
        
        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                hashed_string_yield = ex.value
                break

        outputList.append([byte , hashed_byte , hashed_byte_yield , hashed_string , hashed_string_yield])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")
















if __name__ == "__main__":
    main()
