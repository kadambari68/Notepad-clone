from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from datetime import datetime

root = Tk()
root.title("Notepad")
root.geometry("644x450")
TextArea = scrolledtext.ScrolledText(root , font="lucida 13", undo=True)
TextArea.pack()
file = None

# create menu
MenuBar = Menu(root)
root.config(menu=MenuBar)

# configure File ,About and Edit menus with MenuBar
FileMenu = Menu(MenuBar , tearoff=0)
EditMenu = Menu(MenuBar , tearoff=0)
AboutMenu= Menu(MenuBar , tearoff=0)
MenuBar.add_cascade(label="File",menu=FileMenu)
MenuBar.add_cascade(label="Edit",menu=EditMenu)
MenuBar.add_cascade(label="About",menu=AboutMenu)

# functions for File and Edit menus
def newFile():
    global file
    root.title("Untitled - Notepad")
    TextArea.delete(1.0,END)
    
def openFile():
    global file
    file = askopenfilename(defaultextension =".txt",filetypes=[("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        f = open(file,"r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(defaultextension =".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()    

def time():
        d = datetime.now()
        TextArea.insert('end',d)

def exitFile():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def undo():
    TextArea.event_generate("<<Undo>>") 
def redo():
    TextArea.event_generate("<<Redo>>")       
def about():
    showinfo("Notepad", "Notepad developed 1829")    

# adding new, open, and save file functionality to File menu
FileMenu.add_command(label="New" , command = newFile,accelerator="Ctrl+N")
FileMenu.add_command(label="Open" , command = openFile,accelerator="Ctrl+O")
FileMenu.add_command(label="Save" , command = saveFile,accelerator="Ctrl+S")

# separator inside File menus
FileMenu.add_separator()

# adding exit function to File menu
FileMenu.add_command(label = "Exit" , command = exitFile,accelerator="Ctrl+X")

# adding about function as menu
AboutMenu.add_command(label="About",command=about) 

EditMenu.add_command(label = "Undo" , command = undo,accelerator="Ctrl+Z")

# separator inside Edit menus
EditMenu.add_separator()

# adding cut, copy, paste functionalities to Edit menu
EditMenu.add_command(label = "Cut" , command = cut,accelerator="Ctrl+X")
EditMenu.add_command(label = "Copy" , command = copy,accelerator="Ctrl+C")
EditMenu.add_command(label = "Paste" , command = paste,accelerator="Ctrl+V")

# separator inside Edit menus
EditMenu.add_separator()

EditMenu.add_command(label = "Time" , command = time,accelerator="F5")



root.mainloop()


