import random
import secrets


def main():

    fileName = "randomBytes.bin"

    noOfBytes = 500

    minByteLen = 1
    maxByteLen = 1000

    with open(fileName , "wb") as file:
        for i in range(noOfBytes):
            print(i)
            randomByte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

            file.write(randomByte)
            file.write(b"~:~:~")
    
    print(f"Exported to {fileName}")

      

if __name__ == "__main__":
    main()