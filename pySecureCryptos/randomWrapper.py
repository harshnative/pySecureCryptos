from typing import Union
import random
import string
import time
import secrets
from .encoderDecoders import *
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import math
import numpy





#  ____                        _                       ____    _            _                  
# |  _ \    __ _   _ __     __| |   ___    _ __ ___   / ___|  | |_   _ __  (_)  _ __     __ _  
# | |_) |  / _` | | '_ \   / _` |  / _ \  | '_ ` _ \  \___ \  | __| | '__| | | | '_ \   / _` | 
# |  _ <  | (_| | | | | | | (_| | | (_) | | | | | | |  ___) | | |_  | |    | | | | | | | (_| | 
# |_| \_\  \__,_| |_| |_|  \__,_|  \___/  |_| |_| |_| |____/   \__| |_|    |_| |_| |_|  \__, | 
#                                                                                       |___/  



# class to generate a random string
class RandomString:

    # method to generate a pseduo random string
    # not secure for passwords
    # size = size of the string required
    # seed = seed you want to set in random.seed() func , if None is passed , it will use the system time as seed
    @classmethod
    def generate(cls , size : int , seed : str = None , lowerCase : bool = True , upperCase : bool = True , nums : bool = True , specialChars : bool = True , space : bool = False) -> str:

        if(type(size) != int):
            raise TypeError("size parameter expected to be of int type instead got {} type".format(type(size)))

        if(seed == None):
            seed = str(time.time())

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

        charList = []

        if(lowerCase):
            charList.extend(list(string.ascii_lowercase))
        
        if(upperCase):
            charList.extend(list(string.ascii_uppercase))
        
        if(nums):
            charList.extend(list(string.digits))

        if(specialChars):
            charList.extend(list("~`!@#$%^&*()_+-=|[]\:<>?;,./"))
        
        if(space):
            charList.append(" ")


        # set seed and generate random string
        random.seed(seed)

        randomList = random.choices(charList , k=size)

        randomString = "".join(randomList)

        return randomString












    
    # method to generate a string from the secrets module which claims to be secure
    @classmethod
    def generate_secrets(cls , size : int , lowerCase : bool = True , upperCase : bool = True , nums : bool = True , specialChars : bool = True , space : bool = False) -> str:

        if(type(size) != int):
            raise TypeError("size parameter expected to be of int type instead got {} type".format(type(size)))

        charList = []

        if(lowerCase):
            charList.extend(list(string.ascii_lowercase))
        
        if(upperCase):
            charList.extend(list(string.ascii_uppercase))
        
        if(nums):
            charList.extend(list(string.digits))

        if(specialChars):
            charList.extend(list("~`!@#$%^&*()_+-=|[]\:<>?;,./"))
        
        if(space):
            charList.append(" ")
        
        randomString = ""

        for _ in range(size):
            randomString = randomString + secrets.choice(charList)

        return randomString






















#  _____                         ____                        _                                                                       
# |_   _|  _ __   _   _    ___  |  _ \    __ _   _ __     __| |   ___    _ __ ___            _ __ ___     ___    _   _   ___    ___  
#   | |   | '__| | | | |  / _ \ | |_) |  / _` | | '_ \   / _` |  / _ \  | '_ ` _ \          | '_ ` _ \   / _ \  | | | | / __|  / _ \ 
#   | |   | |    | |_| | |  __/ |  _ <  | (_| | | | | | | (_| | | (_) | | | | | | |         | | | | | | | (_) | | |_| | \__ \ |  __/ 
#   |_|   |_|     \__,_|  \___| |_| \_\  \__,_| |_| |_|  \__,_|  \___/  |_| |_| |_|  _____  |_| |_| |_|  \___/   \__,_| |___/  \___| 
#                                                                                   |_____|                                          



# class to get a true random number from the mouse movements
class TrueRandom_mouse:


    # size = number of mouse movements collected till the progress bar fills
    # higher the size , more numbers can be generated at a time
    # single = number of points from mouse movement collection used to generate a new number
    # higher the single , more randomness it has
    def __init__(self ,  size : int = 10000 , single : int = 100):
        if(type(size) != int):
            raise TypeError(f"size parameter expected to be of {int} type instead got {type(size)} type")

        if(type(single) != int):
            raise TypeError(f"single parameter expected to be of {int} type instead got {type(single)} type")


        self.size = size
        self.single = single
        self.storageList = []














    # method to open a tkinter window to collect the mouse movements inside it
    def setSeed(self , window_title : str = "Move your mouse" , window_height : int = 600 , window_width : int = 800 , window_bg : str = "#121212" , progress_bar_margin : int = 50 , progress_bar_through_color : str = "#FFFFFF" , progress_bar_bar_color : str = "#3700B3" , progress_bar_thickness : int = 32 , button_font_size : int = 32 , button_font_weight : str = 'bold' , button_bg : str = '#BB86FC' , button_activebackground : str = '#03DAC6' , button_fg : str = "#FFFFFF" , button_text : str = "ok") -> None:
        self.storageList = []

        # setting up window
        ws = tk.Tk()
        ws.title(f'{window_title}')
        ws.geometry(f'{window_width}x{window_height}')
        ws.configure(bg=window_bg)

        # setting up progress bar style
        s = ttk.Style()
        s.configure("styler.Horizontal.TProgressbar", troughcolor=progress_bar_through_color, bordercolor=progress_bar_through_color, background=progress_bar_bar_color, lightcolor=progress_bar_bar_color , darkcolor=progress_bar_bar_color , thickness=progress_bar_thickness)

        # setting up progress bar
        pb1 = ttk.Progressbar(ws, orient=tk.HORIZONTAL, length = window_width - progress_bar_margin , mode='determinate' , style="styler.Horizontal.TProgressbar")
        pb1.pack(expand=True)

        # setting up font for button
        myFont = tkFont.Font(size=button_font_size , weight=button_font_weight)
        
        # setting up button
        button = tk.Button(ws , text=button_text , command=ws.destroy , bg=button_bg , activebackground=button_activebackground , fg = button_fg)
        button['font'] = myFont
        button.pack()

        
        # function to capture the mouse coordinates and add to storage list
        def motion(event):
            x, y = event.x, event.y
            ws.update_idletasks()
            pb1['value'] = (len(self.storageList) / self.size) * 100
            self.storageList.append((x,y))

        # bind window to motion detector 
        ws.bind('<Motion>', motion)
        ws.mainloop()

    










    # function to get random integers
    # returns a list of integers possible from sample collected in pool size
    # a is the lower limit of number
    # b is the upper limit of number
    def getRandomNumbers_int(self , a : int , b : int) -> list:

        if(type(a) != int):
            raise TypeError(f"a parameter expected to be of {int} type instead got {type(a)} type")

        if(type(b) != int):
            raise TypeError(f"b parameter expected to be of {int} type instead got {type(b)} type")


        numbersList = []

        storageList_len = len(self.storageList)

        # sub sample from storage list
        middle_storageList = self.storageList[self.single : storageList_len - self.single]
        
        middle_storageList_len = len(middle_storageList)

        # iterate over sub sampled list in chunks of size = single
        # then multiply all coordinates in the chunk to get the final number
        for i in range(0 , middle_storageList_len , self.single):
            currentChunk = middle_storageList[i : i + self.single]

            finalNumber = 1
            for j in currentChunk:
                finalNumber = finalNumber * (j[0] + 1) * (j[1] + 1)
            
            # scale down the number and add to list
            numbersList.append(math.log2(finalNumber))

        
        # convert the random numbers into range required 
        for i in range(len(numbersList)):
            newNum = round(numbersList[i] % b)

            if(newNum + a < b):
                newNum = newNum + a

            numbersList[i] = newNum        


        # return the numbers
        return numbersList    









    # function to get random floats from 0 to 1
    # returns a list of floats possible from sample collected in pool size
    def getRandomNumbers_float(self) -> list:
        
        numbersList = []

        storageList_len = len(self.storageList)

        # sub sample from storage list
        middle_storageList = self.storageList[self.single : storageList_len - self.single]
        
        middle_storageList_len = len(middle_storageList)

        # iterate over sub sampled list in chunks of size = single
        # then multiply all coordinates in the chunk to get the final number
        for i in range(0 , middle_storageList_len , self.single):
            currentChunk = middle_storageList[i : i + self.single]

            finalNumber = 1
            for j in currentChunk:
                finalNumber = finalNumber * (j[0] + 1) * (j[1] + 1)
            
            # scale down the number and add to list
            numbersList.append(math.log2(finalNumber))

        # calculate mean of numbers
        mean = numpy.mean(numbersList)

        # calculate standard deviation of numbers
        sd = numpy.std(numbersList)

        scaled_numbersList = []

        for i in numbersList:
            # normalize numbers using z score normalization
            scaled = abs(i - mean) / sd

            # only keep value if greator less than equal to 1
            if(scaled <= 1):
                scaled_numbersList.append(scaled)

        return scaled_numbersList
    




    # function to make a choice from a iterable 
    # returns a list of choosen iterable of size = size
    # if the size is greator than max possible choices from sample pool , then error will be raised
    # but if raise error is false then error will not be raised instead list of max possible size will be returned
    def make_choices(self , iterable : Union[tuple , list] , size : int , raiseError : bool = True) -> list:

        if(type(iterable) not in [tuple , list]):
            raise TypeError(f"b iterable expected to be of {[tuple , list]} type instead got {type(iterable)} type")


        if(type(size) != int):
            raise TypeError(f"size parameter expected to be of {int} type instead got {type(size)} type")


        if(type(raiseError) != bool):
            raise TypeError(f"raiseError parameter expected to be of {bool} type instead got {type(raiseError)} type")


        len_iterable = len(iterable)

        newIterable = []

        # get random ints in the range of list length
        randomInts = self.getRandomNumbers_int(0 , len_iterable - 1)

        len_randomInts = len(randomInts)

        # if the size is in limit of pool size
        if(size <= len_randomInts):

            # get the corresponding elements from iterable according to index in random index list
            for i in range(size):
                newIterable.append(iterable[randomInts[i]])

        elif(raiseError):
            raise RuntimeError(f"Size requested could not be made form seed collected , max size which can be returned = {len_randomInts}")

        else:
            for i in randomInts:
                newIterable.append(iterable[i])

        return newIterable






    # function to return a random string
    def getRandomString(self , size : int , lowerCase : bool = True , upperCase : bool = True , nums : bool = True , specialChars : bool = True , space : bool = False , raiseError : bool = True) -> str:

        if(type(size) != int):
            raise TypeError(f"size parameter expected to be of {int} type instead got {type(size)} type")

        if(type(raiseError) != bool):
            raise TypeError(f"raiseError parameter expected to be of {bool} type instead got {type(raiseError)} type")

        charList = []

        if(lowerCase):
            charList.extend(list(string.ascii_lowercase))
        
        if(upperCase):
            charList.extend(list(string.ascii_uppercase))
        
        if(nums):
            charList.extend(list(string.digits))

        if(specialChars):
            charList.extend(list("~`!@#$%^&*()_+-=|[]\:<>?;,./"))
        
        if(space):
            charList.append(" ")

        random_string_list = self.make_choices(charList , size , raiseError)

        randomString = "".join(random_string_list)

        return randomString



        



















#  _                  _                       ____                        _                       ____    _            _                  
# | |_    ___   ___  | |_                    |  _ \    __ _   _ __     __| |   ___    _ __ ___   / ___|  | |_   _ __  (_)  _ __     __ _  
# | __|  / _ \ / __| | __|       _____       | |_) |  / _` | | '_ \   / _` |  / _ \  | '_ ` _ \  \___ \  | __| | '__| | | | '_ \   / _` | 
# | |_  |  __/ \__ \ | |_       |_____|      |  _ <  | (_| | | | | | | (_| | | (_) | | | | | | |  ___) | | |_  | |    | | | | | | | (_| | 
#  \__|  \___| |___/  \__|                   |_| \_\  \__,_| |_| |_|  \__,_|  \___/  |_| |_| |_| |____/   \__| |_|    |_| |_| |_|  \__, | 
#                                                                                                                                  |___/  

# method to test the RandomString_generate method
def __test_randomString():

    randomString = RandomString.generate(12)
    randomString2 = RandomString.generate(12 , seed = "hello")

    print(f"randomString = {randomString}")
    print(f"randomString2 = {randomString2}")












# method to test the RandomString_generate_secrets method
def __test_randomString2():

    randomString = RandomString.generate_secrets(32)

    print(f"randomString = {randomString}")
















#  _                  _                       _____                         ____                        _                                                                       
# | |_    ___   ___  | |_                    |_   _|  _ __   _   _    ___  |  _ \    __ _   _ __     __| |   ___    _ __ ___            _ __ ___     ___    _   _   ___    ___  
# | __|  / _ \ / __| | __|       _____         | |   | '__| | | | |  / _ \ | |_) |  / _` | | '_ \   / _` |  / _ \  | '_ ` _ \          | '_ ` _ \   / _ \  | | | | / __|  / _ \ 
# | |_  |  __/ \__ \ | |_       |_____|        | |   | |    | |_| | |  __/ |  _ <  | (_| | | | | | | (_| | | (_) | | | | | | |         | | | | | | | (_) | | |_| | \__ \ |  __/ 
#  \__|  \___| |___/  \__|                     |_|   |_|     \__,_|  \___| |_| \_\  \__,_| |_| |_|  \__,_|  \___/  |_| |_| |_|  _____  |_| |_| |_|  \___/   \__,_| |___/  \___| 
#                                                                                                                              |_____|                                          


def __test__TrueRandom_mouse_getRandomNumbers_int():

    obj = TrueRandom_mouse()

    obj.setSeed()

    rand_int = obj.getRandomNumbers_int(0 , 1000)

    print(len(rand_int))




    import matplotlib.pyplot as plt

    plt.scatter(range(len(rand_int)), rand_int, c ="black")
  
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()








def __test__TrueRandom_mouse_getRandomNumbers_float():

    obj = TrueRandom_mouse()

    obj.setSeed()

    rand_floats = obj.getRandomNumbers_float()

    print(len(rand_floats))

    print(rand_floats)


    import matplotlib.pyplot as plt

    plt.scatter(range(len(rand_floats)), rand_floats, c ="black")
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()












def __test__TrueRandom_mouse_make_choices():

    obj = TrueRandom_mouse()

    obj.setSeed()

    myList = [1,2,3,4,5,6,7,8,9,0]

    choiceList = obj.make_choices(myList , 8 , raiseError=False)

    print(len(choiceList))

    print(choiceList)


    import matplotlib.pyplot as plt

    plt.scatter(range(len(myList)), myList, c ="black")
    plt.scatter(range(len(choiceList)), choiceList, c ="red")
    
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()











def __test__TrueRandom_mouse_getRandomString():

    obj = TrueRandom_mouse()

    obj.setSeed()

    randomString = obj.getRandomString(16 , raiseError=False)

    print(len(randomString))

    print(randomString)









if __name__ == "__main__":
    __test__TrueRandom_mouse_getRandomString()