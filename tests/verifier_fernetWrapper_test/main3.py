import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_fernetWrapper as fernetWrapper

byte = b"my name is john and i am a programmer"

password = "hello world"

encByte = b'gAAAAABhnhAatK3OQfZCq0KVZ4NqBj-wVrBNtl3JCnp-899BxnaV-EtoQJ0JG1Ja7kCiOwSF3I2PhCVxztXS3jwXpjtK6R_5Zgxo3FrpRRZDFNeA_X1Adxt22Hnr49fz_TQwMZEsPqAx:checksum:gAAAAABhnhAaaauXmMaP0fS4ClNgh1B1ENoq5g0XdzuRqFtmpd7R-r4JtF20PPAoiSgJkFNR96Cazi5c21VHQr6PSfMdNuipBHPxOYQ02Ri0s6n1UTBz-dtAXbnpYw-GPNxa0QKcEN1p'
encByte2 = b'gAAAAABhnhAwPV3HiWnJwCuR9o6uyYdQdcmfy3nUWJgVpFFRSR9Q66k37V18A1m_BRyWDzo62UGFH1GGTqkm_JPGgSsnUsyfkxvVNfJiFmglZlm89OFq5soY6xq7eLxUvlRi7-Dyg5JE:checksum:gAAAAABhnhAwUTvIsopyn0YOJqlXI6ql8DI8iSk6K2Yrkeuh5cU9_5HkmV6OTJTHE_yVShtLpCsplzubic9cnaPqyBCjttd5ZGjTp_MFbhmPikcLS2VCxd54l7S0YoBSSLaskcktSJup'

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
    # encrypt2()