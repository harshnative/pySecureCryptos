import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_fernetWrapper_v2_2 as fernetWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encString = "67414141414142687431453146376863645f335332487768704b656772336f69364c526454764f4e537371644f5334394e63745f453955675530657131303767484a595a67586f3469674370516a5a3136562d6f46644a54536a6d7a7962767a366535464b744d736f45684c626f6f5a786466744e3449546f424546384f553975566d617133624e66475164:checksum:6741414141414268743145316965546d5f2d534b66476636654a2d7549696666736c55546963344238686961574e775f613071367857737a7156717a6b65755f4f375854684f6a364d6b65794d7559705f35736a6d696564306d37547a41674355747a38556a6164712d6f355969566d56324b73417857507270705a6f376332705f38575445546e49495678"
encString2 = "67414141414142687431463634655a6f7363344b747665654f4752704663516c4b6a4c66707958553272535744314e69676c51475f7731477534687468726a4d734b535178365671394438686b4c394543773477394670524a727532414a684632515968454f4c4b3458454f6c69655039636d742d486e6c663842595251546953647033354d4c4a3066474a:checksum:6741414141414268743146365052476b31664c4f6f707350386f6a416658466d68534378376b355a4b696b6b395836416a75727971435071585677316932756345412d5151555256622d456865554842674536646342616c78686b506862423948587953584d466c6e687735593031307339574b6e44577373766c4e3569324e35656c32636e514773616d49"

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
    # encrypt2()