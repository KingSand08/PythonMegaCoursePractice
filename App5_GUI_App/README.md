# Python Mega Course Practice -> App 5: Book Manager Desktop GUI Application

This app was written using Python and the `tkinter`, `ttkbootstrap`, `sqlite3`, and `pyinstaller` modules. The purpose of this GUI app is to store and search for books with an interactive interface. Specifically this app accomplishes:

- User adding and storing a book to book manager's local database
- User can also update or delete a book record entry
- An executable .app file in the `/dist` folder.

The .app file can only run on ARM based Mac computers, though users can create their own executable by using pyinstaller with the given `.spec` file. Otherwise, the book manager app can be ran with:

```
App5_GUI_App/bookStoreApp_frontend.py'
```
