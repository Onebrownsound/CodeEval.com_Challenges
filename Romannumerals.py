import sys
import re

def rnum(file):
    with open(file) as f:
        for line in f:
            
            pattern=r'(\d+)'
            digit=re.match(pattern,line)
            digit=digit.group(1)
            converttornum(int(digit))
            
def converttornum(digit):
    masterlist=[]
    decval=[1000,500,100,50,10,5,1]
 
    for item in decval:
        a=digit//item
        digit-=(item*a)
        masterlist.append(a)
    convertmaster(masterlist)


def convertmaster(masterlist):
    baseletters=['M','D','C','L','X','V','I']
    converted=[]
    for c in range(0,7):
        converted.append(baseletters[c]*masterlist[c])
    

    if masterlist[6]==4:
        converted[6]='IV'
        converted[5]=''
    if masterlist[6]+masterlist[5]==5:
        converted[6]='IX'
        converted[5]=''
    if masterlist[4]==4:
        converted[4]='XL'
        converted[3]=''
    if masterlist[4]+masterlist[3]==5:
        converted[4]='XC'
        converted[3]=''
    if masterlist[2]==4:
        converted[2]='CD'
        converted[1]=''
    if masterlist[2]+masterlist[1]==5:
        converted[2]='CM'
        converted[1]=''



    print(''.join(converted))
converttornum(3094)


