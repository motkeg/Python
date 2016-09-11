import socket


def Main():
        
    TCP_IP = '127.0.0.1'
    TCP_PORT = 4430
    BUFFER_SIZE = 1024
   
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print '''Hello ! you can use basic commands:
        >>> 'Q'=quit  
        >>> 'con'=Connect 
        >>> 'print' | 'p' = print users'''
    MESSAGE = raw_input(">>> Enter message:")
    while MESSAGE != 'Q':
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        print "(Client): received data  ", data
        MESSAGE = raw_input(">>> Enter message: ")
    print "Disconnect!"
    s.close()
        
    
 
 
if __name__ =="__main__":
    Main()    
   
     
    