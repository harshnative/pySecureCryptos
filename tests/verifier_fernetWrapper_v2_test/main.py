import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_fernetWrapper_v2 as fernetWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encString = "6741414141414268716659664a5a7733345930764d66526537734946314444513433713970593832726f6b794e50755357726e4839663552796f2d2d4a2d437a44555238362d4c447268495177435a6b2d304d6e6e46746c6a596c6d794d75667a396568333269615a7963774a4174474130736f367a77455a326c4c5a79414f2d5a38667657414965684468:checksum:6741414141414268716659664a70523931513930394b44705550346b314e514939437244615a426763363830686e724331426d3577796752383649314654616a70634132666f544649587373376571524b30334b694c4a616779754378637071536c5344744332693242414156416243307552326e504377344a7a564e7937576336556e565445737a4d5059"
encString2 = "6741414141414268716659427445716632447469786f753447736353664c2d34527a644244495778704a504c2d346366514e396c4a4d336d525551747763455a684353592d6b5334717a46654d4364736f724f394e34795262346775314a5770524e4b39673554386b4536744d306757526d484f3769383642385570567539414f744b5a716d70526a465146:checksum:67414141414142687166594238545953706a6656535271556369346d58754c7957306672325f466770777542596854494e4e51384877554b504156657171454c307a376d617a78676c71766f6939367a307069386363324452306a48324d70754e6c5a416a71616d733056686e5f56682d5a626b7338664365387172714b346c4d6b2d474c79476c55444541"

def encrypt():
    result = fernetWrapper.Encryptor(password).encrypt_string(string)
    print(result)

def encrypt2():
    genObj = fernetWrapper.Encryptor(password).encrypt_string_yield(string)
    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            result = ex.value
            break
    print(result)

def decrypt(enc_string):
    result = fernetWrapper.Encryptor(password).decrypt_string(enc_string)
    if(result != string):
        print("error in decrypt")
    else:
        print("ok decrypt")


def decrypt1(enc_string):
    genObj = fernetWrapper.Encryptor(password).decrypt_string_yield(enc_string)

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