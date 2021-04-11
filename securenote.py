from DES import * #implemented by ourselves
from tkinter import *
from tkinter import simpledialog,ttk
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

import base64
from ttkthemes import ThemedStyle

def newFile():
    global file
    root.title("Untitled - Securenotes")
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
        f = open(file, "r",encoding="utf-8")
        text = f.read()
        #print(text)
        decodekey = simpledialog.askstring(title="Open",prompt="enter the key to decrypt and read/write the file:-")
        if decodekey == "":
         newFile()
        else:
         text = triple_des_decryption(decodekey,text)
         TextArea.insert(1.0, text)
         f.close()

def saveasFile():
        global file
    
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w",encoding="utf-8")
            
            text = TextArea.get(1.0, END)
            l = len(text)
            text += " "*(8 - (l%8))
            encodekey = simpledialog.askstring(title="Save",prompt="enter key for the file to encrypt make the key strong ( min 8 characters):-")
            encrypttext = triple_des_encrption(encodekey,text)
            f.write(encrypttext)
            f.close()
            #print(f.write(TextArea.get(1.0, END))
            root.title(os.path.basename(file) + " - Securenotes")
            print("File Saved")
def saveFile():
        global file
    
        # Save the file
        f = open(file, "w",encoding="utf-8")
        print(TextArea.get(1.0, END))
        
        #print(f.write(TextArea.get(1.0, END))
        text = TextArea.get(1.0, END)
        encodekey = simpledialog.askstring(title="Save",prompt="enter previous key or create new key for the file to encrypt make the key strong ( min 8 characters):-")
        encrypttext = triple_des_encrption(encodekey,text)
        f.write(encrypttext)
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Securenotes", "Securenotes secure notes for secured conscious people\n project by dhruvik and shubham gandhi \nStable version:- 1.0.8 \nDate of production:-11/4/2021 \nMIT licensed\u00a9\n\n")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Securenotes")
    root.geometry("800x500")
    style = ThemedStyle(root)
    style.theme_use('equilux') 

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_command(label = "Save As", command = saveasFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Securenotes", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends
    #toolbar



    toolbar2 = ttk.Frame(root)

       #toolbarend
    root.config(menu=MenuBar)







    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
