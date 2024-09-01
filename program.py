import tkinter

import pandas as pd
import openpyxl
import numpy as np
from time import sleep
#from tkinter import *
from customtkinter import *

# Assets
WINDOW_ICON = "Assets/programicon.ico"

#functions

#def disable_fullscreen(masterWindow):
    #if masterWindow.


class Aplication(CTk):
    def __init__(self):
        super().__init__()


        sc_height = self.winfo_screenheight()
        sc_width = self.winfo_screenwidth()

        self.iconbitmap(WINDOW_ICON)

        self.minsize(250,300)
        self.resizable = True
        self.geometry(f'{sc_width}x{sc_height}+0+0')

        print(self.geometry())

        self.title("Construtor de Tabela de Juros")

        # Initializing children and program
        MainFrame(self)
        self.mainloop()

class MainFrame(CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        toplevel = self.winfo_toplevel()
        nColumns, nRows = toplevel.grid_size()

        print(nColumns,nRows)
        self.configure(fg_color = "#FFFFFF")
        self.pack(fill = BOTH, expand = 1)
     
        #TaskBar(self)
        MenuBackground(self)

class TaskBar(CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.configure(
            fg_color = "#e600ff",
            height = 50,
            )
        self.pack(fill = X)



class MenuBackground(CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.configure(
            fg_color = "#625f5f",
            bg_color = "#625f5f",
            border_width = 0,
            width = 150
            
        )
        self.pack(side = LEFT, fill = Y)
        MenuButton(self,'TestButton123')
        
class MenuButton(CTkButton):
    def __init__(self,parent,text,actCallback = None, paddingY = None):
        super().__init__(parent)
        self._text = text
        self.width = 150
        self.height = 50
        self._text_color = 'white'
        self.configure(
            fg_color = "#625f5f",
            bg_color = "#625f5f",
            corner_radius = 0
        )
        self._hover_color= "#545454"
        self.grid()


myApp = Aplication()
