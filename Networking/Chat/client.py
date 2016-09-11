import socket
import threading



lock =threading.Lock()
Quit=False
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
port=0
BUFFER_SIZE = 1024


def recive(name,soc):
    while not Quit:
        try:
            lock.acquire()
            while True:
                data ,addr = soc.recvfrom(BUFFER_SIZE)
                print  data
        except:
            pass
        finally:
            lock.release()

def Main():
             
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP connection
    s.bind((TCP_IP, port))
    s.setblocking(0) 
    
    print '''Hello ! you can use basic commands:
    >>> 'Q': quit  
    >>> 'print' | 'p': print connected users '''
    name = raw_input(">>> Enter user name:")
    
    T=threading.Thread(target=recive ,args=(name,s))
    T.start()
    
    
    MESSAGE = raw_input(name +"::>>> ")
    while MESSAGE != 'Q':
        if MESSAGE !="":
            s.sendto(name+"::"+MESSAGE,(TCP_IP, TCP_PORT))
        
        lock.acquire()
        MESSAGE = raw_input(name +"::>>> ")
        lock.release()
        #time.sleep(0.2)
        
     
    Quit=True
    T.join()    
    print name +"::Disconnect!"
    s.close()
        
    
 
 
if __name__ =="__main__":
    Main()    
   
     
    