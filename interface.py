from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

import readingfile as r
import writingfile as w
import adminInterface as adminInterface
import calendarApp as cal

import datetime

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    def display(self):
#        disproot = Tk()

        disproot.data = {}
    #    height = 3 #make number dynamic for number of entries #done
    #    width = 3 #update number
        offset = 1

        #setup fonts
        headerFont = tkFont.Font(root=self.parent,size=30,underline=True)
        currentEventFont = tkFont.Font(root=disproot,size=40,weight='bold')
        eventFont = tkFont.Font(root=disproot,size=15)

        d = r.fileToDict() #import data from file

        #error checking
        #may require own function
        if d is -1:
            error=Label(disproot, text="No entries in table")
            error.grid(row=0,column=0)
            mainloop()

        currentEvent = True

        for i in range(len(d['name'])): #Rows
            #current events in bold
            if currentEvent is True:
                l1=Label(disproot, text=d['name'][i],font=currentEventFont)
                l2=Label(disproot, text=d['date'][i],font=currentEventFont)
                l3=Label(disproot, text=d['speaker'][i],font=currentEventFont)
                currentEvent = False
            #other events smaller
            else:
                l1=Label(disproot, text=d['name'][i],font=eventFont)
                l2=Label(disproot, text=d['date'][i],font=eventFont)
                l3=Label(disproot, text=d['speaker'][i],font=eventFont)
            l1.grid(row=i+1, column=0)
            l2.grid(row=i+1, column=1)
            l3.grid(row=i+1, column=2)

        #set up headers in larger font
        header=Label(disproot, text="Event Name",font=headerFont)
        header.grid(row=0,column=0,padx=3,pady=3)
        header=Label(disproot, text="Date and Time",font=headerFont)
        header.grid(row=0,column=1,padx=3,pady=3)
        header=Label(disproot, text="Speaker",font=headerFont)
        header.grid(row=0,column=2,padx=3,pady=3)

        #add refresh button
        Button(disproot,text="Refresh",command=lambda:self.refresh(disproot)).grid(row=0,column=3)

        temp = datetime.datetime.now().strftime("%A, %-d %B %Y %-I:%M%p")
        Label(disproot,text=temp).grid(row=2,column=3)

        choose_btn = Button(disproot, text='Choose',command=lambda:self.popup(disproot))
        show_btn = Button(disproot, text='Show Selected',command=lambda:self.print_selected_date(disproot))
        choose_btn.grid(row=3,column=3)
        show_btn.grid(row=4,column=3)
        #set up window
        disproot.title("Events")
       # disproot.attributes("-zoomed",True)
        disproot.grid_columnconfigure([0,1,2,3],weight=1)

    def refresh(self,disproot):
    #refresh currently just destroys the current window and redraws it.
    #in future maybe make it just update the list dynamically
        disproot.destroy()
        self.display()

    def popup(self,disproot):
                #child = tk.Toplevel()
                calendar1 = cal.Calendar(Tk(), disproot.data)

    def print_selected_date(self,disproot):
                print(disproot.data)



if __name__ == "__main__":


    disproot = tk.Tk()
#    disproot = tk.Toplevel(root)
    MainApplication(disproot).display()
#    display()
    disproot.mainloop()


#    MainApplication.display()
#    adminInterface.MainApplication.adminScreen(self)
#
#    mainloop()

