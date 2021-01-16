from tkinter import *
import math
def main():
############################################################
    #Decoder logic function
    def decoder(inpt):
        Z = int(inpt)
        #Logic
        W = math.floor(((math.sqrt(8*Z+1) - 1) / 2))
        T = (math.pow(W,2)+ W)/2
        global Y
        Y = Z - T
        global X
        X = W - Y
        return X,Y
    def encoder(inptx,inpty):
        X = int(inptx)
        Y = int(inpty)
        #Logic
        bracket1 = (X + Y + 1)
        bracket2 = (X + Y)
        global Z
        Z = (bracket1 * bracket2 / 2) + Y
        return Z
################################################################
    #create a GUI window 
    gui = Tk() 
    #set background color
    gui.configure(background="light green") 
    # set the title of GUI window 
    gui.title("Cantor's pairing") 
    # set the configuration of GUI window 
    gui.geometry("1000x1000")
    
    lbly = Label(gui, text="Enter Y:",font=("Arial Bold", 11), bg="light green")
    lbly.grid(column=0, row=36)
    
    lblx = Label(gui, text="Enter X:",font=("Arial Bold", 11), bg="light green")
    lblx.grid(column=0, row=37)
    
    lblz= Label(gui, text="Enter Z:",font=("Arial Bold", 11), bg="light green")
    lblz.grid(column=0, row=4)
    
    lblban1= Label(gui, text="DECODE:",font=("Arial Bold", 12),fg="blue", bg="light green")
    lblban1.grid(column=0, row=1)

    lblban2= Label(gui, text="ENCODE",font=("Arial Bold", 12),fg="blue", bg="light green")
    lblban2.grid(column=0, row=15)

    lblen= Label(gui, text="ResultX,Y",font=("Arial Bold", 11), bg="light blue")
    lblen.grid(column= 3, row=36)
    
    lblde= Label(gui, text="Result Z",font=("Arial Bold", 11), bg="light blue")
    lblde.grid(column = 3, row = 4)
    #Entry for decoding
    txty = Entry(gui,width=10)
    txty.grid(column=1, row=36)
    
    txtx = Entry(gui,width=10)
    txtx.grid(column=1, row=37)
    
    txtz = Entry(gui,width=10)
    txtz.grid(column=1, row=4)

    #click function
    def clickedde():
        inpt = txtz.get()
        if inpt.isnumeric() and inpt != "0":
             ref = decoder(inpt)
             lblde.configure(text = ref)
        else:
             lblde.configure(text= "Please enter positive integers only!")
    def clickedee():
        inptx = txtx.get()
        inpty = txty.get()
        if (inptx.isnumeric() and inptx !="0") and (inpty.isnumeric() and inpty != "0"):
            refr = encoder(inptx,inpty)
            lblen.configure(text = refr)
        else:
            lblen.configure(text = "Please enter positive integers only!")
    #Decode button
    btn1 = Button(gui, text="Enter Z", command=clickedde)
    btn1.grid(column=2, row=4)
    btn2 = Button(gui, text="Enter X,Y", command=clickedee)
    btn2.grid(column=2, row=39)
    #run
    gui.mainloop()




#Driver code
if __name__ == "__main__": 
    main()
    