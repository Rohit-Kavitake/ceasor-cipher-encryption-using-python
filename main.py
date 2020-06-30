
import random
import time


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

a = input("Enter your message here")
b= encryption(a)
print("The Encryption: {}".format(b))
c = decryption(b)
print("the Decryption:{}".format(c))