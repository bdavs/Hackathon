from tkinter import *

root = Tk()

height = 3 #make number dynamic for number of entries
width = 3 #update number

for i in range(height): #Rows
    for j in range(width): #Columns
            b = Label(root, text="Hello")
             #pull information from reader
            b.grid(row=i+1, column=j)

e1=Label(root, text="Name")
e1.grid(row=0,column=0)
e2=Label(root, text="Date")
e2.grid(row=0,column=1)
#add remaining fields


mainloop()
