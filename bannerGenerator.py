from pyfiglet import Figlet
import pyperclip



# Figlet object
custom_fig = Figlet(width=99**99)

# input text to render
text = input("Enter text : ")

print()

# re arrange text to increase spacing btw chars
newText = ""

for i in text:
    if(i == " "):
        newText = newText + "    "
    else:
        newText = newText + i
    
    newText = newText + " "


# print rearranged text
print(newText)

# write rendered text to output file
toOutput = custom_fig.renderText(newText)

with open("rendered_Text.txt" , "w") as file:
    file.write(toOutput)

print("\ncopied to clipboard :)\n")

pyperclip.copy(toOutput)


