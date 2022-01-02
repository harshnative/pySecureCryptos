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

    fileName = "HexConvertor_yield_test_testCases.bin"

    number = 100

    outputList = []

    for i in range(number):
        print(i)

        byte = getRandomByte()
        gen = encoderDecoders.HexConvertor.encode_yield(byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                stringFromByte = ex.value
                break
        
        outputList.append([byte , stringFromByte])
        

    pickledList = pickle.dumps(outputList)

    with open(fileName , "wb") as file:
        file.write(pickledList)

    print("DONE")



if __name__ == "__main__":
    main()
