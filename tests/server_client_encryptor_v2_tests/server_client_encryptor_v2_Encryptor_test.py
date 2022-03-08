from pySecureCryptos.server_client_encryptor_v2 import *
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
def test_encrypt_byte():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    myByte_server = getRandomByte()



    encryptedByte_server = encObj_server.encrypt_byte(myByte_server)


    encObj_client = Encryptor(publicKey_server , privateKey_client)

    myByte_client = getRandomByte()


    encryptedByte_client = encObj_client.encrypt_byte(myByte_client)


    decryptedByte_client = encObj_client.decrypt_byte(encryptedByte_server)
    

    assert decryptedByte_client == myByte_server , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")


    decryptedByte_server = encObj_server.decrypt_byte(encryptedByte_client)

    assert decryptedByte_server == myByte_client , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")
    













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield1():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    myByte_server = getRandomByte()



    genObj = encObj_server.encrypt_byte_yield(myByte_server)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedByte_server = ex.value
            break


    encObj_client = Encryptor(publicKey_server , privateKey_client)

    myByte_client = getRandomByte()


    genObj = encObj_client.encrypt_byte_yield(myByte_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedByte_client = ex.value
            break

    decryptedByte_client = encObj_client.decrypt_byte(encryptedByte_server)
    

    assert decryptedByte_client == myByte_server , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")


    decryptedByte_server = encObj_server.decrypt_byte(encryptedByte_client)

    assert decryptedByte_server == myByte_client , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")
    













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield2():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    myByte_server = getRandomByte()



    genObj = encObj_server.encrypt_byte_yield(myByte_server)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedByte_server = ex.value
            break


    encObj_client = Encryptor(publicKey_server , privateKey_client)

    myByte_client = getRandomByte()


    genObj = encObj_client.encrypt_byte_yield(myByte_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            encryptedByte_client = ex.value
            break

    genObj = encObj_client.decrypt_byte_yield(encryptedByte_server)
    
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedByte_client = ex.value
            break


    assert decryptedByte_client == myByte_server , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")


    genObj = encObj_server.decrypt_byte_yield(encryptedByte_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedByte_server = ex.value
            break

    assert decryptedByte_server == myByte_client , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")
    













@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield3():

    keyObj_server = KeyGenerator()

    publicKey_server = keyObj_server.get_publicKey_bytes()
    privateKey_server = keyObj_server.get_privateKey_bytes()

    keyObj_client = KeyGenerator()

    publicKey_client = keyObj_client.get_publicKey_bytes()
    privateKey_client = keyObj_client.get_privateKey_bytes()


    encObj_server = Encryptor(publicKey_client , privateKey_server)

    myByte_server = getRandomByte()



    encryptedByte_server = encObj_server.encrypt_byte(myByte_server)

    encObj_client = Encryptor(publicKey_server , privateKey_client)

    myByte_client = getRandomByte()


    encryptedByte_client = encObj_client.encrypt_byte(myByte_client)


    genObj = encObj_client.decrypt_byte_yield(encryptedByte_server)
    
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedByte_client = ex.value
            break


    assert decryptedByte_client == myByte_server , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")


    genObj = encObj_server.decrypt_byte_yield(encryptedByte_client)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            decryptedByte_server = ex.value
            break

    assert decryptedByte_server == myByte_client , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")
    
