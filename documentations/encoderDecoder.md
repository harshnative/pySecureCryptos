
# encoder Decoders

<br>
<br>
<br>








 <!-- _                                      _    
(_)  _ __ ___    _ __     ___    _ __  | |_  
| | | '_ ` _ \  | '_ \   / _ \  | '__| | __| 
| | | | | | | | | |_) | | (_) | | |    | |_  
|_| |_| |_| |_| | .__/   \___/  |_|     \__| 
                |_|                           -->


# Importing - 

``` python
from pySecureCryptos import encoderDecoders as ED
```

<br>
<br>
<br>
<br>
<br>








<!-- 
                    _     _                   _        
 _ __ ___     ___  | |_  | |__     ___     __| |  ___  
| '_ ` _ \   / _ \ | __| | '_ \   / _ \   / _` | / __| 
| | | | | | |  __/ | |_  | | | | | (_) | | (_| | \__ \ 
|_| |_| |_|  \___|  \__| |_| |_|  \___/   \__,_| |___/ 
                                                        -->


# Methods - 

1. B2S - Convert Byte to String & vice versa
2. S2B - Convert String to Byte & vice versa
3. B2S hex - Convert Byte to Hexa Decimal String & vice versa {[Recommended]()}

4. S2B v2 - Convert String to Byte & vice versa {[Recommended]()}
5. B2S v2 - Convert Byte to String & vice versa
6. Base36Encoder - Convert Byte to String & vice versa 
7. Base90Encoder - Convert Byte to String & vice versa 
8. Base64_64 - Convert Byte to String & vice versa 
9. Base64_16 - Convert Byte to String & vice versa 
10. Base64_32 - Convert Byte to String & vice versa 
11. Base64_85 - Convert Byte to String & vice versa 

<br>

Byte to string method can convert any byte to string using encoder , and only this string can be converted back to original byte using decoder of same class.

String to Byte method can convert any string to byte using encoder and only this byte can be converted back to original string using decoder of the same class.

Using encoder of another class and decoder of other class will not work.

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


# 1. B2S - Convert Byte to String & vice versa

<br>
<br>

### 1.1 Convert any Byte to String  

``` python
# encode method
ED.Byte2String.encode(byte)
```

Arguments - 

* byte -> any bytes or byteArray object to convert it into string , ex - usefull when you want to store a byte object in text field in database 



<br>
<br>

### 1.2 Convert above encoded string back to byte

``` python
# decode method
ED.Byte2String.decode(string)
```

Arguments - 

* string -> string which was returned from ED.Byte2String.encode() method to convert it back to byte

<br>
<br>

Example - 

``` python
    myByte = b"hello world"

    stringFromByte = Byte2String.encode(myByte)

    print(stringFromByte , type(stringFromByte))

    byteAgain = Byte2String.decode(stringFromByte)

    print(byteAgain)
```

Output - 

``` shell
104101108108111032119111114108100 <class 'str'>
bytearray(b'hello world')
```


<br>
<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>
















### 1.3 Generator version - Convert any Byte to String  

``` python
# encode method
ED.Byte2String_yield.encode(byte)
```

Arguments - 

* byte -> any bytes or byteArray object to convert it into string , ex - usefull when you want to store a byte object in text field in database 



<br>
<br>

### 1.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Byte2String_yield.decode(string)
```

Arguments - 

* string -> string which was returned from ED.Byte2String.encode() method to convert it back to byte

<br>
<br>


both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py


Example - 

``` python
    # big object to encode decode 
    myByte = b"hello world" * 1000

    # creating the generator obj for the method
    generatorObj_encode = Byte2String_yield.encode(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            
            """ you can get this function for here - https://www.blog.letscodeofficial.com/@harshnative/best-standalone-progress-bar-for-terminal-in-python/ """

            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    
    # similarly for decode
    generatorObj_decode = Byte2String_yield.decode(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    if(byteAgain == myByte):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
Progress: |██████████████████████████████████████████████████| 100.0% Complete
Progress: |█████████████████████████████████████████████████-| 100.0% Complete
ok
```


<br>
<br>
<br>
<br>
<br>
<br>
















 <!-- ____   
|___ \  
  __) | 
 / __/  
|_____| 
         -->


# 2. S2B - Convert String to Byte & vice versa

<br>
<br>

### 2.1 Convert any String to Byte  

``` python
# encode method
ED.String2Byte.encode(string)
```

Arguments - 

* string -> any string you want to convert to bytes type. returns bytearray object



<br>
<br>

### 2.2 Convert above encoded Byte back to String

``` python
# decode method
ED.String2Byte.decode(byte)
```

Arguments - 

* byte -> byte which was returned from ED.String2Byte.encode() method to convert it back to string

<br>
<br>

Example - 

``` python
    myString = "hello world"

    byteFromString = String2Byte.encode(myString)

    print(byteFromString , type(byteFromString))

    stringAgain = String2Byte.decode(byteFromString)

    print(stringAgain)
```

Output - 

``` shell
bytearray(b'hello world') <class 'bytearray'>
hello world
```


<br>
<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 2.3 Generator version - Convert any String to Byte  

``` python
# encode method
ED.String2Byte_yield.encode(string)
```

Arguments - 

* string -> any string you want to convert to bytes type. returns bytearray object


<br>
<br>

### 2.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.String2Byte_yield.decode(byte)
```

Arguments - 

* byte -> byte which was returned from ED.String2Byte.encode() method to convert it back to string

<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test4() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python
    
    # big object to encode decode 
    myString = "hello world" * 1000

    # creating the generator obj for the method
    generatorObj_encode = String2Byte_yield.encode(myString)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar

            """ you can get this function for here - https://www.blog.letscodeofficial.com/@harshnative/best-standalone-progress-bar-for-terminal-in-python/ """
            
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            byteFromString = ex.value
            break

    
    # similarly for decode
    generatorObj_decode = String2Byte_yield.decode(byteFromString)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            stringAgain = ex.value
            break

    if(stringAgain == myString):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
Progress: |██████████████████████████████████████████████████| 100.0% Complete
Progress: |██████████████████████████████████████████████████| 100.0% Complete

ok
```


<br>
<br>
<br>
<br>
<br>
<br>

















 <!-- _____  
|___ /  
  |_ \  
 ___) | 
|____/  
         -->


# 3. B2S hex - Convert Byte to Hexa Decimal string and vice versa

Compression ratio is higher than above byte to string convertor , suitable for large files.

<br>
<br>

### 3.1 Convert any Byte to String in hexadecimal representation

``` python
# encode method
ED.HexConvertor.encode(byte)
```

Arguments - 

* byte -> any byte you want to convert to string type. returns hexa decimal version of string
* encoded string is twice the length of byte and works with any bytes data.


<br>
<br>

### 3.2 Convert above encoded string back to bytes

``` python
# decode method
ED.HexConvertor.decode(string)
```

Arguments - 

* string -> string which was returned from ED.HexConvertor.encode() method to convert it back to bytes

<br>
<br>

Example - 

``` python
    
    myByte = b"hello world"

    stringFromByte = HexConvertor.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = HexConvertor.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")

```

Output - 

``` shell
stringFromByte = 68656c6c6f20776f726c64
byte Again = b'hello world'
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 3.3 Generator version - Convert any Byte to String in hexa decimal representation.  

``` python
# encode method
ED.HexConvertor.encode_yield(byte , chunkSize = 1)
```

Arguments - 

* byte -> any byte you want to convert to string type. returns hexa decimal version of string
* chunkSize -> chunk size in MB , generator function yield after encoding every chunk. so decide the chunk size based on your processing power.
* encoded string is twice the length of byte and works with any bytes data.



<br>
<br>

### 3.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.HexConvertor.decode_yield(string , chunkSize = 1)
```

Arguments - 

* string -> string which was returned from ED.HexConvertor.encode() method to convert it back to bytes
* chunkSize should be same as used in ED.HexConvertor.encode_yield() method

<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_HexConvertor2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python
    
    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = HexConvertor.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = HexConvertor.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")

```

Output - 

``` shell
myByte len =  184549376 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  369098752 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  184549376 


ok
```


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


# 4. S2B v2 - Convert String to Byte & vice versa

Compression ratio is higher than above byte to string convertor , suitable for large files.

This version two is much faster than the version 1 as it uses in built utf-8 encoding. if your files are compatible with utf-8 use the version 1 of the encoder.

<br>
<br>

### 4.1 Convert any String to Byte

``` python
# encode method
ED.String2Byte_v2.encode(string)
```

Arguments - 

* string -> string to convert to bytes.
* length of encoded byte is same as the length of input string

<br>
<br>

### 4.2 Convert above encoded byte back to string

``` python
# decode method
ED.String2Byte_v2.decode(byte)
```

Arguments - 

* byte -> byte which was returned from ED.String2Byte_v2.encode() method to convert it back to string

<br>
<br>

Example - 

``` python
    
    # big object to encode decode 
    myString = "hello world"

    print("myString = " , myString)
    print("str len = " , len(myString) , "\n")

    # creating the generator obj for the method
    byteFromString = String2Byte_v2.encode(myString)

    print("byteFromString = " , byteFromString)
    print("byteFromString len = " , len(byteFromString) , "\n")
    
    # similarly for decode
    stringAgain = String2Byte_v2.decode(byteFromString)

    print("stringAgain = " , stringAgain)
    print("stringAgain len = " , len(stringAgain) , "\n")

    if(stringAgain == myString):
        print("\nok")
    else:
        print("\nerror")


```

Output - 

``` shell
myString =  hello world
str len =  11 

byteFromString =  b'hello world'
byteFromString len =  11 

stringAgain =  hello world
stringAgain len =  11 


ok
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 4.3 Generator version - Convert any String to byte

``` python
# encode method
ED.String2Byte_v2.encode_yield(string , chunkSize = 1)
```

Arguments - 

* string -> string to convert to bytes.
* chunkSize -> chunk size in MB , generator function yield after encoding every chunk. so decide the chunk size based on your processing power.
* length of encoded byte is same as the length of input string



<br>
<br>

### 4.4 Generator version - Convert above encoded byte back to string

``` python
# decode method
ED.String2Byte_v2.decode_yield(byte , chunkSize = 1)
```

Arguments - 


* byte -> byte which was returned from ED.String2Byte_v2.encode() method to convert it back to string
* chunkSize should be same as used in ED.String2Byte_v2.encode_yield() method

<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_string2bytev2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python
    
    # big object to encode decode 
    myString = "hello world" * 1024 * 1024 * 8

    print("str len = " , len(myString) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = String2Byte_v2.encode_yield(myString)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            byteFromString = ex.value
            break

    print("byteFromString len = " , len(byteFromString) , "\n")
    
    # similarly for decode
    generatorObj_decode = String2Byte_v2.decode_yield(byteFromString)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            stringAgain = ex.value
            break

    print("stringAgain len = " , len(stringAgain) , "\n")

    if(stringAgain == myString):
        print("\nok")
    else:
        print("\nerror")

```

Output - 

``` shell
str len =  92274688 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteFromString len =  92274688 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringAgain len =  92274688 


ok
```


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


# 5. B2S v2 - Convert Byte to String & vice versa

Compression ratio is higher than above byte to string convertor , suitable for large files. even higher than the hexConvertor.

This version two is much faster than the version 1 as it uses in built utf-8 encoding. if your files are compatible with utf-8 use the version 1 of the encoder.

So many bytes object may not be compatible to encode wtih this encoder so its is recommended to use hexConvertor but sometimes you may need that compression to reduce the space required to keep the encoded string.

<br>
<br>

### 5.1 Convert utf-8 compatible Byte to String

``` python
# encode method
ED.Byte2String_v2.encode(byte)
```

Arguments - 

* byte -> byte to convert to string.
* length of encoded string is same as the length of input byte

<br>
<br>

### 5.2 Convert above encoded string back to byte

``` python
# decode method
ED.Byte2String_v2.decode(string)
```

Arguments - 

* string -> string which was returned from ED.Byte2String_v2.encode() method to convert it back to byte

<br>
<br>

Example - 

``` python
    

    # big object to encode decode 
    myByte = b"hello world"

    print("myByte = " , myByte)
    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    stringFromByte = Byte2String_v2.encode(myByte)

    print("stringFromByte = " , stringFromByte)
    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    byteAgain = Byte2String_v2.decode(stringFromByte)

    print("byteAgain = " , byteAgain)
    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
myByte =  b'hello world'
myByte len =  11 

stringFromByte =  hello world
stringFromByte len =  11 

byteAgain =  b'hello world'
byteAgain len =  11 


ok
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 5.3 Generator version - Convert Byte to String

``` python
# encode method
ED.Byte2String_v2.encode_yield(byte , chunkSize = 1)
```

Arguments - 

* byte -> byte to convert to string.
* chunkSize -> chunk size in MB , generator function yield after encoding every chunk. so decide the chunk size based on your processing power.
* length of encoded string is same as the length of input byte



<br>
<br>

### 5.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Byte2String_v2.decode_yield(string , chunkSize = 1)
```

Arguments - 


* string -> string which was returned from ED.Byte2String_v2.encode() method to convert it back to bytes
* chunkSize should be same as used in ED.Byte2String_v2.encode_yield() method

<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_byte2stringv2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python
    
    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 8

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Byte2String_v2.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Byte2String_v2.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
myByte len =  92274688 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  92274688 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  92274688 


ok
```


<br>
<br>
<br>
<br>
<br>
<br>

































  <!-- __    
 / /_   
| '_ \  
| (_) | 
 \___/  
         -->



# 6. Base36Encoder - Convert Byte to String & vice versa


<br>
<br>

### 6.1 Convert any Byte to String

``` python
# encode method
ED.Base36Encoder.encode(byte : bytes , chunkSize : int = 128) -> str:
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in bytes


<br>
<br>

### 6.2 Convert above encoded string back to bytes

``` python
# decode method
ED.Base36Encoder.decode(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base36Encoder.encode() method to convert it back to bytes

<br>
<br>

Example - 

``` python
    
    myByte = b"hello world"

    stringFromByte = Base36Encoder.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base36Encoder.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")

```

Output - 

``` shell
stringFromByte = FUVRSIVVNFRBJWAJO
byte Again = b'hello world'



Time taken = 5.400100053520873e-05
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 6.3 Generator version - Convert any Byte to String 

``` python
# encode method
ED.Base36Encoder.encode_yield(byte : bytes , chunkSize : int = 128) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in bytes



<br>
<br>

### 6.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Base36Encoder.decode_yield(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base36Encoder.encode() method to convert it back to bytes


<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_Base36Encoder2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python

    # big object to encode decode 
    myByte = b"h" * 1024 * 1024

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base36Encoder.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base36Encoder.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")


```

Output - 

``` shell
myByte len =  1048576 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  1630207 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  1048576 


ok



Time taken = 7.930383637998602
```


<br>
<br>
<br>
<br>
<br>
<br>
















































<!-- 
 _____  
|___  | 
   / /  
  / /   
 /_/    
        
 -->



# 7. Base90Encoder - Convert Byte to String & vice versa


<br>
<br>

### 7.1 Convert any Byte to String

``` python
# encode method
ED.Base90Encoder.encode(byte : bytes , chunkSize : int = 128) -> str:
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in bytes


<br>
<br>

### 7.2 Convert above encoded string back to bytes

``` python
# decode method
ED.Base90Encoder.decode(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base90Encoder.encode() method to convert it back to bytes

<br>
<br>

Example - 

``` python

    myByte = b"hello world"

    obj = Base90Encoder()

    stringFromByte = obj.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = obj.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")


```

Output - 

``` shell
stringFromByte = 6*LYov@LOBW<{4
byte Again = b'hello world'



Time taken = 0.15293503299471922
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 7.3 Generator version - Convert any Byte to String 

``` python
# encode method
ED.Base90Encoder.encode_yield(byte : bytes , chunkSize : int = 128) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in bytes



<br>
<br>

### 7.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Base90Encoder.decode_yield(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base90Encoder.encode() method to convert it back to bytes


<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_Base90Encoder2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python

    

    # big object to encode decode 
    myByte = b"h" * 1024 * 1024

    print("myByte len = " , len(myByte) , "\n")

    obj = Base90Encoder()

    # creating the generator obj for the method
    generatorObj_encode = obj.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = obj.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")


```

Output - 

``` shell
myByte len =  1048576 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  1292799 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  1048576 


ok



Time taken = 23.05900487799954
```


<br>
<br>
<br>
<br>
<br>
<br>





















































<!-- 
  ___   
 ( _ )  
 / _ \  
| (_) | 
 \___/  
        
 -->


# 8. Base64_64 - Convert Byte to String & vice versa


<br>
<br>

### 8.1 Convert any Byte to String

``` python
# encode method
ED.Base64_64.encode(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes


<br>
<br>

### 8.2 Convert above encoded string back to bytes

``` python
# decode method
ED.Base64_64.decode(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_64.encode() method to convert it back to bytes

<br>
<br>

Example - 

``` python
    myByte = b"hello world"

    stringFromByte = Base64_64.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_64.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")
```

Output - 

``` shell
stringFromByte = aGVsbG8gd29ybGQ=
byte Again = b'hello world'



Time taken = 4.8089001211337745e-05
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 8.3 Generator version - Convert any Byte to String 

``` python
# encode method
ED.Base64_64.encode_yield(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes



<br>
<br>

### 8.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Base64_64.decode_yield(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_64.encode() method to convert it back to bytes


<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_Base64_64_2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_64.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_64.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
myByte len =  184549376 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  246067004 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  184549376 


ok



Time taken = 31.135886867996305
```


<br>
<br>
<br>
<br>
<br>
<br>








































  <!-- ___   
 / _ \  
| (_) | 
 \__, | 
   /_/  
         -->



# 9. Base64_16 - Convert Byte to String & vice versa


<br>
<br>

### 9.1 Convert any Byte to String

``` python
# encode method
ED.Base64_16.encode(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes


<br>
<br>

### 9.2 Convert above encoded string back to bytes

``` python
# decode method
ED.Base64_16.decode(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_16.encode() method to convert it back to bytes

<br>
<br>

Example - 

``` python
    myByte = b"hello world"

    stringFromByte = Base64_16.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_16.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")
```

Output - 

``` shell
stringFromByte = 68656C6C6F20776F726C64
byte Again = b'hello world'



Time taken = 0.0001499050049460493
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 9.3 Generator version - Convert any Byte to String 

``` python
# encode method
ED.Base64_16.encode_yield(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes



<br>
<br>

### 9.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Base64_16.decode_yield(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_16.encode() method to convert it back to bytes


<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_Base64_16_2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_16.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_16.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
myByte len =  184549376 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  369099452 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  184549376 


ok



Time taken = 41.15198873999907
```


<br>
<br>
<br>
<br>
<br>
<br>

















































<!-- 
 _    ___   
/ |  / _ \  
| | | | | | 
| | | |_| | 
|_|  \___/  
            
 -->


# 10. Base64_32 - Convert Byte to String & vice versa


<br>
<br>

### 10.1 Convert any Byte to String

``` python
# encode method
ED.Base64_32.encode(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes


<br>
<br>

### 10.2 Convert above encoded string back to bytes

``` python
# decode method
ED.Base64_32.decode(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_32.encode() method to convert it back to bytes

<br>
<br>

Example - 

``` python
    myByte = b"hello world"

    stringFromByte = Base64_32.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_32.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")
```

Output - 

``` shell
stringFromByte = NBSWY3DPEB3W64TMMQ======
byte Again = b'hello world'



Time taken = 0.00018349599849898368
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 10.3 Generator version - Convert any Byte to String 

``` python
# encode method
ED.Base64_32.encode_yield(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes



<br>
<br>

### 10.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Base64_32.decode_yield(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_32.encode() method to convert it back to bytes


<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_Base64_32_2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_32.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_32.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
myByte len =  184549376 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  295280828 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  184549376 


ok



Time taken = 95.15050082400558
```


<br>
<br>
<br>
<br>
<br>
<br>























































<!-- 
 _   _  
/ | / | 
| | | | 
| | | | 
|_| |_| 
         -->


# 11. Base64_85 - Convert Byte to String & vice versa


<br>
<br>

### 11.1 Convert any Byte to String

``` python
# encode method
ED.Base64_85.encode(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes


<br>
<br>

### 11.2 Convert above encoded string back to bytes

``` python
# decode method
ED.Base64_85.decode(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_85.encode() method to convert it back to bytes

<br>
<br>

Example - 

``` python
    myByte = b"hello world"

    stringFromByte = Base64_85.encode(myByte)

    print(f"stringFromByte = {stringFromByte}")

    byteAgain = Base64_85.decode(stringFromByte)

    print(f"byte Again = {byteAgain}")
```

Output - 

``` shell
stringFromByte = Xk~0{Zy<MXa%^M
byte Again = b'hello world'



Time taken = 0.0006863300004624762
```

<br>

Note - Both the above method also have a generator function which are helpfull in case you have large objects to encode decode and you want to track progress

<br>
<br>









### 11.3 Generator version - Convert any Byte to String 

``` python
# encode method
ED.Base64_85.encode_yield(byte : bytes , chunkSize : int = 1) -> str
```

Arguments - 

* byte -> any byte you want to convert to string type.
* chunksize in mega bytes



<br>
<br>

### 11.4 Generator version - Convert above encoded string back to byte

``` python
# decode method
ED.Base64_85.decode_yield(string : str) -> bytes
```

Arguments - 

* string -> string which was returned from ED.Base64_85.encode() method to convert it back to bytes


<br>
<br>

both the generator function returns a generator object , see the example to know how to use them. This example is implemented in __test_Base64_85_2() function. visit here to see the full code - https://github.com/harshnative/pySecureCryptos/blob/master/pySecureCryptos/encoderDecoders.py

Example - 

``` python


    # big object to encode decode 
    myByte = b"hello world" * 1024 * 1024 * 16

    print("myByte len = " , len(myByte) , "\n")

    # creating the generator obj for the method
    generatorObj_encode = Base64_85.encode_yield(myByte)

    # looping until generator obj returns
    while(True):
        try:
            # generator obj yield current count - (on) and total count - (total steps)
            currentCount , totalCount = next(generatorObj_encode)

            # sample progress bar
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        # as soon as the generator object returns StopIteration is raised
        # except it as a var and var.value is the thing that generator object returned
        except StopIteration as ex:

            # getting the returned value
            stringFromByte = ex.value
            break

    print("stringFromByte len = " , len(stringFromByte) , "\n")
    
    # similarly for decode
    generatorObj_decode = Base64_85.decode_yield(stringFromByte)

    while(True):
        try:
            currentCount , totalCount = next(generatorObj_decode)
            printProgressBar(currentCount, totalCount, prefix = 'Progress:', suffix = 'Complete', length = 50)

        except StopIteration as ex:
            byteAgain = ex.value
            break

    print("byteAgain len = " , len(byteAgain) , "\n")

    if(myByte == byteAgain):
        print("\nok")
    else:
        print("\nerror")
```

Output - 

``` shell
myByte len =  184549376 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
stringFromByte len =  230687420 

Progress: |██████████████████████████████████████████████████| 100.0% Complete
byteAgain len =  184549376 


ok



Time taken = 105.09517668099579
```


<br>
<br>
<br>
<br>
<br>
<br>