import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import fernetWrapper

byte = b"my name is john and i am a programmer"

password = "hello world"

encByte = b'gAAAAABhng8EKzD1ACAMiE_lNIIDrdo6KNFVpba5iioZ0BPt3bCaq0lcWuB7Ga8BDrZUjPzrhm5JVegaThXyEcqvIDYh9fIxtr6n6JdIpl6sw-6auYQqowswvbqaRIAQq261mEVikknQ'
encByte2 = b'gAAAAABhng7zQBenikanpdIM7JF3MEw1hFtPwsZXlHolTYFUz0-D9WjT70aqFAja0oUx7UH2_TPRNLYSpDS7qGbYFpQ4XkcE2_fFPtpb4C8laWCwF8q-QSYq-LYJJeFqy-qohfpyF9kt'

def encrypt():
    result = fernetWrapper.BytesEncryptor(password).encrypt(byte)
    print(result)

def encrypt2():
    genObj = fernetWrapper.BytesEncryptor(password).encrypt_yield(byte)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_byte):
    result = fernetWrapper.BytesEncryptor(password).decrypt(enc_byte)
    if(result != byte):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_byte):
    genObj = fernetWrapper.BytesEncryptor(password).decrypt_yield(enc_byte)

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