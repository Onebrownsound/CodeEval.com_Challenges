import sys
def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def setintersection(file):
    
    with open(file) as f:
        for line in f:
            line=line.strip('\n').split(';')
            if len(line)<1:
                pass
            if len(line)>1:
                left=[int(s) for s in line[0].replace(',',' ').split() if s.isdigit()]
                right=[int(s) for s in line[1].replace(',',' ').split() if s.isdigit()]
                line=[]
                calculate=list(set(left)&set(right))
                if len(calculate)<1:
                    print('')
                else:
                    print(calculate)
setintersection('helloworld.txt')
        
            



