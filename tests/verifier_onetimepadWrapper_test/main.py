import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_onetimepadWrapper as onetimepadWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encString = "504f101e873406002500555581658ac67115c515357c505401200b9531119a06c1451a1341:checksum:00a55e0015335757553516375400000705550055090550510205700010007022001ae5b6050025506555065a53b1353505516170a050060400f000505007032b"
encString2 = "504f101e873406002500555581658ac67115c515357c505401200b9531119a06c1451a1341:checksum:00a55e0015335757553516375400000705550055090550510205700010007022001ae5b6050025506555065a53b1353505516170a050060400f000505007032b"

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
    # encrypt()