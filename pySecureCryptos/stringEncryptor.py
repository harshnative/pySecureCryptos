import onetimepad
import hashlib
import random



# class to shuffle and deshuffle the passed list
class Shuffler:
    
    @classmethod
    def shuffle_under_seed(cls , ls, seed):
        # Shuffle the list ls using the seed `seed`
        random.seed(seed)
        random.shuffle(ls)
        return ls

    @classmethod
    def unshuffle_list(cls , shuffled_ls, seed):
        n = len(shuffled_ls)
        # Perm is [1, 2, ..., n]
        perm = [i for i in range(1, n + 1)]
        # Apply sigma to perm
        shuffled_perm = cls.shuffle_under_seed(perm, seed)
        # Zip and unshuffle
        zipped_ls = list(zip(shuffled_ls, shuffled_perm))
        zipped_ls.sort(key=lambda x: x[1])
        return [a for (a, b) in zipped_ls]


    # function to shuffle a string
    @classmethod
    def shuffleString(cls , string , seed):
        
        # convert the string to list and pass to main method
        shuffledList =  cls.shuffle_under_seed(list(string) , seed)

        # convert the shuffled list back to list
        stringFromList = "".join(shuffledList)
        return stringFromList
    

    # function to shuffle a string
    @classmethod
    def deShuffleString(cls , shuffledString , seed):

        # convert the shuffledString to list and pass to main method
        deshuffledList = cls.unshuffle_list(list(shuffledString) , seed)
        
        # convert the deshuffled list back to string
        stringFromList = "".join(deshuffledList)
        return stringFromList



# class containing encryption methods using one time pad at the end
class OnetimepadWrapper:


    # function to encrypt a string using a password using onetimepad encryption tech
    @classmethod
    def encryptString_password(cls , stringToEncrypt , password , specificSHA = 256):

        """
        ALGO  - 

        1. convert the password to specific SHA form
                SHA available are [224 , 256 , 384 , 512]
                Note - you need to pass the exact specificSHA value while decrypting also , so it is better to just use the default
                Note - do not store the sha of your password you are using here anywhere else. Ex - if you are using SHA256 here , then you can store SHA512 or SHA384 but don't store SHA256
                Note - do not store the md5 hashed value of your password anywhere else

           The string to converted to SHA to increase the length of the key as the encryption of onetimepad is strong only when length of key > length of message
        
        
        2. convert the password to md5 hash


        3. shuffle the SHA hashed password from step 1 according to seed = md5 hashed password


        4. break the string to encrypt into chunks into size = half of len(SHA hashed password)


        5. encrypt the individual chunks using one time pad and shuffle them individually


        6. return the chunks as a joint string 
        """

        # validate type
        stringToEncrypt = str(stringToEncrypt)
        password = str(password)
        specificSHA = int(specificSHA)


        # step 1 - 

        # list containing all the valid sha's present in hashlib library
        # sha224() , sha256() , sha384() , sha512()
        hashFunctionsValidList = [224 , 256 , 384 , 512]


        # check if the specificSHA value is in valid list
        # if not raise ValueError
        if(specificSHA not in hashFunctionsValidList):
            raise ValueError("sha{} is not avaiable please use sha from {}".format(specificSHA , hashFunctionsValidList))


        # make the function string form the sha value
        hashFunctionString = "hashlib.sha{}".format(specificSHA)

        # get the function object
        hashFunction = eval(hashFunctionString)


        # encode the password to pass to hashFunction
        encodedPassword = password.encode()

        # hash the password
        hashedPassword = hashFunction(encodedPassword)

        # converting hashedPassword string type from byte type
        hashedPassword = hashedPassword.hexdigest()

        # hashedlength can be [ 56 , 64 , 96 , 128 ]
        hashedLength = len(hashedPassword)
        hashedLengthby2 = int(hashedLength / 2)

        lenStringToEncrypt = len(stringToEncrypt)

        # step 2 - 

        md5HashedPassword = hashlib.md5(password.encode()).hexdigest()

        # step 3 - 

        hashedPasswordShuffled = Shuffler.shuffleString(hashedPassword , md5HashedPassword)

        # step 4 - 

        # split in the string to chunks each of len hashedLength
        chunkList = []
    
        for i in range(0 , lenStringToEncrypt , hashedLengthby2):
            
            # if the string is not about to end
            # means string still as greator number of elements left than lenStringToEncry pt
            if((i + hashedLengthby2) < lenStringToEncrypt):

                # string from i to i + hashedLengthby2 
                chunkList.append(stringToEncrypt[i : i + hashedLengthby2]) 
            else:
                chunkList.append(stringToEncrypt[i : ]) 

        result = ""

        # step 5 -
        
        for i in chunkList:
            
            # output string is of double the length of input string
            encryptedChunk = onetimepad.encrypt(i , hashedPasswordShuffled)
            encryptedChunkShuffled = Shuffler.shuffleString(encryptedChunk , md5HashedPassword)
            
            
            # step 6 - 

            result = result + encryptedChunkShuffled

        return result



    # function to decrypt a string encrypted using encryptString_password method of this class
    @classmethod
    def decryptString_password(cls , stringToDecrypt , password , specificSHA = 256):
        
        """
        ALGO  - 

        1. convert the password to specific SHA form
                SHA available are [224 , 256 , 384 , 512]
                Note - you need to pass the exact specificSHA value you used to encrypt the string
                Note - do not store the sha of your password you are using here anywhere else. Ex - if you are using SHA256 here , then you can store SHA512 or SHA384 but don't store SHA256
                Note - do not store the md5 hashed value of your password anywhere else

           The string to converted to SHA to increase the length of the key as the encryption of onetimepad is strong only when length of key > length of message
        
        
        2. convert the password to md5 hash


        3. shuffle the SHA hashed password from step 1 according to seed = md5 hashed password


        4. break the string to decrypt into chunks into size = len(SHA hashed password)


        5. shuffle them individually and decrypt the individual chunks using one time pad


        6. return the chunks as a joint string 
        """

        # validate type
        stringToDecrypt = str(stringToDecrypt)
        password = str(password)
        specificSHA = int(specificSHA)


        # step 1 - 

        # list containing all the valid sha's present in hashlib library
        # sha224() , sha256() , sha384() , sha512()
        hashFunctionsValidList = [224 , 256 , 384 , 512]


        # check if the specificSHA value is in valid list
        # if not raise ValueError
        if(specificSHA not in hashFunctionsValidList):
            raise ValueError("sha{} is not avaiable please use sha from {}".format(specificSHA , hashFunctionsValidList))


        # make the function string form the sha value
        hashFunctionString = "hashlib.sha{}".format(specificSHA)

        # get the function object
        hashFunction = eval(hashFunctionString)


        # encode the password to pass to hashFunction
        encodedPassword = password.encode()

        # hash the password
        hashedPassword = hashFunction(encodedPassword)

        # converting hashedPassword string type from byte type
        hashedPassword = hashedPassword.hexdigest()

        # hashedlength can be [ 56 , 64 , 96 , 128 ]
        hashedLength = len(hashedPassword)

        lenStringToDecrypt = len(stringToDecrypt)

        # step 2 - 

        md5HashedPassword = hashlib.md5(password.encode()).hexdigest()

        # step 3 - 

        hashedPasswordShuffled = Shuffler.shuffleString(hashedPassword , md5HashedPassword)


        # step 4 - 

        # split in the string to chunks each of len hashedLength
        chunkList = []
    
        for i in range(0 , lenStringToDecrypt , hashedLength):
            
            # if the string is not about to end
            # means string still as greator number of elements left than lenStringToDecrypt
            if((i + hashedLength) < lenStringToDecrypt):

                # string from i to i + hashedLength (remember output string is 2 times the length of input string) 
                chunkList.append(stringToDecrypt[i : i + hashedLength]) 
            else:
                chunkList.append(stringToDecrypt[i : ]) 

        result = ""

        # step 5 -
        
        for i in chunkList:

            # output string is of half the length of input string
            chunkDeShuffled = Shuffler.deShuffleString(i , md5HashedPassword)
            decryptedChunk = onetimepad.decrypt(chunkDeShuffled , hashedPasswordShuffled)
            
            
            # step 6 - 

            result = result + decryptedChunk

        return result

        






if __name__ == "__main__":
    encryptedString = OnetimepadWrapper.encryptString_password("hello world " * 100 , "hello" , 224)
    
    print(encryptedString)

    decryptedString = OnetimepadWrapper.decryptString_password(encryptedString , "hello" , 224)

    print(decryptedString)