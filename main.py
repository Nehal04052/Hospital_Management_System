# main.py
from tkinter import Tk
from home.gui import Application  # Import the Application class from home.gui

def main():
    root = Tk()
    root.state('zoomed')  # This will maximize the window
    app = Application(master=root)  # Create an instance of Application
    app.mainloop()

if __name__ == "__main__":
    main()
