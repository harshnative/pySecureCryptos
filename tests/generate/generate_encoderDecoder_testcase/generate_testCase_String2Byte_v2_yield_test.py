from pySecureCryptos import encoderDecoders
import random
import secrets
import pickle


# function to generate a random string
def getRandomString():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr






def main():

    fileName = "String2Byte_v2_yield_test_testCases.bin"

    number = 100

    outputList = []

    for i in range(number):
        print(i)

        string = getRandomString()
        gen = encoderDecoders.String2Byte_v2.encode_yield(string)

        while(True):
            try:
                next(gen)
            except Exception as ex:
                ByteFromString = ex.value
                break

        
        outputList.append([string , ByteFromString])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")



if __name__ == "__main__":
    main()
