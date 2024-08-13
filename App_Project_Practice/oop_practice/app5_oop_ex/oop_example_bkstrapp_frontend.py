from tkinter import *
import ttkbootstrap as tb
from oop_example_bkstrapp_backend import Database

database = Database()

# Frontend Commands
def getSelectedRow(event):
    global selectedTuple
    try:
        index=storeResultsList_l.curselection()[0] # First index of the tuple
        selectedTuple = storeResultsList_l.get(index)
        title_e.delete(0, END)
        title_e.insert(END, selectedTuple[1])
        author_e.delete(0, END)
        author_e.insert(END, selectedTuple[2])
        year_e.delete(0, END)
        year_e.insert(END, selectedTuple[3])
        isbn_e.delete(0, END)
        isbn_e.insert(END, selectedTuple[4])
    except IndexError as e:
        # print(f"There is an {e}, since the listbox is currently empty, so nothing can be selected.")
        pass

def viewCommand():
    storeResultsList_l.delete(0, END)  # Clear the Listbox
    for row in database.view():
        storeResultsList_l.insert(END, row)

def searchCommand():
    storeResultsList_l.delete(0, END)  # Clear the Listbox
    if title_e.get() == "" and author_e.get() == "" and year_e.get() == "" and isbn_e.get() == "":
        storeResultsList_l.insert(END, "ENTER INTO AT LEAST ONE OF THE TEXT AVAILABLE PROMPTS TO INTERACT WITH THE APPLICATION")
    else:
        for row in database.search(title_e.get(), author_e.get(), year_e.get(), isbn_e.get()):
            storeResultsList_l.insert(END, row)

def insertCommand():
    storeResultsList_l.delete(0, END)  # Clear the Listbox
    if title_e.get() == "" and author_e.get() == "" and year_e.get() == "" and isbn_e.get() == "":
        storeResultsList_l.insert(END, "ENTER INTO AT LEAST ONE OF THE TEXT AVAILABLE PROMPTS TO INTERACT WITH THE APPLICATION")
    else:
        database.insert(title_e.get(), author_e.get(), year_e.get(), isbn_e.get())
        storeResultsList_l.insert(END, "Successfully inserted!")
        storeResultsList_l.insert(END, title_e.get())
        storeResultsList_l.insert(END, author_e.get())
        storeResultsList_l.insert(END, year_e.get())
        storeResultsList_l.insert(END, isbn_e.get())

def deleteCommand():
    database.delete(selectedTuple[0])
    viewCommand()

def updateCommand():
    database.update(selectedTuple[0], title_e.get(), author_e.get(), year_e.get(), isbn_e.get())
    viewCommand()

window = tb.Window(themename="darkly")
window.title("BookStoreApp")

# Main Frame
wv = tb.Frame(window)
wv.pack(pady=20, fill=BOTH, expand=True)

# Frame Containers
inputFrame = tb.Frame(wv)
inputFrame.grid(pady=10, row=0, column=0, columnspan=2)

outputFrame = tb.Frame(wv)
outputFrame.grid(pady=10, padx=(20, 10), row=1, column=0)

buttonFrame = tb.Frame(wv)
buttonFrame.grid(pady=10, padx=(10, 20), row=1, column=1)

# Labels
title_l = Label(inputFrame, text="Title")
title_l.grid(row=0, column=0, sticky='w', padx=(10,5))

title_userText = StringVar()
title_e = Entry(inputFrame, textvariable=title_userText)
title_e.grid(row=0, column=1, sticky='w', padx=(0, 20))

author_l = Label(inputFrame, text="Author")
author_l.grid(row=0, column=2, sticky='w', padx=(10, 5))

author_userText = StringVar()
author_e = Entry(inputFrame, textvariable=author_userText)
author_e.grid(row=0, column=3, sticky='w', padx=(0, 20))

year_l = Label(inputFrame, text="Year")
year_l.grid(row=1, column=0, sticky='w', padx=(10, 5))

year_userText = StringVar()
year_e = Entry(inputFrame, textvariable=year_userText)
year_e.grid(row=1, column=1, sticky='w', padx=(0, 20))

isbn_l = Label(inputFrame, text="ISBN")
isbn_l.grid(row=1, column=2, sticky='w', padx=(10, 5))

isbn_userText = StringVar()
isbn_e = Entry(inputFrame, textvariable=isbn_userText)
isbn_e.grid(row=1, column=3, sticky='w', padx=(0, 20))

# Listbox and Scroller
storeResultsList_l = Listbox(outputFrame, height=15, width=45)
storeResultsList_l.grid(row=0, column=0, rowspan=6)

scrlBr = tb.Scrollbar(outputFrame, orient='vertical', bootstyle='success round')
scrlBr.grid(row=0, column=1, rowspan=6, sticky='ns', pady=(0, 0))

storeResultsList_l.configure(yscrollcommand=scrlBr.set)
scrlBr.configure(command=storeResultsList_l.yview)

storeResultsList_l.bind('<<ListboxSelect>>', getSelectedRow)

# Buttons
viewAll_b = tb.Button(buttonFrame, text="View All", bootstyle="success-toolbutton", width=12, command=viewCommand)
viewAll_b.grid(row=0, column=2, pady=5)

searRes_b = tb.Button(buttonFrame, text="Search Entry", bootstyle="success-toolbutton", width=12, command=searchCommand)
searRes_b.grid(row=1, column=2, pady=5)

addEntr_b = tb.Button(buttonFrame, text="Add Entry", bootstyle="success-toolbutton", width=12,command=insertCommand)
addEntr_b.grid(row=2, column=2, pady=5)

updSect_b = tb.Button(buttonFrame, text="Update Section", bootstyle="success-toolbutton", width=12, command=updateCommand)
updSect_b.grid(row=3, column=2, pady=5)

delSect_b = tb.Button(buttonFrame, text="Delete Section", bootstyle="success-toolbutton", width=12, command=deleteCommand)
delSect_b.grid(row=4, column=2, pady=5)

close_b = tb.Button(buttonFrame, text="Close", bootstyle="success-outline", width=12, command=window.destroy)
close_b.grid(row=5, column=2, pady=5)

# Final
wv.mainloop()