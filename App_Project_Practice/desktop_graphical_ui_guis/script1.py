from tkinter import *


# Create window
window=Tk()



window.title("Miles to Km App")

def kmToMiles():
    mi = float(e1Val.get()) * 1.609344
    t1.delete("1.0", END)
    t1.insert(END, str(mi) + " mi")

# Add button widget
b1=Button(window, text="Execute", command=kmToMiles)
b1.grid(row=0, column=1)

# Add entry widget
e1Val=StringVar()
e1=Entry(window, textvariable=e1Val)
e1.grid(row=0, column=0)

# Add text widget
t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)


# Open the window
window.mainloop()