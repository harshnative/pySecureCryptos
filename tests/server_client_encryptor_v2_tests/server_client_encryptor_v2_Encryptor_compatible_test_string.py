from pySecureCryptos import server_client_encryptor_v2
import pytest
import repeatTimes
import secrets
import random
import pickle













def getAssetionMessage(locals , message):
    locals_stored = locals

    result = str(message) + "\n\n\nFunction Vars Dump -\n"
    count = 1

    for name,val in locals_stored.items():
        result = result + f"\n\n{count}. {name} is {type(val)} = \n{val}\n"
        count = count + 1

    return result






# function to generate a random byte
def getRandomByte():
    minByteLen = 1
    maxByteLen = 1000

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





def test_compatible_server_string():

    with open(fileName_client_messages , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    with open(fileName_server_public_key , "rb") as file:
        publicKey_server = file.read()

    with open(fileName_server_private_key , "rb") as file:
        privateKey_server = file.read()

    with open(fileName_client_public_key , "rb") as file:
        publicKey_client = file.read()

    with open(fileName_client_private_key , "rb") as file:
        privateKey_client = file.read()

    encObj = server_client_encryptor_v2.Encryptor(publicKey_client , privateKey_server)

    for string , encString in pickledList:

        decryptedString = encObj.decrypt_string(encString)

        assert string == decryptedString , getAssetionMessage(locals() , "decrypted string does not match the original string")








def test_compatible_server_string_yield():

    with open(fileName_client_messages , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    with open(fileName_server_public_key , "rb") as file:
        publicKey_server = file.read()

    with open(fileName_server_private_key , "rb") as file:
        privateKey_server = file.read()

    with open(fileName_client_public_key , "rb") as file:
        publicKey_client = file.read()

    with open(fileName_client_private_key , "rb") as file:
        privateKey_client = file.read()

    encObj = server_client_encryptor_v2.Encryptor(publicKey_client , privateKey_server)

    for string , encString in pickledList:

        gen = encObj.decrypt_string_yield(encString)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decryptedString = ex.value
                break

        assert string == decryptedString , getAssetionMessage(locals() , "decrypted string does not match the original string")















def test_compatible_client_string():

    with open(fileName_server_messages , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    with open(fileName_server_public_key , "rb") as file:
        publicKey_server = file.read()

    with open(fileName_server_private_key , "rb") as file:
        privateKey_server = file.read()

    with open(fileName_client_public_key , "rb") as file:
        publicKey_client = file.read()

    with open(fileName_client_private_key , "rb") as file:
        privateKey_client = file.read()

    encObj = server_client_encryptor_v2.Encryptor(publicKey_server , privateKey_client)

    for string , encstring in pickledList:

        decryptedstring = encObj.decrypt_string(encstring)

        assert string == decryptedstring , getAssetionMessage(locals() , "decrypted string does not match the original string")












def test_compatible_client_string_yield():

    with open(fileName_server_messages , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)

    with open(fileName_server_public_key , "rb") as file:
        publicKey_server = file.read()

    with open(fileName_server_private_key , "rb") as file:
        privateKey_server = file.read()

    with open(fileName_client_public_key , "rb") as file:
        publicKey_client = file.read()

    with open(fileName_client_private_key , "rb") as file:
        privateKey_client = file.read()

    encObj = server_client_encryptor_v2.Encryptor(publicKey_server , privateKey_client)

    for string , encstring in pickledList:

        gen = encObj.decrypt_string_yield(encstring)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decryptedstring = ex.value
                break

        assert string == decryptedstring , getAssetionMessage(locals() , "decrypted string does not match the original string")




