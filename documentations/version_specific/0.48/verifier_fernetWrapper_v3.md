# verifier fernet Wrapper v3

Much faster version of the fernet wrapper using multiprocessing to encrypting huge objects with ease





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
from pySecureCryptos import verifier_fernetWrapper_v3 as FW 
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

1. Get key
2. Encrypt and Decrypt bytes
3. Encrypt and Decrypt string


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


# 1. Get key

Before proceding to encryption , you must get fernet key from getKey method


```python
myKey = Keys.getKey(password , iterations=390000)
```

Arguments - 
* password -> password is used to derive a key. password need to be string type and should be at least 12 digit long for better security.
* iterations -> Set to max your machine can hold on.

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

# 2. Encrypt and Decrypt bytes

<br> 

## 2.1 Encrypt & Decrypt in memory data 

data can be between = 8 to 800 MB , depends on the chunk size

```python

# encrypt method
FW.Encryptor.main_encrypt_byte(byte , key , chunkSize = 8)
```

Arguments - 
* byte - byte you want to encrypt
* key - key you got from Keys.getKey()
* chunkSize - In MB , data is divided into chunks and then processed on seperate cores. More powerfull the CPU , more you can make the chunkSize
* returns encrypted byte

<br>
<br>


```python

# decrypt method
FW.Encryptor.main_decrypt_byte(enc_byte , key)
```

Arguments - 
* enc_byte - encrypted byte returned from main_encrypt_byte() method
* key - key you got from Keys.getKey()
* returns decrypted byte


<br>
<br>

Example - 
```python

    print("starting")

    key = Keys.getKey("hello")

    n = 1024 * 1024 * 24
    toenc = b"h" * n

    start = time.perf_counter()

    enc = Encryptor.main_encrypt_byte(toenc , key)
    dec = Encryptor.main_decrypt_byte(enc , key)

    end = time.perf_counter()

    print(len(enc))
    print(len(dec))

    print(toenc == dec)


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , len(toenc) / 1024 / 1024))

```

Output - 

```shell
starting
33554935
25165824
True
time_taken = 0.9858170200022869 , to encrypt the size of 24.0 MB
```



<br>
<br>
<br>
<br>




## 2.2 Encrypt & Decrypt a in large file from disk

data can be between = 8 to 800 MB , depends on the chunk size

```python

# encrypt method
FW.Encryptor.encrypt_file(filepath , destinationPath , key)
```

Arguments - 
* filepath - file name with path you want to encrypt
* destinationPath - path where you want the encrypted file to be stored. method reads , encrypt and write data in chunks so that less memory is used. Best chunksize is auto decided according to machine core count. final file will be named as exact with .enc extension. It is recommended to not change the .enc extension as their can be problem in decryption.
* key - key you got from Keys.getKey()
* returns None.

<br>
<br>


```python

# decrypt method
FW.Encryptor.decrypt_file(filepath , destinationPath , key)
```

Arguments - 
* filepath - encrypted file with .enc extension with path
* destinationPath - where you want the decrypted file to be stored
* key - key you got from Keys.getKey()
* returns None


Example - 

```python

    print("starting")

    key = Keys.getKey("hello")

    fileName = "testVideo.mp4"

    filePath = f"/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/{fileName}"
    destPath = "/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/"
    
    filePath2 = f"/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/{fileName}.enc"
    destPath2 = "/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/dec/"

    start = time.perf_counter()

    enc_obj = Encryptor.encrypt_file(filePath , destPath , key)

    print()
    for i in enc_obj:
        print(f"\r{i}" , end = "")
    print()

    dec_obj = Encryptor.decrypt_file(filePath2 , destPath2 , key)

    print()
    for i in dec_obj:
        print(f"\r{i}" , end = "")
    print()

    end = time.perf_counter()


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , os.stat(filePath).st_size / 1024 / 1024))

```


Output - 

```shell
starting

(3, 3)

(4, 4)
time_taken = 3.6183117940090597 , to encrypt the size of 72.17074584960938 MB
```







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

# 3. Encrypt and Decrypt strings

<br> 

## 3.1 Encrypt & Decrypt in memory data 

data can be between = 8 to 800 MB , depends on the chunk size

```python

# encrypt method
FW.Encryptor.main_encrypt_string(string , key , chunkSize = 4)
```

Arguments - 
* string - string you want to encrypt
* key - key you got from Keys.getKey()
* chunkSize - In MB , data is divided into chunks and then processed on seperate cores. More powerfull the CPU , more you can make the chunkSize
* returns encrypted string

<br>
<br>


```python

# decrypt method
FW.Encryptor.main_decrypt_string(enc_string , key)
```

Arguments - 
* enc_string - encrypted string returned from main_encrypt_string() method
* key - key you got from Keys.getKey()
* returns decrypted string


<br>
<br>

Example - 
```python

    print("starting")

    key = Keys.getKey("hello")

    toenc = 'h' * (1024 * 1024 * 16)

    start = time.perf_counter()

    enc = Encryptor.main_encrypt_string(toenc , key)
    dec = Encryptor.main_decrypt_string(enc , key)

    end = time.perf_counter()

    print(len(enc))
    print(len(dec))

    print(toenc == dec)


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , len(toenc) / 1024 / 1024))

```

Output - 

```shell
starting
44740600
16777216
True
time_taken = 1.1332922559959115 , to encrypt the size of 16.0 MB
```



<br>
<br>
<br>
<br>




## 3.2 Encrypt & Decrypt a large file from disk

data can be between = 8 to 800 MB , depends on the chunk size

```python

# encrypt method
FW.Encryptor.encrypt_file(filepath , destinationPath , key)
```

Arguments - 
* filepath - file name with path you want to encrypt
* destinationPath - path where you want the encrypted file to be stored. method reads , encrypt and write data in chunks so that less memory is used. Best chunksize is auto decided according to machine core count. final file will be named as exact with .enc extension. It is recommended to not change the .enc extension as their can be problem in decryption.
* key - key you got from Keys.getKey()
* returns None.

<br>
<br>


```python

# decrypt method
FW.Encryptor.decrypt_file(filepath , destinationPath , key)
```

Arguments - 
* filepath - encrypted file with .enc extension with path
* destinationPath - where you want the decrypted file to be stored
* key - key you got from Keys.getKey()
* returns None


Example - 

```python

    print("starting")

    key = Keys.getKey("hello")

    fileName = "bigText.txt"

    filePath = f"/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/{fileName}"
    destPath = "/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/"
    
    filePath2 = f"/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/{fileName}.enc"
    destPath2 = "/media/veracrypt64/Projects/pyModules/pySecureCryptos/tests/binaryTestMatrial/dec/"

    start = time.perf_counter()

    enc_obj = Encryptor.encrypt_file(filePath , destPath , key)

    print()
    for i in enc_obj:
        print(f"\r{i}" , end = "")
    print()

    dec_obj = Encryptor.decrypt_file(filePath2 , destPath2 , key)

    print()
    for i in dec_obj:
        print(f"\r{i}" , end = "")
    print()

    end = time.perf_counter()


    print("time_taken = {} , to encrypt the size of {} MB".format(end - start , os.stat(filePath).st_size / 1024 / 1024))
```


Output - 

```shell
starting

(5, 5)

(6, 6)
time_taken = 6.578146893996745 , to encrypt the size of 138.760479927063 MB
```







<br>
<br>
<br>
<br>
<br>
<br>
