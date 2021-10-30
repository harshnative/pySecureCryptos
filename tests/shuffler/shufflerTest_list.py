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
def shufflerTester_list(howManyTimes , writeErrors = True):
    avgTime = 0
    errorList = []
    totalErrors = 0

    # repeat the test howManyTimes
    for k in range(howManyTimes):

        print(f"\ron {k} / {howManyTimes}" , end = "")

        # list size
        testListSize = random.randint(0 , 1000)
        testList = []

        # adding random things to list
        for i in range(testListSize):
            # adding string
            if(random.random() <= 0.3):
                randList = random.choices(mainList , k=random.randint(10 , 100))
                randString = "".join(randList)
                testList.append(randString)

            # adding number
            elif(random.random() <= 0.6):
                randInt = random.randint(0 , 5000)
                testList.append(randInt)

            # adding byte
            else:
                randList = random.choices(mainList , k=random.randint(10 , 100))
                randString = "".join(randList)
                randString = bytes(randString , encoding="utf-8")
                testList.append(randString)

        # random string for the seed
        randList = random.choices(mainList , k=random.randint(10 , 1000))
        randString = "".join(randList)

        # executing the functions to test and calculating time
        startTime = time.time()
        shuffledTestList = Shuffler.shuffe_list(testList , randString)

        deShuffledList = Shuffler.unShuffle_list(shuffledTestList , randString)
        endTime = time.time()

        # avgTime
        avgTime = avgTime + (endTime - startTime)

        # if the result is not true than add to error list
        if(deShuffledList != testList):
            errorList.append([testList , shuffledTestList , deShuffledList])
            totalErrors = totalErrors + 1

    # write the error list to the file
    if(totalErrors != 0):
        with open(fileName + "shufflerTester_list" + ".txt" , "w") as file:
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
shufflerTester_list(1000)

            


            



