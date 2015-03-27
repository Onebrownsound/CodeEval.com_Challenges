__author__ = 'dom'
import sys,re

def takeinfile(file):
    with open(file) as f:
        for line in f:
            brokenline=line.split(';')
            if brokenline[0]!='\n':
                pattern1=r'\S+'
                pattern2=r'\d{1,2}'
                sentence=re.findall(pattern1,brokenline[0])#find the information
                digits=re.findall(pattern2,brokenline[1])
                realdigits=list(map(int,digits))
                length=len(sentence)

                difference=findmissingdigit(length,realdigits) #finds the missing piece

                newlist=realdigits
                newlist.append(difference)




                combo=dict(zip(newlist,sentence))
                masterlist=[]
                for num in combo:
                    masterlist.append(combo[num])
                print(' '.join(masterlist))










def findmissingdigit(length,realdigits):
    reallist=list(range(1,length+1))
    reallist=set(reallist)
    realdigits=set(realdigits)
    difference=reallist-realdigits
    difference=difference.pop()
    return difference







takeinfile('helloworld.txt')