from pySecureCryptos import encoderDecoders
import random
import secrets
import pickle



# function to generate a random byte
def getRandomByte():
    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    return byte






def main():

    fileName = "binFiles/encoderDecoder_testcases_bin/Base64_16_test_testCases.bin"

    number = 10

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()
        stringFromByte = encoderDecoders.Base64_16.encode(byte)
        
        outputList.append([byte , stringFromByte])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")



if __name__ == "__main__":
    main()
