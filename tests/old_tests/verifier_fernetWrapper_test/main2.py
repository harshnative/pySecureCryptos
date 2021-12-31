import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_fernetWrapper as fernetWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encByte = b'gAAAAABhng_4ZdEHBFWz1oVUjlyWjbhMm9USKaOEbOUhRjrDxJAj7gKSpkdal6n7ruGRUx1EymxxzFMRpiVlXPVUPil3aJS8QFEKJdqcjLf0veGAX5ZNxToOaxxXoSuLOltswTk76-BM:checksum:gAAAAABhng_4K20AKNqZXMvORdAab38lw8YDY2QDL4WL2rbI7JaX_HJit_X_RYU2pnRVnnLIDw8mgNJaao6QN7ixciF7YHeWbdCeFJWaZVhUukKtOrgkur_uEg8s7Xwbz448Jp7n6gZV'
encByte2 = b'gAAAAABhng_nAezf-7ltVhWhvLcJ_wrHBCE1l6AQANqZYaT6TSVKSUjmPncyPGyMjgeWq8FDpZZPqruUPjG13CZnje7GGy1uQmrV8gmH1Z_cDqp49ajgesCVcWUQ8mGiwzo7hpG2jhvE:checksum:gAAAAABhng_nZu2NuGHdRd3PZGIqULXZIzT085k2WUeWUDh8OXYQJVDWOSvmBBFKSu8bdEczueD-aKat54q-JkyFaB7R1RsRXLOsMpAiSr7FBuWI_fstvna7IK4kG-_lr2UdNUjGhywm'

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
    # encrypt()