from tkinter import *
from tkinter import ttk
import readingfile as r
import time

def display():
    disproot = Tk()

#    height = 3 #make number dynamic for number of entries #done
#    width = 3 #update number


    d = r.fileToDict() #import data from file

    #error checking
    #may require own function
    if d is -1:
        error=Label(disproot, text="No entries in table")
        error.grid(row=0,column=0)
        mainloop()
        quit()

    for i in range(len(d['name'])): #Rows
        #for v in val: #range(width): #Columns
        e1=Label(disproot, text=d['name'][i])
        e2=Label(disproot, text=d['date'][i])
        e3=Label(disproot, text=d['speaker'][i])
        e1.grid(row=i+1, column=0)
        e2.grid(row=i+1, column=1)
        e3.grid(row=i+1, column=2)
        #add remaining fields
    header=Label(disproot, text="Event Name")
    header.grid(row=0,column=0)
    header=Label(disproot, text="Date and Time")
    header.grid(row=0,column=1)
    header=Label(disproot, text="Speaker")
    header.grid(row=0,column=2)
    disproot.title("Events")

def add_field(root,dic,saveButton, addRow):
    e1=Entry(root, text='')
    e2=Entry(root, text='')
    e3=Entry(root, text='')
    e1.grid(row=root.heightvar+1, column=0)
    e2.grid(row=root.heightvar+1, column=1)
    e3.grid(row=root.heightvar+1, column=2)
    dic['name'].append(e1)
    dic['date'].append(e2)
    dic['speaker'].append(e3)
    root.heightvar+=1
    saveButton.grid(row=root.heightvar+1, column=2)
    addRow.grid(row=root.heightvar+1, column=0)

def save_entries(dic,saveButton):
    for key,value in dic.items():
        for v in value:
            print(key + ": " + v.get())
#        print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
#    saveButton.config(text="SAVED!")
#    time.sleep(5)
#    saveButton.config(text="SAVE")
def adminScreen():
    root = Tk()

    root.heightvar = 4
    dic = {}
    dic['name'] = []
    dic['date'] = []
    dic['speaker'] = []


    for i in range(root.heightvar): #Rows
        #for v in val: #range(width): #Columns
        e1=Entry(root, text='')
        e2=Entry(root, text='')
        e3=Entry(root, text='')
        e1.grid(row=i+1, column=0)
        e2.grid(row=i+1, column=1)
        e3.grid(row=i+1, column=2)
        dic['name'].append(e1)
        dic['date'].append(e2)
        dic['speaker'].append(e3)
    header=Label(root, text="Event Name")
    header.grid(row=0,column=0)
    header=Label(root, text="Date and Time")
    header.grid(row=0,column=1)
    header=Label(root, text="Speaker")
    header.grid(row=0,column=2)
#    e2.pack()

    saveButton = Button(root, text='SAVE', command=lambda: save_entries(dic,saveButton))
    saveButton.grid(row=root.heightvar+1, column=2)
    addRow = Button(root, text='+', command=lambda: add_field(root,dic,saveButton,addRow))
    addRow.grid(row=root.heightvar+1, column=0)
    root.title("Admin Screen")

adminScreen()
#display()
mainloop()

