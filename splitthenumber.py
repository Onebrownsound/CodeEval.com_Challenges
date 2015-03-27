import sys
def splitthenumber(file):
    with open(file) as f:
        for line in f:
            broken=line.strip('\n').split(' ')
          
            digits=[]
            puzzle=[]
            for elem in broken:
                numbers = ''.join([i for i in elem if i.isdigit()])
                for c in numbers:
                    digits.append(c)
                letters = ''.join([i for i in elem if not i.isdigit()])
                for c in letters:
                    puzzle.append(c)
                if '+' in puzzle:
                   combo(puzzle,digits)
                elif '-' in puzzle:
                   subtract(puzzle,digits)
def combo(puzzle,digits):
    addlocation=puzzle.index('+')
    
    m=digits[:addlocation]
    n=digits[addlocation:]
    print(int(''.join(m))+int(''.join(n)))






def subtract(puzzle,digits):
    sublocation=puzzle.index('-')
    m=digits[:sublocation]
    n=digits[sublocation:]
    print(int(''.join(m))-int(''.join(n)))
        
        
                


splitthenumber('helloworld.txt')
 
