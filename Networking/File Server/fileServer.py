import socket
import threading
import os


host = '127.0.0.1'
port = 4430
BUFFER_SIZE = 1024

def retrive(name,sock):
    filename=sock.recv(BUFFER_SIZE)
    if os.path.isfile(filename):
        sock.send("Exists"+ filename +" (size): " + str(os.path.getsize(filename)))
        respond=sock.recv(BUFFER_SIZE)
        
        if respond[:3] == "yes":
            with open(filename, 'rb') as f:
                byts=f.read(BUFFER_SIZE)
                sock.send(byts)
                while byts != "":
                    byts=f.read(BUFFER_SIZE)
                    sock.send(byts)
                    
    else:
        sock.send("Error :"+ filename +"Not Exists !" )
        
    sock.close()
    
    
    
def Main():
    s = socket.socket() # A default TCP connection 
    s.bind((host,port))
    s.listen(5)
    
    print "Wait for Connections..."
    
    while True:
        conn ,addr = s.accept()
        print "Client connected on : <" + str(addr) +">"
        
        T = threading.Thread(target=retrive ,args=("RetriveThread" ,conn))
        T.start()
        
    s.close() 
    print "(Server) Disconnecting.."
 
    
if __name__ =="__main__":
    Main()       
        
            
    