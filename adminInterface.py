from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import readingfile as r
import writingfile as w
import time
import datetime
import sys
import test1 as cal


a = ['']
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
#        self._global_wealth = 1

    def add_field(self,root,dic,saveButton, addRow):
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

    def save_entries(self,dic,saveButton,root):
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

    
    # @property

#    def global_wealth_get(self):
#            return self._global_wealth


#    def global_wealth_set(self,value):
#        self._global_wealth = value
#        print("aaa")
        #for callback in self._observers:
        #    print('announcing change')
        #    callback(self._global_wealth)
    

    def adminScreen(self):
        #root = Tk()

        #global_wealth = 2
        
        root.data = {}
        #global_wealth =3
        
        root.heightvar = 3 #default number of new entries
        dic = {}
        dic['name'] = []
        dic['date'] = []
        dic['speaker'] = []

        caption = "hello?"
        content = StringVar()
        for i in range(root.heightvar): #Rows
            #for v in val: #range(width): #Columns
            e1=Entry(root, text='')
            e2=Entry(root,text=caption, textvariable=content)
            choose_btn = Button(root, text='Choose',command=lambda:self.popup(root,content))
            e3=Entry(root, text='')
#            e2.insert(0,"poop")
            content.set("test")
            e1.grid(row=i+1, column=0)
            e2.grid(row=i+1, column=1)
            choose_btn.grid(row=i+1, column=2)
            e3.grid(row=i+1, column=3)
            dic['name'].append(e1)
            dic['date'].append(e2)
            dic['speaker'].append(e3)
        header=Label(root, text="Event Name")
        header.grid(row=0,column=0)
        header=Label(root, text="Date and Time")
        header.grid(row=0,column=1)
        header=Label(root, text="Speaker")
        header.grid(row=0,column=3)

        saveButton = Button(root, text='SAVE', command=lambda: self.save_entries(dic,saveButton,root))
        saveButton.grid(row=root.heightvar+1, column=2)
        addRow = Button(root, text='+', command=lambda: self.add_field(root,dic,saveButton,addRow))
        addRow.grid(row=root.heightvar+1, column=0)
        root.title("Admin Screen")

    def popup(self,root,content):

#        lambda a:content[0].set(a[0]))
        
        calendar1 = cal.Calendar(tk.Tk(), a)
        print(calendar1.values)
        content.set(a[0])
#        temp = datetime.datetime.now().strftime("%A, %-d %B %Y %-I:%M%p")
#        print("content " + str(content[0]))
#
#    global_wealth = property(global_wealth_get, global_wealth_set)

if __name__ == '__main__':
#    print("hello")
#global_wealth=6
    root = tk.Tk()
    MainApplication(root).adminScreen()
#display()
    root.mainloop()

