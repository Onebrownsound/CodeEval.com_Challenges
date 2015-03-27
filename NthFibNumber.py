import sys
def openfile(file):
    with open(file,'r') as f:
        emptylist=[]
        for line in f:
            emptylist.append(int(line))
        for elem in emptylist:
            print(F(elem))
            
            

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

        
       
    
    








openfile(sys.argv[1])
 
