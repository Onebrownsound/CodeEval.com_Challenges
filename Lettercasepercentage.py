import sys


def main(file):
    with open(file) as f:
        for line in f:
            line=line.strip('\n')
            upper=0
            lower=0
            if len(line)>0:
                for elem in line:
                    if elem.isupper():
                        upper+=1
                    if elem.islower():
                        lower+=1
                
                total=upper+lower
                
                
                upperper=(upper/total)*100
                lowerper=(lower/total)*100
                print('lowercase: %.2f uppercase: %.2f'%(lowerper,upperper))
            else:
                pass
                    







main('helloworld.txt')
