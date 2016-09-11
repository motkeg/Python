import socket 
import time

def Main():   
    
    
    
    TCP_IP = '127.0.0.1'
    TCP_PORT = 4430
    BUFFER_SIZE = 1024

    clients=[]
    
    def Print():
        print clients
        return str(clients)
        
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP connection
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print "Waiting for connection..."   
    conn, addr = s.accept()
    print time.ctime(time.time())+'\t Connection address:', addr
    while True:
        try:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
                
            print time.ctime(time.time())+ "\t (Server):received data ", data.upper() 
            if (data=="con"):
                if addr not in clients:
                    clients.append(addr)
                print time.ctime(time.time())+"\t Add new User: " ,addr
                 
            elif (data=="print" or data=="p" or data=="P"):
                data=Print()  
                   
            conn.send(data.upper())  # echo
            
        except :
            print "An Error happened"
            pass
            
    print time.ctime(time.time())+"\t (server): user disconnected..."    
    conn.close()


if __name__ =="__main__":
    Main()
    