from wwtbem import *
import pygame.mixer
sounds = pygame.mixer
sounds.init()
def wait_finish(channel):
    while channel.get_busy():
        pass

outcome = input("A question has been asked. Please enter 1 for a correct answer and 2 for a wrong answer \n")
numbercorrect=0
numberwrong=0
total=numberwrong+numbercorrect

def correct_click():
    print("hopefully a sound is played")
    s = sounds.Sound("heartbeat.wav")
    wait_finish(s.play())
    numbercorrect+=1
def incorrect_click():
    print('you were wrong hopefully a sound plays')
    s3 = sounds.Sound("ohno.wav")
    wait_finish(s3.play())
    numberwrong+=1
def display_results():   
    print ('You got %d correct, %d wrong out of a total of %d questions' % (numbercorrect,numberwrong,total))
