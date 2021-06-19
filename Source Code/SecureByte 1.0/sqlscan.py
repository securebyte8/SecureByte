import tkinter as tk
from tkinter import *
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import sys

root=Tk()
root.title("SQL Scanner")
root.geometry("1000x500")
root.iconbitmap("logo.ico")

Label(root,text="Enter the URL to be scanned:",font=("Arial",12)).grid(row=1,column=1,padx=10,pady=5)
        
e1=Entry(root,font=("Arial",12))
e1.grid(row=1,column=2,pady=5)

def sql():
    url = e1.get()

    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"  
            
    f=open("output.txt",'w')
    sys.stdout=f    
            
    def get_all_forms(url):
        soup = bs(s.get(url).content, "html.parser")
        return soup.find_all("form")

    def get_form_details(form):
        details = {}
        try:
            action = form.attrs.get("action").lower()
        except:
            action = None
    
        method = form.attrs.get("method", "get").lower()
    
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            input_value = input_tag.attrs.get("value", "")
            inputs.append({"type": input_type, "name": input_name, "value": input_value})
    
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details

    def is_vulnerable(response):
        errors = {
            "you have an error in your sql syntax;",
            "warning: mysql",
            "unclosed quotation mark after the character string",
            "quoted string not properly terminated",
                }
                
        for error in errors:
            if error in response.content.decode().lower():
                return True
            return False

    def scan_sql_injection(url):
        for c in "\"'":
            new_url = f"{url}{c}"
            print("[!] Trying", new_url)
            res = s.get(new_url)
            if is_vulnerable(res):
                print("[+] SQL Injection vulnerability detected, link:", new_url)
                return

        forms = get_all_forms(url)
        print(f"[+] Detected {len(forms)} forms on {url}.")
        for form in forms:
            form_details = get_form_details(form)
            for c in "\"'":
                data = {}
                for input_tag in form_details["inputs"]:
                    if input_tag["type"] == "hidden" or input_tag["value"]:
                        try:
                            data[input_tag["name"]] = input_tag["value"] + c
                        except:
                            pass
                    elif input_tag["type"] != "submit":
                        data[input_tag["name"]] = f"test{c}"
                        
                url = urljoin(url, form_details["action"])
                if form_details["method"] == "post":
                    res = s.post(url, data=data)
                elif form_details["method"] == "get":
                    res = s.get(url, params=data)
            
                if is_vulnerable(res):
                    print("[+] SQL Injection vulnerability detected, link:", url)
                    print("[+] Form:")
                    pprint(form_details)
                    break
            
    scan_sql_injection(url)

    f.close()
    f=open("output.txt",'r').read()
    f1 = open("report.txt", "a")
    data = f
    f1.write(data)
    f1.close()
    Label(root,text="").grid(row=4,column=3,padx=20,pady=30)
    label1=Label(root,text="Output Of SQL Scan",font=("Arial 18 underline"))
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

button=Button(root,text="Start",command=sql)
button.grid(row=2,column=2,padx=30,pady=10)

root.mainloop()