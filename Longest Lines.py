__author__ = 'dom'
import re,sys



def takeinfile(file):
    with open(file) as f:
       f= f.read().split('\n')
       for item in f:
        if item=='':
            f.remove('')
       numberofitems=int(f[0])
       g=sorted(f[1:],key=len,reverse=True)
       for num in range(0,numberofitems):
            print(g[num])





takeinfile('helloworld.txt')