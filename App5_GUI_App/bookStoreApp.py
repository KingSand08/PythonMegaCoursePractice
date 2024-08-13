from tkinter import *
import ttkbootstrap as tb

window = tb.Window(themename="darkly")
window.title("BookStoreApp")

wv = tb.Frame(window)
wv.pack(pady=20)

title_l = Label(wv, text="Title")
title_l.grid(row=0, column=0)

title_userText = StringVar()
title_e = Entry(wv, textvariable=title_userText)
title_e.grid(row=0, column=1)

author_l = Label(wv, text="Author")
author_l.grid(row=0, column=2)

author_userText = StringVar()
author_e = Entry(wv, textvariable=author_userText)
author_e.grid(row=0, column=3)

year_l = Label(wv, text="Year")
year_l.grid(row=1, column=0)

year_userText = StringVar()
year_e = Entry(wv, textvariable=year_userText)
year_e.grid(row=1, column=1)

isbn_l = Label(wv, text="ISBN")
isbn_l.grid(row=1, column=2)

isbn_userText = StringVar()
isbn_e = Entry(wv, textvariable=isbn_userText)
isbn_e.grid(row=1, column=3)

storeResults_t = Text(wv, height=15, width=35)
storeResults_t.grid(row=2, column=0, rowspan=6, columnspan=2, padx=(15, 0), pady=(15, 0))

scrlBr = tb.Scrollbar(wv, orient='vertical', bootstyle='success round')
scrlBr.grid(row=2, column=2, rowspan=6, sticky='ns', pady=(15, 0))

storeResults_t.configure(yscrollcommand=scrlBr.set)
scrlBr.configure(command=storeResults_t.yview)

viewAll_b = tb.Button(wv, text="View All", bootstyle="success-toolbutton", width=12)
viewAll_b.grid(row=2, column=3, pady=5)

searRes_b = tb.Button(wv, text="Search Entry", bootstyle="success-toolbutton", width=12)
searRes_b.grid(row=3, column=3, pady=5)

addEntr_b = tb.Button(wv, text="Add Entry", bootstyle="success-toolbutton", width=12)
addEntr_b.grid(row=4, column=3, pady=5)

updSect_b = tb.Button(wv, text="Update Section", bootstyle="success-toolbutton", width=12)
updSect_b.grid(row=5, column=3, pady=5)

delSect_b = tb.Button(wv, text="Delete Section", bootstyle="success-toolbutton", width=12)
delSect_b.grid(row=6, column=3, pady=5)

close_b = tb.Button(wv, text="Close", bootstyle="success-outline", width=12)
close_b.grid(row=7, column=3, pady=5)