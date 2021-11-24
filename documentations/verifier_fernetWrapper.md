
# verifier _ fernet Wrapper

This the extension of the in built [fernet wrapper](https://www.letscodeofficial.com/documentations/pSC_fernetWrapper#/)

This also add a encrypted checksum to the end to the encrypted output which is then verfied at the time of decryption to make the data is same as the data before encryption and no error as occured.

<br>
<br>
<br>

# Importing - 

``` python
from pySecureCryptos import verifier_fernetWrapper as FW 
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

# 1. Encrypt and Decrypt Strings

<br>

## Setup

You need to make a object from the class StringEncryptor

```python
stringEnc_obj = StringEncryptor(password , iterations=390000)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* iterations -> a fernet encryption key is derived using your password using cryptography built in function - PBKDF2HMAC. iterations should be set as high as possible. but not to much high as it can reduce your codes performance and increase load on hardware. default 390000 is sufficient and recommend value.

<br>
<br>
<br>


### 1.1 Encrypt the string

``` python
# encrypt method
stringEnc_obj.encrypt(string , returnString = True)
```

Arguments - 

* string -> string you want to encrypt , can be of any length.
* returnString -> as fernet works mainly with bytes type while encrypting and decrypting. we need to first convert the string to byte to encrypt and fernet returns encrypted byte itself. so if you don't want the output of encryption in string format and can deal with bytes , its is better to make returnString = False which will lead to faster performance as byte is longer needed to be converted back to string.


Note (IMP) -> Do not store SHA224 , SHA256 or MD5 hashed version of your password anywhere. instead use , SHA384 , SHA512 for hashing and password verification systems.



<br>
<br>

### 1.2 Decrypt String

#### 1.2.1 If you choosed returnString = True in encryption function


``` python
# decrypt method
stringEnc_obj.decrypt_string(enc_string)
```

Arguments - 

* enc_string -> string returned by stringEnc_obj.encrypt(returnString = True) method. The encrypted string.
* returns a decrypted string 

<br>
<br>


#### 1.2.2 If you choosed returnString = False in encryption function


``` python
# decrypt method
stringEnc_obj.decrypt_byte(enc_byte)
```

Arguments - 

* enc_byte -> byte returned by stringEnc_obj.encrypt(returnString = False) method. The encrypted byte.
* returns a decrypted string 

<br>
<br>

Example - 

we choose to get string object from encrytor

``` python
    obj = StringEncryptor("hello world")

    myString = "my name is john"

    print("\nlen myString string = {}\n".format(len(myString)))

    encryptedString = obj.encrypt(myString , True)

    print("\nencrypted string = {}\n".format(encryptedString))

    decryptedString = obj.decrypt_string(encryptedString)

    print("\ndecrypted string = {}\n".format(decryptedString))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell

len myString string = 15


encrypted string = 103065065065065065066104110104075111056071078121106103055101120101106101117087098117085050082118120073067095086118048114097067078048057082110045069122114104055051083077114045085104101082074049066066114103101086069056086081106115103084116116052115057082083090053053069104071071115082122048079065061061:checksum:103065065065065065066104110104075111056095084074051105100048077106073051066050088120073089086100090121083110076106099077111084076100069114051118078053070053076087108106080067053118110070057066066104084119052088102089085083088116076081101119107107112056071117078086082105070067071097071071045097076048080090074113112066056097112097107117065083079109111097050114119049117078121088076051108098083107075095079108049112050097090104107068054090114084089115100070075090068053117066119105108065117067088114055066079114114057087097065084067072065116050121081061


decrypted string = my name is john


ok
```


<br>
<br>

Example 2 - 

we choose to get byte object from encrytor

``` python
    obj = StringEncryptor("hello world")

    myString = "my name is john"

    print("\nlen myString string = {}\n".format(len(myString)))

    encryptedByte = obj.encrypt(myString , False)

    print("\n encryptedByte = {}\n".format(encryptedByte))

    decryptedString = obj.decrypt_byte(encryptedByte)

    print("\n decryptedString = {}\n".format(decryptedString))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell

len myString string = 15


 encryptedByte = b'gAAAAABhnhLVrqz6lmbAeIafU-AXNARQmLb_pgaNvZi8tLbNQSzEQdXqIJ17hwSHZsfq9p6bcTXD3GuEBp8BohXgbCYdWTA-Eg==:checksum:gAAAAABhnhLVcHbCa19y1k6Qw_QRQiCpAi7UANPgpX0OLZ44FCsPjTBdnNaNM8XW55tfc-8xTpVtIhCk0McTqdMmnvDa52z-Vu0y7w4Q9cyrm4BIyukGhAuksU3I8uVlxdcGN4wKJVUA'


 decryptedString = my name is john


ok
```


<br>
<br>
<br>
<br>


Note - Both the above method also have a generator function which are helpfull in case you have large objects to encrypt decrypt and you want to track progress. As on the files of size more than few KBS. method may take long time and if the progress is not shown to the user , user may think the program is just stuck

<br>
<br>

### 1.3 Generator version - Encrypt the string

``` python
# encrypt method
stringEnc_obj.encrypt_yield(string , returnString = True)
```

Arguments - 

* string -> string you want to encrypt , can be of any length.
* returnString -> as fernet works mainly with bytes type while encrypting and decrypting. we need to first convert the string to byte to encrypt and fernet returns encrypted byte itself. so if you don't want the output of encryption in string format and can deal with bytes , its is better to make returnString = False which will lead to faster performance as byte is longer needed to be converted back to string.


Note (IMP) -> Do not store SHA224 , SHA256 or MD5 hashed version of your password anywhere. instead use , SHA384 , SHA512 for hashing and password verification systems.



<br>
<br>

### 1.4 Generator version - Decrypt String

#### 1.4.1 If you choosed returnString = True in encryption function


``` python
# decrypt method
stringEnc_obj.decrypt_string_yield(enc_string)
```

Arguments - 

* enc_string -> string returned by stringEnc_obj.encrypt(returnString = True) method. The encrypted string.
* returns a decrypted string 

<br>
<br>


#### 1.4.2 If you choosed returnString = False in encryption function


``` python
# decrypt method
stringEnc_obj.decrypt_byte_yield(enc_byte)
```

Arguments - 

* enc_byte -> byte returned by stringEnc_obj.encrypt(returnString = False) method. The encrypted byte.
* returns a decrypted string 

<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test2() nad __test3() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/fernetWrapper.py


<br>
<br>

Example - 

we choose to get string object from encrytor

``` python
    obj = StringEncryptor("hello world")

    myString = "my name is john" * 1123

    print("\nlen myString string = {}\n".format(len(myString)))

    objGen_encryptor = obj.encrypt_yield(myString , True)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_encryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    print("\nlen encrypted string = {}\n".format(len(encryptedString)))

    objGen_decryptor = obj.decrypt_string_yield(encryptedString)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_decryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print("\nlen decryptedString = {}\n".format(len(decryptedString)))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell

len myString string = 16845


45942 , 45942

len encrypted string = 87755


45876 , 46248

len decryptedString = 16845


ok
```


<br>
<br>

Example 2 - 

we choose to get byte object from encrytor

``` python
    obj = StringEncryptor("hello world")

    myString = "my name is john" * 1123

    print("\nlen myString string = {}\n".format(len(myString)))

    objGen_encryptor = obj.encrypt_yield(myString , False)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_encryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    print("\nlen encryptedByte = {}\n".format(len(encryptedByte)))

    objGen_decryptor = obj.decrypt_byte_yield(encryptedByte)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_decryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    print("\nlen decryptedString = {}\n".format(len(decryptedString)))

    if(decryptedString == myString):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell

len myString string = 16845


16986 , 16986

len encryptedByte = 29431


16920 , 17184

len decryptedString = 16845


ok
```


<br>
<br>


Note - the final yield of currentYield will be less than totalYield from the decryption function as it is impossible to determine the size of decryted string from the encrypted byte. program just takes the max size possible.

<br>
<br>
<br>
<br>
<br>
<br>




# 2. Encrypt and Decrypt Bytes

<br>

## Setup

You need to make a object from the class BytesEncryptor

```python
bytesEnc_obj = BytesEncryptor(password , iterations=390000)
```


Arguments - 

* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and longer and not easily guessable the password is , the stronger is the encryption.
* iterations -> a fernet encryption key is derived using your password using cryptography built in function - PBKDF2HMAC. iterations should be set as high as possible. but not to much high as it can reduce your codes performance and increase load on hardware. default 390000 is sufficient and recommend value.

<br>
<br>
<br>


### 2.1 Encrypt byte

``` python
# encrypt method
bytesEnc_obj.encrypt(byte)
```

Arguments - 

* byte -> byte you want to encrypt , can be of any length.
* returns encrypted bytes object 


Note (IMP) -> Do not store SHA224 , SHA256 or MD5 hashed version of your password anywhere. instead use , SHA384 , SHA512 for hashing and password verification systems.



<br>
<br>

### 2.2 Decrypt byte


``` python
# decrypt method
bytesEnc_obj.decrypt(enc_byte)
```

Arguments - 

* enc_byte -> byte returned by bytesEnc_obj.encrypt() method. The encrypted byte.
* returns a decrypted byte 

<br>
<br>

Example - 

``` python
    
    obj = BytesEncryptor("hello world")

    myByte = b"my name is john"

    print("\nlen myByte = {}\n".format(len(myByte)))

    encryptedByte = obj.encrypt(myByte)

    print("\nencryptedByte = {}\n".format(encryptedByte))

    decryptedByte = obj.decrypt(encryptedByte)

    print("\ndecryptedByte = {}\n".format(decryptedByte))

    if(decryptedByte == myByte):
        print("\nok")
    else:
        print("\nerror")

```

Output - 

``` shell

len myByte = 15


encryptedByte = b'gAAAAABhnhNLbUjDc6ZHB-zJdjf0TaWZNkONXj133Vj2QhtZm8CcxGSmN9aFdkdEzKsN5s81ILAB7IXXOgMolfMeOW-g0hofJw==:checksum:gAAAAABhnhNLOxzKC0NNV_lAkPx08k91OAnMLNKZOhv-eQJ6QAufmOxofnxICdm6YBcyyRPHTp7eqrqHEQPexYsis47ld84arTvdB9KWHP_hopuL9lDY-SEv6QmABs-bLy6eJToNAnVl'


decryptedByte = b'my name is john'


ok
```


<br>
<br>
<br>
<br>


Note - Both the above method also have a generator function which are helpfull in case you have large objects to encrypt decrypt and you want to track progress. As on the files of size more than few KBS. method may take long time and if the progress is not shown to the user , user may think the program is just stuck

<br>
<br>

### 2.3 Generator version - Encrypt string

``` python
# encrypt method
bytesEnc_obj.encrypt_yield(byte)
```

Arguments - 

* byte -> byte you want to encrypt , can be of any length.
* returns encrypted bytes object 


Note (IMP) -> Do not store SHA224 , SHA256 or MD5 hashed version of your password anywhere. instead use , SHA384 , SHA512 for hashing and password verification systems.



<br>
<br>

### 2.4 Decrypt byte


``` python
# decrypt method
bytesEnc_obj.decrypt_yield(enc_byte)
```

Arguments - 

* enc_byte -> byte returned by bytesEnc_obj.encrypt() method. The encrypted byte.
* returns a decrypted byte 

<br>
<br>
<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test4() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/fernetWrapper.py


<br>
<br>

Example - 

``` python
    
    obj = BytesEncryptor("hello world")

    myByte = b"my name is john" * 11233

    print("\nlen myByte = {}\n".format(len(myByte)))

    objGen_encryptor = obj.encrypt_yield(myByte)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_encryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    print("\nlen encrypted byte = {}\n".format(len(encryptedByte)))

    objGen_decryptor = obj.decrypt_yield(encryptedByte)

    print()
    while(True):
        try:
            currentYield , totalYields = next(objGen_decryptor)
            print("\r{} , {}".format(currentYield , totalYields) , end="")

        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    print("\nlen decryptedByte = {}\n".format(len(decryptedByte)))

    if(decryptedByte == myByte):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell

len myByte = 168495


1401 , 1401

len encrypted byte = 293100


742 , 803

len decryptedByte = 168495


ok
```


<br>
<br>
<br>
<br>
<br>
<br>


Note - fernet claims to be very secure encryption algo , just keep your password strong , at least 20 digit password with combination of lower upper , nums and specials chars is recommended for sensitive content

<br>
<br>
<br>
<br>
<br>
<br>