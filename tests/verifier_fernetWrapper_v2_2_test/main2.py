import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_fernetWrapper_v2_2 as fernetWrapper

byte = b"my name is john and i am a programmer"

password = "hello world"

encByte = b'gAAAAABht1GptmqvhT0nnTC7Gqy1v5aKOA8FtQ9AwRo_L9R29nWvFnT_l3KUNQDRgGgMMXyV5B0Q8t-t6_UlYuJiLvWv0fT2vdeFX2_ApaS8yqJHAak9Ch3FuByK7TEm3j5pNFjtUv3q:checksum:gAAAAABht1Gpdlykl5ZDejModmcS6PW-SUM2oSsnY8q5jWQo_Dc1pnUlo49fp2Uv0-k6lygos5el1RpF949sVnYIcxUScoA2H4L7ZSO7MDmJ9LYhfJjkT6IgtGfwGMrlkYolpBhQa_ez'
encByte2 = b'gAAAAABht1HBHr1bLcxZKoWm6NiOMmSSp2NaQEMaKdCNQ1YvlofnLO75c1OeJ-MttcuDS8aTVlozSR_ZHCJYOIN_U90S83CvR6GwB0oseGvCsFxgWIdKevP4HlpKvskOpWJNZAkKwZmc:checksum:gAAAAABht1HB5-lvKri3HCCf5awFq1Fq-nS1EqRGmJEX8kazdhQqdif1oc1Nvm7_1lUti8QDe5vDOVnhJwD03dsv7e0JyDbQS_OOKfEi4Atu0lJiHmzrQr390X13nDCGUKXgrKnPITHW'

def encrypt():
    result = fernetWrapper.Encryptor(password).encrypt_byte(byte)
    print(result)

def encrypt2():
    genObj = fernetWrapper.Encryptor(password).encrypt_byte_yield(byte)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_byte):
    result = fernetWrapper.Encryptor(password).decrypt_byte(enc_byte)
    if(result != byte):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_byte):
    genObj = fernetWrapper.Encryptor(password).decrypt_byte_yield(enc_byte)

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