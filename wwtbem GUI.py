from whowantstobeamillionaire import *
from tkinter import *
app = Tk()
app.title("Who Wants To Be A Millionaire")
app.geometry('450x100+200+100')


b1 = Button(app, text = "Correct Answer", width = 20, command=correct_click)
b1.pack(side='left', padx=30,pady=30)

b2 = Button(app, text = "Incorrect Answer!", width = 20, command=incorrect_click)
b2.pack(side='right', padx=30,pady=30)

b3 = Button(app, text = "Display Results", width = 20, command=display_results)
b3.pack(side='bottom', padx=30,pady=30)
app.mainloop()
