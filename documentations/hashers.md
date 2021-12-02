
# hashers

It is a wrapper over hashlib algo's making them more secure using shuffling.

<br>
<br>
<br>

# Importing - 

``` python
from pySecureCryptos import hashers
```

<br>
<br>
<br>
<br>
<br>
<br>

# Methods - 
1. sha256
2. sha384
3. sha512

<br>
<br>
<br>
<br>
<br>
<br>

# 1. SHA256

<br>
<br>

``` python
hashObj = hashers.SHA256(bytesObj , chunkSize = 2048)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 2048. 
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

hashed value = be36a6bfc21c202b9fdd32faa5cd8f30ea97c467142b88639e3ba4f56bd6a5a2

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

hashed value = b'\xbe6\xa6\xbf\xc2\x1c +\x9f\xdd2\xfa\xa5\xcd\x8f0\xea\x97\xc4g\x14+\x88c\x9e;\xa4\xf5k\xd6\xa5\xa2'

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

(122, 122)

hashed value = 1c707d7ba0003e90d8bdbd2256cb555a93edb53c4ae3d1f7e3743469d33de643

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

(122, 122)

hashed value = b'\x1cp}{\xa0\x00>\x90\xd8\xbd\xbd"V\xcbUZ\x93\xed\xb5<J\xe3\xd1\xf7\xe3t4i\xd3=\xe6C'

hashed len = 32
```



<br>
<br>
<br>
<br>
<br>
<br>
<br>





# 2. SHA384

<br>
<br>

``` python
hashObj = hashers.SHA384(bytesObj , chunkSize = 2048)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 2048. 
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

hashed value = b94c241b95416c09b28a8120dc1af4b77f768cdd9fcb3252c4ecb8b450bf3b4d64d4934c60ed490b43a75a937654b58d

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

hashed value = b'\xb9L$\x1b\x95Al\t\xb2\x8a\x81 \xdc\x1a\xf4\xb7\x7fv\x8c\xdd\x9f\xcb2R\xc4\xec\xb8\xb4P\xbf;Md\xd4\x93L`\xedI\x0bC\xa7Z\x93vT\xb5\x8d'

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

(122, 122)

hashed value = 3c2f2faa072550d3510102c4d56f240df2c4e608c2348fcbedbd26cee0cb507bf370228b0699668c1c868321459e064f

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

(122, 122)

hashed value = b'<//\xaa\x07%P\xd3Q\x01\x02\xc4\xd5o$\r\xf2\xc4\xe6\x08\xc24\x8f\xcb\xed\xbd&\xce\xe0\xcbP{\xf3p"\x8b\x06\x99f\x8c\x1c\x86\x83!E\x9e\x06O'

hashed len = 48
```



<br>
<br>
<br>
<br>
<br>
<br>
<br>




# 3. SHA512

<br>
<br>

``` python
hashObj = hashers.SHA512(bytesObj , chunkSize = 2048)
```

Arguments - 

* bytesObj -> bytesObj to generate the hash of. you can use [encoder decoder](https://www.letscodeofficial.com/documentations/pSC_encoderDecoders#/) to convert string into byte.
* chunkSize -> bytes data is divided into chunks to hash properly. chunkSize determines the size of chunk of each hash updater. default it is set to 2048. 
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

hashed value = 2d62dd7b42a7c0555a5531c4adcfe68da58a67144c9f0601d1ee80f7a7d2a740e8f0af727a91535339ba9fc48de6b4a3e0e5a596ca8d941744391ab79f19f79e

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

hashed value = b'-b\xdd{B\xa7\xc0UZU1\xc4\xad\xcf\xe6\x8d\xa5\x8ag\x14L\x9f\x06\x01\xd1\xee\x80\xf7\xa7\xd2\xa7@\xe8\xf0\xafrz\x91SS9\xba\x9f\xc4\x8d\xe6\xb4\xa3\xe0\xe5\xa5\x96\xca\x8d\x94\x17D9\x1a\xb7\x9f\x19\xf7\x9e'

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

(122, 122)

hashed value = e1a344e8a87dff0a7ab579fe5e9be45a0f4494f78486fd7fd148aaf7c037cfa0bdf8a0bc1d650bb126cd6e0b73dd19067c0dbea8f54ece2763522458312574c0

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

(122, 122)

hashed value = b"\xe1\xa3D\xe8\xa8}\xff\nz\xb5y\xfe^\x9b\xe4Z\x0fD\x94\xf7\x84\x86\xfd\x7f\xd1H\xaa\xf7\xc07\xcf\xa0\xbd\xf8\xa0\xbc\x1de\x0b\xb1&\xcdn\x0bs\xdd\x19\x06|\r\xbe\xa8\xf5N\xce'cR$X1%t\xc0"

hashed len = 64
```



<br>
<br>
<br>
<br>
<br>

NOTE -> SHA512 is latest and recommended in mordern era.