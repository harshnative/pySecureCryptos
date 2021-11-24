import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import fernetWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encString = "103065065065065065066104110103049108114069122076118085100077116085082050118053070067052114075118114088070100114048078104065069118087065105055049049115119107112104070116115098048086083072080114082066104099111101082069051052087073050076054074087070110087065117122070048114053109119051104056097073108097045070083068113050100045053109075045100106083115119113104083122081067087121088050084049052101076108116054095076079097115"
encString2 = "103065065065065065066104110103049083112070112053074099114112048102119069080054081055106071114071119075088098120048077114090083065098065111067107055057050056082081053080078065078068066077055070049116119074113106069049087054048111121097109051076118104106053107070077106112118122097107085076073052112120112097048110051117076102104099053070057052050120085106122112089055077116066111073097086072105073052105090113113070075088"

def encrypt():
    result = fernetWrapper.StringEncryptor(password).encrypt(string , True)
    print(result)

def encrypt2():
    genObj = fernetWrapper.StringEncryptor(password).encrypt_yield(string , True)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_string):
    result = fernetWrapper.StringEncryptor(password).decrypt_string(enc_string)
    if(result != string):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_string):
    genObj = fernetWrapper.StringEncryptor(password).decrypt_string_yield(enc_string)

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