# verifier fernet Wrapper v2.2

version 2.2 of the verifier fernet wrapper.

This is much faster than version one and version 2 due to increased chunk size and controlled yield making more use of CPU at a time and using inbuilt conversion methods.

But as less compatability for strings. as strings needed to be converted in bytes. to encrypt the strings , strings should be utf-8 compatible.

if you need to encrypt strings which are not utf-8 compatible then use [version 2](https://www.letscodeofficial.com/documentations/pSC_V_fernetWrapper_v2#/) of fernet wrapper.






<br>
<br>
<br>













<!-- 


 _                                      _    
(_)  _ __ ___    _ __     ___    _ __  | |_  
| | | '_ ` _ \  | '_ \   / _ \  | '__| | __| 
| | | | | | | | | |_) | | (_) | | |    | |_  
|_| |_| |_| |_| | .__/   \___/  |_|     \__| 
                |_|                           -->


# Importing - 

``` python
from pySecureCryptos import verifier_fernetWrapper_v2_2 as FW 
```




<br>
<br>
<br>
<br>
<br>












<!-- 


                    _     _                   _  
 _ __ ___     ___  | |_  | |__     ___     __| | 
| '_ ` _ \   / _ \ | __| | '_ \   / _ \   / _` | 
| | | | | | |  __/ | |_  | | | | | (_) | | (_| | 
|_| |_| |_|  \___|  \__| |_| |_|  \___/   \__,_| 
                                                  -->


# Methods - 

1. Encrypt and Decrypt bytes
2. Encrypt and Decrypt string


<br>
<br>
<br>
<br>
<br>
<br>





















<!-- 
 _  
/ | 
| | 
| | 
|_| 
     -->


# 1. Bytes Encryptor

<br>

## Setup

You need to make a object from the class Encryptor

```python
encObj = FW.Encryptor(password , iterations=390000 , chunkSize=512)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* iterations -> a fernet encryption key is derived using your password using cryptography built in function - PBKDF2HMAC. iterations should be set as high as possible. but not to much high as it can reduce your codes performance and increase load on hardware. default 390000 is sufficient and recommend value.
* chunkSize - chunk size in KB , each chunks is encrypted individually and then joined together

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
encryptedByte = b'gAAAAABhvnyULbH_tto_0U2A3XDgyZ3zpKrVomyjQW2JD5TiJS_kjGTHzXAH2NVfNhh7gVKkFNlGsBdckSG0I9qhKJouvyOA8w==:checksum:gAAAAABhvnyU650YlgyT-gJ1A1L_Ne9wL_i8XV68zr4z43OqS551b9oVCVJRu57c1B2J51e9JxHqQd-JJQpC5hNWpIF1YlsYxwqV8RvZCiTX1Mk0GNFP2KGrPeS7cwbRRREhA5C4PSMj' len = 250
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

    myByte = b"h" * 1024 * 1024 * 16

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
encrypting byte of len = 16777216

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedByte len = 22373041

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedByte len = 16777216

ok
```



<br>
<br>
<br>
<br>
<br>














<!-- 
 ____   
|___ \  
  __) | 
 / __/  
|_____| 
         -->


# 2. String Encryptor

<br>

## Setup

You need to make a object from the class Encryptor

```python
encObj = FW.Encryptor(password , iterations=390000 , chunkSize=512)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* iterations -> a fernet encryption key is derived using your password using cryptography built in function - PBKDF2HMAC. iterations should be set as high as possible. but not to much high as it can reduce your codes performance and increase load on hardware. default 390000 is sufficient and recommend value.
* chunkSize - chunk size in KB , each chunks is encrypted individually and then joined together

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
encryptedString = 6741414141414268766e306a722d74644c5a333743534c597772314430767074387370642d3074347167634d2d635562775472526b76674c61494a3241725633343465553768346659424a474c3752636b75584e7453474352715578724454554d513d3d:checksum:6741414141414268766e306a73762d366837796c6952556f6f613077577136654e62786873646f5f4e6f6679716d7971526745414845382d5f3351716c4b7347544e7a2d4d644e5f795674465a4f584c3869756a343555514e76655275357530795f5834374e6737494e6e2d6342414944436d386b5a61686649774f49686859486c6538382d36314c726834 len = 490
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

    myString = "h" * 1024 * 1024 * 16

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
encrypting string of len = 16777216

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedString len = 44745917

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedString len = 16777216

ok
```