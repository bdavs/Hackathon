from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import readingfile as r
import writingfile as w
import adminInterface as adminInterface
import time

def display():
    disproot = Tk()

#    height = 3 #make number dynamic for number of entries #done
#    width = 3 #update number
    offset = 1

    #setup fonts
    headerFont = tkFont.Font(size=30,underline=True)
    currentEventFont = tkFont.Font(size=40,weight='bold')

    d = r.fileToDict() #import data from file

    #error checking
    #may require own function
    if d is -1:
        error=Label(disproot, text="No entries in table")
        error.grid(row=0,column=0)
        mainloop()
#        break
#        quit()
    currentEvent = True

    for i in range(len(d['name'])): #Rows
        #for v in val: #range(width): #Columns
        if currentEvent is True:
            l1=Label(disproot, text=d['name'][i],font=currentEventFont)
            l2=Label(disproot, text=d['date'][i],font=currentEventFont)
            l3=Label(disproot, text=d['speaker'][i],font=currentEventFont)
            currentEvent = False
        else:
            l1=Label(disproot, text=d['name'][i])
            l2=Label(disproot, text=d['date'][i])
            l3=Label(disproot, text=d['speaker'][i])
        l1.grid(row=i+1, column=0)
        l2.grid(row=i+1, column=1)
        l3.grid(row=i+1, column=2)

    header=Label(disproot, text="Event Name",font=headerFont)
    header.grid(row=0,column=0,padx=3,pady=3)
    header=Label(disproot, text="Date and Time",font=headerFont)
    header.grid(row=0,column=1,padx=3,pady=3)
    header=Label(disproot, text="Speaker",font=headerFont)
    header.grid(row=0,column=2,padx=3,pady=3)
    Button(disproot,text="Refresh").grid(row=0,column=3)
    disproot.title("Events")

display()
adminInterface.adminScreen()

mainloop()

