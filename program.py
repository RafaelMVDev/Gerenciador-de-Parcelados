import tkinter

import pandas as pd
import openpyxl
import numpy as np
from tkinter import *


# Assets
WINDOW_ICON = "Assets/programicon.ico"
class Aplication(Tk):
    def __init__(self):
        super().__init__()


        sc_height = self.winfo_screenheight()
        sc_width = self.winfo_screenwidth()

        self.iconbitmap(WINDOW_ICON)

        self.minsize(250,300)
        self.resizable = True
        self.geometry("%dx%d" % (sc_width, sc_height))

        self.title("Construtor de Tabela de Juros")

        # Initializing children and program
        MainFrame(self)
        self.mainloop()

class MainFrame(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.configure(background = "#FFFFFF")
        self.pack(fill = BOTH, expand = True)

        MenuBackground(self)

class MenuBackground(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.configure(
            background = "#625f5f",
        )
        self.pack()



myApp = Aplication()
