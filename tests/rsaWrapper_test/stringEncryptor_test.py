import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")

import string
import random
import time


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
from pySecureCryptos.rsaWrapper import Encryptor , KeyGenerator


# main function to run the test
def StringEncryptorTest_func(howManyTimes , writeErrors = True):
    avgTime = 0
    errorList = []
    totalErrors = 0


    for k_main in range(howManyTimes // 10):

        keyGenObj = KeyGenerator()

        privateKey_bytes = keyGenObj.get_privateKey_bytes()
        privateKey_string = keyGenObj.get_privateKey_string()

        publicKey_bytes = keyGenObj.get_publicKey_bytes()
        publicKey_string = keyGenObj.get_publicKey_string()


        # repeat the test howManyTimes
        for k in range(howManyTimes):

            print(f"\n\non {k_main , k} / {howManyTimes}")

            # string size
            stringSize = random.randint(10000 , 100000)

            # string for seed
            randList = random.choices(mainList , k=random.randint(1 , 1000))
            randString1 = "".join(randList)

            # string for shuffle test
            randList = random.choices(mainList , k=stringSize)
            randString2 = "".join(randList)

            if(random.random() > 0.5):
                encObj = Encryptor(publicKey_bytes , privateKey_bytes)
            
            else:
                encObj = Encryptor(publicKey_string , privateKey_string)



            # executing the functions to test and calculating time
            startTime = time.perf_counter()
            genObj_encrypt = encObj.encrypt_string_yield(randString2)

            while(True):
                try:
                    onCount , totalCount = next(genObj_encrypt)
                    print(f"\renc {onCount} / {totalCount}" , end="")
                except StopIteration as ex:
                    encrytedString = ex.value
                    break

            print()

            genObj_decrypt = encObj.decrypt_string_yield(encrytedString)
            while(True):
                try:
                    onCount , totalCount = next(genObj_decrypt)
                    print(f"\rdec {onCount} / {totalCount}" , end="")
                except StopIteration as ex:
                    decryptedString = ex.value
                    break
            
            endTime = time.perf_counter()

            # avgTime
            avgTime = avgTime + (endTime - startTime)

            # if the result is not true than add to error list
            if(decryptedString != randString2):
                errorList.append([randString2 , encrytedString , decryptedString])
                totalErrors = totalErrors + 1

    # write the error list to the file
    if(totalErrors != 0):
        with open(fileName + "StringEncryptorTest_func" + ".txt" , "w") as file:
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
StringEncryptorTest_func(50)

            


            



