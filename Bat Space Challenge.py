__author__ = 'dom'
import re,sys

def takeindata(file):
    with open(file) as f:
        for line in f:
            pattern=r"\d{1,3}"
            results=re.findall(pattern,line)
            results=list(map(int,results))
            #print(results)
            Lengthofwire=results[0]

            Spacing=results[1]
            Batpopulation=results[2]
            Batlocations=results[3:]
            '''if len(Batlocations)==0:
                battally=(Lengthofwire-6)//Spacing
                print(Batpopulation+battally)
            else:'''
            Perfectlist=[x for x in range(6,Lengthofwire-5,Spacing)]
            Masterblackout=[]

            for item in range(0,len(Batlocations)):

                minimum=Batlocations[item]-Spacing
                maximum=Batlocations[item]+Spacing
                blackout=list(range(minimum,maximum+1))
                Masterblackout+=blackout

            a=set(Perfectlist)
            b=set(Masterblackout)
            c=a-b
            print(len(c))


takeindata('helloworld.txt')