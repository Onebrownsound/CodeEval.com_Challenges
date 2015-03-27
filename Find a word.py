import re
import sys

def breakup(file):
    with open(file) as f:
        for line in f:
            split=line.split('|')
            
            if len(split)==1:
                pass
            else:
                answer=[]
                m=split[0]
                n=getpos(split[1])
                for item in n:
                    answer.append(m[item])
                print(''.join(answer))
                
                


def getpos(numbers):
    poslist=[]
    pattern=r'(\d{1,5})'
    numbers=re.findall(pattern,numbers)
    for num in numbers:
        poslist.append(int(num)-1)
    
    return(poslist)


breakup('helloworld.txt')
