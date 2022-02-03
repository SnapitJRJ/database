from tkinter import *
from tkinter import ttk
import sqlite3

stipends_table = """
CREATE table if not exists stipends (
    
    name text,
    date text,
    assignment text,
    credit text,
    debit text,
    comment text
);
"""

# Connect to Database
def create_connection(pathToDataBase):
    connection = None
    try:
        connection = sqlite3.connect(pathToDataBase)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#Inconveniencing piece of code
connection = create_connection('stipends_data.db.sqlite3')
cursor = connection.cursor()


#ROOT Setup
root = Tk()
root.title("Stipends")

#MainFrame Window 
window = ttk.Frame(root, padding="5", width=400, height=250)
window.grid(column=0, row=0, sticky=(N, W, E, S))


#Retrieves the data from the form inputs;
#Sends the data to the Database
def post(*args):
    try:

        cursor.execute(stipends_table)

        profile = (name.get(),date.get(),assignment.get(),credit.get(),debit.get(),comment.get())
        print(len(profile))
        cursor.execute("INSERT into stipends(name,date,assignment,credit,debit,comment) values (?,?,?,?,?,?)", profile)
        
        connection.commit()
        cursor.close

        empty_fields()
       
    except ValueError:
        pass


#Input Variables
name_var = StringVar()
date_var = StringVar()
assignment_var = StringVar()
credit_var = StringVar()
debit_var = StringVar()
comment_var = StringVar()

name_lbl = ttk.Label(window, text="Name: ")
name = ttk.Entry(window, textvariable=name_var)
name_lbl.grid(column=1, row=0, sticky=W)
name.grid(column=1, row=1, sticky='we',columnspan=3)

date_lbl = ttk.Label(window, text="Date: ")
date = ttk.Entry(window, textvariable=date_var)
date_lbl.grid(column=1, row=2, sticky=W)
date.grid(column=1, row=3, sticky='we',columnspan=3)

assignment_lbl = ttk.Label(window, text="Assignment: ")
assignment = ttk.Entry(window, textvariable=assignment_var)
assignment_lbl.grid(column=1, row=4, sticky=W)
assignment.grid(column=1, row=5, sticky='we',columnspan=3)

credit_lbl = ttk.Label(window, text="Credit: ")
credit = ttk.Entry(window, textvariable=credit_var)
credit_lbl.grid(column=1, row=6, sticky=W)
credit.grid(column=1, row=7, sticky='we',columnspan=3)

debit_lbl = ttk.Label(window, text="Debit: ")
debit = ttk.Entry(window, textvariable=debit_var)
debit_lbl.grid(column=1, row=8, sticky=W)
debit.grid(column=1, row=9, sticky='we',columnspan=3)

comment_lbl = ttk.Label(window, text="Comment: ")
comment = ttk.Entry(window, textvariable=comment_var)
comment_lbl.grid(column=1, row=10, sticky=W)
comment.grid(column=1, row=11, sticky='we',columnspan=3)



rand_btn = ttk.Button(window, text="UPDATE")
rand_btn.grid(column=2, row=12, sticky=W)
rand_btn.configure(state='disabled')

post_btn = ttk.Button(window, text="POST", command=post, width=12)
post_btn.grid(column=1, row=12, sticky='we')

def empty_fields():
    name.delete(0, END)
    date.delete(0, END)
    assignment.delete(0, END)
    credit.delete(0, END)
    debit.delete(0, END)
    comment.delete(0, END)




root.mainloop()
