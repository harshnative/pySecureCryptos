from pySecureCryptos import verifier_fernetWrapper_v2 as vfw
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
    randomByte = getRandomByte()
    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    encryptedByte = obj.encrypt_byte(randomByte)

    decryptedByte = obj.decrypt_byte(encryptedByte)

    assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")



















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string():
    randomString = getRandomString()

    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    encryptedString = obj.encrypt_string(randomString)

    decryptedString = obj.decrypt_string(encryptedString)

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")














@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield_1():
    randomByte = getRandomByte()

    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    gen = obj.encrypt_byte_yield(randomByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedByte = ex.value
            break


    gen = obj.decrypt_byte_yield(encryptedByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decryptedByte = ex.value
            break

    assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")





















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield_2():
    randomByte = getRandomByte()

    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    gen = obj.encrypt_byte_yield(randomByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedByte = ex.value
            break

    decryptedByte = obj.decrypt_byte(encryptedByte)

    assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")
























@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield_3():
    randomByte = getRandomByte()

    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    encryptedByte = obj.encrypt_byte(randomByte)

    gen = obj.decrypt_byte_yield(encryptedByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decryptedByte = ex.value
            break

    assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")






















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string_yield_1():
    randomString = getRandomString()

    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    gen = obj.encrypt_string_yield(randomString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedString = ex.value
            break

    gen = obj.decrypt_string_yield(encryptedString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decryptedString = ex.value
            break

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")



















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string_yield_2():
    randomString = getRandomString()

    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    gen = obj.encrypt_string_yield(randomString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedString = ex.value
            break


    decryptedString = obj.decrypt_string(encryptedString)

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")



























@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string_yield_3():
    randomString = getRandomString()

    password = getRandomString(1 , 100)

    obj = vfw.Encryptor(password)

    encryptedString = obj.encrypt_string(randomString)

    gen = obj.decrypt_string_yield(encryptedString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decryptedString = ex.value
            break

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")



















