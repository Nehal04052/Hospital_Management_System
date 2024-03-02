# gui.py
from datetime import datetime

import random
from tkinter import *
from tkinter import ttk
import secrets
import string
from tkinter import messagebox
from .database import Database
from .button_functions import ButtonFunctions  # Importing the ButtonFunctions class
import sys
import mysql.connector
from fpdf import FPDF
from tkinter import filedialog

N = 12

class Pharmacist_Gui:
    def __init__(self, root, username):
        self.root = root
        self.root.state('zoomed')
        self.database = Database()
        # Add your GUI code here
        self.root.title("PHARMACIST")
        self.root.geometry("1920x1080+0+0")
        self.root.wm_iconbitmap(r'D:\College\SEM-5\Software Engneering\Project\Hospital_Management_System\hospital.ico')
        self.button_functions = ButtonFunctions(self,self.database,self.root) 

        #=====Variable to store data======

        self.NameofTablet=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablet=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffects=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.BloodPressure=StringVar()
        self.HowTOUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
       

        # Creating and placing the title label
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HMS PHARMACY", fg="red", bg="white",
                         font=("Comic Sans MS", 48, 'bold'),width=27)
        lbltitle.grid(row=0, column=3, columnspan=2)

        # Creating and placing the profile label with the username parameter
        lblprofile_text = f"User Name :- {username}"
        lblprofile = Label(self.root, bd=20, relief=RIDGE, text=lblprofile_text, fg="black", bg="white",font=("Comic Sans MS", 20, 'bold'),height=2,width=23)
        lblprofile.grid(row=0, column=0, columnspan=2)

    #==================FIRST DATAFRAME=====================
       
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)


        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("Comic Sans MS", 12, 'bold'),text="Patient Information")
        DataframeLeft.place(x=0,y=10,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("Comic Sans MS", 12, 'bold'),text="Patient Information")
        DataframeRight.place(x=990,y=10,width=495,height=350)

        #==============Buttons Frame=============

        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=86)
        
        #==============Details Frame=============

        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=618,width=1530,height=180)
        
        #=========Dataframe Left==================

        lblNameTablet=Label(DataframeLeft,text="Name Of Medicine",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblNameTablet.grid(row=0,column=0)
        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.NameofTablet,font=("Comic Sans MS", 11, 'bold'),width=33)
         # ComboBox variable
        
        self.comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.NameofTablet,font=("Comic Sans MS", 11, 'bold'), width=33)
        self.comNametablet.grid(row=0, column=1) 
        self.fetch_medicine_data()


        lblref=Label(DataframeLeft,text="Referece No:",font=("Comic Sans MS", 11, 'bold'),padx=2)
        lblref.grid(row=1,column=0)
        txtref=ttk.Entry(DataframeLeft,textvariable=self.ref,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtref.insert(0,''.join(secrets.choice(string.ascii_uppercase + string.digits)for i in range(N)))
        txtref.grid(row=1,column=1)


        lblDose=Label(DataframeLeft,text="Dose:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblDose.grid(row=2,column=0)
        txtDose=ttk.Entry(DataframeLeft,textvariable=self.Dose,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,text="Number of Tablets:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblNoOftablets.grid(row=3,column=0)
        txtNoOftablets=ttk.Entry(DataframeLeft,textvariable=self.NumberofTablet,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,text="Lot:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblLot.grid(row=4,column=0)
        txtLot=ttk.Entry(DataframeLeft,textvariable=self.Lot,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,text="Issue Date:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblissueDate.grid(row=5,column=0)
        txtissueDate=ttk.Entry(DataframeLeft,textvariable=self.Issuedate,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,text="Expire Date:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblExpDate.grid(row=6,column=0)
        txtExpDate=ttk.Entry(DataframeLeft,textvariable=self.Expdate,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,text="Daily Dose:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblDailyDose.grid(row=7,column=0)
        txtDailyDose=ttk.Entry(DataframeLeft,textvariable=self.DailyDose,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,text="Side Effect:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=5)
        lblSideEffect.grid(row=8,column=0)
        txtSideEffect=ttk.Entry(DataframeLeft,textvariable=self.sideEffects,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,text="Further Information:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=3)
        lblFurtherinfo.grid(row=0,column=2)
        txtFurtherinfo=ttk.Entry(DataframeLeft,textvariable=self.FurtherInformation,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtFurtherinfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,text="BloodPressure:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=3)
        lblBloodPressure.grid(row=1,column=2)
        txtBloodPressure=ttk.Entry(DataframeLeft,textvariable=self.BloodPressure,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtBloodPressure.grid(row=1,column=3)

        lblStorageAdvice=Label(DataframeLeft,text="StorageAdvice:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=2)
        lblStorageAdvice.grid(row=2,column=2)
        txtStorageAdvice=ttk.Entry(DataframeLeft,textvariable=self.StorageAdvice,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtStorageAdvice.grid(row=2,column=3)

        lblMedication=Label(DataframeLeft,text="Medication:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=2)
        lblMedication.grid(row=3,column=2)
        txtMedication=ttk.Entry(DataframeLeft,textvariable=self.HowTOUseMedication,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtMedication.grid(row=3,column=3) 

        lblPatientId=Label(DataframeLeft,text="Patient Id:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=2)
        lblPatientId.grid(row=4,column=2)
        txtPatientId=ttk.Entry(DataframeLeft,textvariable=self.PatientId,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtPatientId.insert(0,"#")
        txtPatientId.insert(1,random.randint(0,sys.maxsize))
        txtPatientId.grid(row=4,column=3)       

        lblNHSNo=Label(DataframeLeft,text="NHS Number:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=2)
        lblNHSNo.grid(row=5,column=2)
        txtNHSNo=ttk.Entry(DataframeLeft,textvariable=self.nhsNumber,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtNHSNo.grid(row=5,column=3) 

        lblPatientName=Label(DataframeLeft,text="Patient Name:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=2)
        lblPatientName.grid(row=6,column=2)
        txtPatientName=ttk.Entry(DataframeLeft,textvariable=self.PatientName,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtPatientName.grid(row=6,column=3) 

        lblDOB=Label(DataframeLeft,text="Date Of Birth:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=2)
        lblDOB.grid(row=7,column=2)
        txtDOB=ttk.Entry(DataframeLeft,textvariable=self.DateOfBirth,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtDOB.grid(row=7,column=3)

        lblPatientAdd=Label(DataframeLeft,text="Patient Address:",font=("Comic Sans MS", 11, 'bold'),padx=2,pady=2)
        lblPatientAdd.grid(row=8,column=2)
        txtPatientAdd=ttk.Entry(DataframeLeft,textvariable=self.PatientAddress,font=("Comic Sans MS", 11, 'bold'),width=33)
        txtPatientAdd.grid(row=8,column=3)


        #===============DataframeRIght==========
        self.txtPrecription=Text(DataframeRight,font=("Comic Sans MS", 11, 'bold'),width=49,height=13,padx=1,pady=3)
        self.txtPrecription.grid(row=0,column=0)

        # Add a print button to DataframeRight
        self.print_button = Button(DataframeRight, text="PDF", command=self.print_data,borderwidth=1,background='red',relief='ridge', activebackground='white', font=("Comic Sans MS", 11, 'bold'),fg='white',width=49)
        self.print_button.grid(row=1, column=0)
        #=======Butttons=====================

        btnPrecription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("Comic Sans MS", 12, 'bold'),width=23,height=1,padx=20,pady=6,command=self.button_functions.Prescription)
        btnPrecription.grid(row=0,column=0)

        btnPrecriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("Comic Sans MS", 12, 'bold'),width=23,height=1,padx=2,pady=6,command=self.button_functions.PrescriptionData)
        btnPrecriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("Comic Sans MS", 12, 'bold'),width=23,height=1,padx=2,pady=6,command=self.button_functions.update_data)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("Comic Sans MS", 12, 'bold'),width=23,height=1,padx=2,pady=6,command=self.button_functions.delete)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("Comic Sans MS", 12, 'bold'),width=23,height=1,padx=2,pady=6,command=self.button_functions.clear)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("Comic Sans MS", 12, 'bold'),width=23,height=1,padx=2,pady=6,command=self.button_functions.Exit)
        btnExit.grid(row=0,column=5)

        #=======Table=============
        #===================Scrollbar===========
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablet","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command = self.hospital_table.xview)

        scroll_y = ttk.Scrollbar(command = self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftablet",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablet",text="No Of Tablet")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expire Date")
        self.hospital_table.heading("dailydose",text="DailyDose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        
        
        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=105)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablet",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.button_functions.get_cursor)
        self.button_functions.set_hospital_table(self.hospital_table)
        self.button_functions.fetch_data()
                # Bind the window close event to the function that destroys the window
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def on_close(self):
        # Implement any additional logic you need before closing the window
     if messagebox.askokcancel("Quit", "Do you want to quit?"):
      self.root.destroy()

    def fetch_medicine_data(self):
        try:
            # Connect to the MySQL database
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Nehal@5268", database="Hospital_Management_System_Database"
            )
            cursor = conn.cursor()

            # Execute the query to fetch data
            cursor.execute("SELECT name FROM medicineinfo")
            data = cursor.fetchall()
            print(data)
            # Extract the names of tablets from the fetched data
            tablet_names = [item[0] for item in data]
            print(tablet_names)
            # Update the values in the ComboBox
            self.update_combobox_values(tablet_names)

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

        finally:
            # Close the database connection
            cursor.close()
            conn.close()

    def update_combobox_values(self, tablet_names):
        # Update the values in the ComboBox
        self.comNametablet["values"] = tuple(tablet_names)
    
    def print_data(self):
    # Get the data from the txtPrescription Text widget
     data_to_print = self.txtPrecription.get("1.0", "end-1c")
             # Check if the text widget is empty
     if not data_to_print.strip():
       # If it's empty, show a message
      messagebox.showinfo("Information", "Please add data to the prescription.")
     else:
    # Create a PDF object
      pdf = FPDF()

    # Add a page
      pdf.add_page()
      pdf.ln(1 * 10)
    # Set the font
      pdf.set_font("Times", 'B', 24)

    # Add the name of the organization at the top
      pdf.cell(0, 10, 'H M S', 0, 1, 'C')

    # Add an icon
      pdf.image('D:\College\SEM-3\Internship\Project\Major\Hospital_Management_System\hospital.png', x = 10, y = 10, w = 30, h = 30)
      pdf.ln(2 * 10)
    # Add the date and time
      pdf.set_font("Times", size = 14)

      pdf.cell(0, 10, f'Date: {datetime.now().strftime("%d-%m-%Y")}', 0, 0, 'L')
      pdf.cell(0, 10, f'Time: {datetime.now().strftime("%I:%M:%S %p")}', 0, 1, 'R')

    # Draw a line across the page
      pdf.line(10, pdf.get_y(), pdf.w - 10, pdf.get_y())
     
      pdf.ln(1 * 10)
    # Add the data
      pdf.multi_cell(0, 10, data_to_print)

    # Show a save dialog and get the selected file name
      filename = filedialog.asksaveasfilename(defaultextension=".pdf")

    # Save the PDF
      if filename:
        pdf.output(filename)

