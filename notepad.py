from tkinter import BOTH, RIGHT, SCROLL, Scrollbar, Text, Toplevel, Button, Tk, Menu, scrolledtext  
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from turtle import ScrolledCanvas

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

root = Tk()  

TextArea = scrolledtext.ScrolledText(root , font="lucida 13")
TextArea.pack(expand=True,fill=BOTH)
file = None

menubar = Menu(root)  

def cut():
    TextArea.event_generate(("<<cut>>"))

def copy():
    TextArea.event_generate(("<<copy>>"))

def paste():
    TextArea.event_generate(("<<paste>>"))

def about():
    showinfo("Notepad", "Notepad developed 1829")

    
file = Menu(menubar, tearoff=0)  
file.add_command(label="New",command=newFile)  
file.add_command(label="Open",command=openFile)  
file.add_command(label="Save",command=saveFile)   
  
file.add_separator()  
  
file.add_command(label="Exit", command=root.quit)  
  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
  
edit.add_separator()  
  
edit.add_command(label="Cut",command=cut)  
edit.add_command(label="Copy",command=copy)  
edit.add_command(label="Paste",command=paste)  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")  
  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About",command=about)  
menubar.add_cascade(label="Help", menu=help) 



  
root.config(menu=menubar) 


root.mainloop()  