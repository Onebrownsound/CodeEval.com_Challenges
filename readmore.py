import sys

def readmore(file):
    
    with open(file) as f:
        for line in f:
            m=line#.strip('\n')
            print(len(m))
            if len(m)<=55:
                print(m)
            elif len(m)>=55:
                n=m[0:40]
                if n[39]== ' ':
                    print(n[0:39]+'... <Read More>')
                else:
                    print(n[0:38]+'... <Read More>')
    

readmore('helloworld.txt')
