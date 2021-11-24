import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")


from pySecureCryptos import verifier_fernetWrapper as fernetWrapper

string = "my name is john and i am a programmer"

password = "hello world"

encString = "103065065065065065066104110103045110106084107075115115076112114080119074070050066109086071067101120095045101106098080117121101111072072070086119066083118080048117102102118085048090090065054107077073052095095099119057078122072103057077105122084079115075112090078072111054118118107078111103084049121090114045083120045106050088097055109116110083056053067054065049089072105099088088067117084045112056111051077114103102072067:checksum:103065065065065065066104110103045110056099065082110101072106085088117105050097089089116102105067072084114088121086107089055054111074105051068065120049108073067110085111072112089115120080112067122050071069049049057066052068057109112045102105056053049049109084113077083100089075076113071045077107119073095068109119085078071103088070073066052068101083121116052077090109066080066070105079057106052089067106106045048049087102120098055107082051118069069107102088084089084045089120120045107048081087080049072089066068116108089120114079049111122107084104069061"
encString2 = "103065065065065065066104110103045054121090118072078082111113084071095109088085105109056119103049085111065057052100089069111069068052090076087076057069115114119054056120086098045054072071045115050119122056106115065077079052078122090118067072081077050050120072095074105102068115052051083097115118115053050112106048113107076112078081117080048052048090057084099076121074069072078089054081065121111086076097083098049119052049:checksum:103065065065065065066104110103045054120107101121067085088119089101101100087073066053069052115084087101106067115068074105106045082068098074075071072080067050103076112067082068045083120075106119071109105110115055076107050110075086078087099088070084048111088056052071052088104086111116051115051068105088048055057075097122053097105073120120121101112079057075097115118114098080108080071072098086111105112110099114054057122090117087105105115101118069051102102052049053051089108051074102095105112074052067090086068066118049069122089110049101053073118110115061"

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
    # encrypt2()