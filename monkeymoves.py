from decimal import *

def main():
    tallylist=[]
    calculatelist=[]
    for x in range(-300,300):
        for y in range(-300,300):
            calculatelist.append((x,y))
    for x,y in calculatelist:
        m=str(x).strip('-')
        n=str(y).strip('-')
    
        if sum_digits(m)+sum_digits(n)<19:
            tallylist.append((x,y))
    print(tallylist,len(tallylist))
        
        
def sum_digits(digit):
    b = 0
    for a in digit:
        b += int(a)
    return b    
main()    
        
    




