from venmo_api import Client
import plotly
import plotly.graph_objects as go
import pandas as pd
import tkinter as tk
import tkinter.font as font
from functools import partial
from graphics import *



def main():

    def submitTemp():
        print("hello world")

    loginwindow = tk.Tk()
    loginwindow.title("Login Window")
    loginwindow.geometry("700x400")
    entry_font = ('Verdana', 20)
    username = tk.StringVar(value='entry_font')
    password = tk.StringVar(value='entry_font')

    welcomelabel = tk.Label(loginwindow, text="hello and welcome to money buddy!")
    welcomelabel.config(font=("Consolas", 16))
    welcomelabel.grid(column = 1, row = 1, sticky="NESW")

    userlabel = tk.Label(loginwindow, text="Username:  ",width = 14)
    userlabel.config(font=("Consolas",16))
    userlabel.grid(column=1, row=2, sticky="w")

    userinput = tk.Entry(loginwindow, width = 20, textvariable = username, font=("Consolas",12))
    userinput.grid(column=2, row=2, sticky="e")

    passlabel = tk.Label(loginwindow, text = "Password:  ", width = 14)
    passlabel.config(font=("Consolas", 16))
    passlabel.grid(column=1, row = 3, sticky="nw")
    
    passinput = tk.Entry(loginwindow, width = 20, textvariable = password, font=("Consolas",12), show="*")
    passinput.grid(column=2, row = 3, sticky="ne")

    submit = tk.Button(loginwindow, text="login", command= submitTemp, width = 14)
    submit.grid(column = 2, row = 4, sticky="ne")
    
    loginwindow.grid_rowconfigure(0, weight=1)
    loginwindow.grid_rowconfigure(3, weight=1)
    loginwindow.grid_columnconfigure(0, weight=1)
    loginwindow.grid_columnconfigure(3, weight=1)
    

    loginwindow.mainloop()





main()



def test():
        
    access_token = Client.get_access_token(username="", password="");

    venmo = Client(access_token=access_token)


    users = venmo.user.search_for_users(query="Peter");
    for user in users:
        print(user.username)

    """
    #in order to log out:
    venmo.log_out("Bearer access_token")
    #access_token is a variable that holds the value of the access code. replace with the given access token

    """


    """
    #structure of transaction





    """


    def callback(transactions_list):
        for transaction in transactions_list:
            print(transaction)
            #print(transaction.id)
            #print(type(transaction))
            #break;

    used = venmo.user.get_my_profile();

    """
    print("type below");
    print(type(used));
    print("==-==-=-=-=-=");
    """

    venmo.user.get_user_transactions(user=used,callback=callback,limit=1000)


        
    #venmo.log_out("Bearer " + access_token)
    #print(access_token)


    """
    try:
        #this is to search for users
        users = venmo.user.search_for_users(query="Peter");
        for user in users:
            print(user.username)


        #use callback to make it multi-threaded

        def callback(users):
            for user in users:
                print(user.username)
        venmo.user.search_for_users(query="",callback=callback,page=2,count=10)




        
        #need to log out manually access token doesn't expire
        venmo.log_out("")

        #request money
        venmo.payment.request_money(money int, "message", id)


        #send money
        venmo.payment.send_money(money int, "messsage", id)



        #callback to get transactions
        def callback(transactions_list):
            for transaction in transactions_list:
                print(transaction)

        venmo_api.user.get_user_transactions(user_id="", callback=callback)



    except:
        print("an error has occured");
    """


