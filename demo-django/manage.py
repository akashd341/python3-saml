#!/usr/bin/env python
import os
import sys
import subprocess
import webbrowser
import multiprocessing
from demo import views
import PySimpleGUI as sg 
import socket
x="False"
y="False"
t="False"

def add():
    while(True):
        
        out = subprocess.check_output(['tasklist','/fi','imagename eq notepad.exe','/fo','csv'])
        result=out.decode('utf-8')
        # print(result)
        pk=result.split(',')
        try:
            #create client socket to recieve message
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((socket.gethostname(),1234))
            msg=s.recv(1024)
            global x
            global y
            x=str(msg.decode("utf-8"))
            # condition to prevent every time true auth in loop not open notepad
            if(x!=y and x=="True"):
                subprocess.call(["notepad.exe"])
            y=x
            print("new_data-->"+str(msg.decode("utf-8")))
        except:
            pass

        # print(pk[0].rstrip()=="INFO: No tasks are running which match the specified criteria.")
        if(pk[0].rstrip()=="INFO: No tasks are running which match the specified criteria."):
            
            continue
       
        else:
            global t
            # print("found taskkill /IM notepad.exe")
            if(x=="False"):
                subprocess.check_output(['taskkill','/IM','notepad.exe'])
                if(x!=t):
                    webbrowser.open('http://localhost:8000/?sso') 
                if(t=="False"):
                    event,values=sg.Window('OneLogin Protected App',[[sg.Text('Continue to Login')],[sg.Button('Continue')]],size=(300,100)).read(close=True)                
                    if(event=='Continue'):
                        webbrowser.open('http://localhost:8000/?sso')                  
                    else:
                        print("cancel")
                

                t=x
            
        
            

            continue
def sud():
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
    
    p1=multiprocessing.Process(name='p1',target=sud)
    p=multiprocessing.Process(name='p',target=add)
    p1.start()
    p.start()

    