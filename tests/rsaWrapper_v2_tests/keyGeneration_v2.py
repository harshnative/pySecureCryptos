from pySecureCryptos import rsaWrapper_v2

class GetKey:

    keyGenObj = rsaWrapper_v2.KeyGenerator()

    keyPublic = keyGenObj.get_publicKey_bytes()

    keyPrivate = keyGenObj.get_privateKey_bytes()

    keyPublic_str = keyGenObj.get_publicKey_string()

    keyPrivate_str = keyGenObj.get_privateKey_string()