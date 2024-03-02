# button_functions.py
import random
import secrets
import string
from tkinter import *
from tkinter import messagebox
import sys
N = 12

class ButtonFunctions:
    def __init__(self,gui_instance,database_instance,root):
        self.gui = gui_instance
        self.database = database_instance  # Initialize the database attribute
        self.root = root
 # Add other GUI-related functions here
    #==================Funtionality Declration==========
    def set_hospital_table(self, hospital_table):
        self.hospital_table = hospital_table

    def PrescriptionData(self):
        if self.gui.NameofTablet.get() == "" or self.gui.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            data = (
                self.gui.NameofTablet.get(), self.gui.ref.get(), self.gui.Dose.get(),
                self.gui.NumberofTablet.get(), self.gui.Lot.get(), self.gui.Issuedate.get(),
                self.gui.Expdate.get(), self.gui.DailyDose.get(), self.gui.StorageAdvice.get(),
                self.gui.nhsNumber.get(), self.gui.PatientName.get(), self.gui.DateOfBirth.get(),
                self.gui.PatientAddress.get()
            )
            self.database.insert_data(data)
            self.fetch_data()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        data = (
            self.gui.NameofTablet.get(), self.gui.Dose.get(), self.gui.NumberofTablet.get(),
            self.gui.Lot.get(), self.gui.Issuedate.get(), self.gui.Expdate.get(),
            self.gui.DailyDose.get(), self.gui.StorageAdvice.get(), self.gui.nhsNumber.get(),
            self.gui.PatientName.get(), self.gui.DateOfBirth.get(), self.gui.PatientAddress.get(),
            self.gui.ref.get(),
        )
        self.database.update_data(data)
        self.fetch_data()
        messagebox.showinfo("Success", "Record has been Updated")

    def fetch_data(self):
        rows = self.database.fetch_data()
        print(rows)
        if len(rows) != 0:
            self.gui.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.gui.hospital_table.insert("", END, values=i)

    def delete(self):
        if self.gui.ref.get():
            self.database.delete_data(self.gui.ref.get())
            self.fetch_data()
            messagebox.showinfo("Deleted", "Patient information deleted successfully")
        else:
            messagebox.showerror("Error", "Please select a record to delete")

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.gui.NameofTablet.set(row[0])
        self.gui.ref.set(row[1])
        self.gui.Dose.set(row[2])
        self.gui.NumberofTablet.set(row[3])
        self.gui.Lot.set(row[4])
        self.gui.Issuedate.set(row[5])
        self.gui.Expdate.set(row[6])
        self.gui.DailyDose.set(row[7])    
        self.gui.StorageAdvice.set(row[8])
        self.gui.nhsNumber.set(row[9])
        self.gui.PatientName.set(row[10])
        self.gui.DateOfBirth.set(row[11])
        self.gui.PatientAddress.set(row[12])
    
    def Prescription(self):
        print("Prescription button clicked")
        self.gui.txtPrecription.insert(END,"Name of Tablets:\t\t\t"+self.gui.NameofTablet.get()+"\n")
        self.gui.txtPrecription.insert(END,"Referce No:\t\t\t"+self.gui.ref.get()+"\n")
        self.gui.txtPrecription.insert(END,"Dose:\t\t\t"+self.gui.Dose.get()+"\n")
        self.gui.txtPrecription.insert(END,"Number of Tablet:\t\t\t"+self.gui.NumberofTablet.get()+"\n")
        self.gui.txtPrecription.insert(END,"Lot:\t\t\t"+self.gui.Lot.get()+"\n")
        self.gui.txtPrecription.insert(END,"Issue Date:\t\t\t"+self.gui.Issuedate.get()+"\n")
        self.gui.txtPrecription.insert(END,"Expire Date:\t\t\t"+self.gui.Expdate.get()+"\n")
        self.gui.txtPrecription.insert(END,"Daily Dose:\t\t\t"+self.gui.DailyDose.get()+"\n")
        self.gui.txtPrecription.insert(END,"Storage Adivce:\t\t\t"+self.gui.StorageAdvice.get()+"\n")
        self.gui.txtPrecription.insert(END,"NHS Number:\t\t\t"+self.gui.nhsNumber.get()+"\n")
        self.gui.txtPrecription.insert(END,"Patient Name:\t\t\t"+self.gui.PatientName.get()+"\n")
        self.gui.txtPrecription.insert(END,"Date of Birth:\t\t\t"+self.gui.DateOfBirth.get()+"\n")
        self.gui.txtPrecription.insert(END,"Patient Address:\t\t\t"+self.gui.PatientAddress.get()+"\n")
        self.gui.txtPrecription.insert(END,"Patient Name:\t\t\t"+self.gui.PatientName.get()+"\n")
        self.gui.txtPrecription.insert(END,"name of Tablets:\t\t\t"+self.gui.HowTOUseMedication.get()+"\n")
        self.gui.txtPrecription.insert(END,"Medication:\t\t\t"+self.gui.BloodPressure.get()+"\n")
        self.gui.txtPrecription.insert(END,"Further Information:\t\t\t"+self.gui.FurtherInformation.get()+"\n")
        self.gui.txtPrecription.insert(END,"Side effects:\t\t\t"+self.gui.sideEffects.get()+"\n")
 
    def clear(self):
        self.gui.NameofTablet.set("")
        self.gui.ref.set("")
        self.gui.Dose.set("")
        self.gui.NumberofTablet.set("")
        self.gui.Lot.set("")
        self.gui.Issuedate.set("")
        self.gui.Expdate.set("")
        self.gui.DailyDose.set("")
        self.gui.sideEffects.set("")
        self.gui.FurtherInformation.set("")
        self.gui.StorageAdvice.set("")
        self.gui.BloodPressure.set("")
        self.gui.HowTOUseMedication.set("")
        self.gui.PatientId.set("")
        self.gui.nhsNumber.set("")
        self.gui.PatientName.set("")
        self.gui.DateOfBirth.set("")
        self.gui.PatientAddress.set("")
        self.gui.txtPrecription.delete("1.0",END)
        self.update_entry()
        
        
    def Exit(self):
        Exit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if Exit>0:
            self.root.destroy()
            return
    
    def update_entry(self):
        self.gui.ref.set(str((''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N)))))
        self.gui.PatientId.set(str('#')+str(random.randint(0,sys.maxsize)))


    def exit_program(self):
        exit_confirmation = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")

        if exit_confirmation > 0:
            self.database.close_connection()
            self.root.destroy()
