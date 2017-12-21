from tkinter import *
from tkinter import ttk
import readingfile as r

def display():
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
    root.title("Events")

def show_entry_fields(dic):
    for key,value in dic.items():
        for v in value:
            print(key + ": " + v.get())
#        print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def adminScreen():
    root = Tk()
    dic = {}
    dic['name'] = []
    dic['date'] = []


    for i in range(3): #Rows
        #for v in val: #range(width): #Columns
        e1=Entry(root, text='')
        e2=Entry(root, text='')
        e1.grid(row=i+1, column=0)
        e2.grid(row=i+1, column=1)
        dic['name'].append(e1)
        dic['date'].append(e2)

    header=Label(root, text="Event Name")
    header.grid(row=0,column=0)
    header=Label(root, text="Event Date")
    header.grid(row=0,column=1)
#    e2.pack()

    Button(root, text='SAVE', command=lambda: show_entry_fields(dic)).grid(row=4, column=0)
    root.title("Admin Screen")

adminScreen()
#display()
mainloop()

