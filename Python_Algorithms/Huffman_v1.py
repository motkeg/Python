import operator

                     
            

class node():
    def __init__(self,path):
        self.path=path
        self.array=self.__build_array()
        self.MapTree=self.__build_Tree()
        self.encode=self.__encode()
        
        
        
        
        
    def __build_array(self):
        arr={}
        file=open(self.path,'r')
        for l in file:
            for w in l:
                arr[w]=0
        file.close()
        file=open(self.path,'r')        
        for l in file:
            for w in l:
                arr[w]=arr[w]+1
        file.close()    
        return sorted( arr.items(), key=operator.itemgetter(1))   
            
        
        
    def __build_Tree(self):
        
        map=self.array
        temp=[]
        while len(map) >1:
            temp=[]
            tree=((map[0],map[1]),map[0][1]+map[1][1])
            temp.append(tree)
            for i in map[2:]:
                temp.append(i)
            map=temp    
            map.sort(key=lambda tup: tup[1])             
        return tree
    
    
    
    def __encode(self):
               
        it,ch ,enc=type(1),type("w"),{}
    
        ##################################
        def build(map,dir=""):            
                                           
            if type(map[0])==ch:           
                enc[map[0]]=dir            
                                           
            else:                          
                build(map[0][0],dir+'0')   
                build(map[1][0],dir+'1')   
        ###################################        
        build(self.MapTree[0])     
        return enc  
               
    def Encode_txt(self):
        write=open("Huffman-encode.txt","w")
        file=open(self.path,'r')
        for l in file:
            for w in l:
                write.write(self.encode[w])
         
        write.close()                    
        print "write END success"  
        
        
    def Decode_txt(self,dec_path):
        read=open(dec_path,'r')
        write=open("Huffman-decode.txt",'w')
        temp=self.MapTree[0]
        for l in read:
            for w in l:
                if type(temp[int(w)][0])==type("d"):
                    write.write(temp[int(w)][0])
                    temp=self.MapTree[0]
                
                else:
                    temp=temp[int(w)][0]  
        read.close()
        write.close()    
        print "Decode END Success"
                  
            
##############################################################3


n=node("text.txt")
print "arry: {0}".format( n.array)
print "tree: {0}".format( n.MapTree)
print "encode: {0}".format(n.encode)
n.Encode_txt()
n.Decode_txt('Huffman-encode.txt')
           
        