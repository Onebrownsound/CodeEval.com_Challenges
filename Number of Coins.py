__author__ = 'dom'
import sys,re


def extractdata(file):
    with open(file) as f:
        for value in f:
            value=int(value)
            print(onestopshop(value))

            '''
            total=0
            coins=0
            coins,value=fivecoin(value)
            total+=coins
            coins,value=threecoin(value)
            total+=coins
            coins,value=onecoin(value)
            total+=coins
            print(total)'''


def onestopshop(value):

    total=0
    for x in [5,3,1]:
        maxcoins=value//x
        remainder=value-(maxcoins*x)
        total+=maxcoins
        value=remainder
    return total


def fivecoin(value):
    coinnumber=value//5
    remainder=value-(coinnumber*5)
    return coinnumber,remainder

def threecoin(value):
    coinnumber=value//3
    remainder=value-(coinnumber*3)
    return coinnumber,remainder
def onecoin(value):
    coinnumber=value//1
    remainder=value-(coinnumber*1)
    return coinnumber,remainder





extractdata('helloworld.txt')