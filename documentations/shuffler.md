
# Shuffler

<br>
<br>
<br>

# Importing - 

``` python
from pySecureCryptos.shuffler import Shuffler
```

<br>
<br>

# Methods - 
1. Shuffle a list and UnShuffle a list
2. Shuffle a string and UnShuffle a string

<br>
<br>

# 1. Shuffle and UnShuffle a list

<br>
<br>

1. Shuffle list  

``` python
# shuffle method
Shuffler.shuffe_list(ls, seed , copyList = True)
```

Arguments - 

* ls -> list to shuffle
* seed -> list is shuffled using this seed. seed is set into random.seed() before performing random.shuffle(). String type seed is recommended.
* copyList -> ls passed is copied using deepcopy to prevent the original list from been directly shuffled. Default i.e True Value is recommended.

<br>
<br>

2. UnShuffle list 

``` python
# deshuffle method
Shuffler.unShuffle_list(shuffled_ls, seed)
```

Arguments - 

* shuffled_ls -> list to unshuffle , output of shuffe_list() method
* seed -> same as used in shuffe_list() method

<br>
<br>

Example - 

``` python
    myList = [1,7,2,4,6,9]
    seed = "hello"
    print("list = {} , seed = {}".format(myList , seed))

    shuffledList = Shuffler.shuffe_list(myList , seed , copyList = True)

    print("shuffledList = {}".format(shuffledList))

    deShuffledList = Shuffler.unShuffle_list(shuffledList , seed)

    print("deShuffledList = {}".format(deShuffledList))

    if(myList == deShuffledList):
        print("ok")
    else:
        print("error")
```

Output - 

``` shell
list = [1, 7, 2, 4, 6, 9] , seed = hello
shuffledList = [9, 7, 4, 1, 6, 2]
deShuffledList = [1, 7, 2, 4, 6, 9]
ok
```


<br>
<br>

# 2. Shuffle and UnShuffle a string

<br>
<br>

1. Shuffle list  

``` python
# shuffle method
Shuffler.shuffle_string(string , seed)
```

Arguments - 

* string -> string to shuffle
* seed -> string is shuffled using this seed. seed is set into random.seed() before performing random.shuffle(). String type seed is recommended.

<br>
<br>

2. UnShuffle list 

``` python
# deshuffle method
Shuffler.unShuffle_string(shuffledString , seed)
```

Arguments - 

* shuffledString -> string to unshuffle , output of shuffle_string() method
* seed -> same as used in shuffle_string() method

<br>
<br>

Example - 

``` python
    myString = "hello world"
    seed = "hello"
    print("string = {} , seed = {}".format(myString , seed))

    shuffledString = Shuffler.shuffle_string(myString , seed)

    print("shuffledString = {}".format(shuffledString))

    deShuffledString = Shuffler.unShuffle_string(shuffledString , seed)

    print("deShuffledString = {}".format(deShuffledString))

    if(myString == deShuffledString):
        print("ok")
    else:
        print("error")
```

Output - 

``` shell
string = hello world , seed = hello
shuffledString = lodlwholer 
deShuffledString = hello world
ok
```


<br>
<br>
