import sys


import operator


def openfile(file):
    with open(file,'r') as f:

        

        n=[]
        stringsortedlist=[]
        for line in f:
            stringlist=line.strip('\n').split(' ')
            for item in stringlist:
                n.append(float(item))
            
            sortedlist=sorted(n)

            for item in sortedlist:
                
                stringsortedlist.append("{:0.03f}".format(item))
            
                
            print (' '.join(stringsortedlist))
            n[:]=[]
            stringsortedlist[:]=[]
openfile('helloworld.txt')
 
