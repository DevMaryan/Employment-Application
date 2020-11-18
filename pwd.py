from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import hashlib
import uuid

con = sqlite3.connect('employer.db')
cur = con.cursor()


class paswd(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('280x110+750+450')
        self.title('Lock the Application')
        self.resizable(False, False)
        self.config(bg = '#333')

        ### Frames in the Main Window ###
        
        # Top Frame
        self.main = Frame(self, bg = '#333')
        self.main.pack(fill = X)


        self.lbl_username = Label(self.main,
                                text = 'Username: ',
                                bg = '#333',
                                fg = '#FFF')
        self.lbl_username.grid(row = 0,
                            column = 0,
                            pady = 5)


        username_value = StringVar()
        username_value.set('Administrator')
        self.username = Entry(self.main,
                            textvariable = username_value,
                            state = 'readonly',
                            width = 30,
                            relief = FLAT)
        self.username.grid(row = 0, column = 1, pady = 5)


        self.lbl_password = Label(self.main,
                                text = 'Password: ',
                                bg = '#333', fg = '#FFF')
        self.lbl_password.grid(row = 1, column = 0, pady = 5, padx = 8)
        self.password_entry = Entry(self.main,
                            width = 30,
                            relief = FLAT,
                            cursor = 'hand2')
        self.password_entry.focus()
        self.password_entry.grid(row = 1, column = 1, pady = 5, padx = 8)
        self.password_entry.config(show = '*', relief = FLAT)


        self.btnLogin = Button(self.main,
                            text = 'Lock',
                            width = 5,
                            padx = 25,
                            bd = 0,
                            cursor = 'hand2',
                            bg = '#1DB954',
                            fg = '#FFF',
                            command = self.chkPass)
        self.btnLogin.grid(row = 3, column = 0, padx = 25, pady =10, columnspan = 2, rowspan = 2, sticky = W)

        self.btnCancel = Button(self.main,
                            text = 'Cancel',
                            width = 5,
                            padx = 25,
                            bd = 0,
                            cursor = 'hand2',
                            bg = '#1DB954',
                            fg = '#FFF',
                            command = self.Destr)
        self.btnCancel.grid(row = 3, column = 1, padx = 25, pady =10, columnspan = 2, rowspan = 2, sticky = E)
            
    def chkPass(self):
  
        def check_password(hashed_password, user_password):
            password, salt = hashed_password.split(':')
            return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
        pas = self.password_entry.get()
        print('Guess pass',pas)

        try:
            query = "SELECT system_password FROM 'system'"
            cur.execute(query,)
            records = cur.fetchone()
            old_pass = records[0]
            print('DB pass ', old_pass)

            if check_password(old_pass, pas):
                messagebox.showinfo('Login was Successful', 'Welcome to Marianos Employment Application')
            else:
                messagebox.showerror('Error', 'The password is incorrect, please try again')
            cur.close()
        except:
            messagebox.showwarning('Warning', 'Fatal Error! What the heck did you do?', icon = 'warning') 

    def Destr(self):
        self.destroy()