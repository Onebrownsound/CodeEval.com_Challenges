import sys

def is_even(file):
    numberslist=[]
    with open(file) as f:
        for line in f:
            numberslist.append(line)
    
    for c in range(0,len(numberslist)):
        if int(numberslist[c])%2==0:
            numberslist[c]= 1
        else:
            numberslist[c]=0
    for item in numberslist:
        print(item)
    
    
    
    
    
    
    
    
    
    
is_even('is_even.txt')
