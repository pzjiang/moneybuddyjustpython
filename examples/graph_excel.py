import plotly
import plotly.graph_objects as go
import pandas as pd
import tkinter as tk
from functools import partial


def scatter(file_name):
   

    df = pd.read_excel(file_name)
    print(df)


    data = [go.Scatter(x = df["Months on Position"], y=df["Current Base"],mode = 'markers',text=df["Personnel ID"])]
    #print(df["Months on Position"])


    fig = go.Figure(data)

    button = [dict(args = [{"x":0}],label = "Empty",method = "restyle")]
    button2 = [dict(args = [{"y":0}],label = "Empty",method = "restyle")]

    for col in df:
        button.append(dict(args = [{"x":[df[col]]},{"xaxis":{"title":col}}],label = col,method = "update"))
        button2.append(dict(args = [{"y":[df[col]]},{"yaxis":{"title":col}}],label = col,method = "update"))

    #print (button)

    fig.update_layout(
        title = "Test Title",
        xaxis_title = "Start: Months on Position",
        yaxis_title = "Start: Current Base",
        updatemenus=[
            dict(
                
                buttons = button,
                direction="down",
                pad={"r":10,"t":10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.12,
                yanchor="top"
                ),
            dict(
                buttons = button2,
                direction = "down",
                pad={"r":10,"t":10},
                showactive=True,
                x=0.4,
                xanchor="left",
                y=1.12,
                yanchor="top",

                )


            ],
        annotations=[
            dict(text = "X axis:",x=0,xref = "paper",y=1.08,yref = "paper",align="left",showarrow = False),
            dict(text = "Y axis:",x=.25,xref = "paper",y=1.08,yref = "paper",align="left",showarrow = False)
,
            ]

        )
    fig.show()
    return 1


    
    #plotly.offline.plot(fig, filename = "share.html")

#scatter()


def box_plot(file_name):
    excel_file = file_name
    df = pd.read_excel(excel_file)
    print(df)

    data = [go.Box( y=df["Months on Position"],x=df["Department"])]
    fig = go.Figure(data)


    
    button = [dict(args = [{"x":0}],label = "Empty",method = "restyle")]
    button2 = [dict(args = [{"y":0}],label = "Empty",method = "restyle")]

    for col in df:
        button.append(dict(args = [{"x":[df[col]]},{"xaxis":{"title":col}}],label = col,method = "update"))
        button2.append(dict(args = [{"y":[df[col]]},{"yaxis":{"title":col}}],label = col,method = "update"))


  
    fig.update_layout(
        title = "Test Title",
        yaxis_title = "months",
        xaxis_title = "Department",

        updatemenus=[
            dict(
                
                buttons = button,
                direction="down",
                pad={"r":10,"t":10},
                showactive=True,
                x=0.1,
                xanchor="left",
                y=1.18,
                yanchor="top"
                ),
            dict(
                buttons = button2,
                direction = "down",
                pad={"r":10,"t":10},
                showactive=True,
                x=0.4,
                xanchor="left",
                y=1.18,
                yanchor="top",

                )


            ]
        )

    fig.show()

    return 1
    



    
def main():
    """
    df = pd.read_excel("example.xlsx")
    

    buttons=list([
                    #dict(args=["x",df["Personnel ID"]],label="Personal ID",method="restyle"),
                    dict(args = [{"x":[df["Current Base"]]}],label = "Base",method = "restyle"),
                    #dict(args=["x",df["Increase amount"]],label="increase",method="restyle"),
                    dict(args = [{"x":[df["Months on Position"]]}],label="Month",method="restyle")

                    ])

    print(buttons)
    
    for col in df:
        print(col)
    """
    window = tk.Tk()
    window.title("Main Window")
    window.geometry("300x300")
    texting = tk.StringVar()
    def scatter_event(event):
        scatter(texting.get())

    def box_event():
        #print(texting.get())
        box_plot(texting.get())
    
    files_name = tk.Entry(window,width = 25,textvariable = texting)
    label1 = tk.Label(text="Please enter file path below")
    label1.grid(column=1,row=1)
    files_name.grid(column=1,row=2)
    
    #graph_options = tk.OptionMenu(window,tk.IntVar(),"Scatter","Box")

    
    button1 = tk.Button(window,text = "Scatter Plot Button")
    button1.grid(column=3,row=4)
    button1.bind("<Button-1>",scatter_event)
    button2 = tk.Button(window,text = "Box Plot Button",command = partial(box_event))
    button2.grid(column =3, row = 5)
    
    
    
    window.mainloop()
    




    
    print("welcome to Quarantine Boredom Project 2")
    print("Please enter the file path for the excel file we will be working with today:")
    file_name = input()
   

    while (True):
        print("Enter the number of the graph you would like to work with")
        print("1. Scatter Plot\n2. Nothing yet")
        graph_choice = eval(input())

        if graph_choice==1:

            scatter("example.xlsx")
        elif graph_choice==2:
            print("What would you like the box plots to be sorted by?")
            sort_box_by = input()
            
            box_plot("example.xlsx")
            break

    







main()
