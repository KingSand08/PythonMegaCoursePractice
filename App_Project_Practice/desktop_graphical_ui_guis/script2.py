from tkinter import *


# Create window
window=Tk()



window.title("Kg to (Grams, Pounds, and Ounces)")

def conversion():
    grams = float(e1Val.get()) * 1000
    oz = float(e1Val.get()) * 35.274
    lb = float(e1Val.get()) * 2.20462
    
    tgr.delete("1.0", END)
    toz.delete("1.0", END)
    tlb.delete("1.0", END)
    
    tgr.insert(END, str(grams))
    toz.insert(END, str(oz))
    tlb.insert(END, str(lb))

# Add label widget
b1=Label(window, text="Kg")
b1.grid(row=0, column=0)

# Add entry widget
e1Val=StringVar()
e1=Entry(window, textvariable=e1Val)
e1.grid(row=0, column=1)

# Add button widget
b1=Button(window, text="Execute", command=conversion)
b1.grid(row=0, column=2)

# Add text widgets
tgr=Text(window, height=1, width=20)
tgr.grid(row=1, column=0)
tlb=Text(window, height=1, width=20)
tlb.grid(row=1, column=1)
toz=Text(window, height=1, width=20)
toz.grid(row=1, column=2)

# Open the window
window.mainloop()