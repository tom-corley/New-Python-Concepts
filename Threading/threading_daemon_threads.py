import threading
import time

#Daemon threads do not have to finish for program to terminate
path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open("text.txt","r") as f:
            text = f.read()
        time.sleep(3)

def printloop():
    for x in range(10):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)
t1.start()
t2.start()