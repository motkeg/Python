import socket
import time



stop = False

def Main():
    
    def Print():
        print clients
        return str(clients)
    
   

    host = '127.0.0.1'
    port = 5000
    BUFFER_SIZE = 1024
    
    clients = []
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    s.setblocking(0)
    
    
    
    print "Waiting for connections...\n"   
    
    while not stop:
        try:
            data, addr = s.recvfrom(BUFFER_SIZE)
            print time.ctime(time.time())+ ":\t "+ 'Connection address:', addr    
            print time.ctime(time.time())+ ":\t "+"(Server):received data ", data.upper() 
            
            if "Q" in str(data):
                stop = True
            elif (data=="print" or data=="p" or data=="P"):
                data=Print()          
            if addr not in clients:
                clients.append(addr)
                print time.ctime(time.time())+":\t "+"Add new User: " ,addr
           
                
            print time.ctime(time.time()) + str(addr) + ": :" + str(data)
            for client in clients:
                s.sendto(data.upper(), client)
        except:
            #print "An Error happened!"
            pass
    print time.ctime(time.time())+":\t "+"  (server): user disconnected..."    
    s.close()
    
def Stop():
    stop=True   
    
if __name__ =="__main__":
    Main()
    