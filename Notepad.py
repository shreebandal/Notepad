from tkinter import *
import tkinter.messagebox as tmsg
import datetime
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def createFile(temp):
    window.title("Untitled - Notepad")
    window.file=None
    window.textArea.delete(1.0,END)
def openNewWindow(temp):
    # os.system('Notepad')
    obj = newWindow()
    obj.createMenuBar()
    obj.outputScreen()
def openFile(temp):
    window.file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if window.file == "":
        window.file = None
    else:
        window.title(os.path.basename(window.file) + " - Notepad")
        window.textArea.delete(1.0,END)
        print(window.file)
        file = open(window.file,"r")
        window.textArea.insert(1.0,file.read())
        file.close()
def saveFile(temp):
    if window.file == None:
        window.file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if window.file == "":
            window.file = None
        else:
            file = open(window.file, "w")
            file.write(window.textArea.get(1.0, END))
            file.close()
            window.title(os.path.basename(window.file) + " - Notepad")
    else:
        file = open(window.file, "w")
        file.write(window.textArea.get(1.0, END))
        file.close()
def saveAsFile(temp):
    window.file = asksaveasfilename(initialfile=os.path.basename(window.file), defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if window.file == "":
        window.file = None
    else:
        file = open(window.file, "w")
        file.write(window.textArea.get(1.0, END))
        file.close()
        window.title(os.path.basename(window.file) + " - Notepad")
def exitFile(temp):
    window.destroy()
def undo(temp):
    if window.file != None:
        window.fileContent = window.textArea.get(1.0, END)
        window.textArea.delete(1.0, END)
        file = open(window.file, "r")
        window.textArea.insert(1.0, file.read())
        file.close()
def redo(temp):
    if window.fileContent != "":
        window.textArea.delete(1.0, END)
        window.textArea.insert(1.0,window.fileContent)
def cut(temp):
    window.textArea.event_generate(("<<Cut>>"))
def copy(temp):
    window.textArea.event_generate(("<<Copy>>"))
def paste(temp):
    window.textArea.event_generate(("<<Paste>>"))
def delete(temp):
    sel = window.textArea.selection_get()
    startIndex = window.textArea.search(sel, '1.0', stopindex=END)
    endIndex = f"1.{int(window.textArea.search(sel, '1.0', stopindex=END)[2::])+len(sel)}"
    window.textArea.delete(startIndex,endIndex)
def find(temp):
    newWindow = Toplevel(window)
    newWindow.wm_iconbitmap("search.ico")
    newWindow.title("Find")
    newWindow.geometry("370x120")
    newWindow.minsize(370, 120)
    newWindow.maxsize(370, 120)
    newFrame = Frame(newWindow)
    Label(newFrame, text='\t').pack(side=LEFT)
    newFrame.pack()
    frame = Frame(newWindow)
    Label(frame, text='Find What\t\t').pack(side=LEFT)
    edit = Entry(frame)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    Label(frame, text='   ').pack(side=LEFT)
    Find = Button(frame, text='Find Next')
    Find.pack(side=RIGHT)
    frame.pack()
    def find():
        window.textArea.tag_remove(SEL, "1.0", "end")
        sel = edit.get()
        if sel:
            try:
                start = window.textArea.search(sel, window.start, nocase=1,stopindex=END)
                end = '% s+% dc' % (start, len(sel))
                window.textArea.tag_add(SEL, start , end)
                window.start = end
            except:
                window.start = 1.0
                start = window.textArea.search(sel, window.start, nocase=1, stopindex=END)
                end = '% s+% dc' % (start, len(sel))
                window.textArea.tag_add(SEL, start, end)
                window.start = end
        edit.focus_set()
    Find.config(command=find)
def replace(temp):
    newWindow = Toplevel(window)
    newWindow.wm_iconbitmap("search.ico")
    newWindow.title("Replace")
    newWindow.geometry("370x160")
    newWindow.minsize(370, 160)
    newWindow.maxsize(370, 160)
    newFrame1 = Frame(newWindow)
    Label(newFrame1, text='\t').pack(side=LEFT)
    newFrame1.pack()
    frame1 = Frame(newWindow)
    Label(frame1, text='Find What   \t\t').pack(side=LEFT)
    edit = Entry(frame1)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    Label(frame1, text='   ').pack(side=LEFT)
    frame1.pack()
    newFrame2 = Frame(newWindow)
    Label(newFrame2, text='\t').pack(side=LEFT)
    newFrame2.pack()
    frame2 = Frame(newWindow)
    Label(frame2, text='Replace With\t\t').pack(side=LEFT)
    edit1 = Entry(frame2)
    edit1.pack(side=LEFT, fill=BOTH, expand=1)
    edit1.focus_set()
    Label(frame2, text='   ').pack(side=LEFT)
    frame2.pack()
    newFrame3 = Frame(newWindow)
    Label(newFrame3, text='\t').pack(side=LEFT)
    newFrame3.pack()
    newFrame4 = Frame(newWindow)
    ReplaceAll = Button(newFrame4, text='Replace All')
    ReplaceAll.pack(side=RIGHT)
    newFrame4.pack()
    def replace():
        window.textArea.tag_remove(SEL, "1.0", "end")
        sel = edit.get()
        sel1 = edit1.get()
        if sel and sel1:
            while 1:
                start = window.textArea.search(sel, window.start, nocase=1,stopindex=END)
                if not start: break
                end = '% s+% dc' % (start, len(sel))
                window.textArea.delete(start, end)
                window.textArea.insert(start, sel1)
                end = '% s+% dc' % (start, len(sel1))
                window.textArea.tag_add(SEL, start, end)
                window.start = end
        window.start = 1.0
    edit.focus_set()
    ReplaceAll.config(command=replace)

def selectAll(temp):
    window.textArea.tag_add(SEL, "1.0", END)
    window.textArea.mark_set(INSERT, "1.0")
    window.textArea.see(INSERT)
def dateTime(temp):
    window.textArea.insert(INSERT,datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S"))
def zoomIn(temp):
    GUI.size += 3
    window.textArea.config(font = ("Arial", GUI.size))
def zoomOut(temp):
    GUI.size -= 3
    window.textArea.config(font=("Arial", GUI.size))
def defaultZoom(temp):
    GUI.size = 12
    window.textArea.config(font=("Arial", GUI.size))
def about(temp):
    tmsg.showinfo("Notepad","Notepad created by shree")

class GUI(Tk):
    size = 12
    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("Notepad.ico")
        self.title("Untitled - Notepad")
        self.geometry("1200x660")
        self.minsize(1200,660)
        self.file = None
        self.fileContent = ""
        self.start = 1.0

    def createMenuBar(self):
        menuBar = Menu(self)
        #fileMenu
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New",command=createFile)
        fileMenu.add_command(label="New Window",command=openNewWindow)
        fileMenu.add_command(label="Open",command=openFile)
        fileMenu.add_command(label="Save",command=saveFile)
        fileMenu.add_command(label="Save As",command=saveAsFile)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit",command=exitFile)
        menuBar.add_cascade(label="File", menu=fileMenu)
        #editMenu
        editMenu = Menu(menuBar, tearoff=0)
        editMenu.add_command(label="Undo",command=undo)
        editMenu.add_command(label="Redo",command=redo)
        editMenu.add_separator()
        editMenu.add_command(label="Cut",command=cut)
        editMenu.add_command(label="Copy",command=copy)
        editMenu.add_command(label="Paste",command=paste)
        editMenu.add_command(label="Delete",command=delete)
        editMenu.add_separator()
        editMenu.add_command(label="Find",command=find)
        editMenu.add_command(label="Replace",command=replace)
        editMenu.add_separator()
        editMenu.add_command(label="Select All",command=selectAll)
        editMenu.add_command(label="Date/Time",command=dateTime)
        menuBar.add_cascade(label="Edit", menu=editMenu)
        #viewMenu
        viewMenu = Menu(menuBar, tearoff=0)
        viewMenu.add_command(label="Zoom In",command=zoomIn)
        viewMenu.add_command(label="Zoom Out",command=zoomOut)
        viewMenu.add_command(label="Restore Default Zoom",command=defaultZoom)
        menuBar.add_cascade(label="View", menu=viewMenu)
        # helpMenu
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About",command=about)
        menuBar.add_cascade(label="Help", menu=helpMenu)
        self.config(menu=menuBar)

    def outputScreen(self):
        self.textArea = Text(self,font="Arial 12")
        self.textArea.pack(expand=True,fill=BOTH)
        scrollY = Scrollbar(self.textArea)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollY.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=scrollY.set)

    def shortcuts(self):
        self.textArea.bind("<Control-n>", createFile)
        self.textArea.bind("<Control-w>", openNewWindow)
        self.textArea.bind("<Control-o>", openFile)
        self.textArea.bind("<Control-s>", saveFile)
        self.textArea.bind("<Control-a>", saveAsFile)
        self.textArea.bind("<Control-e>", exitFile)
        self.textArea.bind("<Control-z>", undo)
        self.textArea.bind("<Control-r>", redo)
        self.textArea.bind("<Control-f>", find)
        self.textArea.bind("<Control-h>", replace)
        self.textArea.bind("<Control-d>", dateTime)
        self.textArea.bind("<Control-+>", zoomIn)
        self.textArea.bind("<Control-*>", zoomOut)
        self.textArea.bind("<Control-0>", defaultZoom)
        self.textArea.bind("<Control-q>", about)

class newWindow(Toplevel,GUI):
    def __init__(self):
        Toplevel.__init__(self, master=None)
        self.wm_iconbitmap("Notepad.ico")
        self.geometry("1200x660")
        self.minsize(1200, 660)
        self.file = None
        self.fileContent = ""

if __name__=='__main__':
    window = GUI()
    window.createMenuBar()
    window.outputScreen()
    window.shortcuts()
    window.mainloop()