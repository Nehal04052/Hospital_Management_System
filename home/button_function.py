# button_function.py
from tkinter import Tk
from login.loginGui import LoginGui   # Import the LoginGui class
def login(master,loginbutton):
    print("Login button clicked!")
    # You can create an instance of LoginGui or perform other actions related to login
    new_root = Tk()
    login_gui = LoginGui(new_root,master,loginbutton)
    # Additional code for login functionality goes here
    new_root.lift()

