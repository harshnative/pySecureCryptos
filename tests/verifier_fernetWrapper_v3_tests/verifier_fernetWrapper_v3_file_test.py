from pySecureCryptos import verifier_fernetWrapper_v3 as vfw



def test_compatible():

    fileName_mainfile = "binFiles/verifier_fernetWrapper_v3_testcases_bin/bytes_mainFile.bin"
    fileName_decfile = "binFiles/verifier_fernetWrapper_v3_testcases_bin/dec/"
    fileName_decfile_name = "binFiles/verifier_fernetWrapper_v3_testcases_bin/dec/bytes_mainFile.bin"
    fileName_encfile = "binFiles/verifier_fernetWrapper_v3_testcases_bin/bytes_mainFile.bin.enc"
    fileName_key = "binFiles/verifier_fernetWrapper_v3_testcases_bin/key_bytes.bin"


    with open(fileName_key , "rb") as file:
        key = file.read()

    dec_obj = vfw.Encryptor.decrypt_file(fileName_encfile , fileName_decfile , key)

    for i in dec_obj:
        continue

    with open(fileName_decfile_name , "rb") as file:
        data = file.read()


    with open(fileName_mainfile , "rb") as file:
        data2 = file.read()

    assert data == data2 , "decrypted data does not match original data"




if __name__ == "__main__":
    test_compatible()
