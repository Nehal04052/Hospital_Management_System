# database.py
import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(host="localhost", username="root", password="Nehal@5268", database="Hospital_Management_System_Database")
        self.cursor = self.connection.cursor()

    def insert_data(self, data):
        query = "INSERT INTO hospitaldata VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, data)
        self.connection.commit()

    def update_data(self, data):
        query = "UPDATE hospitaldata SET NameofTablets = %s, Dose = %s, NoOfTablets = %s, Lot = %s, IssueDate = %s, ExpDate = %s, DailyDate = %s, Storage = %s, NHSNumber = %s, PatientName = %s, DOB = %s, Address = %s WHERE ReferenceNo = %s"
        self.cursor.execute(query, data)
        self.connection.commit()

    def fetch_data(self):
        query = "SELECT * FROM hospitaldata"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_data(self, reference_no):
        query = "DELETE FROM hospitaldata WHERE ReferenceNo=%s"
        self.cursor.execute(query, (reference_no,))
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()