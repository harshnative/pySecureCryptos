import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")

import string
import random
import time
import secrets


# create objects to print colored strings
from colored import fg
blueColor = fg('blue')
greenColor = fg('green')
redColor = fg('red')
yellowColor = fg('yellow')
whiteColor = fg('white')

# file name in which the errors will be written to 
fileName = "testResult"

# list of lettes , nums , special chars
mainList = list(string.ascii_letters + string.digits + "!@#$%^&*(){}[]:;'<,>./")


# importing module for testing
from pySecureCryptos.verifier_fernetWrapper_v2_2 import Encryptor


# main function to run the test
def byteEncryptorTest_func(howManyTimes , writeErrors = True):
    avgTime = 0
    errorList = []
    totalErrors = 0

    # repeat the test howManyTimes
    for k in range(howManyTimes):

        print(f"\ron {k} / {howManyTimes}" , end = "")

        # string size
        byteLength = random.randint(0 , 10000)

        randomByte = secrets.token_bytes(byteLength)

        # string for seed
        randList = random.choices(mainList , k=random.randint(1 , 1000))
        randString1 = "".join(randList)

        fernetObj = Encryptor(randString1)

        # executing the functions to test and calculating time
        startTime = time.perf_counter()
        encrytedByte = fernetObj.encrypt_byte(randomByte)

        decryptedByte = fernetObj.decrypt_byte(encrytedByte)
        endTime = time.perf_counter()

        # avgTime
        avgTime = avgTime + (endTime - startTime)

        # if the result is not true than add to error list
        if(decryptedByte != randomByte):
            errorList.append([randomByte , encrytedByte , decryptedByte])
            totalErrors = totalErrors + 1

    # write the error list to the file
    if(totalErrors != 0):
        with open(fileName + "ByteEncryptorTest_func" + ".txt" , "w") as file:
            for i in errorList:
                for j in i:
                    file.write(str(j))
                    file.write("\n")
                file.write("\n\n")

    avgTime = avgTime / howManyTimes

    print()

    # print the result
    if(totalErrors == 0):
        print(blueColor + "avg time taken by function per cycle = {}".format(avgTime))
        print(greenColor + "function test passed")
    else:
        print(redColor + "function test failed")
        print(blueColor + "errors has been logged to the (file + functionName).txt")

# execute the function
byteEncryptorTest_func(500)

            


            



