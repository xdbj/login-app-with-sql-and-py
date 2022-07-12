import tkinter
from attr import has
import messagebox
import bcrypt
main_window=tkinter.Tk()
main_window.title('pyfit')
main_window.geometry('600x600')
user_input=tkinter.StringVar()
pass_input=tkinter.StringVar()
reguser_input = tkinter.StringVar()
reguserpass_input = tkinter.StringVar()
padd=20
main_window['padx']=padd

import sqlite3







# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *


# mainloop, runs infinitelymainloop()

















info_label=tkinter.Label(main_window, text='Login Application')
info_label.grid(row=0, column=0, pady=20)

info_user=tkinter.Label(main_window, text='Username')
info_user.grid(row=1, column=0)
userinput=tkinter.Entry(main_window, textvariable=user_input)
userinput.grid(row=1, column=1)

info_pass=tkinter.Label(main_window, text='Password')
info_pass.grid(row=2, column=0, pady=20)
passinput=tkinter.Entry(main_window, textvariable=pass_input, show='*')
passinput.grid(row=2, column=1)

lablee = tkinter.Label(main_window, text='REGISTER')
lablee.grid(row=4, column=0, pady=20)
info_user=tkinter.Label(main_window, text='create a Username')
info_user.grid(row=5, column=0)
reguserinput=tkinter.Entry(main_window, textvariable=reguser_input)
reguserinput.grid(row=5, column=1)

info_pass=tkinter.Label(main_window, text='create a Password')
info_pass.grid(row=7, column=0, pady=20)
regpassinput=tkinter.Entry(main_window, textvariable=reguserpass_input, show='*')
regpassinput.grid(row=7, column=1)
db=sqlite3.connect('main.db')
cursor=db.cursor()
#cursor.execute("""DROP TABLE "users" """)



def login():
    db=sqlite3.connect('main.db')
    cursor=db.cursor()
    
    cursor.execute("SELECT * FROM users where username=? AND password=?",(userinput.get(), passinput.get()))
    row=cursor.fetchone()
    if row:
        messagebox.showinfo('info', 'login success')
    else:
        messagebox.showinfo('info', 'login failed')
        cursor.connection.commit()
        db.close()


def register():
    

    db = sqlite3.connect('main.db')

    cur = db.cursor()
    sqlite_insert_query = f"INSERT INTO users (username, password) VALUES ('{reguserinput.get()}', '{regpassinput.get()}')"
    lene = len(regpassinput.get())
    if lene <= 8:

        
        cur.connection.commit()
        messagebox.showinfo('warning', 'password must be longer than 8 characters')



    cur.execute(f"SELECT * FROM users WHERE username='{reguserinput.get()}'")
    exists = cur.fetchone()
    if exists:
        messagebox.showinfo('info', 'username already exists')



    
    
    
    else:
        count = cur.execute(sqlite_insert_query)
        row=cur.fetchall()
        cur.connection.commit()
        import time
        messagebox.showinfo('info', 'register success')

login_btn=tkinter.Button(main_window, text='Login', command=login)
login_btn.grid(row=4, column=1)
login_btn=tkinter.Button(main_window, text='Register', command=register)
login_btn.grid(row=8, column=1)


main_window.mainloop()




