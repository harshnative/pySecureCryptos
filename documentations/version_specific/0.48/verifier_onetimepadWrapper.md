
# verifier _ onetimepad Wrapper

This the extension of the in built [onetimepad wrapper](https://www.letscodeofficial.com/documentations/pSC_onetimepadWrapper#/)

This also add a encrypted checksum to the end to the encrypted output which is then verfied at the time of decryption to make the data is same as the data before encryption and no error as occured.

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
from pySecureCryptos import verifier_onetimepadWrapper as OW 
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

1. Encrypt and Decrypt strings
2. Encrypt and Decrypt bytes


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


# 1. Encrypt and Decrypt Strings

<br>
<br>

### 1.1 Encrypt the string

``` python
# encrypt method
OW.StringEncryptor.encrypt(string , password)
```

Arguments - 

* string -> string you want to encrypt , can be of any length.
* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and not easily guessable the password is , the stronger is the encryption.
* returns a encrypted string


Note -> as you know in onetimepad , message will be of the same length as key . that problem is auto handled here. This algo is heavily customized to provide the best possible encryption version of onetimepad.

Note (IMP) -> Do not store SHA224 or MD5 hashed version of your password anywhere. instead use SHA256 , SHA384 , SHA512 for hashing and password verification systems.



<br>
<br>

### 1.2 Decrypt String

``` python
# decrypt method
OW.StringEncryptor.decrypt(enc_string , password)
```

Arguments - 

* enc_string -> string returned by OW.StringEncryptor.encrypt() method. The encrypted string.
* password -> password used to encrypt the string
* returns a decrypted string

<br>
<br>

Example - 

``` python
    string = "hello world"
    encryptedString = StringEncryptor.encrypt(string , "hello")
    decryptedString = StringEncryptor.decrypt(encryptedString , "hello")

    print("string = " , string)
    print("encryptedString = " , encryptedString)
    print("decryptedString = " , decryptedString)

    if(string == decryptedString):
        print("ok")
    else:
        print("error")
```

Output - 

``` shell
string =  hello world
encryptedString =  4d955a54b6005f571505a5:checksum:b5447755025555005500663ae005080510003358255a5550b00005374575954444005c505065008065432f4542af0600102050e5c80507502050507b02053320
decryptedString =  hello world
ok
```


<br>
<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encrypt decrypt and you want to track progress. As on the files of size more than few KBS. method may take long time and if the progress is not shown to the user , user may think the program is just stuck

<br>
<br>















### 1.3 Generator version - Encrypt the string

``` python
# encrypt method
OW.StringEncryptor_yield.encrypt(string , password)
```

Arguments - 

* string -> string you want to encrypt , can be of any length.
* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and not easily guessable the password is , the stronger is the encryption.
* returns a encrypted string


Note -> as you know in onetimepad , message will be of the same length as key . that problem is auto handled here. This algo is heavily customized to provide the best possible encryption version of onetimepad.

Note (IMP) -> Do not store SHA224 or MD5 hashed version of your password anywhere. instead use SHA256 , SHA384 , SHA512 for hashing and password verification systems.




<br>
<br>

### 1.4 Generator version - Decrypt String

``` python
# decrypt method
OW.StringEncryptor_yield.decrypt(enc_string , password)
```

Arguments - 

* enc_string -> string returned by OW.StringEncryptor.encrypt() method. The encrypted string.
* password -> password used to encrypt the string
* returns a decrypted string

<br>
<br>


both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_stringEncrytor2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/onetimepadWrapper.py


Example - 

``` python
    string = "hello world" * 1123
    genObj_encrypt = StringEncryptor_yield.encrypt(string , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end="")
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    genObj_decrypt = StringEncryptor_yield.decrypt(encryptedString , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end="")
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    if(string == decryptedString):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell

on 448 out of 448   

on 448 out of 448   

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













<!-- 
 ____   
|___ \  
  __) | 
 / __/  
|_____| 
         -->


# 2. Encrypt and Decrypt Bytes

<br>
<br>

### 2.1 Encrypt Byte

``` python
# encrypt method
OW.BytesEncryptor.encrypt(byteObject , password , returnByteObject = True)
```

Arguments - 

* byteObject -> byteObject you want to encrypt , can be of any length. bytes or bytearray type.
* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and not easily guessable the password is , the stronger is the encryption. 
* returnByteObject -> Onetimepad by default works with strings only , so to encrypt a byte object we need to first convert it into string using https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/. So an extra step is involed. So if you think you don't need to convert the encrypted string to byte to store it somewhere , make this False. No matter what return type you choose , you will always get back a decrypted byte object only. It is just that you will save some resources if you make this False.
* returns a encrypted string


Note -> as you know in onetimepad , message will be of the same length as key . that problem is auto handled here. This algo is heavily customized to provide the best possible encryption version of onetimepad.

Note (IMP) -> Do not store SHA224 or MD5 hashed version of your password anywhere. instead use SHA256 , SHA384 , SHA512 for hashing and password verification systems.



<br>
<br>

### 2.2 Decrypt Byte

#### 2.2.1 If you choosed returnByteObject = False in encryption function

``` python
# decrypt method
OW.BytesEncryptor.decrypt(enc_string , password)
```

Arguments - 

* enc_string -> string returned by OW.BytesEncryptor.encrypt(returnByteObject = False) method. The encrypted string.
* password -> password used to encrypt the byte
* returns a decrypted byte object

<br>
<br>


#### 2.2.2 If you choosed returnByteObject = True in encryption function

``` python
# decrypt method
OW.BytesEncryptor.decrypt_byte(enc_byteObject , password)
```

Arguments - 

* enc_byteObject -> byte returned by OW.BytesEncryptor.encrypt(returnByteObject = True) method. The encrypted byte.
* password -> password used to encrypt the byte
* returns a decrypted byte object

<br>
<br>

Example - 

``` python
    byteObject = b"hello world"
    encryptedString = BytesEncryptor.encrypt(byteObject , "hello" , returnByteObject=False)
    decryptedByte = BytesEncryptor.decrypt(encryptedString , "hello")

    if(byteObject == decryptedByte):
        print("ok")
    else:
        print("error")

    print("\n\ntest 2\n\n")


    byteObject = b"hello world"
    
    # we will get bytes object from the encryptor function , say you are storing this on a blob storage
    encryptedByte = BytesEncryptor.encrypt(byteObject , "hello" , returnByteObject=True)
    decryptedByte = BytesEncryptor.decrypt_byte(encryptedByte , "hello")


    if(byteObject == decryptedByte):
        print("ok")
    else:
        print("error")
```

Output - 

``` shell
ok


test 2


ok
```


<br>
<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encrypt decrypt and you want to track progress. As on the files of size more than few KBS , method may take long time and if the progress is not shown to the user , user may think the program is just stuck

<br>
<br>



















### 2.3 Generator version - Encrypt the Byte

``` python
# encrypt method
OW.BytesEncryptor_yield.encrypt(byteObject , password , returnByteObject = True)
```

Arguments - 

* byteObject -> byteObject you want to encrypt , can be of any length. bytes or bytearray type.
* password -> password will be used to encrypt the string. should be at least 10 to 12 digits long containing combination of lower , upper case and digits as well as special chars. The more strong and not easily guessable the password is , the stronger is the encryption. 
* returnByteObject -> Onetimepad by default works with strings only , so to encrypt a byte object we need to first convert it into string using https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/. So an extra step is involed. So if you think you don't need to convert the encrypted string to byte to store it somewhere , make this False. No matter what return type you choose , you will always get back a decrypted byte object only. It is just that you will save some resources if you make this False.
* returns a encrypted string


Note -> as you know in onetimepad , message will be of the same length as key . that problem is auto handled here. This algo is heavily customized to provide the best possible encryption version of onetimepad.

Note (IMP) -> Do not store SHA224 or MD5 hashed version of your password anywhere. instead use SHA256 , SHA384 , SHA512 for hashing and password verification systems.



<br>
<br>

### 2.4 Generator version - Decrypt Byte

#### 2.4.1 If you choosed returnByteObject = False in encryption function

``` python
# decrypt method
OW.BytesEncryptor_yield.decrypt(enc_string , password)
```

Arguments - 

* enc_string -> string returned by OW.BytesEncryptor.encrypt(returnByteObject = False) method. The encrypted string.
* password -> password used to encrypt the byte
* returns a decrypted byte object

<br>
<br>


#### 2.4.2 If you choosed returnByteObject = True in encryption function

``` python
# decrypt method
OW.BytesEncryptor_yield.decrypt_byte(enc_byteObject , password)
```

Arguments - 

* enc_byteObject -> byte returned by OW.BytesEncryptor.encrypt(returnByteObject = True) method. The encrypted byte.
* password -> password used to encrypt the byte
* returns a decrypted byte object

<br>
<br>



both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_byteEncrytor2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/onetimepadWrapper.py


Example - 

``` python
    byteObject = b"hello world" * 1123

    genObj_encrypt = BytesEncryptor_yield.encrypt(byteObject , "hello" , returnByteObject=False)

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    genObj_decrypt = BytesEncryptor_yield.decrypt(encryptedString , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    if(byteObject == decryptedByte):
        print("\nok")
    else:
        print("\nerror")




    print("\n\ntest 2\n\n")


    byteObject = b"hello world" * 1123

    genObj_encrypt = BytesEncryptor_yield.encrypt(byteObject , "hello" , returnByteObject=True)

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    genObj_decrypt = BytesEncryptor_yield.decrypt_byte(encryptedByte , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("\ron {} out of {}   ".format(onCount , totalCount) , end = "")
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    if(byteObject == decryptedByte):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell

on 13683 out of 13683   

on 13683 out of 13695   

ok


test 2



on 87801 out of 87801   

on 87801 out of 87807   

ok
```


<br>
<br>
<br>
<br>
<br>
<br>


Note - Onetimepad is slow for bytes encryption , it would be better to use fernetWrapper of this module for that. But for small tasks , it does not matter.



<br>
<br>
<br>
<br>
<br>
<br>