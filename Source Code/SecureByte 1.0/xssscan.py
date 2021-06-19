import tkinter as tk
from tkinter import *
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import sys

root=Tk()
root.title("XSS Scanner")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the URL to be scanned:",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)
        
e1=Entry(root,font=("Arial",12))
e1.grid(row=1,column=2,pady=5)
        
def xss():
    url = e1.get()
            
    f=open("output.txt",'w')
    sys.stdout=f    
    def get_all_forms(url):
        soup = bs(requests.get(url).content, "html.parser")
        return soup.find_all("form")

    def get_form_details(form):
        details = {}
        action = form.attrs.get("action").lower()
        method = form.attrs.get("method", "get").lower()
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details

    def submit_form(form_details, url, value):
        target_url = urljoin(url, form_details["action"])
        inputs = form_details["inputs"]
        data = {}
        for input in inputs:
            if input["type"] == "text" or input["type"] == "search":
                input["value"] = value
            input_name = input.get("name")
            input_value = input.get("value")
            if input_name and input_value:
                data[input_name] = input_value

            if form_details["method"] == "post":
                return requests.post(target_url, data=data)
            else:
                return requests.get(target_url, params=data)

    def scan_xss(url):
        forms = get_all_forms(url)
        print(f"[+] Detected {len(forms)} forms on {url}.")
        js_script = "<Script>alert('hi')</scripT>"
        is_vulnerable = False
        for form in forms:
            form_details = get_form_details(form)
            content = submit_form(form_details, url, js_script).content.decode()
            if js_script in content:
                print(f"[+] XSS Detected on {url}")
                print(f"[*] Form details:")
                pprint(form_details)
                is_vulnerable = True
            return is_vulnerable

    print(scan_xss(url))
    f.close()
    f=open("output.txt",'r').read()
    f1 = open("report.txt", "a")
    data = f
    f1.write(data)
    f1.close()
    Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
    label1=Label(root,text="Output Of XSS Scan",font=("Arial 18 underline"))
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

button=Button(root,text="Start",command=xss)
button.grid(row=2,column=2,padx=30,pady=10)

root.mainloop()