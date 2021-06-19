import tkinter as tk
from tkinter import *
import requests
import sys

root=Tk()
root.title("Subdomain Scanner")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the domain to scan:",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)
        
e1=Entry(root,font=("Arial",12))
e1.grid(row=1,column=2,pady=5)

def sub():
    domain = e1.get()
  
    file = open("subdomains.txt")
    content = file.read()
    subdomains = content.splitlines()
    discovered_subdomains = []

    f=open("output.txt",'w')
    sys.stdout=f 
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain:", url)
            discovered_subdomains.append(url)
    
    f.close()
    f=open("output.txt",'r').read()
    f1 = open("report.txt", "a")
    data = f
    f1.write(data)
    f1.close()
    Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
    label1=Label(root,text="Output Of Subdomain Scan",font=("Arial 18 underline"))
    label1.grid(row=5,column=3,padx=20,pady=10)
    #label2=Label(root,text=f,font=("Arial",12))
    #label2.grid(row=6,column=3,padx=20,pady=10)
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

button=Button(root,text="Start",command=sub)
button.grid(row=2,column=2,padx=30,pady=10)

root.mainloop()