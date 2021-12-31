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
            



# function to test Byte2String encode with Byte2String_yield decode
@pytest.mark.parametrize("byte" , getByteList())
def test_main(byte):
    stringFromByte = encoderDecoders.Byte2String.encode(byte)

    genObj = encoderDecoders.Byte2String_yield.decode(stringFromByte)

    while(True):
        try:
            next(genObj)
        except StopIteration as ex:
            byteAgain = ex.value
            break

    assert byte == byteAgain , "decoded byte does not match the original byte"







if __name__ == "__main__":
    getByteList()

