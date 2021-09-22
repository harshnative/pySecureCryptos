import onetimepad
import hashlib
import random



# class to shuffle and deshuffle the passed list
class Shuffler:
    
    @classmethod
    def shuffle_under_seed(cls , ls, seed):
        # Shuffle the list ls using the seed `seed`
        random.seed(seed)
        random.shuffle(ls)
        return ls

    @classmethod
    def unshuffle_list(cls , shuffled_ls, seed):
        n = len(shuffled_ls)
        # Perm is [1, 2, ..., n]
        perm = [i for i in range(1, n + 1)]
        # Apply sigma to perm
        shuffled_perm = cls.shuffle_under_seed(perm, seed)
        # Zip and unshuffle
        zipped_ls = list(zip(shuffled_ls, shuffled_perm))
        zipped_ls.sort(key=lambda x: x[1])
        return [a for (a, b) in zipped_ls]


    # function to shuffle a string
    @classmethod
    def shuffleString(cls , string , seed):
        
        # convert the string to list and pass to main method
        shuffledList =  cls.shuffle_under_seed(list(string) , seed)

        # convert the shuffled list back to list
        stringFromList = "".join(shuffledList)
        return stringFromList
    

    # function to shuffle a string
    @classmethod
    def deShuffleString(cls , shuffledString , seed):

        # convert the shuffledString to list and pass to main method
        deshuffledList = cls.unshuffle_list(list(shuffledString) , seed)
        
        # convert the deshuffled list back to string
        stringFromList = "".join(deshuffledList)
        return stringFromList



# class OnetimepadWrapper:


#     @classmethod
#     def
