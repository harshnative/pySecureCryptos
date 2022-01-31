import random
import copy



# TODO : you can add yielder method to all the shufflers
# you can divide the list into equal chunks
# then shuffle individual list and yield progress
# then shuffle these individual lists order and combine and return


# TODO : you can add true random shuffle
# choose a element from list using secrets.choice then remove the element form list , then choice another
# no unshuffle method will be provided




#        _                __    __   _                
#  ___  | |__    _   _   / _|  / _| | |   ___   _ __  
# / __| | '_ \  | | | | | |_  | |_  | |  / _ \ | '__| 
# \__ \ | | | | | |_| | |  _| |  _| | | |  __/ | |    
# |___/ |_| |_|  \__,_| |_|   |_|   |_|  \___| |_|    
                                                    

# class to shuffle and deshuffle
class Shuffler:






    #      _   _         _    
    # | | (_)  ___  | |_  
    # | | | | / __| | __| 
    # | | | | \__ \ | |_  
    # |_| |_| |___/  \__| 
                        
    
    # method to shuffle a passed list using a seed
    @classmethod
    def shuffe_list(cls , ls : list , seed : str , copyList : bool = True) -> list:

        if(type(ls) != list):
            raise TypeError("ls parameter expected to be of list type instead got {} type".format(type(ls)))

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

        # copy list so that the original list stays the same
        if(copyList):
            ls = copy.deepcopy(ls)
        
        random.seed(seed)
        random.shuffle(ls)
        return ls



    # method to unshuffel a list shuffled using shuffe_list() method of this class
    # seed should be same for both the methods
    @classmethod
    def unShuffle_list(cls , shuffled_ls : list , seed : str) -> list:

        if(type(shuffled_ls) != list):
            raise TypeError("shuffled_ls parameter expected to be of list type instead got {} type".format(type(shuffled_ls)))

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))


        n = len(shuffled_ls)

        # reference list containing numbers from 0 to n - 1
        perm = [i for i in range(n)]

        # Apply sigma to perm
        # that is shuffle this refrence list using the same seed
        shuffled_perm = cls.shuffe_list(perm, seed)

        # combine the shuffled reference list and shuffled list passed
        # if the seed was same then the shuffled list passed index would be same as shuffled_perm
        zipped_ls = list(zip(shuffled_ls, shuffled_perm))

        # sort the shuffled list according to shuffled perm
        zipped_ls.sort(key=lambda x: x[1])
        
        # get and return the unshuffledList from zipped_ls
        # unshuffled list elements were at index 0 or at a in zipped_ls
        unshuffledList = [a for (a, b) in zipped_ls]

        return unshuffledList
















    #            _            _                  
    #  ___  | |_   _ __  (_)  _ __     __ _  
    # / __| | __| | '__| | | | '_ \   / _` | 
    # \__ \ | |_  | |    | | | | | | | (_| | 
    # |___/  \__| |_|    |_| |_| |_|  \__, | 
    #                                 |___/  


    # method to shuffle a string
    @classmethod
    def shuffle_string(cls , string : str , seed : str) -> str:

        if(type(string) != str):
            raise TypeError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

        # convert the string to list and pass to main method
        shuffledList =  cls.shuffe_list(list(string) , seed)

        # convert the shuffled list back to string
        stringFromList = "".join(shuffledList)
        return stringFromList
    

    # function to shuffle a string
    @classmethod
    def unShuffle_string(cls , shuffledString : str , seed : str) -> str:

        if(type(shuffledString) != str):
            raise TypeError("shuffledString parameter expected to be of str type instead got {} type".format(type(shuffledString)))

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))


        # convert the shuffledString to list and pass to main method
        deshuffledList = cls.unShuffle_list(list(shuffledString) , seed)
        
        # convert the deshuffled list back to string
        stringFromList = "".join(deshuffledList)
        return stringFromList














    # _               _           
    # | |__    _   _  | |_    ___  
    # | '_ \  | | | | | __|  / _ \ 
    # | |_) | | |_| | | |_  |  __/ 
    # |_.__/   \__, |  \__|  \___| 
    #         |___/               

    # method to shuffle a byte
    @classmethod
    def shuffle_byte(cls , byte : bytes , seed : str) -> bytes:

        if(type(byte) != bytes):
            raise TypeError("byte parameter expected to be of bytes type instead got {} type".format(type(byte)))

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

        # convert the string to list and pass to main method
        shuffledList =  cls.shuffe_list(list(byte) , seed)

        # convert the shuffled list back to byte
        shuffledByte = bytes(shuffledList)
        return shuffledByte
    

    # function to shuffle a byte
    @classmethod
    def unShuffle_byte(cls , shuffledByte : bytes  , seed : str) -> bytes:

        if(type(shuffledByte) != bytes):
            raise TypeError("shuffledByte parameter expected to be of bytes type instead got {} type".format(type(shuffledByte)))

        if(type(seed) != str):
            raise TypeError("seed parameter expected to be of str type instead got {} type".format(type(seed)))


        # convert the shuffledString to list and pass to main method
        deshuffledList = cls.unShuffle_list(list(shuffledByte) , seed)
        
        # convert the deshuffled list back to string
        byteFromList = bytes(deshuffledList)
        return byteFromList

















#  _                  _                       _   _         _    
# | |_    ___   ___  | |_                    | | (_)  ___  | |_  
# | __|  / _ \ / __| | __|       _____       | | | | / __| | __| 
# | |_  |  __/ \__ \ | |_       |_____|      | | | | \__ \ | |_  
#  \__|  \___| |___/  \__|                   |_| |_| |___/  \__| 
                                                               

def __test():
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








#  _                  _                             _            _                  
# | |_    ___   ___  | |_                     ___  | |_   _ __  (_)  _ __     __ _  
# | __|  / _ \ / __| | __|       _____       / __| | __| | '__| | | | '_ \   / _` | 
# | |_  |  __/ \__ \ | |_       |_____|      \__ \ | |_  | |    | | | | | | | (_| | 
#  \__|  \___| |___/  \__|                   |___/  \__| |_|    |_| |_| |_|  \__, | 
#                                                                            |___/  


def __test2():

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





#  _                  _                       _               _           
# | |_    ___   ___  | |_                    | |__    _   _  | |_    ___  
# | __|  / _ \ / __| | __|       _____       | '_ \  | | | | | __|  / _ \ 
# | |_  |  __/ \__ \ | |_       |_____|      | |_) | | |_| | | |_  |  __/ 
#  \__|  \___| |___/  \__|                   |_.__/   \__, |  \__|  \___| 
#                                                     |___/               

def __test3():

    myByte = b"hello world"
    seed = "hellooo"
    print("byte = {} , seed = {}".format(myByte , seed))

    shuffledByte = Shuffler.shuffle_byte(myByte , seed)

    print("shuffledByte = {}".format(shuffledByte))

    deShuffledByte = Shuffler.unShuffle_byte(shuffledByte , seed)

    print("deShuffledByte = {}".format(deShuffledByte))

    if(myByte == deShuffledByte):
        print("ok")
    else:
        print("error")
    



























if __name__ == "__main__":
    __test3()