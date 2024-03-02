import tkinter as tk
from tkinter import messagebox
from .button_function import ButtonFunction
from .medicine_info import MedicineInfo

class AdminGui:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Admin")
        
        self.root.geometry('400x110')  # Set the window size
        self.root.resizable(0, 0)  # Disable maximize button

        # Center the window
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth()/2 - window_width/2 - 30)
        position_down = int(self.root.winfo_screenheight()/2 - window_height/2 - 110)
        self.root.geometry("+{}+{}".format(position_right, position_down))
        self.root.wm_iconbitmap(r'D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\hospital.ico')

        # Create a frame
        frame = tk.Frame(self.root, bg='light blue')
        frame.pack(fill='both', expand=True)

        self.button_function = ButtonFunction()

        # Add padding between the widgets
        tk.Button(frame, text="Add Medicine", command=self.add_medicine, bg='lawngreen',relief='ridge',borderwidth=0, font=("Comic Sans MS",14,'bold'),fg='black').grid(row=1, column=0, sticky="w", pady=(10, 0),padx=2)
        tk.Label(frame, text=f"UserName: {username}", bg='light blue',font=("Comic Sans MS", 15,'bold')).grid(row=0, column=1, pady=(10, 0))
        tk.Label(frame, text="UserType: admin", bg='light blue',font=("Comic Sans MS", 15,'bold')).grid(row=1, column=1, pady=(10, 0))
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def on_close(self):
        # Implement any additional logic you need before closing the window
     if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.root.destroy()

    def add_medicine(self):
        # Open the medicine information form
     self.medicine_info_root = tk.Toplevel(self.root)
     app = MedicineInfo(self.medicine_info_root, self.button_function,self.root)
     self.medicine_info_root.mainloop()
        
