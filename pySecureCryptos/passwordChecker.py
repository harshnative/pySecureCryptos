import string

# class to check password strength
class Check:

    specialChars = """!@#$%^&*()_-+=~`{[}]|:;"'<,>.?/"""

    # method to check if the password qualifies for the low level security purposes
    # default parameters are designed in way to ensure a low level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_low(cls , password , minLen = 10 , lowerChars = True , upperChars = False , nums = True , specialChars = False):
        
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













    
    # method to check if the password qualifies for the medium level security purposes
    # default parameters are designed in way to ensure a medium level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_medium(cls , password , minLen = 12 , lowerChars = True , upperChars = True , nums = True , specialChars = False):
        
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

        # add missing to error list
        if(lowerChars and (not(lowerChars_present))):
            errorList.append(f"at least one lower case letter is required in password [a-z]")
        
        if(upperChars and (not(upperChars_present))):
            errorList.append(f"at least one upper case letter is required in password [A-Z]")
        
        if(nums and (not(nums_present))):
            errorList.append(f"at least one number is required in password [0-9]")
        
        if(specialChars and (not(specialChars_present))):
            errorList.append(f"at least one special character is required in password like !@#$%& etc")

        # return the status
        if(len(errorList) == 0):
            return None
        else:
            return errorList











    # method to check if the password qualifies for the high level security purposes
    # default parameters are designed in way to ensure a high level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_high(cls , password , minLen = 15 , lowerChars = True , upperChars = True , nums = True , specialChars = True):
        
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

        # add missing to error list
        if(lowerChars and (not(lowerChars_present))):
            errorList.append(f"at least one lower case letter is required in password [a-z]")
        
        if(upperChars and (not(upperChars_present))):
            errorList.append(f"at least one upper case letter is required in password [A-Z]")
        
        if(nums and (not(nums_present))):
            errorList.append(f"at least one number is required in password [0-9]")
        
        if(specialChars and (not(specialChars_present))):
            errorList.append(f"at least one special character is required in password like !@#$%& etc")

        # return the status
        if(len(errorList) == 0):
            return None
        else:
            return errorList









    # method to check if the password qualifies for the max level security purposes
    # default parameters are designed in way to ensure a max level security application password
    # returns None if the password qualifies
    # return error list containing string listing the errors in password in english langauge
    @classmethod
    def check_max(cls , password , minLen = 20 , lowerChars = True , upperChars = True , nums = True , specialChars = True):
        
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

        # add missing to error list
        if(lowerChars and (not(lowerChars_present))):
            errorList.append(f"at least one lower case letter is required in password [a-z]")
        
        if(upperChars and (not(upperChars_present))):
            errorList.append(f"at least one upper case letter is required in password [A-Z]")
        
        if(nums and (not(nums_present))):
            errorList.append(f"at least one number is required in password [0-9]")
        
        if(specialChars and (not(specialChars_present))):
            errorList.append(f"at least one special character is required in password like !@#$%& etc")

        # return the status
        if(len(errorList) == 0):
            return None
        else:
            return errorList
















def __test_low():
    myPassword = "hello world12"

    print(Check.check_low(myPassword))

    myPassword = "hello wor"

    print(Check.check_low(myPassword))







def __test_medium():
    myPassword = "hello world12W"

    print(Check.check_medium(myPassword))

    myPassword = "hello wor"

    print(Check.check_medium(myPassword))







def __test_high():
    myPassword = "hello world12W#"

    print(Check.check_high(myPassword))

    myPassword = "hello wor"

    print(Check.check_high(myPassword))







def __test_max():
    myPassword = "Th!s P@sssword 1s Ve#y Compl$x"

    print(Check.check_max(myPassword))

    myPassword = "hello wor"

    print(Check.check_max(myPassword))



if __name__ == "__main__":
    __test_max()