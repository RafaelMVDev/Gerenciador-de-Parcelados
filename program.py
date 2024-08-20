import tkinter

import pandas as pd
import openpyxl
import numpy as np
#from tkinter import *
from customtkinter import *

# Assets
WINDOW_ICON = "Assets/programicon.ico"
class Aplication(CTk):
    def __init__(self):
        super().__init__()


        sc_height = self.winfo_screenheight()
        sc_width = self.winfo_screenwidth()

        self.iconbitmap(WINDOW_ICON)

        self.minsize(250,300)
        self.resizable = True
        self.geometry(f'{sc_width}x{sc_height}+{sc_width / 2 - sc_width}x{sc_height / 2 - sc_height}')
        print(self.geometry())

        self.title("Construtor de Tabela de Juros")

        # Initializing children and program
        MainFrame(self)
        self.mainloop()

class MainFrame(CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        #self.configure(background = "#FFFFFF")
        self.pack(fill = BOTH, expand = True)

        MenuBackground(self)

class MenuBackground(CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        #self.configure(
            #background = "#625f5f",
        #)
        self.pack()



myApp = Aplication()
