import random

def main():
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    noOfStrings = 500

    minStringLen = 1
    maxStringLen = 1000

    fileName = "randomBytes_utf.bin"

    with open(fileName , "wb") as file:
        for i in range(noOfStrings):
            print(i)
            randomStr = ""
            for _ in range(random.randint(minStringLen , maxStringLen)):
                randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
                randomStr = randomStr + randomChar

            randomByte = bytes(randomStr , "utf-8")

            file.write(randomByte)
            file.write(b"~:~:~")

        
    print(f"Exported to {fileName}")

        

if __name__ == "__main__":
    main()