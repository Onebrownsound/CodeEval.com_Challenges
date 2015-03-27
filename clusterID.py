import re
from collections import defaultdict



def getemaillinks(file): #need to extract emails from the data file and add the values of who they spoke to
    idbook=[]
    d={}
    with open(file,'r') as f:
        for line in f:
            match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
            idbook.append([match[0],match[1]])

    for key, val in idbook:
        d.setdefault(key, []).append(val)
    idlinks(d)






def idlinks(d):
    
    keylist=[]
    valuelist=[]
    linkedlist=[]
    for item in d.keys():
        keylist.append(item)

    for a in keylist:
     for b in range(len(keylist)-1,-1,-1):
         if a in d[keylist[b]] and keylist[b] in d[a]:
             linkedlist.append([a,keylist[b]])
         else:
             pass
    prune(linkedlist)

def lists_overlap(a, b):
    mergedlist=[]
    if set(a) & set(b):
        mergedlist.extend(a)
        mergedlist.extend(b)
    else:
        pass
        
    prunemerged(mergedlist)


def prune(linkedlist): #purpose is to weed out double links aka [A,C] == [C-A] so there is no need to have both
    
    for item in linkedlist:
        if item[::-1] in linkedlist:
            linkedlist.remove(item[::-1])
    print (len(linkedlist),linkedlist)
    for a in linkedlist:
        for b in range(len(linkedlist)-1,-1,-1):
            lists_overlap(a,linkedlist[b])
        
            
def prunemerged(mergedlist):
    print (mergedlist)



def idmatches(x,y):
    linkedlist=[]
    print( x+" and "+y+" are linked ")
    linkedlist.append([x,y])
    print (linkedlist)












getemaillinks("facebook.txt")
