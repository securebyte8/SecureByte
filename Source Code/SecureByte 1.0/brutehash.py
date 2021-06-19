import tkinter as tk
from tkinter import *
from urllib.request import urlopen, hashlib
import sys

root=Tk()
root.title("Brute Hash")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the hash that decoded into password:",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)

e1=Entry(root,font=("Arial",12))
e1.grid(row=1,column=2,pady=5)

def brute():
    sha1hash = e1.get()
    .0
    f=open("output.txt",'w')
    sys.stdout=f
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == sha1hash:
            print("The password is ", str(guess))
            break
        elif hashedGuess != sha1hash:
            print("Password guess ",str(guess)," does not match, trying next...")
        else:
            print("Password not in database, we'll get them next time.")
    f.close()
    f=open("output.txt",'r').read()
    f1 = open("report.txt", "a")
    data = f
    f1.write(data)
    f1.close() 
    Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
    label1=Label(root,text="Output Of Brute Hash",font=("Arial 18 underline"))
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

button=Button(root,text="Start",command=brute)
button.grid(row=2,column=2,padx=30,pady=10)

root.mainloop()