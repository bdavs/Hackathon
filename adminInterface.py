from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import readingfile as r
import writingfile as w
import time
import datetime
import sys
import test1 as cal


def add_field(root,dic,saveButton, addRow):
    e1=Entry(root, text='')
    choose_btn = Button(root, text='Choose',command=lambda:popup(root))
    e3=Entry(root, text='')
    e1.grid(row=root.heightvar+1, column=0)
    choose_btn.grid(row=root.heightvar+1, column=1)
    e3.grid(row=root.heightvar+1, column=2)
    dic['name'].append(e1)
    dic['date'].append(str(root.data))
    dic['speaker'].append(e3)
    root.heightvar+=1
    saveButton.grid(row=root.heightvar+1, column=2)
    addRow.grid(row=root.heightvar+1, column=0)

def save_entries(dic,saveButton,root):
    valueDict = {}
    print(root.data)
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
def adminScreen():
    root = Tk()
    root.data = {}

    root.heightvar = 3 #default number of new entries
    dic = {}
    dic['name'] = []
    dic['date'] = []
    dic['speaker'] = []


    for i in range(root.heightvar): #Rows
        #for v in val: #range(width): #Columns
        e1=Entry(root, text='')
        l2=Label(root,text='data')
        choose_btn = Button(root, text='Choose',command=lambda:popup(root))
        e3=Entry(root, text='')
        e1.grid(row=i+1, column=0)
        l2.grid(row=i+1, column=1)        
        choose_btn.grid(row=root.heightvar+1, column=1)
        e3.grid(row=i+1, column=2)
        dic['name'].append(e1)
        dic['date'].append(l2)
        dic['speaker'].append(e3)
    header=Label(root, text="Event Name")
    header.grid(row=0,column=0)
    header=Label(root, text="Date and Time")
    header.grid(row=0,column=1)
    header=Label(root, text="Speaker")
    header.grid(row=0,column=2)

    saveButton = Button(root, text='SAVE', command=lambda: save_entries(dic,saveButton,root))
    saveButton.grid(row=root.heightvar+1, column=2)
    addRow = Button(root, text='+', command=lambda: add_field(root,dic,saveButton,addRow))
    addRow.grid(row=root.heightvar+1, column=0)
    root.title("Admin Screen")

def popup(root):
            calendar1 = cal.Calendar(Tk(), root.data)
            print(root.data)

#adminScreen()
#display()
#mainloop()

