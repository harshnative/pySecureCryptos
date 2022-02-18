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
from .hashers_v2 import *
import pathlib
import bisect


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



    # function to get random bytes
    # if raise error is true than run time error will be raised if size required cannot be acheived by the sample pool
    def getRandomBytes(self , size : int , raiseError : bool = True) -> str:

        # get random ints in the range of list length
        randomInts = self.getRandomNumbers_int(0 , 256)

        len_randomInts = len(randomInts)

        # if the size is in limit of pool size
        if(size <= len_randomInts):
            return bytes(randomInts[:size])

        elif(raiseError):
            raise RuntimeError(f"Size requested could not be made form seed collected , max size which can be returned = {len_randomInts}")

        else:
            return bytes(randomInts)





























#  ____                        _                       ___   ____   
# |  _ \    __ _   _ __     __| |   ___    _ __ ___   |_ _| |  _ \  
# | |_) |  / _` | | '_ \   / _` |  / _ \  | '_ ` _ \   | |  | | | | 
# |  _ <  | (_| | | | | | | (_| | | (_) | | | | | | |  | |  | |_| | 
# |_| \_\  \__,_| |_| |_|  \__,_|  \___/  |_| |_| |_| |___| |____/  
                                                                  



# class to generate a non repeating random string id
class RandomID:

    # len_bytes = length of random bytes to be used as salt
    # prefix = string to add to id start
    # sufix = string to add to id end
    # adder = prefix + adder + id + adder + sufix
    # md5 - 32
    # sha1 - 40
    # sha224 - 56
    # sha256 - 64
    # sha384 - 96
    # sha512 - 128
    def __init__(self , len_bytes = 32 , prefix = "" , suffix = ""):

        # assign to self
        self.len_bytes = len_bytes
        self.prefix = prefix
        self.sufix = suffix


        # current time in bytes
        currentTime = String2Byte_v2.encode(str(time.time()))

        # random bytes
        randomBytes = secrets.token_bytes(self.len_bytes)

        # final bytes
        self.finalBytes = currentTime + randomBytes



    # method to return a md5 hashed id
    def md5(self) -> str:

        genObj = MD5(self.finalBytes).get_string_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                return self.prefix + ex.value + self.sufix
                



    # method to return a sha1 hashed id
    def sha1(self) -> str:

        genObj = SHA1(self.finalBytes).get_string_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                return self.prefix + ex.value + self.sufix
                
                


    # method to return a sha224 hashed id
    def sha224(self) -> str:

        genObj = SHA224(self.finalBytes).get_string_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                return self.prefix + ex.value + self.sufix
                
                


    # method to return a sha256 hashed id
    def sha256(self) -> str:

        genObj = SHA256(self.finalBytes).get_string_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                return self.prefix + ex.value + self.sufix
                
                


    # method to return a sha384 hashed id
    def sha384(self) -> str:

        genObj = SHA384(self.finalBytes).get_string_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                return self.prefix + ex.value + self.sufix
                
                


    # method to return a sha512 hashed id
    def sha512(self) -> str:

        genObj = SHA512(self.finalBytes).get_string_yield()

        while(True):
            try:
                next(genObj)
            except StopIteration as ex:
                return self.prefix + ex.value + self.sufix
                
        

































#   ___    _____   ____   
#  / _ \  |_   _| |  _ \  
# | | | |   | |   | |_) | 
# | |_| |   | |   |  __/  
#  \___/    |_|   |_|     
                        


class OTP:

    # size in digits like 6 or 4 digit otp
    # timeout in secs
    # filePath = path were otp file will be stored
    # fileName = name of file you want to store otp in
    # if fileName is None , a random name will be assigned , you can get filePath using .fileName attribute
    def __init__(self , size = 6 , timeout = 180 , filePath = "./" , fileName = None , oneTime = True):
        self.timeout = timeout
        
        path = pathlib.Path(filePath)

        if(not(path.is_dir())):
            raise FileNotFoundError(f"no dir at {path}")

        if(fileName == None):
            fileName = RandomID(prefix="OTP_file_" , suffix=".txt").md5()

        self.fileName = pathlib.Path(filePath , fileName)

        self.digits = [str(i) for i in range(10)]
        self.size = size
        self.expireTime = int(time.time())
        self.oneTime = oneTime



    # function to generate a otp
    def generateOTP(self):
        otp = ""

        for i in range(self.size):
            otp = otp + secrets.choice(self.digits)

        self.expireTime = int(time.time()) + self.timeout

        with open(self.fileName , "w") as file:
            file.write(f"{otp},{self.expireTime}")

        return int(otp)




    # get otp
    # returns None if OTP is not generated , or is expired
    # else returns OTP
    def getOTP(self):

        try:
            with open(self.fileName , "r") as file:
                data = file.read()
        except FileNotFoundError:
            return None

        file_otp , timeout = data.split(",")

        if(len(file_otp) < self.size):
            return None

        file_otp = int(file_otp)
        timeout = int(timeout)

        if(timeout < int(time.time())):
            return None

        return file_otp




    # verify the otp
    # True if valid
    # False if expired
    # None if not valid
    def verifyOTP(self , otp : int):

        otp = int(otp)

        try:
            with open(self.fileName , "r") as file:
                data = file.read()
        except FileNotFoundError:
            return None

        file_otp , timeout = data.split(",")

        if(len(file_otp) < self.size):
            return None

        file_otp = int(file_otp)
        timeout = int(timeout)

        if(file_otp == otp):

            if(timeout < int(time.time())):
                return False

            else:
                if(self.oneTime):
                    with open(self.fileName , "w") as file:
                        file.write("0,0")
                return True

        else:
            return None




    # get otp verification time left
    # return None if OTP is expired or not generated
    # else return time left in seconds
    def getTimeLeft(self):
        try:
            with open(self.fileName , "r") as file:
                data = file.read()
        except FileNotFoundError:
            return None

        file_otp , timeout = data.split(",")

        if(len(file_otp) < self.size):
            return None

        file_otp = int(file_otp)
        timeout = int(timeout)

        if(timeout < int(time.time())):
            return None
        else:
            return abs(int(time.time()) - timeout)

































#  _   _                   ____                                  _     _   _                       _                          
# | \ | |   ___    _ __   |  _ \    ___   _ __     ___    __ _  | |_  | \ | |  _   _   _ __ ___   | |__     ___   _ __   ___  
# |  \| |  / _ \  | '_ \  | |_) |  / _ \ | '_ \   / _ \  / _` | | __| |  \| | | | | | | '_ ` _ \  | '_ \   / _ \ | '__| / __| 
# | |\  | | (_) | | | | | |  _ <  |  __/ | |_) | |  __/ | (_| | | |_  | |\  | | |_| | | | | | | | | |_) | |  __/ | |    \__ \ 
# |_| \_|  \___/  |_| |_| |_| \_\  \___| | .__/   \___|  \__,_|  \__| |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|    |___/ 
#                                        |_|                                                                                  

class NonRepeatNumbers:

    # min - lower limit
    # max - upper limit
    # filePath = path were otp file will be stored
    # fileName = name of file you want to store otp in
    # if fileName is None , a random name will be assigned , you can get filePath using .fileName attribute
    # store = save state to disk
    def __init__(self , min , max , filePath = "./" , fileName = None , store = True):
        self.min = min
        self.max = max
        self.store = store
        
        path = pathlib.Path(filePath)

        if(not(path.is_dir())):
            raise FileNotFoundError(f"no dir at {path}")
        
        self.doneList = []

        self.fileName = fileName

        # make file name
        if(self.fileName == None):
            self.fileName = RandomID(prefix="NonRepeatNumbers_file_" , suffix=".txt").md5()

        self.fileName = pathlib.Path(filePath , self.fileName)

        # generate object
        if(self.store):
            with open(self.fileName , "r") as file:

                # restore data which is already generated
                if(fileName != None):
                    data = file.read()

                    dataList = data.splitlines()

                    self.doneList = sorted([int(i) for i in dataList])

                    self.doneList.insert(0 , self.min - 1)
                    self.doneList.append(self.max + 1)


        else:
            self.doneList.append(self.max + 1)
            






    # main function
    # function to generate a unique value
    # returns one value at a time
    def generate(self):

        """
        process - 

        lets say we need to generate random numbers btw 0 and 100

        we add -1 and 101 to done list and also suppose 10 and 25 are already generated

        doneList = [-1 , 10 , 25 , 101]


        now we traverse this done list
        we can generate new random number btw [-1 , 10] , [10 , 25] , [25 , 101]
                                      index = [ 0 , 1 ] , [ 1 , 2 ] , [ 2 , 3  ]
                                      general index = [ i , i+1 ]

        we randomly pick in which we will generate a value
        
        then we generate a random value and update done list in which i and i+1 should be excluded as they are already generated

        constraint - number at i+1 index should not be 1 + number at i index 
        as their is no number btw i and i+1
        ex - no random number btw 4 and 5 as 4 and 5 are already generated and no integer btw 4 and 5 , so 4,5 pair will not be generated

        """
        functionPairList = []

        # generating the pair list for random number function
        for i in range(len(self.doneList) - 1):
            if(self.doneList[i] < (self.doneList[i+1] - 1)):
                functionPairList.append([self.doneList[i] , self.doneList[i+1]])


        # if no pair list is generated means all numbers in range are already generated
        if(len(functionPairList) == 0):
            raise RuntimeError("No New Random Number can be generated within {}-{} range".format(self.min , self.max))

        # choosing a random pair from pair list
        functionPairListChossen = secrets.choice(functionPairList)

        # generating random number
        random.seed(secrets.token_bytes(256))
        randomInt = random.randint(functionPairListChossen[0]+1 , functionPairListChossen[1]-1)

        # insert into done list
        bisect.insort(self.doneList, randomInt)

        if(self.store):
            with open(self.fileName , "a") as file:
                file.write(str(randomInt) + "\n")

        return randomInt






































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










def __test__TrueRandom_mouse_getRandomBytes():

    obj = TrueRandom_mouse()

    obj.setSeed()

    randomBytes = obj.getRandomBytes(16 , raiseError=False)

    print(len(randomBytes))

    print(randomBytes)




















#  _                  _                       ____                        _                       ___   ____   
# | |_    ___   ___  | |_                    |  _ \    __ _   _ __     __| |   ___    _ __ ___   |_ _| |  _ \  
# | __|  / _ \ / __| | __|       _____       | |_) |  / _` | | '_ \   / _` |  / _ \  | '_ ` _ \   | |  | | | | 
# | |_  |  __/ \__ \ | |_       |_____|      |  _ <  | (_| | | | | | | (_| | | (_) | | | | | | |  | |  | |_| | 
#  \__|  \___| |___/  \__|                   |_| \_\  \__,_| |_| |_|  \__,_|  \___/  |_| |_| |_| |___| |____/  
                                                                                                             



def __test_RandomID():
    obj = RandomID()

    print(obj.md5() , len(obj.md5()))
    print(obj.sha1() , len(obj.sha1()))
    print(obj.sha224() , len(obj.sha224()))
    print(obj.sha256() , len(obj.sha256()))
    print(obj.sha384() , len(obj.sha384()))
    print(obj.sha512() , len(obj.sha512()))



















#  _                  _                        ___    _____   ____   
# | |_    ___   ___  | |_                     / _ \  |_   _| |  _ \  
# | __|  / _ \ / __| | __|       _____       | | | |   | |   | |_) | 
# | |_  |  __/ \__ \ | |_       |_____|      | |_| |   | |   |  __/  
#  \__|  \___| |___/  \__|                    \___/    |_|   |_|     
                                                                   


def __test_OTP():

    obj = OTP(timeout=10 , oneTime=False)

    mainOTP = obj.generateOTP()

    print("mainOTP" , mainOTP)

    while(True):
        otp = obj.getOTP()

        if(otp == None):
            print("getOTP == None")
            break
    
        print(otp , obj.verifyOTP(otp) , obj.verifyOTP(123456) , obj.getTimeLeft())

        time.sleep(0.9)


    print("out of loop")

    print(mainOTP , obj.verifyOTP(mainOTP) , obj.verifyOTP(123456) , obj.getTimeLeft())

    time.sleep(0.9)

    print(mainOTP , obj.verifyOTP(mainOTP) , obj.verifyOTP(123456) , obj.getTimeLeft())
    
    print("testing empty otp")
    
    print(mainOTP , obj.verifyOTP("0") , obj.verifyOTP(123456) , obj.getTimeLeft())













#  _                  _                       _   _                   ____                                  _     _   _                       _                          
# | |_    ___   ___  | |_                    | \ | |   ___    _ __   |  _ \    ___   _ __     ___    __ _  | |_  | \ | |  _   _   _ __ ___   | |__     ___   _ __   ___  
# | __|  / _ \ / __| | __|       _____       |  \| |  / _ \  | '_ \  | |_) |  / _ \ | '_ \   / _ \  / _` | | __| |  \| | | | | | | '_ ` _ \  | '_ \   / _ \ | '__| / __| 
# | |_  |  __/ \__ \ | |_       |_____|      | |\  | | (_) | | | | | |  _ <  |  __/ | |_) | |  __/ | (_| | | |_  | |\  | | |_| | | | | | | | | |_) | |  __/ | |    \__ \ 
#  \__|  \___| |___/  \__|                   |_| \_|  \___/  |_| |_| |_| \_\  \___| | .__/   \___|  \__,_|  \__| |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|    |___/ 
#                                                                                   |_|                                                                                  


def __test_NonRepeatNumbers():

    obj = NonRepeatNumbers(0,1000)

    for i in range(1002):
        print(i , obj.generate())






def __test_NonRepeatNumbers_2():
    fileName="test_NonRepeatNumbers.txt"

    with open(fileName , "w") as file:
        pass
    
    obj = NonRepeatNumbers(0,1000 , fileName = fileName)

    for i in range(500):
        print(i , obj.generate())

    input()

    obj = NonRepeatNumbers(0,1000 , fileName = fileName)

    for i in range(502):
        print(i , obj.generate())






if __name__ == "__main__":
    # __test_NonRepeatNumbers_2()
    __test_OTP()