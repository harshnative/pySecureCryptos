import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_onetimepadWrapper as onetimepadWrapper

byte = b"my name is john and i am a programmer"

password = "hello world"

encByte = b'56070d55651170055501005155003650105360632050055451304000451626000625553536535510350d4505500480003350005b6049550500505565679645060082250555505b50505425309054505505753d50668000057255c0050200657653470550b2c0000300505615155006:checksum:05031500005230255b3c0074724000030d0033058505194857092356050550000005005900008e500270265001000500600504001677035512093e59500175164075005551b02001a8020040de30005503050d07600d0505013550d500717025'
encByte2 = b'56070d55651170055501005155003650105360632050055451304000451626000625553536535510350d4505500480003350005b6049550500505565679645060082250555505b50505425309054505505753d50668000057255c0050200657653470550b2c0000300505615155006:checksum:05031500005230255b3c0074724000030d0033058505194857092356050550000005005900008e500270265001000500600504001677035512093e59500175164075005551b02001a8020040de30005503050d07600d0505013550d500717025'

def encrypt():
    result = onetimepadWrapper.BytesEncryptor.encrypt(byte , password)
    print(result)

def encrypt2():
    genObj = onetimepadWrapper.BytesEncryptor_yield.encrypt(byte , password)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_byte):
    result = onetimepadWrapper.BytesEncryptor.decrypt_byte(enc_byte , password)
    if(result != byte):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_byte):
    genObj = onetimepadWrapper.BytesEncryptor_yield.decrypt_byte(enc_byte , password)

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
    decrypt(encByte)
    decrypt1(encByte)
    decrypt(encByte2)
    decrypt1(encByte2)
    # encrypt()