import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_onetimepadWrapper as onetimepadWrapper

byte = b"my name is john and i am a programmer"

password = "hello world"

encString = "56070d55651170055501005155003650105360632050055451304000451626000625553536535510350d4505500480003350005b6049550500505565679645060082250555505b50505425309054505505753d50668000057255c0050200657653470550b2c0000300505615155006:checksum:5503a00505045025504d00733b7103520a053606b6355aad5c022154060005051000005e0055bfd03715440009080556205507503371065042550550201755a6"
encString2 = "56070d55651170055501005155003650105360632050055451304000451626000625553536535510350d4505500480003350005b6049550500505565679645060082250555505b50505425309054505505753d50668000057255c0050200657653470550b2c0000300505615155006:checksum:5503a00505045025504d00733b7103520a053606b6355aad5c022154060005051000005e0055bfd03715440009080556205507503371065042550550201755a6"

def encrypt():
    result = onetimepadWrapper.BytesEncryptor.encrypt(byte , password , False)
    print(result)

def encrypt2():
    genObj = onetimepadWrapper.BytesEncryptor_yield.encrypt(byte , password , False)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_String):
    result = onetimepadWrapper.BytesEncryptor.decrypt(enc_String , password)
    if(result != byte):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_String):
    genObj = onetimepadWrapper.BytesEncryptor_yield.decrypt(enc_String , password)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break

    if(result != byte):
        print("error in decrypt1")
    else:
        print("ok decrypt1")


if __name__ == "__main__":
    decrypt(encString)
    decrypt1(encString)
    decrypt(encString2)
    decrypt1(encString2)
    # encrypt2()