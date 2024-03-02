# loginGui.py
import tkinter as tk
from tkinter import ttk
from login import button_function

class LoginGui:
    def __init__(self,new_root,master,loginbutton):
        
        new_root.title("Login Form")

        new_root.geometry('332x240')
        new_root.resizable(0, 0)

        window_width = new_root.winfo_reqwidth()
        window_height = new_root.winfo_reqheight()
        position_right = int(new_root.winfo_screenwidth()/2 - window_width/2 - 30)
        position_down = int(new_root.winfo_screenheight()/2 - window_height/2 - 110)
        new_root.geometry("+{}+{}".format(position_right, position_down))

        new_root.wm_iconbitmap(r'D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\hospital.ico')

        frame = tk.Frame(new_root, bg='light blue')
        frame.pack(fill='both', expand=True)

        label_username = tk.Label(frame, text="User Name", bg='light blue',font=("Comic Sans MS", 12,'bold'))
        label_password = tk.Label(frame, text="Password", bg='light blue',font=("Comic Sans MS", 12,'bold'))
        label_usertype = tk.Label(frame, text="User Type", bg='light blue',font=("Comic Sans MS", 12,'bold'))

        entry_username = ttk.Entry(frame,font=("Comic Sans MS", 12,'bold'))
        entry_password = ttk.Entry(frame, show="*",font=("Comic Sans MS", 12,'bold'))
        entry_usertype = ttk.Combobox(frame, values=["Pharmacist", "Admin"],font=("Comic Sans MS", 12,'bold'))

        button_login = tk.Button(frame, text="Login", command=lambda: button_function.login(entry_username, entry_password, entry_usertype,new_root,master,loginbutton), bg='blueviolet',relief='ridge',borderwidth=0, font=("Comic Sans MS", 15,'bold'),fg='white',width=10)

        button_create = tk.Button(frame,text="Create Account", command=lambda: button_function.create_account_gui(new_root),bg='gray70',relief='ridge',borderwidth=0,font=("Comic Sans MS", 15, 'bold'),fg='black',width=14)

        label_username.grid(row=0, column=0, pady=(10, 0),padx=4)
        label_password.grid(row=1, column=0, pady=(10, 0))
        label_usertype.grid(row=2, column=0, pady=(10, 0),padx=5)
        entry_username.grid(row=0, column=1, pady=(10, 0))
        entry_password.grid(row=1, column=1, pady=(10, 0))
        entry_usertype.grid(row=2, column=1, pady=(10, 0),padx=5)
        button_login.grid(row=3, column=1, pady=(10, 0),padx=0)
        button_create.grid(row=4, column=1, pady=(10, 0),padx=-0)

        
