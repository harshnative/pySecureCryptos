import sys
sys.path.append("/media/veracrypt64/Projects/pyModules/pySecureCryptos/pySecureCryptos")

from pySecureCryptos import rsaWrapper

def generateKey():
    keyGenObj = rsaWrapper.KeyGenerator()

    privateKey_bytes = keyGenObj.get_privateKey_bytes()
    privateKey_Byte = keyGenObj.get_privateKey_Byte()

    publicKey_bytes = keyGenObj.get_publicKey_bytes()
    publicKey_Byte = keyGenObj.get_publicKey_Byte()


    with open("publickey.txt" , "wb") as file:
        file.write(publicKey_bytes)


    with open("privateKey.txt" , "wb") as file:
        file.write(privateKey_bytes)


myString = "hello world"

encString1 = "0aeae867e6ba1e955e4a4212117114070ec3f93b5276681cfc0bec0fcdb03e0e6b1c7706cb10626d5d06248d09c00b6946c07e4bbfee9b9aaf1f2a7498f0964fdf3d413a935d5c3da5aef8d5d30de4e00ca823cd4986d3265bd4d3ac41ad5c2158f8fc87a04fc3b3b4287db6fb83863341edfd21905df0ebef8240a88cd6e404d989a41cd724f24478a2d3fdf8aadfcbf3db76c95e7995241a3b3ae0a9642358d21ccc16ee72441830cecc206c9a79b97f280b8d972ffd49c32c2108ad518860b49ded28134783410dd4a9aad2640a1d95f7107990c36d0486a54b69b04ef81566c077b95cb49429d5171ce8a476f95acfbec54a7a81921e63d2ec23db0c667753c2af4e127fc7bad9f96e9704f1520ab23fd55b45e5f98e190776244d092aedc3fe47d378dd66fe48d4758e60f48f75168010941e9284ff647774893e00535fb961966cfc682cf70046df7a329e69fea7d7af7b8cc118f92770a4e80ebb738e4a1abf0b2697e29dfb8a083a1f73c80e92b3ea78dab0420657fdc16bd96b093788a4d32e5dfd71607483bc1dbc88f558b7d97a26cdfcd3672e807fee0852aaebf3a46e51d244b96e02f07870c4f00e91ec138230ce7c3f9a2b58185f9c93b3dbbffbea66b9dfc4e0d6bcecae7666567768d9e6bc615180f8c2bb98f92601601cf38ca8a2e07c59c97fcb975ce852220ea99102248b983eab884c053d37dd32f3:checksum:26c54b776baea8e412cca146686c79842ecc6c3adf71b00815cd23805eafd4f54b801061c096af1c55111c15a19b837c0d1aa035770ea04068dfcb5d1a52f6903825444e31e1085dbf6fa50c9d9b5ca02dfe1fb1f90bce86c60b7ea10d35766c9c66d65d02be8c759fe50362a14d35a71d4452975bb31e79e1adf3c4fccb555180a941ca48a0dbd8e16f56c430f85bd861abb118924d29139104e76da5dd77895888caea03c07546222d275dcb71d5d0abf03e4637fc59d06ccbce477b2c300eaea4e5917d27ded0668a77c4254ea30d1ea05a7daedf3e6b4de1a69654769b78a217af27fb4cad659d43d5930cd474d33d738999b10c960ff434c5b65273207d7dc394f5c0e4b5c9e8f340e0d013336db3a35228e83a2b51938d32eae1c1647428442160ba77a08141ba9c2e9ed8e3d346c1f8604d36b61a9a406be73c9b21a4aa15a035f86c467484037b1d87645b96d60087a4cd06f64a2fc9d6cc88d1ef9975a8010d81d8b1e76186af90a1fd3d45eb7a51f61fa668b092d211591bab0263d9297b7c3cf6846619b7d5d896f56d4aa3288248206f7a52c5ba576477b6aef76dcf8887c0542676da1a8d710de621d4d35c405f172b47b7694f6f700889f8ebffcb4af80b0716e708800fa6415d814ef43616738be13a1ba32520768b04619311a7134b9c06ce8306577e135f1dfed88c5490395a28bab7a4af71404110669b"

encString2 = "430c14d63eddb717ea9ae5ce9ed8eecdb2de6330188e1de2a4267e20bdc791d18d31754ba2e07a81bb53f437126c9800a68a7cb28730af6c32c315d2419a3aba8b79b73bb0b9e1682075a9405edd2632cf61aa91570d8da59031835471360fc920ee66bdc01db5323f4cf4f710d6dfad8b85a234bdfebb8df3c9f21910c369697c8501db22c2ac9f8e61d1e2121e3e180600c55d12b5cadcd6953ca8a2e14d16887e52bbe6cb86cf807fb489d0a17bb96f83182aefb327018791a9cda9992b098c8c504d16974b0ed6eb4355374a69b4b024998d8bfdb23f0755fe9cdb64c645e56584a7ae28bc42abdfed4f6cce5c318be116c48db0073227b1113fa0f522ba9e9be17199d9480ec3a293e8b4e03a335520ab606d8e2d334e7370ca19b21c9b6e660e44c0f4154b6fd4616e1e2fd1899966fbc04728d7834d15650ba7966f993cbdfe12873061dbabb2c6b709afc01ecc33952a5aea1c97f522c163d2a92fbff0ddb3f9476cb60b8da4d7621742642fe408607062afb528d01ed3f3b2b717eea13a11ee126b9250b74c610ffff336ee4bc3963c03e8159c1397e181db5a1a4ad50c0b7679ca98551b90cbec578aa00395c31a0c32a1bb49de9d8c1686164aee8fde441cd902d2012990cca7c3789cf891fb1888fe89093667c50bac25c8d4e760c6a718989706d625f0243b8151e6640c21345cd042bb83971f4a21f84c54e0:checksum:1bae9b715b6a4b781c8fd208cd06ac33c15e3e525e47588ed23ecaf041c55e81b6ec699ea65f4af35cc8927244bee224c2684fcfd6a0d25bdfad136272ee4446885e1d20ab92a51429df57a278c58b1518b3d273ca5f417169ca82a55e1dbc4e101383092b729f7eafac182036be7b7f97a3e344268a5fc4812ae014af1701ea410a649c169d4e5dcc372f33630d242b3a2f8f2e0fb3df472b6e8d4b1860492ccc37af2dbf7dda2e95c3552afcd9315e386ce01f6e98d7be5061194956162885e2ca10095008d81c90e6fab6e359afc66e8b8ce568f62467f7b9a23d7f20275847603360e023bf092c72925fe3280806fabf215903e25631b7c5a025a771ab67b4c8125098d4be22a6c9ee944d7d5644e13814b915ed4eea3e50df1bb58c49ce1157f94c6c0c05fad856e850d0dee601c9fe663cedabd39ebc2a28771013d8617e3b995fe3b1ddbec2f99fd404fc8f14d27a2bb51af39b630fd99a4f4ef8fc24f134ccd7c19330c176444eab42e082aaf9b1e23357640b0ce1cb9850ff228b923b81c08427d77c49bfedf60f4e41934622534bf1361d69604b19f877a49436016ee0023e3c33b3af78600d11934c1069c98a895961092ee144df653e35f4ee021949f59e4c1503f7799a3d60fee1e5765a11500c409eb82ec1d4e9a1bc904d3d6382f202f3544eeeb3cb28f7b95e282501cce7fae5b53516e5f093967e3a0407"



def enc():
    with open("publickey.txt" , "rb") as file:
        publicKey_bytes = file.read()


    with open("privateKey.txt" , "rb") as file:
        privateKey_bytes = file.read()


    encObj = rsaWrapper.Encryptor(publicKey_bytes , privateKey_bytes)

    encryptedString1 = encObj.encrypt_string(myString)

    genObj = encObj.encrypt_string_yield(myString)

    while(True):
        try:
            _ , _ = next(genObj)
        except StopIteration as ex:
            encryptedString2 = ex.value
            break

    print(encryptedString1)

    print('\n\n')

    print(encryptedString2)





def dec():
    with open("publickey.txt" , "rb") as file:
        publicKey_bytes = file.read()


    with open("privateKey.txt" , "rb") as file:
        privateKey_bytes = file.read()


    encObj = rsaWrapper.Encryptor(publicKey_bytes , privateKey_bytes)

    decryptedString1 = encObj.decrypt_string(encString1)

    genObj = encObj.decrypt_string_yield(encString1)

    while(True):
        try:
            _ , _ = next(genObj)
        except StopIteration as ex:
            decryptedString2 = ex.value
            break



    if(decryptedString1 == decryptedString2 == myString):
        print("ok")

    else:
        print("error")







def dec2():
    with open("publickey.txt" , "rb") as file:
        publicKey_bytes = file.read()


    with open("privateKey.txt" , "rb") as file:
        privateKey_bytes = file.read()


    encObj = rsaWrapper.Encryptor(publicKey_bytes , privateKey_bytes)

    decryptedString1 = encObj.decrypt_string(encString2)

    genObj = encObj.decrypt_string_yield(encString2)

    while(True):
        try:
            _ , _ = next(genObj)
        except StopIteration as ex:
            decryptedString2 = ex.value
            break



    if(decryptedString1 == decryptedString2 == myString):
        print("ok")

    else:
        print("error")



if __name__ == "__main__":
    # generateKey()
    # enc()
    dec()
    dec2()
    pass