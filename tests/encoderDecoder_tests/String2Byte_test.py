import pytest
from pySecureCryptos import encoderDecoders

# function to get random bytes from file
def getStringList():
    fileName = "randomStrings.txt"

    with open(fileName , "r") as file:
        data = file.read()
        data = data.split("~:~:~")
        data = data[:-1]

    return data
            



# function to test String2Byte encode decode
@pytest.mark.parametrize("string" , getStringList())
def test_main(string):
    byteFromString = encoderDecoders.String2Byte.encode(string)

    stringAgain = encoderDecoders.String2Byte.decode(byteFromString)

    assert string == stringAgain , "decoded string does not match the original string"





if __name__ == "__main__":
    print(getStringList())

