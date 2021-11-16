# class containing method to encode or decode any byte 
class Byte2String:

    # method to convert any byte into string
    @classmethod
    def encode(cls , byte):

        """
        ALGO - 
        convert each byte into int - result = int btw 0 to 255

        convert the int into string type. 

        make the int string 3 chars long means if the string is 49 convert to 049

        append to main string and return main string
        """

        string = ""

        for i in byte:
            i = str(int(i))
            i = ("0" * (3 - len(i))) + i 
            string = string + i

        return string

    # method to convert the output string from above method into byte again
    # returns a bytearray type object
    @classmethod
    def decode(cls , string):

        """
        ALGO - 

        traverse the string and slice the string into 3 chars long

        convert the string back to int

        pass the int list to bytearray and return
        """

        intList = []

        for i in range(0 , len(string) , 3):
            toAppend = int(string[i : i + 3])
            intList.append(toAppend)

        return bytearray(intList)



class String2Byte:

    # method to convert string to byte
    # returns bytearray
    @classmethod
    def encode(cls , string):

        """
        convert each char in string to corresponding ASCII value (int)

        convert this intList to byteArray
        """
        intList = []

        for i in string:
            intList.append(ord(i))

        return bytearray(intList)


    @classmethod
    def decode(cls , byte):
        string = ""

        for i in byte:
            i = chr(int(i))
            string = string + i

        return string

        



# function to test the above class
def __test():
    pass
    
if __name__ == "__main__":
    __test()


