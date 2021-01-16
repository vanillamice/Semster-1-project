import math

#Functionality 1
def encoder():
    #input validation
    positive = False
    while positive == False:
        inpt1 = input("Enter X:")
        inpt2 = input("Enter Y:")
        if (inpt1.isnumeric() and inpt1 != "0") and (inpt2.isnumeric() and inpt2 != "0"):
            positive = True
            X = int(inpt1)
            Y = int(inpt2)
            #Logic
            bracket1 = (X + Y + 1)
            bracket2 = (X + Y)
            Z = (bracket1 * bracket2 / 2) + Y
            return Z
            break
        else:
            print("Please enter positive integers!!")

#Functionality 2
def decoder():
    #Input validation
    positive = False
    while positive == False:
        inpt = input("Enter Z:")
        if  inpt.isnumeric() and inpt != "0":
            positive = True
            Z = int(inpt)
             #Logic
            W = math.floor(((math.sqrt(8*Z+1) - 1) / 2))
            T = (math.pow(W,2)+ W)/2
            Y = Z - T
            X = W - Y
            return X,Y
        else:
            print("Please enter a positive integer!!")
   
#to drive the code without the GUI
while True:
    print("Enter 1 for encoding, 0 for decoding.")
    f = int(input(":"))
    if f == 1:
        print("Z = ",encoder())
    elif f == 0:
        print("π",decoder())
        break
    else:
        print("invalid")
        break