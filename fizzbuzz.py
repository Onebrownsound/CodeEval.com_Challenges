import re
import sys

def evaluatefizzbuzz(n,x,y): # this function evaluates the broken down list based off n=compared number and x and y being divisors
 
    if n % x == 0 and n % y == 0:
        return 'FB'
    elif n % x == 0:
        return 'F'
    elif n % y == 0:
        return 'B'
    else:
        return n

def breakuplines(file): #this reads the file and splits each line into a seperate list and joins that list
    fizzlist =[]
    with open(file) as f:
        polyShape = []
        for line in f:
            line = line.split() # to deal with blank 
            if line:            # lines (ie skip them)
                   line = [int(i) for i in line]
                   polyShape.append(line)
    breakuplist(polyShape)      
            
def breakuplist(combo): #this takes each index of the previously joined combolist and sends them to get evaluated independently
    for item in range(0,len(combo)):
        x=combo[item]
        getreadyforfizz(x[0],x[1],x[2])

        
def getreadyforfizz(x,y,z):
    testlist=[num for num in range(1,z+1)]
    constructedlist=[]
    for item in testlist:
        constructedlist.append(evaluatefizzbuzz(item,x,y))
    print (' '.join(map(str, constructedlist)))


breakuplines(sys.argv[1])
