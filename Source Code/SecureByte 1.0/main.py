import tkinter as tk
from tkinter import *

root=Tk()
root.title("SecureByte")
root.geometry("1000x500")
root.configure(bg="white")
root.iconbitmap("logo.ico")

frame1=LabelFrame(root,text="Pentest Tools",font=("Arial",16),padx=680,pady=50)
frame1.grid(row=1,column=1,pady=30)

frame2=LabelFrame(root,text="Other Tools",font=("Arial",16),padx=680,pady=50)
frame2.grid(row=2,column=1,pady=30)

frame3=LabelFrame(root,text="Report",font=("Arial",16),padx=680,pady=50)
frame3.grid(row=3,column=1,pady=30)

options1 = [ 
    "Port Scanner", 
    "XSS Scanner", 
    "Directory Brute Forcing",
    "Subdomain Scanner",
    "SQL Scanner"
] 

clicked1 = tk.StringVar() 
  
clicked1.set( "Select the tool" ) 

def tool1(t):
    click1=clicked1.get()
    if (click1==options1[0]):
        import portscan
    elif (click1==options1[1]):
        import xssscan
    elif (click1==options1[2]):
        import directorybruteforcing
    elif (click1==options1[3]):
        import subdomainscan
    elif (click1==options1[4]):
        import sqlscan

drop1 = OptionMenu( frame1 , clicked1 , *options1, command=tool1 ) 
drop1.grid(row=1,column=0,padx=20,pady=10)

options2 = [ 
    "Hash Creator", 
    "Brute Hash", 
    "System Directory Scanner",
    "Password Brute Forcing",
    "Zip File Cracker"
] 

clicked2 = tk.StringVar() 
  
clicked2.set( "Select the tool" ) 

def tool2(t):
    click2=clicked2.get()
    if (click2==options2[0]):
        import hashcreator
    elif (click2==options2[1]):
        import brutehash
    elif (click2==options2[2]):
        import systemdirectory
    elif (click2==options2[3]):
        import passwordbruteforcing

drop2 = OptionMenu( frame2 , clicked2 , *options2, command=tool2 ) 
drop2.grid(row=1,column=0,padx=20,pady=10)

def report():
    import report
    

button=Button(frame3,text=" Report Generation....",command=report)
button.grid(row=1,column=0,padx=20,pady=10)

root.mainloop()