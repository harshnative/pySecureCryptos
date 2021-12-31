import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")

import string
import random
import time
import secrets
import os


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
def byteEncryptorTest_func(writeErrors = True):
    avgTime = 0
    errorList = []
    totalErrors = 0

    folderPath = "/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial"

    filesList = os.listdir(folderPath)

    # repeat the test howManyTimes
    for k in filesList:

        print(f"\n\non {k} ")

        print("file reading")
        with open(folderPath + "/" + k , "rb") as file:
            data = file.read()

        print("file size = " , len(data))

        # string for seed
        randList = random.choices(mainList , k=random.randint(1 , 1000))
        randString1 = "".join(randList)

        randomChunkSize = random.randint(1 , 100) * 128


        # executing the functions to test and calculating time
        startTime = time.perf_counter()

        print("file encrypting")

        fernetObj = Encryptor(randString1 , chunkSize=randomChunkSize)

        print("chunkSize = " , randomChunkSize)
        
        genObj = fernetObj.encrypt_byte_yield(data)
        
        while(True):
            try:
                i = next(genObj)
                print("\r{}   ".format(i) , end = "")
            except StopIteration as ex:
                encrytedByte = ex.value
                break

        print("\nfile decrypting")

        genObj = fernetObj.decrypt_byte_yield(encrytedByte)
        
        while(True):
            try:
                i = next(genObj)
                print("\r{}   ".format(i) , end = "")
            except StopIteration as ex:
                decryptedByte = ex.value
                break
        
        endTime = time.perf_counter()

        # avgTime
        avgTime = avgTime + (endTime - startTime)

        # if the result is not true than add to error list
        if(decryptedByte != data):
            errorList.append([data , encrytedByte , decryptedByte])
            totalErrors = totalErrors + 1

    # write the error list to the file
    if(totalErrors != 0):
        with open(fileName + "ByteEncryptorTest_func" + ".txt" , "w") as file:
            for i in errorList:
                for j in i:
                    file.write(str(j))
                    file.write("\n")
                file.write("\n\n")

    avgTime = avgTime / len(filesList)

    print("\n")

    # print the result
    if(totalErrors == 0):
        print(blueColor + "avg time taken by function per cycle = {}".format(avgTime))
        print(greenColor + "function test passed")
    else:
        print(redColor + "function test failed")
        print(blueColor + "errors has been logged to the (file + functionName).txt")

# execute the function
byteEncryptorTest_func()

            


            