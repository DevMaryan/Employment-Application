from tkinter import *

class aboutHowToUse(Toplevel):
    def __init__(self):
        root = Tk()
        root.title('How To Use the APP')
        root.geometry('800x600+400+200')
        root.iconbitmap('w','img/icon.ico')
        root.resizable(False, False)
