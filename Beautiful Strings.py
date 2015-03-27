from collections import Counter

def prettystrings(file):
    with open(file) as f:
        for line in f:
            broken=line.replace('?','').replace('-','').replace('!','').replace('.','').replace("'",'').replace(',','').replace(':','').replace(')','').replace('(','').lower().split()
            
            m=''.join(broken)
            finalscore=[]
            finalscore.append(score(m))
            for item in finalscore:
                if item!=0:
                    print(item)
def score(m):
    freq=Counter(m)
    
    arr = freq.values()
    listvalues=[]
    for item in arr:
        listvalues.append(item)
    listvalues.sort()
    listvalues.reverse()
   
 
    
    
    values_and_counts = zip(range(26, 0, -1), listvalues)
    return sum(x * y for x, y in values_and_counts)
    
    




prettystrings('helloworld.txt')
