from pySecureCryptos import verifier_fernetWrapper_v3 as vfw
import secrets
import random
import numpy

# function to generate a random byte
def getRandomByte(size = 10000):

    byte = numpy.random.bytes(size)

    return byte

# function to generate a random string
def getRandomString(minStringLen = 1 , maxStringLen = 10000):
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr




def main():

    fileName_mainfile = "binFiles/verifier_fernetWrapper_v3_testcases_bin/bytes_mainFile.bin"
    fileName_encfile_path = "binFiles/verifier_fernetWrapper_v3_testcases_bin/"
    fileName_key = "binFiles/verifier_fernetWrapper_v3_testcases_bin/key_bytes.bin"

    # 128 MB
    size = 1024 * 1024 * 128

    size_token = 1024 * 128

    randomBytes = b""

    iterate = size // size_token

    for i in range(iterate):
        print(i , iterate)
        randomBytes = randomBytes + getRandomByte(size_token)

    print("writing main file")
    with open(fileName_mainfile , "wb") as file:
        file.write(randomBytes)

    password = getRandomString(1,100)
    key = vfw.Keys.getKey(password)

    enc_obj = vfw.Encryptor.encrypt_file(fileName_mainfile , fileName_encfile_path , key)

    print()
    for i in enc_obj:
        print(f"\r{i}" , end = "")
    print()

    with open(fileName_key , "wb") as file:
        file.write(key)

    print("DONE")




if __name__ == "__main__":
    main()