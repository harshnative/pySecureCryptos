from Cryptodome import PublicKey
from pySecureCryptos import server_client_encryptor_v2
import random
import secrets
import pickle




# function to generate a random byte
def getRandomByte(minByteLen = 1 , maxByteLen = 1000):

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

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




fileName_server_messages = "binFiles/server_client_encryptor_v2_testcases_bin/server_messages_string.bin"
fileName_server_public_key = "binFiles/server_client_encryptor_v2_testcases_bin/server_public_key_string.bin"
fileName_server_private_key = "binFiles/server_client_encryptor_v2_testcases_bin/server_private_key_string.bin"


fileName_client_messages = "binFiles/server_client_encryptor_v2_testcases_bin/client_messages_string.bin"
fileName_client_public_key = "binFiles/server_client_encryptor_v2_testcases_bin/client_public_key_string.bin"
fileName_client_private_key = "binFiles/server_client_encryptor_v2_testcases_bin/client_private_key_string.bin"



def generateKeys():

    keyObj_server = server_client_encryptor_v2.KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()

    with open(fileName_server_public_key , "wb") as file:
        file.write(publicKey_server)

    privateKey_server = keyObj_server.get_privateKey_bytes()

    with open(fileName_server_private_key , "wb") as file:
        file.write(privateKey_server)


    keyObj_client = server_client_encryptor_v2.KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()

    with open(fileName_client_public_key , "wb") as file:
        file.write(publicKey_client)

    privateKey_client = keyObj_client.get_privateKey_bytes()

    with open(fileName_client_private_key , "wb") as file:
        file.write(privateKey_client)







def server():

    with open(fileName_server_public_key , "rb") as file:
        publicKey_server = file.read()

    with open(fileName_server_private_key , "rb") as file:
        privateKey_server = file.read()

    with open(fileName_client_public_key , "rb") as file:
        publicKey_client = file.read()

    with open(fileName_client_private_key , "rb") as file:
        privateKey_client = file.read()

    number = 2

    encObj = server_client_encryptor_v2.Encryptor(publicKey_client , privateKey_server)

    outputList = []

    for i in range(number):
        print(i)

        string = getRandomString()

        encString = encObj.encrypt_string(string)

        outputList.append([string , encString])


    for i in range(number):
        print(i)

        string = getRandomString(1000 * 1000 * 24 , 1000 * 1000 * 64)

        genObj = encObj.encrypt_string_yield(string)

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                encString = ex.value
                break

        outputList.append([string , encString])



    pickledList = pickle.dumps(outputList)

    with open(fileName_server_messages , "wb") as file:
        file.write(pickledList)

    print("DONE")










def client():


    with open(fileName_server_public_key , "rb") as file:
        publicKey_server = file.read()

    with open(fileName_server_private_key , "rb") as file:
        privateKey_server = file.read()

    with open(fileName_client_public_key , "rb") as file:
        publicKey_client = file.read()

    with open(fileName_client_private_key , "rb") as file:
        privateKey_client = file.read()

    number = 2

    encObj = server_client_encryptor_v2.Encryptor(publicKey_server , privateKey_client)

    outputList = []

    for i in range(number):
        print(i)

        string = getRandomString()

        encString = encObj.encrypt_string(string)

        outputList.append([string , encString])


    for i in range(number):
        print(i)

        string = getRandomString(1000 * 1000 * 24 , 1000 * 1000 * 64)

        genObj = encObj.encrypt_string_yield(string)

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                encString = ex.value
                break

        outputList.append([string , encString])

    pickledList = pickle.dumps(outputList)

    with open(fileName_client_messages , "wb") as file:
        file.write(pickledList)

    print("DONE")

















if __name__ == "__main__":
    print("keys")
    generateKeys()

    print("server")
    server()

    print("client")
    client()

