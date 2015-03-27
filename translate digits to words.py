import sys
def reverse(file):
    with open(file) as f:
        for line in f:
            emptylist=[]
            m=line.strip('\n').split(';')
            for item in m:
                if item=='zero':
                    emptylist.append('0')
                elif item=='one':
                    emptylist.append('1')
                elif item=='two':
                    emptylist.append('2')
                elif item=='three':
                    emptylist.append('3')
                elif item=='four':
                    emptylist.append('4')
                elif item=='five':
                    emptylist.append('5')
                elif item=='six':
                    emptylist.append('6')
                elif item=='seven':
                    emptylist.append('7')
                elif item=='eight':
                    emptylist.append('8')
                elif item=='nine':
                    emptylist.append('9')
                    
            print (''.join(emptylist))
            
        

reverse(sys.argv[1])
