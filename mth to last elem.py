__author__ = 'dom'
import sys,re
def takeinfile(file):
    with open(file) as f:
        for line in f:
            digitp=r'([a-z]{1,1})'
            numberp=r'(\d{1,3})'
            digires=re.findall(digitp,line)
            numberes=re.search(numberp,line)
            if numberes!=None:
                mth=int(numberes.group())
                if mth>len(digires):
                    continue
                else:
                    print(digires[-mth])








takeinfile('helloworld.txt')
