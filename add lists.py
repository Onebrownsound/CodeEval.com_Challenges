__author__ = 'dom'
import sys, re



def takeinfile(file):
    with open(file) as f:
        for line in f:
            answerlist=[]
            m=line.strip('\n')

            pattern=r'(\d{1,3})'
            result=re.findall(pattern,m)

            breakpoint=round(len(result)/2)
            firsthalf=result[:breakpoint]
            secondhalf=result[breakpoint:]

            for num in range(len(firsthalf)):
                answerlist.append(str(int(firsthalf[num])*int(secondhalf[num])))

            print(' '.join(answerlist))







takeinfile('helloworld.txt')