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
            



# function to test HexConvertor encode decode
@pytest.mark.parametrize("byte" , getByteList())
def test_main(byte):
    stringFromByte = encoderDecoders.HexConvertor.encode(byte)

    byteAgain = encoderDecoders.HexConvertor.decode(stringFromByte)

    assert byte == byteAgain , "decoded byte does not match the original byte"





if __name__ == "__main__":
    getByteList()

