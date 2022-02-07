import hashlib










#  __  __   ____    ____   
# |  \/  | |  _ \  | ___|  
# | |\/| | | | | | |___ \  
# | |  | | | |_| |  ___) | 
# |_|  |_| |____/  |____/  
                         


class MD5:

    # constructor
    # type check parameters and assign objects to self
    # string retruned length is 32
    # byte returned len is 16
    def __init__(self , bytesObj : bytes , chunkSize : int = 1048576):

        if(type(bytesObj) != bytes):
            raise TypeError("bytesObj parameter expected to be of bytes type instead got {} type".format(type(bytesObj)))
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        self.bytesObj = bytesObj
        self.lenBytes = len(bytesObj)

        self.md5_hash = hashlib.md5()

        self.chunkSize = chunkSize

    



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string_yield(self) -> str:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.md5_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.md5_hash.hexdigest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte_yield(self) -> bytes:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.md5_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.md5_hash.digest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string(self) -> str:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.md5_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.md5_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte(self) -> bytes:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.md5_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.md5_hash.digest()

        # return
        return finalHash
        
























#  ____    _   _      _      _  
# / ___|  | | | |    / \    / | 
# \___ \  | |_| |   / _ \   | | 
#  ___) | |  _  |  / ___ \  | | 
# |____/  |_| |_| /_/   \_\ |_| 
                              



class SHA1:

    # constructor
    # type check parameters and assign objects to self
    # string retruned length is 40
    # byte returned len is 20
    def __init__(self , bytesObj : bytes , chunkSize : int = 1048576):

        if(type(bytesObj) != bytes):
            raise TypeError("bytesObj parameter expected to be of bytes type instead got {} type".format(type(bytesObj)))
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        self.bytesObj = bytesObj
        self.lenBytes = len(bytesObj)

        self.sha1_hash = hashlib.sha1()

        self.chunkSize = chunkSize

    



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string_yield(self) -> str:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha1_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha1_hash.hexdigest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte_yield(self) -> bytes:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha1_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha1_hash.digest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string(self) -> str:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha1_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha1_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte(self) -> bytes:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha1_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha1_hash.digest()

        # return
        return finalHash
        






























#  ____    _   _      _      ____    ____    _  _    
# / ___|  | | | |    / \    |___ \  |___ \  | || |   
# \___ \  | |_| |   / _ \     __) |   __) | | || |_  
#  ___) | |  _  |  / ___ \   / __/   / __/  |__   _| 
# |____/  |_| |_| /_/   \_\ |_____| |_____|    |_|   
                                                   




class SHA224:

    # constructor
    # type check parameters and assign objects to self
    # string retruned length is 56
    # byte returned len is 28
    def __init__(self , bytesObj : bytes , chunkSize : int = 1048576):

        if(type(bytesObj) != bytes):
            raise TypeError("bytesObj parameter expected to be of bytes type instead got {} type".format(type(bytesObj)))
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        self.bytesObj = bytesObj
        self.lenBytes = len(bytesObj)

        self.sha224_hash = hashlib.sha224()

        self.chunkSize = chunkSize

    



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string_yield(self) -> str:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha224_hash.hexdigest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte_yield(self) -> bytes:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha224_hash.digest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string(self) -> str:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha224_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte(self) -> bytes:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha224_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha224_hash.digest()

        # return
        return finalHash
        




















#  ____    _   _      _      ____    ____     __    
# / ___|  | | | |    / \    |___ \  | ___|   / /_   
# \___ \  | |_| |   / _ \     __) | |___ \  | '_ \  
#  ___) | |  _  |  / ___ \   / __/   ___) | | (_) | 
# |____/  |_| |_| /_/   \_\ |_____| |____/   \___/  
                                                  

class SHA256:

    # constructor
    # type check parameters and assign objects to self
    # string retruned length is 64
    # byte returned len is 32
    def __init__(self , bytesObj : bytes , chunkSize : int = 1048576):

        if(type(bytesObj) != bytes):
            raise TypeError("bytesObj parameter expected to be of bytes type instead got {} type".format(type(bytesObj)))
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        self.bytesObj = bytesObj
        self.lenBytes = len(bytesObj)

        self.sha256_hash = hashlib.sha256()

        self.chunkSize = chunkSize

    



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string_yield(self) -> str:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha256_hash.hexdigest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte_yield(self) -> bytes:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha256_hash.digest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string(self) -> str:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha256_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte(self) -> bytes:

        # sha256 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha256_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha256_hash.digest()

        # return
        return finalHash
        





























#  ____    _   _      _      _____    ___    _  _    
# / ___|  | | | |    / \    |___ /   ( _ )  | || |   
# \___ \  | |_| |   / _ \     |_ \   / _ \  | || |_  
#  ___) | |  _  |  / ___ \   ___) | | (_) | |__   _| 
# |____/  |_| |_| /_/   \_\ |____/   \___/     |_|   
                                                   

class SHA384:

    # constructor
    # type check parameters and assign objects to self
    # string retruned length is 96
    # byte returned len is 48
    def __init__(self , bytesObj : bytes , chunkSize : int = 1048576):

        if(type(bytesObj) != bytes):
            raise TypeError("bytesObj parameter expected to be of bytes type instead got {} type".format(type(bytesObj)))
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        self.bytesObj = bytesObj
        self.lenBytes = len(bytesObj)

        
        self.sha384_hash = hashlib.sha384()

        self.chunkSize = chunkSize

    



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string_yield(self) -> str:

        totalYield = ((self.lenBytes // self.chunkSize) + 1) 
        currentCount = 1

        # sha384 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha384_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha384_hash.hexdigest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte_yield(self) -> bytes:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        # sha384 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha384_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha384_hash.digest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string(self) -> str:

        # sha384 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha384_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha384_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte(self) -> bytes:

        # sha384 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha384_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha384_hash.digest()

        # return
        return finalHash
        











































#  ____    _   _      _      ____    _   ____   
# / ___|  | | | |    / \    | ___|  / | |___ \  
# \___ \  | |_| |   / _ \   |___ \  | |   __) | 
#  ___) | |  _  |  / ___ \   ___) | | |  / __/  
# |____/  |_| |_| /_/   \_\ |____/  |_| |_____| 
                                              

class SHA512:

    # constructor
    # type check parameters and assign objects to self
    # string retruned length is 128
    # byte returned len is 64
    def __init__(self , bytesObj : bytes , chunkSize : int = 1048576):

        if(type(bytesObj) != bytes):
            raise TypeError("bytesObj parameter expected to be of bytes type instead got {} type".format(type(bytesObj)))
        if(type(chunkSize) != int):
            raise TypeError("chunkSize parameter expected to be of int type instead got {} type".format(type(chunkSize)))

        self.bytesObj = bytesObj
        self.lenBytes = len(bytesObj)

        self.sha512_hash = hashlib.sha512()

        self.chunkSize = chunkSize

    



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string_yield(self) -> str:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1


        # sha512 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha512_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha512_hash.hexdigest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte_yield(self) -> bytes:

        totalYield = ((self.lenBytes // self.chunkSize) + 1)
        currentCount = 1

        # sha512 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha512_hash.update(self.bytesObj[i : i+self.chunkSize])

            yield currentCount , totalYield
            currentCount = currentCount + 1

        # get string 
        finalHash = self.sha512_hash.digest()

        # return
        if(currentCount <= totalYield):
            yield totalYield , totalYield
        return finalHash



    # function to get the string of the hashed object
    # this is a yielder function
    def get_string(self) -> str:

        # sha512 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha512_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha512_hash.hexdigest()

        # return
        return finalHash

    



    # function to get the byte of the hashed object
    # this is a yielder function
    def get_byte(self) -> bytes:

        # sha512 hash
        for i in range(0 , self.lenBytes , self.chunkSize):
            self.sha512_hash.update(self.bytesObj[i : i+self.chunkSize])

        # get string 
        finalHash = self.sha512_hash.digest()

        # return
        return finalHash















































#  _                  _          ____    _   _      _      ____    ____     __    
# | |_    ___   ___  | |_       / ___|  | | | |    / \    |___ \  | ___|   / /_   
# | __|  / _ \ / __| | __|      \___ \  | |_| |   / _ \     __) | |___ \  | '_ \  
# | |_  |  __/ \__ \ | |_        ___) | |  _  |  / ___ \   / __/   ___) | | (_) | 
#  \__|  \___| |___/  \__|      |____/  |_| |_| /_/   \_\ |_____| |____/   \___/  
                                                                                
                                                                                                             

def __test_sha256_yield():

    bytesObj = b"hello world" * 1024 * 1024

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

    bytesObj = b"hello world" * 1024 * 1024

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







def __test_sha256():

    bytesObj = b"hello world"

    shaObj = SHA256(bytesObj)

    sha256Hash = shaObj.get_string()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")





def __test_sha256_2():

    bytesObj = b"hello world"

    shaObj = SHA256(bytesObj)

    sha256Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")





















#  _                  _          ____    _   _      _      _____    ___    _  _    
# | |_    ___   ___  | |_       / ___|  | | | |    / \    |___ /   ( _ )  | || |   
# | __|  / _ \ / __| | __|      \___ \  | |_| |   / _ \     |_ \   / _ \  | || |_  
# | |_  |  __/ \__ \ | |_        ___) | |  _  |  / ___ \   ___) | | (_) | |__   _| 
#  \__|  \___| |___/  \__|      |____/  |_| |_| /_/   \_\ |____/   \___/     |_|   
                                                                                 

def __test_sha384_yield():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA384(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha384Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")






def __test_sha384_yield2():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA384(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha384Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")







def __test_sha384():

    bytesObj = b"hello world"

    shaObj = SHA384(bytesObj)

    sha384Hash = shaObj.get_string()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")





def __test_sha384_2():

    bytesObj = b"hello world"

    shaObj = SHA384(bytesObj)

    sha384Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")





























#  _                  _                       ____    _   _      _      ____    _   ____   
# | |_    ___   ___  | |_                    / ___|  | | | |    / \    | ___|  / | |___ \  
# | __|  / _ \ / __| | __|       _____       \___ \  | |_| |   / _ \   |___ \  | |   __) | 
# | |_  |  __/ \__ \ | |_       |_____|       ___) | |  _  |  / ___ \   ___) | | |  / __/  
#  \__|  \___| |___/  \__|                   |____/  |_| |_| /_/   \_\ |____/  |_| |_____| 
                                                                                         

def __test_sha512_yield():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA512(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha512Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")






def __test_sha512_yield2():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA512(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha512Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")







def __test_sha512():

    bytesObj = b"hello world"

    shaObj = SHA512(bytesObj)

    sha512Hash = shaObj.get_string()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")





def __test_sha512_2():

    bytesObj = b"hello world"

    shaObj = SHA512(bytesObj)

    sha512Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")















#  _                  _                       ____    _   _      _      _  
# | |_    ___   ___  | |_                    / ___|  | | | |    / \    / | 
# | __|  / _ \ / __| | __|       _____       \___ \  | |_| |   / _ \   | | 
# | |_  |  __/ \__ \ | |_       |_____|       ___) | |  _  |  / ___ \  | | 
#  \__|  \___| |___/  \__|                   |____/  |_| |_| /_/   \_\ |_| 
                                                                         
                                                                                  

def __test_sha1_yield():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA1(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha1Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")






def __test_sha1_yield2():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA1(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha1Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")







def __test_sha1():

    bytesObj = b"hello world"

    shaObj = SHA1(bytesObj)

    sha1Hash = shaObj.get_string()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")





def __test_sha1_2():

    bytesObj = b"hello world"

    shaObj = SHA1(bytesObj)

    sha1Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")



















#  _                  _                          _   ____   
# | |_    ___   ___  | |_        _ __ ___     __| | | ___|  
# | __|  / _ \ / __| | __|      | '_ ` _ \   / _` | |___ \  
# | |_  |  __/ \__ \ | |_       | | | | | | | (_| |  ___) | 
#  \__|  \___| |___/  \__|      |_| |_| |_|  \__,_| |____/  
                                                          
                                                      

def __test_md5_yield():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = MD5(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            md5Hash = ex.value
            break
    print()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")






def __test_md5_yield2():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = MD5(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            md5Hash = ex.value
            break
    print()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")







def __test_md5():

    bytesObj = b"hello world"

    shaObj = MD5(bytesObj)

    md5Hash = shaObj.get_string()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")





def __test_md5_2():

    bytesObj = b"hello world"

    shaObj = MD5(bytesObj)

    md5Hash = shaObj.get_byte()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")





















#  _                  _                       ____    _   _      _      ____    ____    _  _    
# | |_    ___   ___  | |_                    / ___|  | | | |    / \    |___ \  |___ \  | || |   
# | __|  / _ \ / __| | __|       _____       \___ \  | |_| |   / _ \     __) |   __) | | || |_  
# | |_  |  __/ \__ \ | |_       |_____|       ___) | |  _  |  / ___ \   / __/   / __/  |__   _| 
#  \__|  \___| |___/  \__|                   |____/  |_| |_| /_/   \_\ |_____| |_____|    |_|   
                                                                                              



def __test_sha224_yield():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA224(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha224Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")






def __test_sha224_yield2():

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA224(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha224Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")







def __test_sha224():

    bytesObj = b"hello world"

    shaObj = SHA224(bytesObj)

    sha224Hash = shaObj.get_string()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")





def __test_sha224_2():

    bytesObj = b"hello world"

    shaObj = SHA224(bytesObj)

    sha224Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")














if __name__ == "__main__":
    # __test_sha512_yield2()
    # __test_md5()
    # __test_md5_2()
    # __test_md5_yield()
    # __test_md5_yield2()
    # __test_sha1()
    # __test_sha1_2()
    # __test_sha1_yield()
    # __test_sha1_yield2()
    # __test_sha224()
    # __test_sha224_2()
    # __test_sha224_yield()
    __test_sha224_yield2()