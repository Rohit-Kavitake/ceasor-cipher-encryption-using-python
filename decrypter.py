from pygame_function import *
import time
import random
space = ("!","@","#","$","=","^","*","&")
def decryption(b):
    decry = ""
    for i in b:
        if i.isalpha():
            if i == "a":
               decry+="x"
            elif i == "b":
                decry+= "y"
            elif i == "c":
                decry+= "z"
            else:
                alphabet = ord(i)-3
                decry+= chr(alphabet)
        if i in space:

            decry += " "

    return decry


screenSize(512,250)
setWindowTitle("Encrypter")
setBackgroundImage("back.png")
name = makeLabel("The Caeser Decrypter",60,50,50,"yellow","Arial Rounded MT Bold","clear")
showLabel(name)
with open("encrypt.txt","r")  as file:
    text = file.read()

content = decryption(text)

with open("decrypt.txt","w") as temp:
    temp.write(content)
time.sleep(1)
rk = makeLabel("PROCESSING",50,120,200,"green","Arial Rounded MT Bold","clear")
showLabel(rk)
time.sleep(0.5)
hideLabel(rk)
done = makeLabel("Done",50,120,200,"green","Arial Rounded MT Bold","clear")
showLabel(done)

endWait()