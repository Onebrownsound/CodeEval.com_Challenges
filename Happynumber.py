import sys
import re


def happynumber(n):
    
    c=0
    counter=0
    while n>1:
        tally=[]
        for elem in str(n):
            for num in elem:
                tally.append(int(num))
        for pos,item in enumerate(tally):
            tally[pos]=item**2
        c=sum(tally)
        n=c
        counter+=1
        if counter>1000: break
            
    if n==1:
        return '1'
    else:
        return '0'

    





def breakdown(file):
    with open(file) as f:
        for line in f:
            m=line.strip('\n')
            print(happynumber(int(m)))


breakdown('helloworld.txt')
