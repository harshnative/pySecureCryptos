from shuffler import Shuffler
import hashlib
import onetimepad

class StringEncryptor:

    @classmethod
    def encrypt(cls , string , password):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        lenString = len(string)
        hashedLength = len(sha224_hashed_password_shuffled)

        for i in range(0 , lenString , hashedLength):
            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

        return result


    @classmethod
    def decrypt(cls , enc_string , password):

        # type checking the parameters
        if(type(enc_string) != str):
            raise ValueError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

        return result



        



def __test():
    string = "hello world"
    encryptedString = StringEncryptor.encrypt(string , "hello")
    decryptedString = StringEncryptor.decrypt(encryptedString , "hello")

    print(string)
    print(encryptedString)
    print(decryptedString)

    if(string == decryptedString):
        print("ok")
    else:
        print("error")



if __name__ == "__main__":
    __test()