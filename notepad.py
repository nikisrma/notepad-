from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename

import os
def newFile():
     global file
     root.tite("Untitled - notepad")
     file = None
     TextArea.delete(1.0,END)
def openFile():
     global file
     file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])

     if file == "":
          file = None
     else:
          root.title(os.path.basename(file) + " - Notepad")
          TextArea.delete(1.0,END)
          f = open(file, "r")

def saveFile():
     global file
     if file == None:
          file = asksaveasfilename(initialfile = 'untitled.txt',defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])
          if file =="":
               file = None
          else:
               f = open(file,"w")
               f.write(TextArea.get(1.0, END))
               f.close
          root.title(os.path.basename(file) + "- Notepad")
          print("File Saved")
     else:
          f = open(file, "w")
          f.write(TextArea.get(1.0, END))
          f.close
def quitApp():
     root.destroy()
def cut():
     TextArea.event_generate((""<<Cut>>""))

def copy():
     TextArea.event_generate((""<<Copy>>""))
def paste():
     TextArea.event_generate((""<<Paste>>""))
def about():
     showinfo("Notepad", "notepad by coder")
if __name__ == '__main__':
     root = Tk()
     root.title("untitled-notepad")
     root.geometry("644x788")

     TextArea = Text(root, font="lucida 13")
     file = None
     TextArea.pack(expand=TRUE,fill=BOTH)

     MenuBar = Menu(root)
     FileMenu = Menu(MenuBar, tearoff=0)

     FileMenu.add_command(label="New", command=newFile)
     FileMenu.add_command(label="Open", command=openFile)
     FileMenu.add_command(label="Save", command=saveFile)
     FileMenu.add_separator()
     FileMenu.add_command(label="Exit", command=quitApp)
     MenuBar.add_cascade(label="File", menu=FileMenu)

     EditMenu = Menu(MenuBar, tearoff=0)
     EditMenu.add_command(label = "cut",command=cut)
     EditMenu.add_command(label="copy", command=copy)
     EditMenu.add_command(label="paste", command=paste)
     MenuBar.add_cascade(label="Edit", menu = EditMenu)

     HelpMenu = Menu(MenuBar, tearoff=0)
     HelpMenu.add_command(label="About Notepad", command=about)
     MenuBar.add_cascade(label="help", menu=HelpMenu)


     root.config(menu=MenuBar)

     Scroll = Scrollbar(TextArea)
     Scroll.pack(side=RIGHT, fill=Y)
     Scroll.config(command=TextArea.yview)
     TextArea.config(yscrollcommand=Scroll.set)



     root.mainloop()