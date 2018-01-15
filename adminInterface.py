from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import readingfile as r
import writingfile as w
import time

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
    valueDict = {}
    valueDict['name'] = []
    valueDict['date'] = []
    valueDict['speaker'] = []
    tempvar = ''
    for key,value in dic.items():
        for v in value:
            tempvar = v.get()
#            print(key + ": " + tempvar)
            valueDict[key].append(tempvar)

    for i in reversed(range(len(valueDict['name']))):
        if valueDict['name'][i] is '' and valueDict['date'][i] is '' and valueDict['speaker'][i] is '' :
            del valueDict['name'][i]
            del valueDict['date'][i]
            del valueDict['speaker'][i]
    w.writeToFile(valueDict)
    saveButton.config(text="SAVED!")
#    print("hello?!?!?")
def adminScreen():
    root = Tk()

    root.heightvar = 3 #default number of new entries
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


#adminScreen()
#display()
#mainloop()

