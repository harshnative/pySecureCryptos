
# password Checker

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
from pySecureCryptos.passwordChecker import Check as checkPassword
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

1. check if password qualifies for low level security
2. check if password qualifies for medium level security
3. check if password qualifies for high level security
4. check if password qualifies for max level security
5. check if password qualifies for your own level security


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


# 1. Low security

<br>
<br>

``` python

checkPassword.check_low(password : str , exclude_subStrings : list = None)
```

Arguments - 

* password -> pass your password here to check
* exclude_subStrings -> list of substrings you do want in the password like username itself , birthdate itself etc as they are really unsecure passwords

<br>
<br>

* default parameters are designed in way to ensure a low level security application password.
* defaults are
    * minLen=8
    * lowerChars=True
    * upperChars=False
    * nums=True
    * specialChars=False
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should not contain '{subString}' in it" 
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

















<!-- 
 ____   
|___ \  
  __) | 
 / __/  
|_____| 
         -->


# 2. Medium security

<br>
<br>

``` python

checkPassword.check_medium(password : str , exclude_subStrings : list = None)
```

Arguments - 

* password -> pass your password here to check
* exclude_subStrings -> list of substrings you do want in the password like username itself , birthdate itself etc as they are really unsecure passwords

<br>
<br>

* default parameters are designed in way to ensure a medium level security application password.
* defaults are
    * minLen=12
    * lowerChars=True
    * upperChars=True
    * nums=True
    * specialChars=False
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should not contain '{subString}' in it" 
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




















<!-- 
 _____  
|___ /  
  |_ \  
 ___) | 
|____/  
         -->


# 3. High security

<br>
<br>

``` python

checkPassword.check_high(password : str , exclude_subStrings : list = None)
```

Arguments - 

* password -> pass your password here to check
* exclude_subStrings -> list of substrings you do want in the password like username itself , birthdate itself etc as they are really unsecure passwords

<br>
<br>

* default parameters are designed in way to ensure a high level security application password.
* defaults are
    * minLen=12
    * lowerChars=True
    * upperChars=True
    * nums=True
    * specialChars=True
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should not contain '{subString}' in it" 
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

















<!-- 
 _  _    
| || |   
| || |_  
|__   _| 
   |_|   
          -->


# 4. Max security

<br>
<br>

``` python

checkPassword.check_max(password : str , exclude_subStrings : list = None)
```

Arguments - 

* password -> pass your password here to check
* exclude_subStrings -> list of substrings you do want in the password like username itself , birthdate itself etc as they are really unsecure passwords

<br>
<br>

* default parameters are designed in way to ensure a max level security application password.
* defaults are
    * minLen=20
    * lowerChars=True
    * upperChars=True
    * nums=True
    * specialChars=True
* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should not contain '{subString}' in it" 
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



























<!-- 
 ____   
| ___|  
|___ \  
 ___) | 
|____/  
         -->


# 5. custom security

<br>
<br>

``` python

checkPassword.check_pass(password : str , exclude_subStrings : list = None , minLen : int = 10 , lowerChars : bool = True , upperChars : bool = False , nums : bool = True , specialChars : bool = False) -> Union[None , list]
```

Arguments - 

* password -> pass your password here to check
* exclude_subStrings -> list of substrings you do want in the password like username itself , birthdate itself etc as they are really unsecure passwords
* minLen -> minimum length password should be
* lowerChars -> if lower case char should be present in password
* upperChars -> if upper case char should be present in password
* nums -> if numbers should be present in password
* specialChars -> if special chars [ !@#$%^&*()_-+=~`{[}]|:;"'<,>.?/ ] should be present in password

<br>
<br>

* returns None if the password qualifies
* return error list containing string listing the errors in password in english langauge

```python
errorList = [
    f"password should not contain '{subString}' in it" 
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


























 <!-- _     _                
| |_  (_)  _ __    ___  
| __| | | | '_ \  / __| 
| |_  | | | |_) | \__ \ 
 \__| |_| | .__/  |___/ 
          |_|            -->



# General Tips 

1. For sensitive applications , make sure your password at least qualifies for high level but max level is recommended.

2. Password should contain all mix of chars from lower , upper , nums and even some special chars.

3. Do not use simple password which are easy to remember as they can be easily cracked by dictionary attack

4. Do not use password related to your daily workflow and about your life as they are easily guessable.



<br>
<br>
<br>

<br>
<br>
<br>


