from Tkinter import *
  
root = Tk() 
root.geometry("300x300") 
root.title(" Check Prime ") 
  
def Take_input(): 
    INPUT = Input_temp.get("1.0", "end-1c") 
    print(INPUT)
    no = int(INPUT)
    c = 0
    for i in range(1,no):
        if no % i == 0:
            c += 1
    if c > 2:
        Output_temp.insert(END, 'False') 
    else:
        Output_temp.insert(END, 'True')
     
      
l = Label(text = "Enter a Number") 
Input_temp =  Text(root, height = 7, width = 25)  
Output_temp = Text(root, height = 5, width = 25)  
Display =   Button(root, height = 2, width = 20, text ="Check", command = lambda:Take_input()) 
  
l.pack() 
Input_temp.pack() 
Display.pack() 
Output_temp.pack() 
  
mainloop()