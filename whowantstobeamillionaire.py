from tkinter import *
app = Tk()
app.title("Who Wants To Be A Millionaire")
app.geometry('700x150+200+100')



import pygame.mixer
sounds = pygame.mixer
sounds.init()
def wait_finish(channel):
    while channel.get_busy():
        pass

num_good = IntVar()
num_good.set(0)
num_bad = IntVar()
num_bad.set(0)
numbercorrect=0
numberwrong=0
total=numberwrong+numbercorrect

def correct_click():
    global numbercorrect
    print("hopefully a sound is played")
    s = sounds.Sound("heartbeat.wav")
    wait_finish(s.play())
    numbercorrect= numbercorrect + 1
    num_good.set(num_good.get()+1)
def incorrect_click():
    global numberwrong
    print('you were wrong hopefully a sound plays')
    s3 = sounds.Sound("ohno.wav")
    wait_finish(s3.play())
    numberwrong= numberwrong + 1
    num_bad.set(num_bad.get()+1)
def display_results():   
    print(str(numbercorrect) + " were correctly answered.")
    print(str(numberwrong) + " were answered incorrectly.")

b1 = Button(app, text = "Correct Answer", width = 20, command=correct_click) #this is how you set a button notice the difference between that and a label
b1.pack(side='left', padx=30,pady=30)

b2 = Button(app, text = "Incorrect Answer!", width = 20, command=incorrect_click)
b2.pack(side='right', padx=30,pady=30)

b3 = Button(app, text = "Display Results", width = 30, command=display_results)
b3.pack(side='bottom', padx=10,pady=10)

l1 = Label(app, textvariable = num_good)  #notice how a label is set, with Label rather than Button in previous examples im guessing label has different parameters from Button as well
l1.pack(side='left', padx=30,pady=30)      #see above line
l2 = Label(app, textvariable = num_bad)
l2.pack(side='right', padx=30,pady=30)




app.mainloop()
