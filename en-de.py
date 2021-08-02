#Import
from base64 import *
import os

#Clear the terminal
os.system('clear')

#Picking a tool
EnDe = input('[Encode, Decode, Help, Quit]: ')

###########################################################

#Encode function
def Encode():
    Repeat = 1
    #User input and converting to "byte like object"
    EnInput = input('To be encoded: ')
    EnInput = EnInput.encode()
    #How many times to repeat
    EnRepeat = input('Encode how many times? ')
    EnRepeat = int(EnRepeat)

    while Repeat <= EnRepeat:

        #Encode the user input
        Encoded = standard_b64encode(EnInput)

        Repeat += 1

        EnInput = Encoded

    #Revert input to a string and print result
    Output = Encoded.decode()
    os.system('clear')
    print(Output)

#Decode function
def Decode():
    Repeat = 1
    #User input and converting to "byte like object"
    DeInput = input("To be decoded: ")
    DeInput = bytes(DeInput, 'utf-8')

    #How many times to repeat
    DeRepeat = input("Decode how many times? ")
    DeRepeat = int(DeRepeat)

    #Decode the user input
    while Repeat <= DeRepeat:

        Decoded = standard_b64decode(DeInput)

        Repeat += 1

        DeInput = Decoded
    #Revert input into a string and print result
    Decoded = Decoded.decode()
    os.system('clear')
    print(Decoded)

def FileEncode():
    File = input('Name of / Path to file: ')
    with open(File, 'r') as Opened:
        Contents = Opened.read()
    Writing = Contents.encode()
    Encoded = standard_b64encode(Writing)
    Output = Encoded.decode()
    with open(File, 'w+') as Outfile:
        Outfile.write(Output)

def FileDecode():
    File = input('Name of / Path to file: ')
    with open(File, 'r') as Opened:
        Contents = Opened.read()
    Writing = Contents.encode()
    Encoded = standard_b64decode(Writing)
    Output = Encoded.decode()
    with open (File, 'w+') as Outfile:
        Outfile.write(Output)

 ######################################################

#Running encode
if EnDe.lower() == "encode" or EnDe.lower() == "e":
    Encode()

if EnDe.lower() == "encode -f" or EnDe.lower() == "e -f":
    FileEncode()

#Running decode
elif EnDe.lower() == "decode" or EnDe.lower() == "d":
    Decode()

elif EnDe.lower() == "decode -f" or EnDe.lower() == "d -f":
    FileDecode()

#Quit option
elif EnDe.lower() == "quit" or EnDe.lower() == "q": 
    pass

elif EnDe.lower() == "help" or EnDe.lower() == "h":
    print("Base64 Multitool by Fr3ki \n Encode: Convert text to base64 (-f File mode) \n Decode: Decode Base64 into plain text (-f File mode) \n --For more information check ReadMe.md-- ")

#Invalid option
else:
    print("Enter A Valid Option")
