from pySecureCryptos.server_client_encryptor import *
import pytest
import repeatTimes
import secrets
import random













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







@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    mystring_server = getRandomString()



    encryptedstring_server = encObj_server.encrypt_string(mystring_server)


    encObj_client = Encryptor(publicKey_server , privateKey_client)

    mystring_client = getRandomString()


    encryptedstring_client = encObj_client.encrypt_string(mystring_client)


    decryptedstring_client = encObj_client.decrypt_string(encryptedstring_server)
    

    assert decryptedstring_client == mystring_server , getAssetionMessage(locals() , "decrypted string does not match the original string")


    decryptedstring_server = encObj_server.decrypt_string(encryptedstring_client)

    assert decryptedstring_server == mystring_client , getAssetionMessage(locals() , "decrypted string does not match the original string")
    













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string_yield1():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    mystring_server = getRandomString()



    genObj = encObj_server.encrypt_string_yield(mystring_server)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedstring_server = ex.value
            break


    encObj_client = Encryptor(publicKey_server , privateKey_client)

    mystring_client = getRandomString()


    genObj = encObj_client.encrypt_string_yield(mystring_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedstring_client = ex.value
            break

    decryptedstring_client = encObj_client.decrypt_string(encryptedstring_server)
    

    assert decryptedstring_client == mystring_server , getAssetionMessage(locals() , "decrypted string does not match the original string")


    decryptedstring_server = encObj_server.decrypt_string(encryptedstring_client)

    assert decryptedstring_server == mystring_client , getAssetionMessage(locals() , "decrypted string does not match the original string")
    













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string_yield2():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    mystring_server = getRandomString()



    genObj = encObj_server.encrypt_string_yield(mystring_server)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedstring_server = ex.value
            break


    encObj_client = Encryptor(publicKey_server , privateKey_client)

    mystring_client = getRandomString()


    genObj = encObj_client.encrypt_string_yield(mystring_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedstring_client = ex.value
            break

    genObj = encObj_client.decrypt_string_yield(encryptedstring_server)
    
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedstring_client = ex.value
            break


    assert decryptedstring_client == mystring_server , getAssetionMessage(locals() , "decrypted string does not match the original string")


    genObj = encObj_server.decrypt_string_yield(encryptedstring_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedstring_server = ex.value
            break

    assert decryptedstring_server == mystring_client , getAssetionMessage(locals() , "decrypted string does not match the original string")
    













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string_yield3():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    mystring_server = getRandomString()



    encryptedstring_server = encObj_server.encrypt_string(mystring_server)

    encObj_client = Encryptor(publicKey_server , privateKey_client)

    mystring_client = getRandomString()


    encryptedstring_client = encObj_client.encrypt_string(mystring_client)


    genObj = encObj_client.decrypt_string_yield(encryptedstring_server)
    
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedstring_client = ex.value
            break


    assert decryptedstring_client == mystring_server , getAssetionMessage(locals() , "decrypted string does not match the original string")


    genObj = encObj_server.decrypt_string_yield(encryptedstring_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedstring_server = ex.value
            break

    assert decryptedstring_server == mystring_client , getAssetionMessage(locals() , "decrypted string does not match the original string")
    
