import pytest
from pySecureCryptos import encoderDecoders

# function to get random bytes from file
def getByteList():
    fileName = "randomBytes.bin"

    with open(fileName , "rb") as file:
        data = file.read()
        data = data.split(b"~:~:~")
        data = data[:-1]

    return data
            



# function to test HexConvertor yield encode with HexConvertor decode
@pytest.mark.parametrize("byte" , getByteList())
def test_main(byte):
    genObj = encoderDecoders.HexConvertor.encode_yield(byte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            stringFromByte = ex.value
            break

    genObj = encoderDecoders.HexConvertor.decode_yield(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , "decoded byte does not match the original byte"





if __name__ == "__main__":
    getByteList()

