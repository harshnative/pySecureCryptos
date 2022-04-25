import os
import sys

def main():
    pathToPackage = "../dist/"
    
    choice = input("Type < continue > if the virtual env is activated : ")

    if(choice.strip().lower() != "continue"):
        print("\nUser exit\n")
        sys.exit()

    
    for i in os.listdir(pathToPackage):
        if("tar.gz" in i):
            os.system("pip uninstall pySecureCryptos")
            os.system(f"pip install {pathToPackage + i}")
            break


if __name__ == "__main__":
    main()