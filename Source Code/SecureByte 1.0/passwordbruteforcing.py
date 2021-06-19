import tkinter as tk
from tkinter import *
import random
import string
import sys

root=Tk()
root.title("Password Brute Forcing")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the Password to crack:",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)

chars=string.printable
chars_list=list(chars)

e1=Entry(root,show="*",font=("Arial",12))
e1.grid(row=1,column=2,pady=5)

def password():
    password=e1.get()
    guess_password=""

    f=open("output.txt",'w')
    sys.stdout=f    
    while(guess_password!=password):
        guess_password=random.choices(chars_list,k=len(password))

        #print("<=========="+str(guess_password)+"===========>")

        if(guess_password==list(password)):
            print("Your Password is : "+ "".join(guess_password))
            break

    f.close()
    f=open("output.txt",'r').read()
    f1 = open("report.txt", "a")
    data = f
    f1.write(data)
    f1.close()
    Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
    label1=Label(root,text="Output Of Password Brute Forcing",font=("Arial 18 underline"))
    label1.grid(row=5,column=3,padx=20,pady=10)
    s=Scrollbar(root)
    s.grid(row=6,column=4)
    t=Text(root,yscrollcommand=s.set,padx=100,pady=50)
    t.grid(row=6,column=3)
    t.insert(END,data)
    s.config(command=t.yview)
            
    def rem():
        t.delete("1.0","end")

    button1=Button(root,text="clear",command=rem)
    button1.grid(row=7,column=3,padx=20)

button=Button(root,text="Start",command=password)
button.grid(row=2,column=2,padx=30,pady=10)


root.mainloop()