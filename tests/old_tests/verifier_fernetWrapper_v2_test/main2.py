import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_fernetWrapper_v2 as fernetWrapper

byte = b"my name is john and i am a programmer"

password = "hello world"

encByte = b'gAAAAABhqfaI_2H4y_WQ956rFsNcSmBRhrLW1wTGOrROwUlnmZHBX5AtUhBa9VpU-n1lXSK3cs0i3RcjJh7WDeVmeXG2TQkHkv7R381Kf7QjoGrqO4zqZQP3ByzwIMYMp3klJy3JvHJ0:checksum:gAAAAABhqfaIrZdxipERGykgGv48Y05R0WIbYesIkdG90qt5RMkn6LaxkDjVGkMjiXlebR44_QkV5EFmi_QqR3n6jN0AGMuR27Yvsk6Wd0Eu5hk3-qm9Cls8J56SbI4arSqxGYQwsLL0'
encByte2 = b'gAAAAABhqfZzQbUzvG6BbJ7cPVwhJLIrsTjtW-YDCPwwGXd3qqFMbu6NHYrA9R95m_KIfxUP2t70BO-34aD5_JbDgeM-kcGICgDNHo2CXxBc8LBbW_ph1GxA6p1ILlS-X7udAzj-gy21:checksum:gAAAAABhqfZzmupfHhf47DJgnKVcIFo9FrZUEtlRFXY-e2-3o8781w7hMxe5_8Do0brCb-000A5TArcpdn4sITyIRyVMTCPUAI83HE_VPjiacXgOsNFU8bGPsRJDhijDOlR1wdT-30ps'

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
    # encrypt()