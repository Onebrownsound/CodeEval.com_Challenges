#Headex

from tkinter import *
app = Tk()
app.title('Head-Ex Deliveries')
import tkinter.messagebox



def save_data():
    try: #tells program to try this code
        f = open("depots.txt", "a") #the append option adds it to the end read/write will overwrite past data
        f.write("Depot:\n")
        f.write(depot.get() )  #entryfields are quick and dirty and do not need a index where to start
        f.write("\nDescription:\n")
        f.write(description.get())
        f.write("\nAddress:\n")
        f.write(address.get("1.0",END)) #large text fields are not quick and dirty and do need an index where to start
        f.close()
        depot.set(None) # however for deleting entry fields index is 0
        description.delete(0,END)
        address.delete("1.0",END) #once again large text fields index starts at "1.0"
    except Exception as ex:#tells program if any exception/error occurs to change title whatever the error is
        tkinter.messagebox.showerror("Error!", "Can't write to the file\n %s" % ex)
        
def read_depots(file):
   depots = []
   depots_f = open(file)
   for line in depots_f:
    depots.append(line.rstrip())
   return depots


depots=[]
Label(app, text = "Depot:").pack() #starts depot field creation
depot = StringVar()
depot.set(None)
options = read_depots("depots.txt")
OptionMenu(app, depot, *options).pack()

Label(app, text = "Description:").pack() #starts description field creation and packs it
description=Entry(app)
description.pack() #sets the description space in the gui

Label(app, text = "Address:").pack() #starts address field creation
address=Text(app)
address.pack() #sets the description space in the gui

save=Button(app, text = "Save", command = save_data).pack()

app.mainloop()
