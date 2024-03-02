import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MedicineInfo:
    def __init__(self, root, button_function,parent):
        self.root = root
        self.root.title("Medicine Info")
        # Set the window size
        self.parent=parent
        self.root.geometry('1207x612')  # Set the window size
        self.root.resizable(0, 0)  # Disable maximize button

        # Center the window
        # Move the window towards the left by subtracting 50 pixels
        shift_left = 460
        shift_up = 250
        self.root.update_idletasks()  # Make sure the window size is updated
        position_right = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) // 2 - shift_left
        position_down = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) // 2 - shift_up
        self.root.geometry(f"+{position_right}+{position_down}")
        self.root.wm_iconbitmap(r'D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\hospital.ico')

        # Create a frame
        frame = tk.Frame(self.root, bg='light blue')
        frame.pack(fill='both', expand=True)

        self.button_function = button_function

        # Define labels and entry fields
        self.name = ttk.Entry(frame,font=("Comic Sans MS",12,'bold'))
        self.name.grid(row=0, column=1, pady=(10, 0))
        tk.Label(frame,font=("Comic Sans MS",14,'bold'), text="Name", bg='light blue').grid(row=0, column=0, pady=(10, 0))

        self.selling_price = ttk.Entry(frame,font=("Comic Sans MS",12,'bold'))
        self.selling_price.grid(row=1, column=1, pady=(10, 0))
        tk.Label(frame,font=("Comic Sans MS",14,'bold'), text="Selling Price", bg='light blue').grid(row=1, column=0, pady=(10, 0))

        self.buying_price = ttk.Entry(frame,font=("Comic Sans MS",12,'bold'))
        self.buying_price.grid(row=2, column=1, pady=(10, 0))
        tk.Label(frame,font=("Comic Sans MS",14,'bold'), text="Buying Price", bg='light blue').grid(row=2, column=0, pady=(10, 0))

        self.quantity = ttk.Entry(frame,font=("Comic Sans MS",12,'bold'))
        self.quantity.grid(row=3, column=1, pady=(10, 0))
        tk.Label(frame,font=("Comic Sans MS",14,'bold'), text="Quantity", bg='light blue').grid(row=3, column=0, pady=(10, 0))

        self.description = ttk.Entry(frame,font=("Comic Sans MS",12,'bold'))
        self.description.grid(row=4, column=1, pady=(10, 0))
        tk.Label(frame,font=("Comic Sans MS",14,'bold'), text="Description", bg='light blue').grid(row=4, column=0, pady=(10, 0))

        # Define buttons
        tk.Button(frame, text="Add", command=self.add_medicine_info,bg='limegreen',relief='ridge',borderwidth=0,font=("Comic Sans MS",15,'bold'),fg='white',width=10).grid(row=5, column=0, pady=(8, 0))

        tk.Button(frame, text="Update", command=self.update_medicine_info,bg='royalblue1',relief='ridge',borderwidth=0, font=("Comic Sans MS", 15,'bold'),fg='white',width=10).grid(row=5, column=1, pady=(8, 0))
        tk.Button(frame, text="Delete", command=self.delete_medicine_info,bg='red1',relief='ridge',borderwidth=0, font=("Comic Sans MS",15,'bold'),fg='white',width=10).grid(row=6, column=1, pady=(8, 0))

         # Define table

        self.table = ttk.Treeview(frame, columns=("ID","Name", "Selling Price", "Buying Price", "Quantity", "Description"), show='headings')
        self.table.grid(row=7, column=0, columnspan=2, pady=(10, 0),padx=3)
        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Selling Price", text="Selling Price")
        self.table.heading("Buying Price", text="Buying Price")
        self.table.heading("Quantity", text="Quantity")
        self.table.heading("Description", text="Description")
        self.table.bind('<ButtonRelease-1>', self.select_item)

        # Load data into table
        self.load_data()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def on_close(self):
        # Implement any additional logic you need before closing the window
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            self.parent.lift()

    def load_data(self):

        # Clear the table

        for i in self.table.get_children():
            self.table.delete(i)

        # Fetch data from database

        data = self.button_function.fetch_medicine_info()
        print(data)

        # Insert data into table

        for item in data:
            self.table.insert('', 'end', values=(item[0],item[1], item[2], item[3], item[4], item[5]))
        
        # Create a style

        style = ttk.Style(self.root)
        style.configure("Treeview", font=('Helvetica', 10), rowheight=25)
        style.configure("Treeview.Heading", font=('Helvetica', 10,'bold'))

        # Center the text in all columns

        columns = ("ID","Name", "Selling Price", "Buying Price", "Quantity", "Description")
        for col in columns:
            self.table.column(col, anchor="center")
            self.table.heading(col, text=col, anchor='center')

        # Update the table

        self.table.update()

    def select_item(self, event):
        
        # Get selected item

        selected_item = self.table.item(self.table.focus())

        # Update form fields
        
        self.name.delete(0, tk.END)
        self.name.insert(tk.END, selected_item['values'][1])

        self.selling_price.delete(0, tk.END)
        self.selling_price.insert(tk.END, selected_item['values'][2])

        self.buying_price.delete(0, tk.END)
        self.buying_price.insert(tk.END, selected_item['values'][3])

        self.quantity.delete(0, tk.END)
        self.quantity.insert(tk.END, selected_item['values'][4])

        self.description.delete(0, tk.END)
        self.description.insert(tk.END, selected_item['values'][5])

    def clear_fields(self):
        # Clear all fields
        self.name.delete(0, tk.END)
        self.selling_price.delete(0, tk.END)
        self.buying_price.delete(0, tk.END)
        self.quantity.delete(0, tk.END)
        self.description.delete(0, tk.END)

    def add_medicine_info(self):
        self.button_function.add_medicine_info(self.name.get(), self.selling_price.get(), self.buying_price.get(), self.quantity.get(), self.description.get())
        self.load_data()
        self.clear_fields()
        self.root.lift()


    def update_medicine_info(self):
        selected_item = self.table.item(self.table.focus())
        id = selected_item['values'][0]  # Assuming that the ID is the first value
        self.button_function.update_medicine_info(id,self.name.get(), self.selling_price.get(), self.buying_price.get(), self.quantity.get(), self.description.get())
        self.load_data()
        self.clear_fields()
        self.root.lift()

    def delete_medicine_info(self):
        selected_item = self.table.item(self.table.focus())
        id = selected_item['values'][0]  # Assuming that the ID is the first value
        self.button_function.delete_medicine_info(id)
        self.load_data()
        self.clear_fields()
        self.root.lift()


