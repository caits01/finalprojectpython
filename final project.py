from tkinter import *
from tkinter.messagebox import *
import os

def read():
    name_file = isi_nama.get()
    with open(f"{name_file}.txt", "r") as f:
        teks = f.read()
        tampil_entry.delete("1.0", END)
        tampil_entry.insert("1.0", teks)

def create():
    name_file = isi_nama.get()
    with open(f"{name_file}.txt", "w") as f:
        teks = text_entry.get("1.0", END)
        f.writelines(teks)
    text_entry.delete("1.0", END)
    read()

def append():
    name_file = isi_nama.get()
    with open(f"{name_file}.txt", "a") as f:
        teks = text_entry.get("1.0", END)
        f.writelines(teks)
    text_entry.delete("1.0", END)
    read()

def delete():
    name_file = isi_file_del.get()
    os.remove(f"{name_file}.txt")
    tampil_entry.delete("1.0", END)
    text_entry.delete("1.0", END)
    isi_nama.set("")
    isi_search.set("")
    isi_update.set("")
    isi_file_del.set("")

def update():
    search_text = isi_search.get()
    replace_text = isi_update.get()
    name_file = isi_nama.get()
    with open(f"{name_file}.txt") as f:
        data = f.read()
        data = data.replace(search_text, replace_text)
    with open(f"{name_file}.txt", "w") as f:
        f.write(data)
    read()
    isi_search.set("")
    isi_update.set("")
    
    
root = Tk()
root.title("GUI CRUD")
root.geometry("800x350")

isi_nama = StringVar()
isi_search = StringVar()
isi_update = StringVar()
isi_file_del = StringVar()

nama_file = Label(root, text="Nama file: ")
nama_file.grid(row = 0, column = 0)
entry_file = Entry(root, textvariable = isi_nama, font = ("calibre", 10, "normal"))
entry_file.grid(row = 0, column = 1, columnspan = 2)

teks = Label(root, text="Teks").grid(row = 1, column = 0)
text_entry = Text(root, height = 10, width = 40, font = ("calibre", 10, "normal"))
text_entry.grid(rowspan = 5, columnspan = 3)

create_button = Button(root, text = "Create", command = lambda: create()).grid(row = 2, column = 4)
append_button = Button(root, text = "Append", command = lambda: append()).grid(row = 3, column = 4)

tampil = Label(root, text="Tampil").grid(row = 1, column = 5)
tampil_entry = Text(root, height = 10, width = 40, font = ("calibre", 10, "normal"))
tampil_entry.grid(row = 2, column = 5, rowspan = 5, columnspan = 3)
read_button = Button(root, text = "Read", command = lambda: read()).grid(row = 2, column = 9)

search_text = Label(root, text="Search Text: ").grid(row = 9)
entry_search = Entry(root, textvariable = isi_search, font = ("calibre", 10, "normal"))
entry_search.grid(row = 10, column = 0, columnspan = 2)

update_text = Label(root, text="Update Text: ").grid(row = 9, column = 2, columnspan = 2)
entry_update = Entry(root, textvariable = isi_update, font = ("calibre", 10, "normal"))
entry_update.grid(row = 10, column = 2)
update_button = Button(root, text = "Update", command = lambda: update()).grid(row = 10, column = 4)

file_delete = Label(root, text="File: ").grid(row = 11, column = 0)
entry_file_del = Entry(root, textvariable = isi_file_del, font = ("calibre", 10, "normal"))
entry_file_del.grid(row = 12, column = 0, columnspan = 2)

delete_button = Button(root, text = "Delete", command = lambda: delete()).grid(row = 12, column = 2, columnspan = 2)


root.mainloop()