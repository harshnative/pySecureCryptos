import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import fernetWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encByte = b'gAAAAABhng4yhO62U6zV2z72jewc5QNX_XFOcCNdneMZFGoyBbQ-6HjTV0HvaE3fQrmcFTYMSAWwbLFC1xivhUJgwohDjnKXH79F_L2ki8rwXJ8LfyCt6yE1hllNwlyGlY64lBYRpODk'
encByte2 = b'gAAAAABhng5nR9KEndgKkyeR3tdKn9vnrWbWGdtn2XYEMC7LuRs4Vd0N3cjqio3zR9zWpsYRQQh5UlKA0LkHrBMmk-hjcqcO3zYKaUrzZZwbsNapWUxMsX5_WVTUyuZBD_SsuxKUPxe9'

def encrypt():
    result = fernetWrapper.StringEncryptor(password).encrypt(string , False)
    print(result)

def encrypt2():
    genObj = fernetWrapper.StringEncryptor(password).encrypt_yield(string , False)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_byte):
    result = fernetWrapper.StringEncryptor(password).decrypt_byte(enc_byte)
    if(result != string):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_byte):
    genObj = fernetWrapper.StringEncryptor(password).decrypt_byte_yield(enc_byte)

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
    decrypt(encByte)
    decrypt1(encByte)
    decrypt(encByte2)
    decrypt1(encByte2)
    # encrypt2()