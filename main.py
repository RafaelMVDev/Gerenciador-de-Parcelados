# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import openpyxl
import numpy as np
from tkinter import *


MainGUI = Tk()
MainGUI.title("Criar Tabela de Parcelados")
MainGUI.resizable(True,True)

MainFrame = Frame(MainGUI)
MainFrame.pack()
def Idk(TkinterVar,index,acessMode):
    print(TkinterVar.__str__()," ",index,acessMode)


StrVal = StringVar()
StrVal.trace_variable('r', Idk)
StrVal.set('Hello')

OGFile = Entry(MainFrame)
OGFile.pack()
OGFile.configure(background = 'Red')

print(StrVal.get())
print(StrVal.trace_vinfo())

MainGUI.mainloop()
meses = [
         'Janeiro','Fevereiro','Março','Abril',
         'Maio','Junho','Julho','Agosto',
         'Setembro','Outubro', 'Novembro','Dezembro'
        ]

MES = '01'

CAMINHO = r'C:\Users\win\Documents\testespython.xlsx'
tabela = pd.read_excel(CAMINHO)

DT = pd.DataFrame()
DT["Column1"] = [1,2,3,4,5]

print(DT)

