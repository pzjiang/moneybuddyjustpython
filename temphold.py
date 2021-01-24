from venmo_api import Client
import plotly
import plotly.graph_objects as go
import pandas as pd
import tkinter as tk
import tkinter.font as font
from functools import partial
from graphics import *




def main():
    loginwindow = tk.Tk()
    loginwindow.title("Login Window")
    loginwindow.geometry("700x400")
    entry_font = ('Verdana', 20)
    username = tk.StringVar(value='entry_font')
    password = tk.StringVar(value='entry_font')

    userlabel = tk.Label(loginwindow, text="Username:  ",width = 14)
    userlabel.config(font=("Consolas",16))
    userlabel.grid(column=1, row=1)
    userinput = tk.Entry(loginwindow, width = 20, textvariable = username, font=("Consolas",12))
    userinput.grid(column=1, row=2)

    passlabel = tk.Label(loginwindow, text = "Password:  ", width = 14)
    passlabel.config(font=("Consolas", 16))
    passlabel.grid(column=1, row = 3)
    
    passinput = tk.Entry(loginwindow, width = 20, textvariable = password, font=("Consolas",12), show="*")
    passinput.grid(column=1, row = 4)
    

    loginwindow.mainloop()





main()
