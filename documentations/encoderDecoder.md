
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

1. Convert Byte to String & vice versa
2. Convert String to Byte & vice versa
3. Convert Byte to Hexa Decimal String & vice versa

<br>

Byte to string method can convert any byte to string , and only this string can be converted back to original byte

String to Byte method can convert any string to byte and only this byte can be converted back to original string

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


# 1. Convert Byte to String & vice versa

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


# 2. Convert String to Byte & vice versa

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


# 3. Convert Byte to Hexa Decimal string and vice versa

Compression ratio is higher than above byte to string convertor , suitable for large files.

<br>
<br>

### 3.1 Convert any Byte to String  

``` python
# encode method
ED.HexConvertor.encode(byte)
```

Arguments - 

* byte -> any byte you want to convert to string type. returns hexa decimal version of string



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
<br>
<br>
<br>
<br>
<br>
<br>
<br>

