from venmo_api import Client
import plotly
import plotly.graph_objects as go
import pandas as pd
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from functools import partial
from graphics import *

def submit(username1, password1, access_token):
    venmo1 = None

    

   
    try:
        venmo1 = Client.get_access_token(username=username1, password=password1)
    except:
        messagebox.showerror(title="Login Error", message="Invalid credentials, please try again :(")
        return "F"

    total = 0
    relationdict = {}

    used = venmo1.user.get_my_profile();
    valueMul = 1

    
    def callback(transactions_list):
        for transaction in transactions_list:
            valueMul = 1
            if transaction.payment_type != "pay":
                valueMul = -1
            if transaction.actor.username == used.username:
                total -= transaction.amount * valueMul
                relationdict[transaction.target.username] -= transaction.amount * valueMul
            else:
                 print ("no")

    """
    print("type below");
    print(type(used));
    print("==-==-=-=-=-=");
    """

    venmo1.user.get_user_transactions(user=used,callback=callback,limit=1000)

    window = GraphWin("Analysis",1200,800)

    
    
    

    
    return venmo1

#315ee5d2cec5ee32a91d4537f9ccd36a93c528be698e87cc7e4cb606f2f022db
def main():

    access_token = ""
    venmo = None

    def submitTemp():
        venmo = submit(userinput.get(),passinput.get(),access_token)


    def logOut():
        messagebox.showinfo(title="Log out", message="Sucessfully logged out!")
        venmo.log_out("Bearer " + access_token)

    def quitProgram():
        loginwindow.destroy()
        exit()

    loginwindow = tk.Tk()
    loginwindow.title("Home")
    loginwindow.geometry("700x400")
    
    username = tk.StringVar()
    password = tk.StringVar()

    

    welcomelabel = tk.Label(loginwindow, text="hello and welcome to money buddy!")
    welcomelabel.config(font=("Consolas", 26))
    welcomelabel.grid(column = 1, row = 1, sticky="N")

    loginPromptLabel = tk.Label(loginwindow, text="Please login to your venmo :) we will not steal your data, pinky swear")
    loginPromptLabel.config(font=("Consolas", 10))
    loginPromptLabel.grid(column = 1, row = 2, sticky="N")

    userlabel = tk.Label(loginwindow, text="Username:  ",width = 14)
    userlabel.config(font=("Consolas",16))
    userlabel.grid(column=1, row=4, sticky="SW")

    userinput = tk.Entry(loginwindow, width = 20, textvariable = username, font=("Consolas",12))
    userinput.grid(column=1, row=4, sticky="ES")

    passlabel = tk.Label(loginwindow, text = "Password:  ", width = 14)
    passlabel.config(font=("Consolas", 16))
    passlabel.grid(column=1, row = 5, sticky="nw")
    
    passinput = tk.Entry(loginwindow, width = 20, textvariable = password, font=("Consolas",12), show="*")
    passinput.grid(column=1, row = 5, sticky="ne")

    submitButton = tk.Button(loginwindow, text="login", command= submitTemp, width = 14)
    submitButton.grid(column = 1, row = 7, sticky = "W")

    logButton = tk.Button(loginwindow, text="logout", command = logOut, width = 14)
    logButton.grid(column = 1, row = 7)

    exitButton = tk.Button(loginwindow, text="exit", command=quitProgram, width=14)
    exitButton.grid(column = 1, row = 7, sticky = "E")

    
    loginwindow.grid_rowconfigure(0, weight=1)
    loginwindow.grid_rowconfigure(8, weight=1)
    loginwindow.grid_columnconfigure(0, weight=1)
    loginwindow.grid_columnconfigure(7, weight=1)
    

    loginwindow.mainloop()


    
    print("logged out")
    venmo.log_out("Bearer " + access_token)





#main()


#f8768ce8edbd17afe00ec7f576c0da42867a1a8dc44de3184c6a36f68bd8747f
def test():
        
    access_token = Client.get_access_token(username="Peter-Jiang-8", password="Tigers1614!");
    #access_token = "4fa83ce2e92005ff3c3c5d3398d256d356897686ded129c8340af93a55dffd29"
    
    venmo = Client(access_token=access_token)

    #venmo.log_out("Bearer 4fa83ce2e92005ff3c3c5d3398d256d356897686ded129c8340af93a55dffd29")

    """
    users = venmo.user.search_for_users(query="Peter");
    for user in users:
        print(user.username)


    """
    """
    #in order to log out:
    venmo.log_out("Bearer access_token")
    #access_token is a variable that holds the value of the access code. replace with the given access token

    """


    """
    #structure of transaction

Transaction: (id=2901185891756146731, payment_id=2901185891152167144, date_completed=1576634309, date_created=1576634308, date_updated=1581921114, payment_type=pay, amount=31.0, audience=friends, status=settled, note=To fund your pro gaming career, device_used=iPhone, actor=User: (id=2895490236547072484, username=Peter-Jiang-8, first_name=Peter, last_name=Jiang, display_name=Peter Jiang, phone=None, profile_picture_url=https://s3.amazonaws.com/venmo/no-image.gif, about= , date_joined=1575955334, is_group=False, is_active=True), target=User: (id=2673829792972800777, username=Rachel-Zhang-34, first_name=Rachel, last_name=Zhang, display_name=Rachel Zhang, phone=None, profile_picture_url=https://pics.venmo.com/02fb030c-3c86-48fc-8cb0-a4f32e582cce?width=460&height=460&photoVersion=2, about= , date_joined=1549531350, is_group=False, is_active=True))



    """


    def callback(transactions_list):
        for transaction in transactions_list:
            #print(transaction)
            print(transaction.payment_type=="pay")
            print(transaction.target.first_name)
            #print(type(transaction))
            #break;

    used = venmo.user.get_my_profile();

    """
    print("type below");
    print(type(used));
    print("==-==-=-=-=-=");
    """

    venmo.user.get_user_transactions(user=used,callback=callback,limit=1000)

    venmo.log_out("Bearer " + access_token)
        
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


