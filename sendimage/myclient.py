import socket
import threading
import time
import pyautogui

a=pyautogui.prompt(text="Enter IP of Server.", title='Server IP' , default='Type your IP')
print(a)

HOST = a    # The remote host
PORT = 50000              # The same port as used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))
except ConnectionRefusedError:
    a=pyautogui.alert(text='Your Server IP is Wrong! Please exit and try again!', title='Warning!', button='Exit')
    if a=="Exit":
        quit()
f=open("images/a1.jpg", "rb")
s.send(f.read())
f.close()
