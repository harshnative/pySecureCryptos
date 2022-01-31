from typing import Union
import string









#         _                     _     
#   ___  | |__     ___    ___  | | __ 
#  / __| | '_ \   / _ \  / __| | |/ / 
# | (__  | | | | |  __/ | (__  |   <  
#  \___| |_| |_|  \___|  \___| |_|\_\ 
                                    

# class to check password strength
class Check:

    specialChars = """!@#$%^&*()_-+=~`{[}]|:;"'<,>.?/"""

    # method to check if the password qualifies for the low level security purposes
    # default parameters are designed in way to ensure a low level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_pass(cls , password : str , exclude_subStrings : list = None , minLen : int = 10 , lowerChars : bool = True , upperChars : bool = False , nums : bool = True , specialChars : bool = False) -> Union[None , list]:

        if(exclude_subStrings == None):
            exclude_subStrings = []
        
        if(type(password) != str):
            raise TypeError(f"password parameter expected to be of {str} type instead got {type(password)} type")
        

        if(type(minLen) != int):
            raise TypeError(f"minLen parameter expected to be of {int} type instead got {type(minLen)} type")

        
        if(type(lowerChars) != bool):
            raise TypeError(f"lowerChars parameter expected to be of {bool} type instead got {type(lowerChars)} type")

        
        if(type(upperChars) != bool):
            raise TypeError(f"upperChars parameter expected to be of {bool} type instead got {type(upperChars)} type")


        if(type(nums) != bool):
            raise TypeError(f"nums parameter expected to be of {bool} type instead got {type(nums)} type")

        
        if(type(specialChars) != bool):
            raise TypeError(f"specialChars parameter expected to be of {bool} type instead got {type(specialChars)} type")

        

        errorList = []
        
        lowerChars_present = False
        upperChars_present = False
        nums_present = False
        specialChars_present = False

        # check length
        lenPass = len(password)

        if(lenPass < minLen):
            errorList.append(f"password should be at least of {minLen} chars")

        # check lower case , upper case , nums , special chars 
        for i in password:
            if(i in string.ascii_lowercase):
                lowerChars_present = True
            elif(i in string.ascii_uppercase):
                upperChars_present = True
            elif(i in string.digits):
                nums_present = True
            elif(i in cls.specialChars):
                specialChars_present = True

            if(lowerChars_present and upperChars_present and nums_present and specialChars_present):
                break


        # check for the sub string
        for i in exclude_subStrings:
            if(password.find(i) != -1):
                errorList.append(f"password should not contain '{i}' in it")


        # add missing to error list
        if(lowerChars and (not(lowerChars_present))):
            errorList.append("at least one lower case letter is required in password [a-z]")
        
        if(upperChars and (not(upperChars_present))):
            errorList.append("at least one upper case letter is required in password [A-Z]")
        
        if(nums and (not(nums_present))):
            errorList.append("at least one number is required in password [0-9]")
        
        if(specialChars and (not(specialChars_present))):
            errorList.append("at least one special character is required in password like !@#$%& etc")

        # return the status
        if(len(errorList) == 0):
            return None
        else:
            return errorList
















    # method to check if the password qualifies for the low level security purposes
    # default parameters are designed in way to ensure a low level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_low(cls , password : str , exclude_subStrings : list = None) -> Union[None , list]:
        
        return cls.check_pass(password , exclude_subStrings , minLen=8 , lowerChars=True , upperChars=False , nums=True , specialChars=False)









    
    # method to check if the password qualifies for the medium level security purposes
    # default parameters are designed in way to ensure a medium level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_medium(cls , password : str , exclude_subStrings : list = None) -> Union[None , list]:
        
        return cls.check_pass(password , exclude_subStrings , minLen=12 , lowerChars=True , upperChars=True , nums=True , specialChars=False)











    # method to check if the password qualifies for the medium level security purposes
    # default parameters are designed in way to ensure a medium level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_high(cls , password : str , exclude_subStrings : list = None) -> Union[None , list]:
        
        return cls.check_pass(password , exclude_subStrings , minLen=12 , lowerChars=True , upperChars=True , nums=True , specialChars=True)









    # method to check if the password qualifies for the max level security purposes
    # default parameters are designed in way to ensure a max level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_max(cls , password : str , exclude_subStrings : list = None) -> Union[None , list]:
        
        return cls.check_pass(password , exclude_subStrings , minLen=20 , lowerChars=True , upperChars=True , nums=True , specialChars=True)














#  _                  _          
# | |_    ___   ___  | |_   ___  
# | __|  / _ \ / __| | __| / __| 
# | |_  |  __/ \__ \ | |_  \__ \ 
#  \__|  \___| |___/  \__| |___/ 
                               







def __test_check_pass():
    myPassword = "optimus prime 123 # $ O"
    exclude = ["hello" , "world"]

    print(Check.check_pass(myPassword , exclude))

    myPassword = "hello world"

    print(Check.check_pass(myPassword , exclude))






def __test_check_low():
    myPassword = "optimus prime 123 # $ O"
    exclude = ["hello" , "world"]

    print(Check.check_low(myPassword , exclude))

    myPassword = "hello world"

    print(Check.check_low(myPassword , exclude))







def __test_check_medium():
    myPassword = "optimus prime 123 # $ O"
    exclude = ["hello" , "world"]

    print(Check.check_medium(myPassword , exclude))

    myPassword = "hello world"

    print(Check.check_medium(myPassword , exclude))







def __test_check_high():
    myPassword = "optimus prime 123 # $ O"
    exclude = ["hello" , "world"]

    print(Check.check_high(myPassword , exclude))

    myPassword = "hello world"

    print(Check.check_high(myPassword , exclude))







def __test_check_max():
    myPassword = "optimus prime 123 # $ O"
    exclude = ["hello" , "world"]

    print(Check.check_max(myPassword , exclude))

    myPassword = "hello world"

    print(Check.check_max(myPassword , exclude))















if __name__ == "__main__":
    # __test_check_pass()
    # __test_check_low()
    # __test_check_medium()
    # __test_check_high()
    __test_check_max()