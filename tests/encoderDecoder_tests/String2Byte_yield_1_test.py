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
            



# function to test String2Byte_yield encode with String2Byte decode
@pytest.mark.parametrize("string" , getStringList())
def test_main(string):
    gen = encoderDecoders.String2Byte_yield.encode(string)

    while(True):
        try:
            next(gen)
        except Exception as ex:
            byteFromString = ex.value
            break

    stringAgain = encoderDecoders.String2Byte.decode(byteFromString)

    assert string == stringAgain , "decoded string does not match the original string"





if __name__ == "__main__":
    print(getStringList())

