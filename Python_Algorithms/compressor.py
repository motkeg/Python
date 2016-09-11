
letters=['a','b','c','d','f','g','h']


def compress(file_to_read,target_name,single=0):#you can send '1' in the function call to compress the txt to single line  
    voc=[]
    text=""
    try:
        #open files
        read_file=open(file_to_read,'r')
        write_file=open(target_name,'w')
        
        count=1
        
        for line in read_file:
            i=0
            if len(line)%2==0:
                n=len(line)-1
            else:
                n=len(line)-2
            #### compressing
            while i < n:
                while i<n and line[i]==line[i+1] and line[i] in letters:
                    count+=1
                    i+=1
               
                voc.append((line[i],count)) 
                i+=1  
                count=1 
            if single==0:    
                voc.append(("\n",1))    
             
        if n%2==0:              
            voc.append((line[i],1))    
                      
    ############### write to new file ####################   
        write_file.write(str(voc)+"\n") 
        for k in voc:
            text+=str(k[0]) 
        write_file.write(text)  
        
        read_file.close()
        write_file.close()        
        print "End Compressing!!" 
        
               
    except ValueError,IOError:
        print "ERROR: file could not open!/index error (ValueError,IOError)"
        


def DEcompress(compFile_to_read,target_name):
    text=""
    try:
        #open files
        read_file=open(compFile_to_read,'r')
        write_file=open(target_name,'w')
        
        voc=eval(read_file.readline())
        
        
        for key in voc:
            
            for j in xrange(key[1]):
                text+=str(key[0])
                
            
        ############ write the uncompress txt
        write_file.write(text)  
        
        read_file.close()
        write_file.close()        
        print "End Decompressing!"
        
        
        
    except ValueError,IOError:
        print "ERROR: file could not open!/index error (ValueError,IOError)"
    
        
        
        
compress("text.txt", "comp_out.txt",1)        
DEcompress("comp_out.txt","decomp_out.txt")        