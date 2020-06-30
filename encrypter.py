from pygame_function import *
import time
import random

space = ("!","@","#","$","=","^","*","&")

def encryption(b):
    cipher = ""
    for i in b:
        if i.isalpha():
            Alphabet = ord(i) + 3
            if Alphabet > ord("z"):
                Alphabet -= 26
            Letter = chr(Alphabet)
            cipher += Letter
        if i == " ":
            sign = random.choice(space)
            cipher += sign

    return(cipher)


screenSize(512,250)
setWindowTitle("Encrypter")
setBackgroundImage("back.png")
name = makeLabel("The Caeser Encrypter",60,50,50,"yellow","Arial Rounded MT Bold","clear")
showLabel(name)
with open("encrypt.txt","r")  as file:
    text = file.read()

content = encryption(text)

with open("encrypt.txt","w") as temp:
    temp.write(content)
time.sleep(1)
rk = makeLabel("PROCESSING",50,120,200,"green","Arial Rounded MT Bold","clear")
showLabel(rk)
time.sleep(0.5)
hideLabel(rk)
done = makeLabel("Done",50,120,200,"green","Arial Rounded MT Bold","clear")
showLabel(done)

endWait()