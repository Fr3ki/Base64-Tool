#Import
from base64 import *

#A surprise tool that will help us later
FiveX = 1

#Picking a tool
EnDe = input('Encode or Decode? ')

#Encode option
if EnDe.lower() == "encode":
   
    #User input and converting to "byte like object"
    EnInput = input('To be encoded: ')
    EnInput = bytes(EnInput, 'utf-8')
    
    #How many times to repeat
    EnRepeat = input('Encode how many times? ')
    EnRepeat = int(EnRepeat)

    while FiveX <= EnRepeat:
        
        #Encode the user input
        Encoded = standard_b64encode(EnInput)
        
        FiveX += 1
        
        EnInput = Encoded
   
    #Print result
    print("Please excuse the b''")
    print(Encoded)


#Decode option
elif EnDe.lower() == "decode":

    #User input and converting to "byte like object"
    DeInput = input("To be decoded: ")
    DeInput = bytes(DeInput, 'utf-8')

    #How many times to repeat
    DeRepeat = input("Decode how many times? ")
    DeRepeat = int(DeRepeat)
    
    #Decode the user input
    while FiveX <= DeRepeat:
        
        Decoded = standard_b64decode(DeInput)
        
        FiveX += 1

        DeInput = Decoded
    #Print result
    print("Please excuse the b''")
    print(Decoded)

#Quit option
#elif EnDe == "Quit":


#Invalid option
else:

    print("Enter A Valid Option")
