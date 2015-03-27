__author__ = 'dom'
import sys,re

def splitlines(file):
    with open(file) as f:
        track=[]
        for line in f:
            m=line.strip('\n')
            if m!='':
                track.append(m)
        lasttrack=len(track)-1




        for pos,item in enumerate(track):
            if pos==0:
                track[0]=track[0].replace('_','|')

            elif pos in range(1,len(track)):
                #print(gettrackpos(track[pos-1]))
                #print(getCpos(track[pos]))
                if checkcor_(track[pos])=='C':
                    if getCpos(track[pos])==gettrackpos(track[pos-1]):
                        track[pos]=track[pos].replace('C','|')
                    if  getCpos(track[pos])>gettrackpos(track[pos-1]):
                        track[pos]=track[pos].replace("C","\\")
                    if getCpos(track[pos])<gettrackpos(track[pos-1]):
                        track[pos]=track[pos].replace('C','/')

                else:
                    if get_pos(track[pos])==gettrackpos(track[pos-1]):
                        track[pos]=track[pos].replace('_','|')
                    if  get_pos(track[pos])>gettrackpos(track[pos-1]):
                        track[pos]=track[pos].replace("_","\\")
                    if get_pos(track[pos])<gettrackpos(track[pos-1]):
                        track[pos]=track[pos].replace('_','/')
        for item in track:
            print(item)


def checkcor_(track):
    if 'C' in track:
        return 'C'
    else:
        return '_'

def gettrackpos(track):
    m=track.find('|')
    if m==-1:
        m=track.find('/')
        if m==-1:
            m=track.find("\\")

            return m
        else:
            return m
    else:
        return m

def getCpos(track):
    m=track.find('C')
    return m

def get_pos(track):
    m=track.find('_')
    return m












splitlines('helloworld.txt')


