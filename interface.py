from tkinter import *
from tkinter import ttk
import readingfile as r

root = Tk()

height = 3 #make number dynamic for number of entries
width = 3 #update number

d = r.fileToDict() #import data from file

#error checking
#may require own function
if d is -1:
    error=Label(root, text="No entries in table")
    error.grid(row=0,column=0)
    mainloop()
    quit()

for i in range(len(d['name'])): #Rows
    #for v in val: #range(width): #Columns
    e1=Label(root, text=d['name'][i])
    e2=Label(root, text=d['date'][i])
    e1.grid(row=i+1, column=0)
    e2.grid(row=i+1, column=1)
    #add remaining fields
header=Label(root, text="Event Name")
header.grid(row=0,column=0)
header=Label(root, text="Event Date")
header.grid(row=0,column=1)

mainloop()
