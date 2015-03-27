__author__ = 'dom'
import re,sys

def multofnumintake(file):
    with open(file) as f:
        for line in f:
           pattern=r'(\d{1,3})'
           m=re.findall(pattern,line)
           print(multofnum(int(m[0]),int(m[1])))

def multofnum(a,b):
    comparelist=[x for x in range(2*a) if x%b==0]

    isnumfound=False
    while isnumfound==False:
        for item in comparelist:
            if a>item:
                isnumfound=False
            else:
                isnumfound=True
                return item







multofnumintake('helloworld.txt')