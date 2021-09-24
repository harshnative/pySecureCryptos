import string
import random
import time



from colored import fg
blueColor = fg('blue')
greenColor = fg('green')
redColor = fg('red')
yellowColor = fg('yellow')
whiteColor = fg('white')


import stringEncryptor




def OnetimepadWrapperTester_password():

    
    def testEncryptionDecryption_password(howMany):

        avgTime = 0
        error = 0
        errorList = []

        for k in range(howMany):

            print(f"\ron {k} / {howMany}" , end = "")

            stringPool = []

            for i in range(32 , 126):
                stringPool.append(chr(i))

            stringLength = random.randint(1 , 100000)

            randomString = ""
            for i in range(stringLength):
                randomString = randomString + random.choice(stringPool)

            randomPassword = ""
            for i in range(random.randint(1 , 100)):
                randomPassword = randomPassword + random.choice(stringPool)

            specificSHA = random.choice([224,256,384,512])

            start = time.time()
            encryptedString = stringEncryptor.OnetimepadWrapper.encryptString_password(randomString , randomPassword , specificSHA)

            decryptedString = stringEncryptor.OnetimepadWrapper.decryptString_password(encryptedString , randomPassword , specificSHA)
            end = time.time()

            avgTime = avgTime + (((end - start) / stringLength) * 1000)

            if(decryptedString != randomString):
                error = error + 1 
                errorList.append(randomString , decryptedString , randomPassword , specificSHA)

        avgTime = avgTime / howMany

        return error , errorList , avgTime


    print("\n\n")

    # testing determinant function 
    print(whiteColor + "Testing encryption decryption password in onetimewrapper")

    error , errorList , avgTime = testEncryptionDecryption_password(1000)

    print()

    if(error == 0):
        print(blueColor + "avg time taken by testEncryptionDecryption_password function per encryption decyption cycle per 1000 chars = {}".format(avgTime))
        print(greenColor + "testEncryptionDecryption_password function test passed")
    else:
        print(redColor + "testEncryptionDecryption_password function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))












def OnetimepadWrapperTester():

    
    def testEncryptionDecryption(howMany):

        avgTime = 0
        error = 0
        errorList = []

        for k in range(howMany):

            print(f"\ron {k} / {howMany}" , end = "")

            stringPool = []

            for i in range(32 , 126):
                stringPool.append(chr(i))

            stringLength = random.randint(1 , 100000)

            randomString = ""
            for i in range(stringLength):
                randomString = randomString + random.choice(stringPool)

            randomPassword = ""
            for i in range(random.randint(1 , 100)):
                randomPassword = randomPassword + random.choice(stringPool)


            start = time.time()
            encryptedString = stringEncryptor.OnetimepadWrapper.encryptString(randomString , randomPassword)

            decryptedString = stringEncryptor.OnetimepadWrapper.decryptString(encryptedString , randomPassword)
            end = time.time()

            avgTime = avgTime + (((end - start) / stringLength) * 1000)

            if(decryptedString != randomString):
                error = error + 1 
                errorList.append(randomString , decryptedString , randomPassword , specificSHA)

        avgTime = avgTime / howMany

        return error , errorList , avgTime


    print("\n\n")

    # testing determinant function 
    print(whiteColor + "Testing encryption decryption in onetimewrapper")

    error , errorList , avgTime = testEncryptionDecryption(1000)

    print()

    if(error == 0):
        print(blueColor + "avg time taken by testEncryptionDecryption function per encryption decyption cycle per 1000 chars = {}".format(avgTime))
        print(greenColor + "testEncryptionDecryption function test passed")
    else:
        print(redColor + "testEncryptionDecryption function test failed")
        print(redColor + "error = {} / {}".format(error , 1000))
        print(redColor + "error list = {}".format(errorList))











if __name__ == "__main__":

    testsDict = {
        1 : OnetimepadWrapperTester_password , 
        2 : OnetimepadWrapperTester , 
        # 3 : transposeFuncTest , 
        # 4 : meanFunctionTest , 
        # 5 : multiplyFunctionTest ,
        # 6 : sortingTester ,
        # 7 : binarySearchIterativeFuncTest ,
        # 8 : binarySearchRecursiveFuncTest ,
    }

    print("Select space seperated choices from below or 0 for all")

    for i,j in testsDict.items():
        print("{}: {}".format(i , j.__name__))

    inputted = input("Enter your choices here : ")

    if(inputted.strip() == "0"):
        for i,j in testsDict.items():
            j()
    else:
        inputtedList = [int(i) for i in inputted.split()]
        for i,j in testsDict.items():
            if(i in inputtedList):
                j()
