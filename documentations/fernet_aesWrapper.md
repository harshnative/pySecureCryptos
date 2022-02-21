# fernet + aes Wrapper

God algo of symmetric encryption + best tokenized encryption algo.

first encrypts with fernet and then aes in each chunk

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
from pySecureCryptos import fernet_aesWrapper as FAW 
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
encObj = FAW.Encryptor(password : str , chunkSize : int = 16 , iterations : int = 390000)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* chunkSize - chunk size in MB , each chunks is encrypted individually and then joined together

Note - do not store SHA256 hash of your password , as it is used in encryption here. use SHA384 or SHA512.

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
encryptedByte = b'(\xa8~v(\xe9\xf7\x7f).P\xb5\xf25\xa2H{\'\x87\xbf\xc9\x19\x9f \xf0L!WR\xeb\\$\xef*\xf9\x10*ps\x7f_\x81\xe5\x13~`\x1e[\xe3\x9aB\x8c\x8b\x1d_\x86J\xe0\x1f\xca\x8c\x87~>\x84\xed$\'\xf4\xf6\xa0\x06\xdc!!\xbc\x848\xaa\xe4\xd2vd\x89\xd1@2\xd8\xbaL\xe3<\xba\xb3\xa8w\xcc\xf7e\xeb\x00Z\tz\xc4g)\x81\x97\x126\xf6\x9f\xae\x07\xae\xdb\xbdS\xca\xf7\r\xe1c\xdd\xcc\x1f\xa4s\xeaQo\xa1\'\xba\xc9\x9e\xd0^\xd6\xc8\xed\x105,\x94-\xd1\x84\xa0\xea%TB\xcb\x0e\x90>\xe3w\x85\xa75\x94\xd8\xf4\xeb\xe8\xc2\xc8s^m\xbc\xa3v\x18\x8a\x95<\xb8e\xef."KKq\xbdu\x1b\x8f^Mp:\xcc\xe5h\xebt\xaa&\x11\x86\xacX\xd5X\x90\x0co.VsbL)\r\x15Dj`0O}o\xee"\xa3\xfe\xe4|\xc9\xb5\x81\xbe^\xf9\xc1\r\x07\xc5\x9eV\x97\xe6/\xc3\xd6:helper:\xd69\xe2\xeb/\xe6lu\x92~\x80zU\xae!\xc3:helper:)I\xf0\xfcp\x13Q\x19:\x18[)\xf0#\xbe\x96' len = 298
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

    myByte = b"h" * 1024 * 1024 * 48

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
encrypting byte of len = 50331648

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedByte len = 67120636

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedByte len = 50331648

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
encObj = FAW.Encryptor(password : str , chunkSize : int = 16 , iterations : int = 390000)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* chunkSize - chunk size in MB , each chunks is encrypted individually and then joined together

Note - do not store SHA256 hash of your password , as it is used in encryption here. use SHA384 or SHA512.

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
encryptedString = d7b5f2eb32ee272b1dc4cd0d4757c890375391e137186b761d9dd4ac7110236e44e55280cf7577f59bded806a6910669a704c5e320c8eb00c1679f0123ab59e329f7b486984eb735ada776374509c341461dfdcec65d2104d65fbb83f32f7828e18d9753081e5dc28437051b2fd527d7222634f25e8a17b5b284903f9e9f79044151f6ae7dfdcc61945ee86224b98304951db3b1415c61438b4b2c9813afe99755b6bd19a681bc5656f2bcb8d19ce3e6a0c62ddc70fef314bf41cb01a5bb1ee7469e1da89ac9fc9612e305860690dfec87ef00b8038b167986229a511d9eff0ea9822b9db730449ae685a2eb5b079fd0e525ef20ef8987835939:helper:7388d8293887450826e7f90df8b8524e:helper:fc6aa21cde1bf31e61859df10cd4c557 len = 580
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
    myString = "h" * 1024 * 1024 * 48

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
encrypting string of len = 50331648

Progress: |██████████████████████████████████████████████████| 100.0% Complete

encryptedString len = 134241076

Progress: |██████████████████████████████████████████████████| 100.0% Complete

decryptedString len = 50331648

ok
```