
# hashers v2

It is a wrapper over hashlib algo's making them more secure using shuffling.

It is faster version of hashers in this module but is less secure as it does not shuffle the data before hashing. But still no one easily identify the original data from the hash.

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
from pySecureCryptos import hashers_v2 as hashers
```

<br>
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
1. sha256
2. sha384
3. sha512
4. md5
5. sha1
6. sha224

<br>
<br>
<br>
<br>
<br>
<br>















 <!-- _  
/ | 
| | 
| | 
|_| 
     -->


# 1. SHA256

<br>
<br>

``` python
hashObj = hashers.SHA256(bytesObj , chunkSize = 1048576)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 1048576. 
* returns a obj of class SHA256 use below methods to get the final hash.

<br>
<br>
<br>

### 1.1 get string value of hash

``` python
hashObj.get_string()
```

* returns string value of the hash.

<br>
<br>
<br>


### 1.2 get byte value of hash

``` python
hashObj.get_byte()
```

* returns byte value of the hash.

<br>
<br>
<br>


Example [ string ] - 

``` python
    bytesObj = b"hello world"

    shaObj = SHA256(bytesObj)

    sha256Hash = shaObj.get_string()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")
```

Output - 

``` shell

hashed value = b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9

hashed len = 64
```


<br>
<br>
<br>


Example [ byte ] - 

``` python
    
    bytesObj = b"hello world"

    shaObj = SHA256(bytesObj)

    sha256Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")
```

Output - 

``` shell

hashed value = b"\xb9M'\xb9\x93M>\x08\xa5.R\xd7\xda}\xab\xfa\xc4\x84\xef\xe3zS\x80\xee\x90\x88\xf7\xac\xe2\xef\xcd\xe9"

hashed len = 32
```



<br>
<br>
<br>


NOTE -> both the above methods have yielder / generators versions which are suitable for hashing large data. it returns the progress after processing each chunk. see example below to see how to use.



<br>
<br>
<br>















### 1.3 generator version - get string value of hash

``` python
hashObj.get_string_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


### 1.4 generator version - get byte value of hash

``` python
hashObj.get_byte_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


Example [ string ] - 

``` python
    
    bytesObj = b"hello world" * 11230

    shaObj = SHA256(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha256Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")
```

Output - 

``` shell

(177, 177)

hashed value = 47cfc9c9c530a1777a5e4010e282cb394b58d8c4b89afe95443514d14a71d770

hashed len = 64
```


<br>
<br>
<br>


Example [ byte ] - 

``` python
    
    bytesObj = b"hello world" * 11230

    shaObj = SHA256(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha256Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha256Hash}")
    print(f"\nhashed len = {len(sha256Hash)}")
```

Output - 

``` shell

(177, 177)

hashed value = b'G\xcf\xc9\xc9\xc50\xa1wz^@\x10\xe2\x82\xcb9KX\xd8\xc4\xb8\x9a\xfe\x95D5\x14\xd1Jq\xd7p'

hashed len = 32
```



<br>
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


# 2. SHA384

<br>
<br>

``` python
hashObj = hashers.SHA384(bytesObj , chunkSize = 1048576)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 1048576. 
* returns a obj of class SHA384 use below methods to get the final hash.

<br>
<br>
<br>

### 2.1 get string value of hash

``` python
hashObj.get_string()
```

* returns string value of the hash.

<br>
<br>
<br>


### 2.2 get byte value of hash

``` python
hashObj.get_byte()
```

* returns byte value of the hash.

<br>
<br>
<br>


Example [ string ] - 

``` python
    
    bytesObj = b"hello world"

    shaObj = SHA384(bytesObj)

    sha384Hash = shaObj.get_string()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")

```

Output - 

``` shell

hashed value = fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd

hashed len = 96
```


<br>
<br>
<br>


Example [ byte ] - 

``` python
    
    bytesObj = b"hello world"

    shaObj = SHA384(bytesObj)

    sha384Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")

```

Output - 

``` shell

hashed value = b'\xfd\xbd\x8eu\xa6\x7f)\xf7\x01\xa4\xe0@8^.#\x98c\x03\xea\x10#\x92\x11\xaf\x90\x7f\xcb\xb85x\xb3\xe4\x17\xcbq\xcedn\xfd\x08\x19\xdd\x8c\x08\x8d\xe1\xbd'

hashed len = 48
```



<br>
<br>
<br>


NOTE -> both the above methods have yielder / generators versions which are suitable for hashing large data. it returns the progress after processing each chunk. see example below to see how to use.



<br>
<br>
<br>
















### 2.3 generator version - get string value of hash

``` python
hashObj.get_string_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


### 2.4 generator version - get byte value of hash

``` python
hashObj.get_byte_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


Example [ string ] - 

``` python
    
    bytesObj = b"hello world" * 11230

    shaObj = SHA384(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha384Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")

```

Output - 

``` shell

(177, 177)

hashed value = 3779afffa8e5ec85cf6686e93f90ac8a366f3a39988f85c531832194f825c482ab6a566b022fd96dd5e0390453c60151

hashed len = 96
```


<br>
<br>
<br>


Example [ byte ] - 

``` python
    
    bytesObj = b"hello world" * 11230

    shaObj = SHA384(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha384Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha384Hash}")
    print(f"\nhashed len = {len(sha384Hash)}")


```

Output - 

``` shell

(177, 177)

hashed value = b'7y\xaf\xff\xa8\xe5\xec\x85\xcff\x86\xe9?\x90\xac\x8a6o:9\x98\x8f\x85\xc51\x83!\x94\xf8%\xc4\x82\xabjVk\x02/\xd9m\xd5\xe09\x04S\xc6\x01Q'

hashed len = 48
```



<br>
<br>
<br>
<br>
<br>
<br>
<br>













<!-- 
 _____  
|___ /  
  |_ \  
 ___) | 
|____/  
         -->


# 3. SHA512

<br>
<br>

``` python
hashObj = hashers.SHA512(bytesObj , chunkSize = 1048576)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 1048576. 
* returns a obj of class SHA512 use below methods to get the final hash.

<br>
<br>
<br>

### 3.1 get string value of hash

``` python
hashObj.get_string()
```

* returns string value of the hash.

<br>
<br>
<br>


### 3.2 get byte value of hash

``` python
hashObj.get_byte()
```

* returns byte value of the hash.

<br>
<br>
<br>


Example [ string ] - 

``` python
    
    bytesObj = b"hello world"

    shaObj = SHA512(bytesObj)

    sha512Hash = shaObj.get_string()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")

```

Output - 

``` shell

hashed value = 309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f

hashed len = 128
```


<br>
<br>
<br>


Example [ byte ] - 

``` python
    
    bytesObj = b"hello world"

    shaObj = SHA512(bytesObj)

    sha512Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")

```

Output - 

``` shell

hashed value = b'0\x9e\xccH\x9c\x12\xd6\xebL\xc4\x0fP\xc9\x02\xf2\xb4\xd0\xedw\xeeQ\x1a|z\x9b\xcd<\xa8mL\xd8o\x98\x9d\xd3[\xc5\xffI\x96p\xda4%[E\xb0\xcf\xd80\xe8\x1f`]\xcf}\xc5T.\x93\xae\x9c\xd7o'

hashed len = 64
```



<br>
<br>
<br>


NOTE -> both the above methods have yielder / generators versions which are suitable for hashing large data. it returns the progress after processing each chunk. see example below to see how to use.

















<br>
<br>
<br>


### 3.3 generator version - get string value of hash

``` python
hashObj.get_string_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


### 3.4 generator version - get byte value of hash

``` python
hashObj.get_byte_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


Example [ string ] - 

``` python
    
    bytesObj = b"hello world" * 11230

    shaObj = SHA512(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha512Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")

```

Output - 

``` shell

(177, 177)

hashed value = 1f32eba29bd564af116b4d46a8987663842c85e8d49b2d62062203342e65ec44de9b851cbde425f644b6a68f540bd83ec16c7a631801651040a2833f7fa85228

hashed len = 128
```


<br>
<br>
<br>


Example [ byte ] - 

``` python
    
    bytesObj = b"hello world" * 11230

    shaObj = SHA512(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha512Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha512Hash}")
    print(f"\nhashed len = {len(sha512Hash)}")

```

Output - 

``` shell

(177, 177)

hashed value = b'\x1f2\xeb\xa2\x9b\xd5d\xaf\x11kMF\xa8\x98vc\x84,\x85\xe8\xd4\x9b-b\x06"\x034.e\xecD\xde\x9b\x85\x1c\xbd\xe4%\xf6D\xb6\xa6\x8fT\x0b\xd8>\xc1lzc\x18\x01e\x10@\xa2\x83?\x7f\xa8R('

hashed len = 64
```



<br>
<br>
<br>
<br>
<br>

### NOTE -> SHA512 is latest and recommended in mordern era.










<br>
<br>
<br>
<br>
<br>
<br>

























<!-- 


 _  _    
| || |   
| || |_  
|__   _| 
   |_|   
          -->


# 4. MD5

<br>
<br>

``` python
hashObj = hashers.MD5(bytesObj , chunkSize = 1048576)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 1048576. 
* returns a obj of class md5 use below methods to get the final hash.

<br>
<br>
<br>

### 4.1 get string value of hash

``` python
hashObj.get_string()
```

* returns string value of the hash.

<br>
<br>
<br>


### 4.2 get byte value of hash

``` python
hashObj.get_byte()
```

* returns byte value of the hash.

<br>
<br>
<br>


Example [ string ] - 

``` python

    bytesObj = b"hello world"

    shaObj = MD5(bytesObj)

    md5Hash = shaObj.get_string()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")
```

Output - 

``` shell

hashed value = 5eb63bbbe01eeed093cb22bb8f5acdc3

hashed len = 32
```


<br>
<br>
<br>


Example [ byte ] - 

``` python

    bytesObj = b"hello world"

    shaObj = MD5(bytesObj)

    md5Hash = shaObj.get_byte()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")
```

Output - 

``` shell

hashed value = b'^\xb6;\xbb\xe0\x1e\xee\xd0\x93\xcb"\xbb\x8fZ\xcd\xc3'

hashed len = 16
```



<br>
<br>
<br>


NOTE -> both the above methods have yielder / generators versions which are suitable for hashing large data. it returns the progress after processing each chunk. see example below to see how to use.



<br>
<br>
<br>















### 4.3 generator version - get string value of hash

``` python
hashObj.get_string_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


### 4.4 generator version - get byte value of hash

``` python
hashObj.get_byte_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


Example [ string ] - 

``` python

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = MD5(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            md5Hash = ex.value
            break
    print()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")
```

Output - 

``` shell

(12, 12)

hashed value = 41d59387d34ef45557d7db17788a16df

hashed len = 32
```


<br>
<br>
<br>


Example [ byte ] - 

``` python

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = MD5(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            md5Hash = ex.value
            break
    print()

    print(f"\nhashed value = {md5Hash}")
    print(f"\nhashed len = {len(md5Hash)}")
```

Output - 

``` shell

(12, 12)

hashed value = b'A\xd5\x93\x87\xd3N\xf4UW\xd7\xdb\x17x\x8a\x16\xdf'

hashed len = 16
```



<br>
<br>
<br>
<br>
<br>
<br>
<br>































<!-- 

 ____   
| ___|  
|___ \  
 ___) | 
|____/  
        
 -->


# 5. SHA1

<br>
<br>

``` python
hashObj = hashers.SHA1(bytesObj , chunkSize = 1048576)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 1048576. 
* returns a obj of class sha1 use below methods to get the final hash.

<br>
<br>
<br>

### 5.1 get string value of hash

``` python
hashObj.get_string()
```

* returns string value of the hash.

<br>
<br>
<br>


### 5.2 get byte value of hash

``` python
hashObj.get_byte()
```

* returns byte value of the hash.

<br>
<br>
<br>


Example [ string ] - 

``` python

    bytesObj = b"hello world"

    shaObj = SHA1(bytesObj)

    sha1Hash = shaObj.get_string()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")
```

Output - 

``` shell

hashed value = 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed

hashed len = 40
```


<br>
<br>
<br>


Example [ byte ] - 

``` python

    bytesObj = b"hello world"

    shaObj = SHA1(bytesObj)

    sha1Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")
```

Output - 

``` shell

hashed value = b'*\xael5\xc9O\xcf\xb4\x15\xdb\xe9_@\x8b\x9c\xe9\x1e\xe8F\xed'

hashed len = 20
```



<br>
<br>
<br>


NOTE -> both the above methods have yielder / generators versions which are suitable for hashing large data. it returns the progress after processing each chunk. see example below to see how to use.



<br>
<br>
<br>















### 5.3 generator version - get string value of hash

``` python
hashObj.get_string_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


### 5.4 generator version - get byte value of hash

``` python
hashObj.get_byte_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


Example [ string ] - 

``` python

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA1(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha1Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")

```

Output - 

``` shell

(12, 12)

hashed value = 55c0e5b0bbad089bb6b2fd506e3631ee4ea034c1

hashed len = 40
```


<br>
<br>
<br>


Example [ byte ] - 

``` python

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA1(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha1Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha1Hash}")
    print(f"\nhashed len = {len(sha1Hash)}")
```

Output - 

``` shell

(12, 12)

hashed value = b'U\xc0\xe5\xb0\xbb\xad\x08\x9b\xb6\xb2\xfdPn61\xeeN\xa04\xc1'

hashed len = 20
```



<br>
<br>
<br>
<br>
<br>
<br>
<br>



































<!-- 

  __    
 / /_   
| '_ \  
| (_) | 
 \___/  
         -->


# 6. SHA224

<br>
<br>

``` python
hashObj = hashers.SHA224(bytesObj , chunkSize = 1048576)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 1048576. 
* returns a obj of class sha224 use below methods to get the final hash.

<br>
<br>
<br>

### 6.1 get string value of hash

``` python
hashObj.get_string()
```

* returns string value of the hash.

<br>
<br>
<br>


### 6.2 get byte value of hash

``` python
hashObj.get_byte()
```

* returns byte value of the hash.

<br>
<br>
<br>


Example [ string ] - 

``` python

    bytesObj = b"hello world"

    shaObj = SHA224(bytesObj)

    sha224Hash = shaObj.get_string()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")
```

Output - 

``` shell

hashed value = 2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b

hashed len = 56
```


<br>
<br>
<br>


Example [ byte ] - 

``` python

    bytesObj = b"hello world"

    shaObj = SHA224(bytesObj)

    sha224Hash = shaObj.get_byte()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")
```

Output - 

``` shell

hashed value = b'/\x05G\x7f\xc2K\xb4\xfa\xef\xd8e\x17\x15m\xaf\xde\xce\xc4[\x8a\xd3\xcf%"\xa5cX+'

hashed len = 28
```



<br>
<br>
<br>


NOTE -> both the above methods have yielder / generators versions which are suitable for hashing large data. it returns the progress after processing each chunk. see example below to see how to use.



<br>
<br>
<br>















### 6.3 generator version - get string value of hash

``` python
hashObj.get_string_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


### 6.4 generator version - get byte value of hash

``` python
hashObj.get_byte_yield()
```

* returns a generator obj. see example below to know how to get the hash value from it.

<br>
<br>
<br>


Example [ string ] - 

``` python

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA224(bytesObj)

    genObj = shaObj.get_string_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha224Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")

```

Output - 

``` shell

(12, 12)

hashed value = 5d8e44a01a813db2befbbc2bf7d13d01d1c9485b417a2b8f0d28fdea

hashed len = 56
```


<br>
<br>
<br>


Example [ byte ] - 

``` python

    bytesObj = b"hello world" * 1024 * 1024

    shaObj = SHA224(bytesObj)

    genObj = shaObj.get_byte_yield()

    print()
    while(True):
        try:
            result = next(genObj)
            print(f"\r{result}" , end="")
        except StopIteration as ex:
            sha224Hash = ex.value
            break
    print()

    print(f"\nhashed value = {sha224Hash}")
    print(f"\nhashed len = {len(sha224Hash)}")
```

Output - 

``` shell

(12, 12)

hashed value = b']\x8eD\xa0\x1a\x81=\xb2\xbe\xfb\xbc+\xf7\xd1=\x01\xd1\xc9H[Az+\x8f\r(\xfd\xea'

hashed len = 28
```



<br>
<br>
<br>
<br>
<br>
<br>
<br>














