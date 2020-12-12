from Tkinter import *
  
root = Tk() 
root.geometry("300x300") 
root.title(" Conversion ") 
  
def Take_input(): 
    INPUT = Input_temp.get("1.0", "end-1c") 
    print(INPUT)
    fehr = ((int(INPUT)*9)/5) + 32
    con = str(fehr) + "F"
    Output_temp.insert(END, con) 
     
      
l = Label(text = "Enter Temperature in C") 
Input_temp = Text(root, height = 7, 
                width = 25, 
                bg = "light yellow") 
  
Output_temp = Text(root, height = 5,  
              width = 25,  
              bg = "light cyan") 
  
Display = Button(root, height = 2, 
                 width = 20,  
                 text ="Convert", 
                 command = lambda:Take_input()) 
  
l.pack() 
Input_temp.pack() 
Display.pack() 
Output_temp.pack() 
  
mainloop()