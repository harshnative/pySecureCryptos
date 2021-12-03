# verifier fernet Wrapper v2

version 2 of the verifier fernet wrapper.

This is much faster than version one due to increased chunk size and controlled yield making more use of CPU at a time.




<br>
<br>
<br>

# Importing - 

``` python
from pySecureCryptos import verifier_fernetWrapper_v2 as FW 
```




<br>
<br>
<br>
<br>
<br>

# Methods - 

1. Encrypt and Decrypt strings
2. Encrypt and Decrypt bytes


<br>
<br>
<br>
<br>
<br>
<br>



# 1. Bytes Encryptor

<br>

## Setup

You need to make a object from the class Encryptor

```python
encObj = FW.Encryptor(password , iterations=390000)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* iterations -> a fernet encryption key is derived using your password using cryptography built in function - PBKDF2HMAC. iterations should be set as high as possible. but not to much high as it can reduce your codes performance and increase load on hardware. default 390000 is sufficient and recommend value.


<br>
<br>

### 1.1 encrypt byte

``` python
encObj.encrypt_byte(byte)
```

* byte -> byte you want to encrypt
* returns encrypted byte

<br>
<br>

### 1.2 decrypt byte

``` python
encObj.decrypt_byte(enc_byte)
```

* enc_byte -> encrypted byte from encObj.encrypt_byte()
* returns decrypted byte

<br>
<br>

Example - 

```python

    password = "hello"

    print("making obj")
    encObj = Encryptor(password)

    myByte = b"hello world"

    print(f"encrypting byte of len = {len(myByte)}")


    encryptedByte = encObj.encrypt_byte(myByte)

    print(f"encryptedByte = {encryptedByte} len = {len(encryptedByte)}")

    
    decryptedByte = encObj.decrypt_byte(encryptedByte)

    print(f"decryptedByte = {decryptedByte} len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")
```


Output - 

```shell
making obj
encrypting byte of len = 11
encryptedByte = b'gAAAAABhqjHkS1_hipcuPNdQ5EpGnm0nLpqZ7yHmGYtETcMRMChyh64SQq0f4__ZahHja1XOCQ682o6KeWXeT-s1eweLcA-ulQ==:checksum:gAAAAABhqjHkI-8bPhF-KIYZgZZ24z9qes5N9cofz3LkJoWJKdT2QOGEP2dDndYhpzfsr1XdXTnoif0ykdm-4nsG5CSWn9qtsgk9E72PzgA0zdeuofjowQvFkix-PYsNvAwUpNrr_NVs' len = 250
decryptedByte = b'hello world' len = 11

ok

```


<br>
<br>
<br>

NOTE -> Both the above method also have a generator version which are important in tracking the progress of encryption and decryption of large data.



<br>
<br>
<br>

### 1.3 generator version - encrypt byte

``` python
encObj.encrypt_byte_yield(byte)
```

* byte -> byte you want to encrypt
* returns encrypted byte

<br>
<br>


### 1.4 generator version - decrypt byte

``` python
encObj.decrypt_byte_yield(enc_byte)
```

* enc_byte -> encrypted byte
* returns decrypted byte

<br>
<br>


Example - 

```python

    password = "hello"

    
    print("making obj")
    encObj = Encryptor(password)

    myByte = b"hello world" * 12345

    print(f"encrypting byte of len = {len(myByte)}")


    genObj = encObj.encrypt_byte_yield(myByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            # print("\r{} , {}".format(currentCount , totalYield) , end="")
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    print(f"encryptedByte len = {len(encryptedByte)}")

    
    genObj = encObj.decrypt_byte_yield(encryptedByte)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    print(f"decryptedByte len = {len(decryptedByte)}")

    if(decryptedByte != myByte):
        print("\nerror")
    else:
        print("\nok")

```

Output - 

```shell
making obj
encrypting byte of len = 135795

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedByte len = 184727

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedByte len = 135795

ok
```



<br>
<br>
<br>
<br>
<br>



# 2. String Encryptor

<br>

## Setup

You need to make a object from the class Encryptor

```python
encObj = FW.Encryptor(password , iterations=390000)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* iterations -> a fernet encryption key is derived using your password using cryptography built in function - PBKDF2HMAC. iterations should be set as high as possible. but not to much high as it can reduce your codes performance and increase load on hardware. default 390000 is sufficient and recommend value.



<br>
<br>

### 2.1 encrypt string

``` python
encObj.encrypt_string(string)
```

* string -> string you want to encrypt
* returns encrypted string

<br>
<br>

### 2.2 decrypt string

``` python
encObj.decrypt_string(enc_string)
```

* enc_string -> encrypted string from encObj.encrypt_string()
* returns decrypted string

<br>
<br>

Example - 

```python

    password = "hello"

    print("making obj")
    encObj = Encryptor(password)

    myString = "hello world"

    print(f"encrypting string of len = {len(myString)}")


    encryptedString = encObj.encrypt_string(myString)

    print(f"encryptedString = {encryptedString} len = {len(encryptedString)}")

    
    decryptedString = encObj.decrypt_string(encryptedString)

    print(f"decryptedString = {decryptedString} len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")

```


Output - 

```shell
making obj
encrypting string of len = 11
encryptedString = 6741414141414268716a4b42625779627573714c746e57703456417a736e49625f6363304e6e497148706b784f59595f3734596d61363939535f6c6f394e417955687639515967676e6b525734696e684671504f345351597931496a384d714b57673d3d:checksum:6741414141414268716a4b424b626a453562514533564f324d484f6c564f62536d65674b304e54586b464b65472d6b6b6a7a6459744e73326f6c316a64546b574f354a364e73695a4c4a5f7a7144387551516a7842623766477873555a4947355a542d633437737a336e5f7944524a446b74774a4a4d7848626d766c764f647955645561484d346c4a383336 len = 490
decryptedString = hello world len = 11

ok
```


<br>
<br>
<br>

NOTE -> Both the above method also have a generator version which are important in tracking the progress of encryption and decryption of large data.



<br>
<br>
<br>

### 2.3 generator version - encrypt string

``` python
encObj.encrypt_string_yield(string)
```

* string -> string you want to encrypt
* returns encrypted string

<br>
<br>


### 2.4 generator version - decrypt string

``` python
encObj.decrypt_string_yield(enc_string)
```

* enc_string -> encrypted string
* returns decrypted string

<br>
<br>


Example - 

```python

    password = "hello"

    print("making obj")
    encObj = Encryptor(password)

    myString = "hello world" * 12345

    print(f"encrypting string of len = {len(myString)}")


    genObj = encObj.encrypt_string_yield(myString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    print(f"encryptedString len = {len(encryptedString)}")

    
    genObj = encObj.decrypt_string_yield(encryptedString)

    print()
    while(True):
        try:
            currentCount , totalYield = next(genObj)
            # print(currentCount , totalYield)
            printProgressBar(currentCount, totalYield, prefix = 'Progress:', suffix = 'Complete', length = 50)
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print(f"decryptedString len = {len(decryptedString)}")

    if(decryptedString != myString):
        print("\nerror")
    else:
        print("\nok")
    
```

Output - 

```shell
making obj
encrypting string of len = 135795

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedString len = 369279

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedString len = 135795

ok
```