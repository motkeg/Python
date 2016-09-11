import socket
from tkinter import *
import tkFileDialog as fd
import os

host = '127.0.0.1'
port = 4430
BUFFER_SIZE = 1024


def Main():
    root = Tk()
    root.withdraw()
    filename = fd.askopenfilename()
    stop = False
    
    
    while not stop:
        s = socket.socket()
        s.connect((host ,port))
        
        #filename = raw_input(">>> Enter file name:")
        if filename !="":
            s.send(filename)
            if os.path.isfile(filename):
                filesize = long(os.path.getsize(filename))
            
            ans = s.recv(BUFFER_SIZE)
            if ans[:6]=="Exists":
                massege= raw_input("file exists do want Download [yes/no]:")
                if massege == "yes":
                    s.send("yes")
                    
                    f = open( filename+"(newFromServer)" ,'wb')#"download/(newFromServer)" +
                    data = s.recv(BUFFER_SIZE)
                    total = len(data)
                    f.write(data)
                    while total < filesize:
                        data = s.recv(BUFFER_SIZE)
                        total += len(data)
                        f.write(data)
                        
                        print "{0}".format((total/float(filesize))*100)+ "% Done"
                    print "Download Complete!" 
                    
            else:
                print  "Error: File does NOT exists!"           
            massege= raw_input("Stop? [yes/no]:")
            if massege == "yes": stop =True
            
            s.close()
    print "Disconnecting.."
    
if __name__ =="__main__":
    Main()       
                    
            
            
    
    