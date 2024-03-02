from .database import Database
from tkinter import messagebox

class ButtonFunction:
    def __init__(self):
        self.database = Database()
    
    def fetch_medicine_info(self):
        return self.database.fetch_medicine()

    def add_medicine_info(self, name, selling_price, buying_price, quantity, description):
        self.database.add_medicine(name, selling_price, buying_price, quantity, description)
        messagebox.showinfo("Success", "Medicine added successfully!")

    def update_medicine_info(self, id, name, selling_price, buying_price, quantity, description):
        self.database.update_medicine(id, name, selling_price, buying_price, quantity, description)
        messagebox.showinfo("Success", "Medicine updated successfully!")

    def delete_medicine_info(self, id):
        self.database.delete_medicine(id)
        messagebox.showinfo("Success", "Medicine deleted successfully!")


