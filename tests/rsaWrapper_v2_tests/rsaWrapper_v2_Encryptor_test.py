from pySecureCryptos import rsaWrapper_v2
import pytest
import repeatTimes
import secrets
import random
import keyGeneration













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

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    encryptedByte = obj.encrypt_byte(randomByte)

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    decryptedByte = obj.decrypt_byte(encryptedByte)

    assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")



















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string():
    randomString = getRandomString()

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    encryptedString = obj.encrypt_string(randomString)

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    decryptedString = obj.decrypt_string(encryptedString)

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")














@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield_1():
    randomByte = getRandomByte()

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.encrypt_byte_yield(randomByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedByte = ex.value
            break

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

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

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.encrypt_byte_yield(randomByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedByte = ex.value
            break

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    decryptedByte = obj.decrypt_byte(encryptedByte)

    assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")
























@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_byte_yield_3():
    randomByte = getRandomByte()

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    encryptedByte = obj.encrypt_byte(randomByte)

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

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

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.encrypt_string_yield(randomString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedString = ex.value
            break

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

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

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.encrypt_string_yield(randomString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedString = ex.value
            break

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    decryptedString = obj.decrypt_string(encryptedString)

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")



























@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_string_yield_3():
    randomString = getRandomString()

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    encryptedString = obj.encrypt_string(randomString)


    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.decrypt_string_yield(encryptedString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decryptedString = ex.value
            break

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")



















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_lbyte_yield():

    # 16 Mb of data
    randomByte = b"h" * 1024 * 1024 * 16

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.encrypt_lbyte_yield(randomByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedByte = ex.value
            break


    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.decrypt_lbyte_yield(encryptedByte)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decryptedByte = ex.value
            break

    assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")

















@pytest.mark.repeat(repeatTimes.RepeatTime.value)
def test_encrypt_lstring_yield():

    # 16 Mb of data
    randomString = "h" * 1024 * 1024 * 16

    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.encrypt_lstring_yield(randomString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            encryptedString = ex.value
            break


    if(random.random() > 0.5):
        publicKey = keyGeneration.GetKey.keyPublic
        privateKey = keyGeneration.GetKey.keyPrivate
    else:
        publicKey = keyGeneration.GetKey.keyPublic_str
        privateKey = keyGeneration.GetKey.keyPrivate_str

    obj = rsaWrapper_v2.Encryptor(publicKey , privateKey)

    gen = obj.decrypt_lstring_yield(encryptedString)

    while(True):
        try:
            next(gen)
        except StopIteration as ex:
            decryptedString = ex.value
            break

    assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted String does not match the original String")


