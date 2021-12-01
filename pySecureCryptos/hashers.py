import hashlib
from shuffler import Shuffler


class SHA256:

    # constructor
    # type check parameters and assign objects to self
    # string retruned length is 64
    # byte returned len is 32
    def __init__(self , bytesObj , chunkSize = 2048):

        if(type(bytesObj) != bytes):
            raise ValueError("bytesObj parameter expected to be of bytes type instead got {} type".format(type(bytesObj)))
        if(type(chunkSize) != int):
            raise ValueError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        self.bytesObj = bytesObj
        self.lenBytes = len(bytesObj)

        self.sha224_hash = hashlib.sha224()
        self.sha256_hash = hashlib.sha256()

        self.chunkSize = chunkSize

    



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string_yield(self):

        # total yield - 2 times , one for 224 hash and second for 256 hash
        totalYield = ((self.lenBytes // self.chunkSize) + 1) * 2
        currentCount = 1

        # sha224 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        bytesObj_sha224_hashed = self.sha224_hash.hexdigest()

        # shuffe bytesObj using sha224 hash value as seed
        shuffledBytesObj = Shuffler.shuffle_byte(self.bytesObj , bytesObj_sha224_hashed)

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(shuffledBytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha256_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte_yield(self):

        # total yield - 2 times , one for 224 hash and second for 256 hash
        totalYield = ((self.lenBytes // self.chunkSize) + 1) * 2
        currentCount = 1

        # sha224 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        bytesObj_sha224_hashed = self.sha224_hash.hexdigest()

        # shuffe bytesObj using sha224 hash value as seed
        shuffledBytesObj = Shuffler.shuffle_byte(self.bytesObj , bytesObj_sha224_hashed)

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(shuffledBytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha256_hash.digest()

        # return
        return finalHash



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string(self):

        # sha224 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

        bytesObj_sha224_hashed = self.sha224_hash.hexdigest()

        # shuffe bytesObj using sha224 hash value as seed
        shuffledBytesObj = Shuffler.shuffle_byte(self.bytesObj , bytesObj_sha224_hashed)

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(shuffledBytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha256_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte(self):

        # sha224 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

        bytesObj_sha224_hashed = self.sha224_hash.hexdigest()

        # shuffe bytesObj using sha224 hash value as seed
        shuffledBytesObj = Shuffler.shuffle_byte(self.bytesObj , bytesObj_sha224_hashed)

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(shuffledBytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha256_hash.digest()

        # return
        return finalHash
        









def __test_sha256_yield():

    bytesObj = b"hello world" * 11230

    shaObj = SHA256(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha256Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")






def __test_sha256_yield2():

    bytesObj = b"hello world" * 11230

    shaObj = SHA256(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha256Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")







def __test_sha256_yield3():

    bytesObj = b"hello world"

    shaObj = SHA256(bytesObj)

    sha256Hash = shaObj.get_string()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")





def __test_sha256_yield4():

    bytesObj = b"hello world"

    shaObj = SHA256(bytesObj)

    sha256Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")



if __name__ == "__main__":
    __test_sha256_yield2()