__author__ = 'dom'
import re,sys

def takeinfile(file):
    with open(file) as f:
        for line in f:
            if line!='\n':
                m=int(line.rstrip())
                print(diagnostic(m))
def diagnostic(n):
    if n <0 or n>100:
        return "This program is for humans"
    elif n in range(66,101):
        return "The Golden Years"
    elif n in range(23,66):
        return "Working for the man"
    elif n in range(19,23):
        return "College"
    elif n in range(15,19):
        return "Highs school"
    elif n in range(12,15):
        return "Middle school"
    elif n in range(5,12):
        return "Elementary school"
    elif n in range(3,5):
        return "Preschool Maniac"
    elif n in range(0,3):
        return "Still in Mama's arms"




takeinfile('helloworld.txt')

