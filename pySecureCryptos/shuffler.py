import random
import copy

# class to shuffle and deshuffle
class Shuffler:
    
    # method to shuffle a passed list using a seed
    @classmethod
    def shuffe_list(cls , ls , seed , copyList = True):

        if(type(ls) != list):
            raise ValueError("ls parameter expected to be of list type instead got {} type".format(type(ls)))

        if(type(seed) != str):
            raise ValueError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

        # copy list so that the original list stays the same
        if(copyList):
            ls = copy.deepcopy(ls)
        
        random.seed(seed)
        random.shuffle(ls)
        return ls



    # method to unshuffel a list shuffled using shuffe_list() method of this class
    # seed should be same for both the methods
    @classmethod
    def unShuffle_list(cls , shuffled_ls, seed):

        if(type(shuffled_ls) != list):
            raise ValueError("shuffled_ls parameter expected to be of list type instead got {} type".format(type(shuffled_ls)))

        if(type(seed) != str):
            raise ValueError("seed parameter expected to be of str type instead got {} type".format(type(seed)))


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


    # method to shuffle a string
    @classmethod
    def shuffle_string(cls , string , seed):

        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(type(seed) != str):
            raise ValueError("seed parameter expected to be of str type instead got {} type".format(type(seed)))

        # convert the string to list and pass to main method
        shuffledList =  cls.shuffe_list(list(string) , seed)

        # convert the shuffled list back to string
        stringFromList = "".join(shuffledList)
        return stringFromList
    

    # function to shuffle a string
    @classmethod
    def unShuffle_string(cls , shuffledString , seed):

        if(type(shuffledString) != str):
            raise ValueError("shuffledString parameter expected to be of str type instead got {} type".format(type(shuffledString)))

        if(type(seed) != str):
            raise ValueError("seed parameter expected to be of str type instead got {} type".format(type(seed)))


        # convert the shuffledString to list and pass to main method
        deshuffledList = cls.unShuffle_list(list(shuffledString) , seed)
        
        # convert the deshuffled list back to string
        stringFromList = "".join(deshuffledList)
        return stringFromList







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
    



if __name__ == "__main__":
    __test()