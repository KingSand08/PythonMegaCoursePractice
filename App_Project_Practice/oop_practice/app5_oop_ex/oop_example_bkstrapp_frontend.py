from tkinter import *
import ttkbootstrap as tb
from oop_example_bkstrapp_backend import Database


class BookStoreGuiApp(object):
    
    def __init__(self, window):
        # Setup database instance
        self.database = Database()
        
        # Setup Window instace
        self.window = window
        
        # Main Window
        self.window.title("BookStoreApp")
        
        # Main Frame
        self.wv = tb.Frame(window)
        self.wv.pack(pady=20, fill=BOTH, expand=True)

        # Frame Containers
        self.inputFrame = tb.Frame(self.wv)
        self.inputFrame.grid(pady=10, row=0, column=0, columnspan=2)

        self.outputFrame = tb.Frame(self.wv)
        self.outputFrame.grid(pady=10, padx=(20, 10), row=1, column=0)

        self.buttonFrame = tb.Frame(self.wv)
        self.buttonFrame.grid(pady=10, padx=(10, 20), row=1, column=1)

        
        # Labels
        title_l = Label(self.inputFrame, text="Title")
        title_l.grid(row=0, column=0, sticky='w', padx=(10,5))

        self.title_userText = StringVar()
        self.title_e = Entry(self.inputFrame, textvariable=self.title_userText)
        self.title_e.grid(row=0, column=1, sticky='w', padx=(0, 20))

        author_l = Label(self.inputFrame, text="Author")
        author_l.grid(row=0, column=2, sticky='w', padx=(10, 5))

        self.author_userText = StringVar()
        self.author_e = Entry(self.inputFrame, textvariable=self.author_userText)
        self.author_e.grid(row=0, column=3, sticky='w', padx=(0, 20))

        year_l = Label(self.inputFrame, text="Year")
        year_l.grid(row=1, column=0, sticky='w', padx=(10, 5))

        self.year_userText = StringVar()
        self.year_e = Entry(self.inputFrame, textvariable=self.year_userText)
        self.year_e.grid(row=1, column=1, sticky='w', padx=(0, 20))

        isbn_l = Label(self.inputFrame, text="ISBN")
        isbn_l.grid(row=1, column=2, sticky='w', padx=(10, 5))

        self.isbn_userText = StringVar()
        self.isbn_e = Entry(self.inputFrame, textvariable=self.isbn_userText)
        self.isbn_e.grid(row=1, column=3, sticky='w', padx=(0, 20))

        # Listbox and Scroller
        self.storeResultsList_l = Listbox(self.outputFrame, height=15, width=45)
        self.storeResultsList_l.grid(row=0, column=0, rowspan=6)

        self.scrlBr = tb.Scrollbar(self.outputFrame, orient='vertical', bootstyle='success round')
        self.scrlBr.grid(row=0, column=1, rowspan=6, sticky='ns', pady=(0, 0))

        self.storeResultsList_l.configure(yscrollcommand=self.scrlBr.set)
        self.scrlBr.configure(command=self.storeResultsList_l.yview)

        self.storeResultsList_l.bind('<<ListboxSelect>>', self.getSelectedRow)

        # Buttons
        viewAll_b = tb.Button(self.buttonFrame, text="View All", bootstyle="success-toolbutton", width=12, command=self.viewCommand)
        viewAll_b.grid(row=0, column=2, pady=5)

        searRes_b = tb.Button(self.buttonFrame, text="Search Entry", bootstyle="success-toolbutton", width=12, command=self.searchCommand)
        searRes_b.grid(row=1, column=2, pady=5)

        addEntr_b = tb.Button(self.buttonFrame, text="Add Entry", bootstyle="success-toolbutton", width=12,command=self.insertCommand)
        addEntr_b.grid(row=2, column=2, pady=5)

        updSect_b = tb.Button(self.buttonFrame, text="Update Section", bootstyle="success-toolbutton", width=12, command=self.updateCommand)
        updSect_b.grid(row=3, column=2, pady=5)

        delSect_b = tb.Button(self.buttonFrame, text="Delete Section", bootstyle="success-toolbutton", width=12, command=self.deleteCommand)
        delSect_b.grid(row=4, column=2, pady=5)

        close_b = tb.Button(self.buttonFrame, text="Close", bootstyle="success-outline", width=12, command=window.destroy)
        close_b.grid(row=5, column=2, pady=5)


        
# Frontend Commands
    def getSelectedRow(self, event):
        global selectedTuple
        try:
            index=self.storeResultsList_l.curselection()[0] # First index of the tuple
            selectedTuple = self.storeResultsList_l.get(index)
            self.title_e.delete(0, END)
            self.title_e.insert(END, selectedTuple[1])
            self.author_e.delete(0, END)
            self.author_e.insert(END, selectedTuple[2])
            self.year_e.delete(0, END)
            self.year_e.insert(END, selectedTuple[3])
            self.isbn_e.delete(0, END)
            self.isbn_e.insert(END, selectedTuple[4])
        except IndexError as e:
            # print(f"There is an {e}, since the listbox is currently empty, so nothing can be selected.")
            pass

    def viewCommand(self):
        self.storeResultsList_l.delete(0, END)  # Clear the Listbox
        for row in self.database.view():
            self.storeResultsList_l.insert(END, row)

    def searchCommand(self):
        self.storeResultsList_l.delete(0, END)  # Clear the Listbox
        if self.title_e.get() == "" and self.author_e.get() == "" and self.year_e.get() == "" and self.isbn_e.get() == "":
            self.storeResultsList_l.insert(END, "ENTER INTO AT LEAST ONE OF THE TEXT AVAILABLE PROMPTS TO INTERACT WITH THE APPLICATION")
        else:
            for row in self.database.search(self.title_e.get(), self.author_e.get(), self.year_e.get(), self.isbn_e.get()):
                self.storeResultsList_l.insert(END, row)

    def insertCommand(self):
        self.storeResultsList_l.delete(0, END)  # Clear the Listbox
        if self.title_e.get() == "" and self.author_e.get() == "" and self.year_e.get() == "" and self.isbn_e.get() == "":
            self.storeResultsList_l.insert(END, "ENTER INTO AT LEAST ONE OF THE TEXT AVAILABLE PROMPTS TO INTERACT WITH THE APPLICATION")
        else:
            self.database.insert(self.title_e.get(), self.author_e.get(), self.year_e.get(), self.isbn_e.get())
            self.storeResultsList_l.insert(END, "Successfully inserted!")
            self.storeResultsList_l.insert(END, self.title_e.get())
            self.storeResultsList_l.insert(END, self.author_e.get())
            self.storeResultsList_l.insert(END, self.year_e.get())
            self.storeResultsList_l.insert(END, self.isbn_e.get())

    def deleteCommand(self):
        self.database.delete(selectedTuple[0])
        self.viewCommand()

    def updateCommand(self):
        self.database.update(selectedTuple[0], self.title_e.get(), self.author_e.get(), self.year_e.get(), self.isbn_e.get())
        self.viewCommand()
        
window = tb.Window(themename="darkly")
BookStoreGuiApp(window)
window.mainloop()