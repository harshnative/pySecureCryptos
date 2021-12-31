import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import onetimepadWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encString = "504f101e873406002500555581658ac67115c515357c505401200b9531119a06c1451a1341"
encString2 = "504f101e873406002500555581658ac67115c515357c505401200b9531119a06c1451a1341"

def encrypt():
    result = onetimepadWrapper.StringEncryptor.encrypt(string , password)
    print(result)

def encrypt2():
    genObj = onetimepadWrapper.StringEncryptor_yield.encrypt(string , password)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_string):
    result = onetimepadWrapper.StringEncryptor.decrypt(enc_string , password)
    if(result != string):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_string):
    genObj = onetimepadWrapper.StringEncryptor_yield.decrypt(enc_string , password)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break

    if(result != string):
        print("error in decrypt1")
    else:
        print("ok decrypt1")


if __name__ == "__main__":
    decrypt(encString)
    decrypt1(encString)
    decrypt(encString2)
    decrypt1(encString2)
    # encrypt2()