import sys
import string


def roadtrip(file):
    with open(file) as f:
        for line in f:
            gas=[]
            m=line.strip(';').split()
            for item in m:
                gas.append(int(''.join(filter(lambda x: x.isdigit(), item))))

            printdifference(sorted(gas))



def printdifference(gas):
    gaslist=[]
    strlist=[]
    gaslist.append(int(gas[0]))
    for item in range(0,len(gas)-1):
        gaslist.append(int(gas[item+1])-int(gas[item]))
    for item in gaslist:
        strlist.append(str(item))
    print (','.join(strlist))
        



roadtrip('helloworld.txt')
