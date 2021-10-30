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
from pySecureCryptos.shuffler import Shuffler



# main function to run the test
def shufflerTester_string(howManyTimes , writeErrors = True):
    avgTime = 0
    errorList = []
    totalErrors = 0

    # repeat the test howManyTimes
    for k in range(howManyTimes):

        print(f"\ron {k} / {howManyTimes}" , end = "")

        # string size
        stringSize = random.randint(1 , 1000)

        # string for seed
        randList = random.choices(mainList , k=random.randint(10 , 1000))
        randString1 = "".join(randList)

        # string for shuffle test
        randList = random.choices(mainList , k=stringSize)
        randString2 = "".join(randList)

        # executing the functions to test and calculating time
        startTime = time.time()
        shuffledString = Shuffler.shuffle_string(randString2 , randString1)

        deShuffledString = Shuffler.unShuffle_string(shuffledString , randString1)
        endTime = time.time()

        # avgTime
        avgTime = avgTime + (endTime - startTime)

        # if the result is not true than add to error list
        if(deShuffledString != randString2):
            errorList.append([randString2 , shuffledString , deShuffledString])
            totalErrors = totalErrors + 1

    # write the error list to the file
    if(totalErrors != 0):
        with open(fileName + "shufflerTester_string" + ".txt" , "w") as file:
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
shufflerTester_string(1000)

            


            



