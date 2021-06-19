import tkinter as tk
from tkinter import *
import socket
import time
import threading
from queue import Queue
import sys

root=Tk()
root.title("Port Scanner")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the host to be scanned:",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)
        
e1=Entry(root,font=("Arial",12))
e1.grid(row=1,column=2,pady=5)

def portscan():
    target = e1.get()
            
    f=open("output.txt",'w')
    sys.stdout = f
            
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()
    t_IP = socket.gethostbyname(target)
    print ('Starting scan on host: ', t_IP)
    
    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((t_IP, port))
            with print_lock:
                print(port, 'is open')
            con.close()
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()
      
    q = Queue()
    startTime = time.time()
    
    for x in range(100):
        t = threading.Thread(target = threader)
        t.daemon = True
        t.start()
   
    for worker in range(1, 500):
        q.put(worker)
   
    q.join()
    print('Time taken:', time.time() - startTime)

    f.close()
    f=open("output.txt",'r').read()
    f1 = open("report.txt", "a")
    data = f
    f1.write(data)
    f1.close()
    Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
    label1=Label(root,text="Output Of Port Scan",font=("Arial 18 underline"))
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
            
button=Button(root,text="Start",command=portscan)
button.grid(row=2,column=2,padx=30,pady=10)

root.mainloop()