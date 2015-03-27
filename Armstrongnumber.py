__author__ = 'dom'
import sys,re


def sendinfile(file):
    with open(file) as f:
        for line in f:
             line=line.strip('\n')
             pattern=r'(\d{1,3})'
             m=re.match(pattern,line)
             if m:
                length=len(m.string)
                value=int(m.string)
                print(isarmstrong(length,value))

def isarmstrong(length,value):
    strvalue=str(value)
    total=0
    for item in strvalue:
        total+=int(item)**length
    if total==value:
        return True
    else:
        return False






sendinfile('helloworld.txt')