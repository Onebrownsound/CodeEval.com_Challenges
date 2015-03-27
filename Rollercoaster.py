import sys
import re


def rollercoaster(file):
    with open(file) as f:
        for line in f:
            masterlist=[]
            counter=0
            line=line.strip('\n')
            for elem in line:
                if elem.isalpha()==True and counter==0:
                    masterlist.append(elem.upper())
                    counter=1
               

                elif  elem.isalpha()==True and counter==1:
                    masterlist.append(elem.lower())
                    counter=0

                

                else:
                    masterlist.append(elem)





            print(''.join(masterlist))   








rollercoaster('helloworld.txt')
