# random Wrapper

Wrapper containing different methods related to random number generations
, even has a true random number generator from the mouse movements.




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
from pySecureCryptos import randomWrapper as RW 
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

1. Random string generator
2. True random generator form mouse movements


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

# 1. Random string generator

<br>
<br>


### 1.1 Generate a pseudo random string

``` python
RW.RandomString.generate(size : int , seed : str = None , lowerCase : bool = True , upperCase : bool = True , nums : bool = True , specialChars : bool = True , space : bool = False)
```

Arguments - 
* size - how long you want random string to be
* seed - specific need you need to set in random.seed() function , if None is passed then it will use default seed that is system time.
* lowerCase - you want string to contains char [ a - z ]
* upperCase - you want string to contains char [ A - Z ]
* nums - you want string to contains char [ 1 - 9 ]
* specialChars - you want string to contains char [ "~`!@#$%^&*()_+-=|[]\:<>?;,./" ]
* space - you want string to contain a space 
* returns a pseduo random string of length = size

<br>
<br>
<br>
<br>





### 1.2 Generate a true random string

``` python
RW.RandomString.generate_secrets(size : int , lowerCase : bool = True , upperCase : bool = True , nums : bool = True , specialChars : bool = True , space : bool = False)
```

Arguments - 
* size - how long you want random string to be
* lowerCase - you want string to contains char [ a - z ]
* upperCase - you want string to contains char [ A - Z ]
* nums - you want string to contains char [ 1 - 9 ]
* specialChars - you want string to contains char [ "~`!@#$%^&*()_+-=|[]\:<>?;,./" ]
* space - you want string to contain a space 
* uses secrets.choice() method to generate a string
* returns a true random string of length = size

<br>
<br>





<br>
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


# 2. True random generator form mouse movements

<br>

## Setup

You need to make a object from the class TrueRandom_mouse

```python
obj = RW.TrueRandom_mouse(size : int = 10000 , single : int = 100)
```

<br>
<br>

Arguments - 

* size - number of mouse movements collected till the progress bar fills , higher the size , more numbers can be generated at a time.
* single - number of mouse movements used to generate a single number , higher the single , more randomness it has.

<br>
<br>

Then you need to set seed by invoking method below. It will open a tkinter window were the user needs to resolve mouse over as randomly as possible , till the progress bar fills.



```python
obj.setSeed(window_title : str = "Move your mouse" , window_height : int = 600 , window_width : int = 800 , window_bg : str = "#121212" , progress_bar_margin : int = 50 , progress_bar_through_color : str = "#FFFFFF" , progress_bar_bar_color : str = "#3700B3" , progress_bar_thickness : int = 32 , button_font_size : int = 32 , button_font_weight : str = 'bold' , button_bg : str = '#BB86FC' , button_activebackground : str = '#03DAC6' , button_fg : str = "#FFFFFF" , button_text : str = "ok")
```

provides a default tkinter gui to collect mouse movements like this

<img src="https://www.letscodeofficial.com/media/imageSharer/Screenshot_from_2022-02-02_16-21-21.png" caption = "pySecureCryptos randomWrapper TrueRandom_mouse default tkinter gui"></img>

<br>
<br>

Arguments - 

* window_title - title of the tkinter window
* window_height - heigth of the window in pixels like 600
* window_width - width of the window in pixels like 800
<br>

Tip - increase the heigth and width to increase the randomness
<br>

* window_bg - hex code of windows background color in string format
* progress_bar_margin - margin of progress from side of window in pixels
* progress_bar_through_color - progress bar background color
* progress_bar_bar_color - progress bar foreground color
* progress_bar_thickness - progress bar thickness in pixel
* button_font_size - size of font inside the button at bottom in pixels
* button_font_weight - font weigth of button
* button_bg - hex code of buttons background color in string format
* button_activebackground - hex code of buttons background color in string format when the button is pressed
* button_fg - hex code of buttons text color in string format
* button_text - text you want to display in button




<br>
<br>



## 2.1 Get some random integers 

``` python
obj.getRandomNumbers_int(a : int , b : int)
```

* a - lower limit of integer to produce
* b - upper limit of integer to produce
* returns a list of random integers possible from the sample collected , you can use these one at a time also if want.

<br>
<br>




## 2.2 Get some random floats 

``` python
obj.getRandomNumbers_float()
```

* returns a list of random floats btw 0 and 1 possible from the sample collected , you can use these one at a time also if want.

<br>
<br>





## 2.3 Choice some elements from a iterable like list

``` python
obj.make_choices(iterable : Union[tuple , list] , size : int , raiseError : bool = True)
```

* iterable - any iterable objects like list or tuple from were you want to choose the elements
* size - number of elements you need to choose from iterable , can also be greator than the length of list
* raiseError - if the size required is greator than the sample pool collected during set seed, then if raiseError is True a RunTimeError will be raised , else a function will make choices till the sample pool finishes out.

if you still want to make choices = size , then collect more sample mouse movements.

<br>
<br>





## 2.4 generate a random string

``` python
obj.getRandomString(size : int , lowerCase : bool = True , upperCase : bool = True , nums : bool = True , specialChars : bool = True , space : bool = False , raiseError : bool = True)
```

* size - how long you want random string to be
* lowerCase - you want string to contains char [ a - z ]
* upperCase - you want string to contains char [ A - Z ]
* nums - you want string to contains char [ 1 - 9 ]
* specialChars - you want string to contains char [ "~`!@#$%^&*()_+-=|[]\:<>?;,./" ]
* space - you want string to contain a space 
* raiseError - if the size required is greator than the sample pool collected during set seed, then if raiseError is True a RunTimeError will be raised , else a function will make string till the sample pool finishes out.

if you still want to make string of exact size , then collect more sample mouse movements.

<br>
<br>



#### NOTE : TrueRandom_mouse class methods , all generate random things from mouse sample collected during setSeed() using maths derivations. So if you want random integers list , you can derive random floats for even random string. So it is recommended to only use one method at a time and generate a new object after that with new mouse movements.




