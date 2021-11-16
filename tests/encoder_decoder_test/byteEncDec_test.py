import secrets
import random 
import time

from colored import fg
blueColor = fg('blue')
greenColor = fg('green')
redColor = fg('red')
yellowColor = fg('yellow')
whiteColor = fg('white')

from pySecureCryptos.encoderDecoders import Byte2String , String2Byte

def testEncodeByte2String(howMany):
    avgTime = 0
    error = 0
    errorList = []

    for k in range(howMany):

        print(f"\ron {k} / {howMany}" , end = "")

        byteLength = random.randint(0 , 100000)

        randomByte = secrets.token_bytes(byteLength)

        start = time.time()
        encodedString = Byte2String.encode(randomByte)
        decodedByte = Byte2String.decode(encodedString)
        end = time.time()

        avgTime = avgTime + (((end - start) / byteLength) * 1000)

        if(decodedByte != randomByte):
            error = error + 1 
            errorList.append([randomByte , decodedByte])

    avgTime = avgTime / howMany

    return error , errorList , avgTime


print("\n\n")

# testing determinant function 
print(whiteColor + "on Byte2String")

error , errorList , avgTime = testEncodeByte2String(1000)

print()

if(error == 0):
    print(blueColor + "avg time taken by testEncodeByte2String function per encode decode cycle per 1000 chars = {}".format(avgTime))
    print(greenColor + "testEncodeByte2String function test passed")
else:
    print(redColor + "testEncodeByte2String function test failed")
    print(redColor + "error = {} / {}".format(error , 1000))
    print(redColor + "error list = {}".format(errorList))



def testEncodeString2Byte(howMany):
    avgTime = 0
    error = 0
    errorList = []

    for k in range(howMany):

        print(f"\ron {k} / {howMany}" , end = "")

        stringPool = []

        for i in range(0 , 256):
            stringPool.append(chr(i))

        stringLength = random.randint(1 , 100000)

        randomString = ""
        for i in range(stringLength):
            randomString = randomString + random.choice(stringPool)

        start = time.time()
        encodedByte = String2Byte.encode(randomString)
        decodedString = String2Byte.decode(encodedByte)
        end = time.time()

        avgTime = avgTime + (((end - start) / stringLength) * 1000)

        if(decodedString != randomString):
            error = error + 1 
            errorList.append([randomString , decodedString])

    avgTime = avgTime / howMany

    return error , errorList , avgTime


print("\n\n")

# testing determinant function 
print(whiteColor + "on String2Byte")

error , errorList , avgTime = testEncodeString2Byte(1000)

print()

if(error == 0):
    print(blueColor + "avg time taken by testEncodeString2Byte function per encode decode cycle per 1000 chars = {}".format(avgTime))
    print(greenColor + "testEncodeString2Byte function test passed")
else:
    print(redColor + "testEncodeString2Byte function test failed")
    print(redColor + "error = {} / {}".format(error , 1000))
    print(redColor + "error list = {}".format(errorList))




