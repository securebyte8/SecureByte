import tkinter as tk
from tkinter import *

new=Tk()
new.title("Report")
new.geometry("1000x500")
new.iconbitmap("logo.ico")
    
scrollbar=Scrollbar(new)
scrollbar.pack(side="right",fill="y")

t = Text(new, width = 15, height = 50, wrap = NONE,yscrollcommand = scrollbar.set)
t.pack(side="top", fill="both")

f=open("report.txt",'r').read()
data=f
t.insert(END,"The reports are displayed below..\n\n")
t.insert(END,data)
   
scrollbar.config(command=t.yview)
new.mainloop()