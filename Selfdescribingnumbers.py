import re
import sys
from collections import Counter


def getnum(file):
    with open(file) as f:
        for line in f:
            checklist={} #emptydictionary we will fill with what the number should be if it is classified as selfdescribing
            digit=line.strip('\n')
            if isSelfDescribing(digit)==False:
                print('0')
            else:
                print('1')




      '''      for pos,item in enumerate(digit):
                checklist[str(pos)]=int(item)
            strdigit=str(digit)
            c= Counter(strdigit) #counts the tally of what actually exists in the number
            boolvalue=comparelists(checklist,c)#sends to a function which compares the theoretical and actual, if true returns such
            if boolvalue==True:
                print('1')
            else:
                print('0')'''

def isSelfDescribing(n):
	s = str(n)
	return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))

def comparelists(checklist,c):

    for item in checklist.keys(): #checks the keys in the counter
        if checklist[item]!=c[item]:
            return False
        else:
            return True



getnum('helloworld.txt')
