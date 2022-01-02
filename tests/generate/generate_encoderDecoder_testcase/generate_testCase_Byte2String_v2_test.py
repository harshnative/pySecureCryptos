from pySecureCryptos import encoderDecoders
import random
import secrets
import pickle


# function to generate a random byte
def getRandomByte():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    minStringLen = 1
    maxStringLen = 1000

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    byte = bytes(randomStr , "utf-8")

    return byte





def main():

    fileName = "Byte2String_v2_test_testCases.bin"

    number = 100

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()
        stringFromByte = encoderDecoders.Byte2String_v2.encode(byte)
        outputList.append([byte , stringFromByte])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")



if __name__ == "__main__":
    main()
