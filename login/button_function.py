from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from login import database
from login.database import create_account
import re
from tkinter import Tk, Toplevel
from pharmacist.gui import Pharmacist_Gui
from admin.adminGui import AdminGui

def login(entry_username, entry_password, entry_usertype,new_root,master,login_button):
    username = entry_username.get()
    usertype = entry_usertype.get()
    mydb = database.create_connection("root", "Nehal@5268", "Hospital_Management_System_Database")
    if mydb is not None:
        cursor = mydb.cursor()
        hashed_password = database.hash_password(entry_password.get())
        query = "SELECT usertype FROM users WHERE BINARY username = %s AND usertype = %s AND password = %s"
        values = (username,usertype, hashed_password)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result is not None:
            usertype = result[0]
            print(f"Logged in as {usertype}")
            new_root.withdraw()
              # Destroy the login window
            login_button.config(text="Logout",bg='red',fg='white', command=lambda: logout(master,login_button))
            
            if usertype == "Pharmacist":
                master.iconify()
                root= Toplevel()  # Create a new top-level window
                gui = Pharmacist_Gui(root, entry_username.get())
            elif usertype == "Admin":
                root = Tk()
                AdminGui(root, entry_username.get())   
        else:
            print("Invalid username or password")
            messagebox.showerror("Error", "Invalid User Name,User Type or Password")
            new_root.lift()

    else:
        print("Could not connect to database")

def logout(master,login_button):
    import home.button_function
    # Add any logout functionality here
    print("Logged out")
    master.deiconify()
    
    login_button.config(text="Login",bg='blueviolet',fg='white', command=lambda: home.button_function.login(master,login_button))
    

def create_account_gui(new_root):
    # Create a new Tkinter window
    create_account_root = tk.Tk()
    create_account_root.title("Create Account")

    # Set the window size
    create_account_root.geometry('382x335')

    # Disable maximize button
    create_account_root.resizable(0, 0)

    # Center the window
    window_width = create_account_root.winfo_reqwidth()
    window_height = create_account_root.winfo_reqheight()
    position_right = int(create_account_root.winfo_screenwidth()/2 - window_width/2 - 30)
    position_down = int(create_account_root.winfo_screenheight()/2 - window_height/2 - 110)
    create_account_root.geometry("+{}+{}".format(position_right, position_down))
    create_account_root.wm_iconbitmap(r'D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\hospital.ico')

    # Create a frame
    frame = tk.Frame(create_account_root, bg='light blue')
    frame.pack(fill='both', expand=True)

    # Create labels and entry fields
    label_firstname = tk.Label(frame, text="First Name", bg='light blue',font=("Comic Sans MS", 12,'bold'))
    label_lastname = tk.Label(frame, text="Last Name", bg='light blue',font=("Comic Sans MS", 12,'bold'))
    label_email = tk.Label(frame, text="Email ID", bg='light blue',font=("Comic Sans MS", 12,'bold'))
    label_username = tk.Label(frame, text="User Name", bg='light blue',font=("Comic Sans MS", 12,'bold'))
    label_password = tk.Label(frame, text="Password", bg='light blue',font=("Comic Sans MS", 12,'bold'))
    label_reenter_password = tk.Label(frame, text="Re-enter Password", bg='light blue',font=("Comic Sans MS", 12,'bold'))
    label_usertype = tk.Label(frame, text="User Type", bg='light blue',font=("Comic Sans MS", 12,'bold'))

    entry_firstname = ttk.Entry(frame,font=("Comic Sans MS", 12,'bold'))
    entry_lastname = ttk.Entry(frame,font=("Comic Sans MS", 12,'bold'))
    entry_email = ttk.Entry(frame,font=("Comic Sans MS", 12,'bold'))
    entry_username = ttk.Entry(frame,font=("Comic Sans MS", 12,'bold'))
    entry_password = ttk.Entry(frame, show="*",font=("Comic Sans MS", 12,'bold'))
    entry_reenter_password = ttk.Entry(frame, show="*",font=("Comic Sans MS", 12,'bold'))
    entry_usertype = ttk.Combobox(frame, values=["Pharmacist", "Admin"],font=("Comic Sans MS", 12,'bold'))

    mydb = database.create_connection("root", "Nehal@5268", "Hospital_Management_System_Database")

    def show_error_message(message):
     messagebox.showerror("Error", message)
     create_account_root.lift()

    def create_account_command():
     firstname = entry_firstname.get()
     lastname = entry_lastname.get()
     email = entry_email.get()
     password = entry_password.get()
     reenter_password = entry_reenter_password.get()
 
    # Check if first name contains only alphabets
     if not firstname.isalpha():
      show_error_message("First name should contain only alphabets.")
      return

    # Check if last name contains only alphabets
     if not lastname.isalpha():
      show_error_message("Last name should contain only alphabets.")
      return

    # Check if email is valid
     if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
      show_error_message("Email should contain '@' and '.com'.")
      return

     if password == reenter_password:
      success = create_account(mydb, firstname, lastname, email, entry_username.get(), password, entry_usertype.get())
      if success:
       messagebox.showinfo("Success", "Account created successfully!")
       create_account_root.destroy()  # Close the create account window
       new_root.lift()
       new_root.attributes('-topmost', True)
      else:
       show_error_message("Could not create account. Please try again.")
     else:
       show_error_message("Passwords do not match. Please try again.")


    button_create = tk.Button(frame, text="Create Account", command=create_account_command,bg='gray70',relief='ridge',borderwidth=0,font=("Comic Sans MS", 15,'bold'),fg='black',width=14)

    # Grid layout
    label_firstname.grid(row=0, column=0, pady=(10, 0))
    label_lastname.grid(row=1, column=0, pady=(10, 0))
    label_email.grid(row=2, column=0, pady=(10, 0))
    label_username.grid(row=3, column=0, pady=(10, 0))
    label_password.grid(row=4, column=0, pady=(10, 0))
    label_reenter_password.grid(row=5, column=0, pady=(10, 0))
    label_usertype.grid(row=6, column=0, pady=(10, 0))
    entry_firstname.grid(row=0, column=1, pady=(10, 0))
    entry_lastname.grid(row=1, column=1, pady=(10, 0))
    entry_email.grid(row=2, column=1, pady=(10, 0))
    entry_username.grid(row=3, column=1, pady=(10, 0))
    entry_password.grid(row=4, column=1, pady=(10, 0))
    entry_reenter_password.grid(row=5, column=1, pady=(10, 0))
    entry_usertype.grid(row=6, column=1, pady=(10, 0))
    button_create.grid(row=7, column=0, columnspan=2, pady=(10, 0))

    def on_close(new_root):
    # Function to be called when the window is closed
     new_root.lift()  # Lift the login window to the top
     new_root.attributes('-topmost', True)
     create_account_root.destroy()  # Close the create account window
     
# Bind the protocol to call the function when the window is closed
    create_account_root.protocol("WM_DELETE_WINDOW", lambda: on_close(new_root))
    create_account_root.mainloop()