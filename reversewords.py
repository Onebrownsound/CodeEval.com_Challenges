import sys
def reverse(file):
    with open(file) as f:
        for line in f:
            m=line.strip('\n').split(' ')
            n=m[::-1]
            print(' '.join(n))
        

reverse(str.argv[1])
