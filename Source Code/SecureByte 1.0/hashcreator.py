import tkinter as tk
from tkinter import *
import hashlib, bcrypt
import sys

root=Tk()
root.title("Hash Creator")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the password that encoded into hash:",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)

e1=Entry(root,font=("Arial",12))
e1.grid(row=1,column=2,pady=5)

def hash():
    password = e1.get()
    
    f=open("output.txt",'w')
    sys.stdout=f
    print("\nSHA1:\n")

    for i in range(1):
        setpass = bytes(password, 'utf-8')
        hash_object = hashlib.sha1(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)

    print("\nMD5:\n")

    for i in range(1):
        setpass = bytes(password, 'utf-8')
        hash_object = hashlib.md5(setpass)
        guess_pw = hash_object.hexdigest()
        print(guess_pw)

    print("\nBCRYPT:\n")

    for i in range(1):
        hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))
        print(hashed)
    f.close()
    f=open("output.txt",'r').read()
    f1 = open("report.txt", "a")
    data = f
    f1.write(data)
    f1.close()
    Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
    label1=Label(root,text="Output Of Hash Creator",font=("Arial 18 underline"))
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

button=Button(root,text="Start",command=hash)
button.grid(row=2,column=2,padx=30,pady=10)

root.mainloop()