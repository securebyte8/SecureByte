import tkinter as tk
from tkinter import *
import requests
import random
import time
import sys

root=Tk()
root.title("Directory Brute Forcing")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the url to scan the website :",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)
        
e1=Entry(root,font=("Arial",12))
e1.grid(row=1,column=2,pady=5)

def directory():
	url = e1.get()
	wordlist = "common1.txt"
	ext = ".php"

	f=open("output.txt",'w')
	sys.stdout=f 
	
	fo = open(wordlist,"r+")

	for i in range(30):
		word = fo.readline(10).strip()
		surl = url+word+ext
		response = requests.get(surl)
		if (response.status_code == 200):
			print ("[+] found :- ",surl)
		else:
			print ("[-] Not found :- ",surl)
			pass
	f.close()
	f=open("output.txt",'r').read()
	f1 = open("report.txt", "a")
	data = f
	f1.write(data)
	f1.close()
	Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
	label1=Label(root,text="Output Of Directory Brute Force",font=("Arial 18 underline"))
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
	
button=Button(root,text="Start",command=directory)
button.grid(row=2,column=2,padx=30,pady=10)

root.mainloop()