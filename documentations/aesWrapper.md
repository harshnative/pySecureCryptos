# aes Wrapper

God algo of symmetric encryption.

can encrypt strings which are utf-8 compatible.






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
from pySecureCryptos import aesWrapper as AW 
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
encObj = AW.Encryptor(password : str , chunkSize : int = 16)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* chunkSize - chunk size in MB , each chunks is encrypted individually and then joined together

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
encryptedByte = b"\xce\x87\xe1\x04!\xc9\xae\x06A\xec\xb0:helper:^ '\x1c\xf6\xbc\x9eK0/\xc2\xd8:\x0b\xb01:helper:\xd9\x1c\xa9\x15<\xd9f\xf4c\xa2E\x19\x9d\xf2\xa4\x8f" len = 59
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

    myByte = b"h" * 1024 * 1024 * 128

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
encrypting byte of len = 134217728

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedByte len = 134218272

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedByte len = 134217728

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
encObj = AW.Encryptor(password : str , chunkSize : int = 16)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* chunkSize - chunk size in MB , each chunks is encrypted individually and then joined together

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
encryptedString = ff32e4c5cb8bf5593502b6:helper:aa2dc73b4848ecc4cd61e90519de955f:helper:b9a54094abf81426768d8d5aa5a860de len = 102
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

    # 16 MB
    myString = "h" * 1024 * 1024 * 128

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
encrypting string of len = 134217728

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedString len = 268436288

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedString len = 134217728

ok
```