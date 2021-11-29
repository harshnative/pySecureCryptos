
# password Checker

<br>
<br>
<br>

# Importing - 

``` python
from pySecureCryptos.passwordChecker import Check as checkPassword
```

<br>
<br>
<br>
<br>
<br>

# Methods - 

1. check if password qualifies for low level security
2. check if password qualifies for medium level security
3. check if password qualifies for high level security
4. check if password qualifies for max level security


<br>
<br>
<br>
<br>
<br>
<br>

# 1. Low security

<br>
<br>

``` python

checkPassword.check_low(password , minLen = 10 , lowerChars = True , upperChars = False , nums = True , specialChars = False)
```

Arguments - 

* password -> pass your password here to check

<br>
<br>

* default parameters are designed in way to ensure a low level security application password , still you can tweak it to your own desire
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should be at least of {minLen} chars" , 
    "at least one lower case letter is required in password [a-z]" ,
    "at least one upper case letter is required in password [A-Z]" ,
    "at least one number is required in password [0-9]" , 
    "at least one special character is required in password like !@#$%& etc"
]
```


<br>
<br>

Example - 

``` python
    myPassword = "hello world12"

    print(Check.check_low(myPassword))

    myPassword = "hello wor"

    print(Check.check_low(myPassword))
```

Output - 

``` shell
None
['password should be at least of 10 chars', 'at least one number is required in password [0-9]']
```


<br>
<br>
<br>


# 2. Medium security

<br>
<br>

``` python

checkPassword.check_medium(password , minLen = 12 , lowerChars = True , upperChars = True , nums = True , specialChars = False)
```

Arguments - 

* password -> pass your password here to check

<br>
<br>

* default parameters are designed in way to ensure a medium level security application password , still you can tweak it to your own desire
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should be at least of {minLen} chars" , 
    "at least one lower case letter is required in password [a-z]" ,
    "at least one upper case letter is required in password [A-Z]" ,
    "at least one number is required in password [0-9]" , 
    "at least one special character is required in password like !@#$%& etc"
]
```


<br>
<br>

Example - 

``` python
    myPassword = "hello world12W"

    print(Check.check_medium(myPassword))

    myPassword = "hello wor"

    print(Check.check_medium(myPassword))
```

Output - 

``` shell
None
['password should be at least of 12 chars', 'at least one upper case letter is required in password [A-Z]', 'at least one number is required in password [0-9]']
```


<br>
<br>
<br>


# 3. High security

<br>
<br>

``` python
checkPassword.check_high(password , minLen = 15 , lowerChars = True , upperChars = True , nums = True , specialChars = True)
```

Arguments - 

* password -> pass your password here to check

<br>
<br>

* default parameters are designed in way to ensure a high level security application password , still you can tweak it to your own desire
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should be at least of {minLen} chars" , 
    "at least one lower case letter is required in password [a-z]" ,
    "at least one upper case letter is required in password [A-Z]" ,
    "at least one number is required in password [0-9]" , 
    "at least one special character is required in password like !@#$%& etc"
]
```


<br>
<br>

Example - 

``` python
    myPassword = "hello world12W#"

    print(Check.check_high(myPassword))

    myPassword = "hello wor"

    print(Check.check_high(myPassword))
```

Output - 

``` shell
None
['password should be at least of 15 chars', 'at least one upper case letter is required in password [A-Z]', 'at least one number is required in password [0-9]', 'at least one special character is required in password like !@#$%& etc']
```


<br>
<br>
<br>

# 4. Max security

<br>
<br>

``` python
checkPassword.check_max(password , minLen = 20 , lowerChars = True , upperChars = True , nums = True , specialChars = True)
```

Arguments - 

* password -> pass your password here to check

<br>
<br>

* default parameters are designed in way to ensure a max level security application password , still you can tweak it to your own desire
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should be at least of {minLen} chars" , 
    "at least one lower case letter is required in password [a-z]" ,
    "at least one upper case letter is required in password [A-Z]" ,
    "at least one number is required in password [0-9]" , 
    "at least one special character is required in password like !@#$%& etc"
]
```


<br>
<br>

Example - 

``` python
    myPassword = "Th!s P@sssword 1s Ve#y Compl$x"

    print(Check.check_max(myPassword))

    myPassword = "hello wor"

    print(Check.check_max(myPassword))
```

Output - 

``` shell
None
['password should be at least of 20 chars', 'at least one upper case letter is required in password [A-Z]', 'at least one number is required in password [0-9]', 'at least one special character is required in password like !@#$%& etc']
```


<br>
<br>
<br>

<br>
<br>
<br>

