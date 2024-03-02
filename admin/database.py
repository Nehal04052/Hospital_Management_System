import mysql.connector

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="localhost", username="root", password="Nehal@5268", database="Hospital_Management_System_Database"
        )
        self.cursor = self.mydb.cursor()

        # Create table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicineinfo (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                selling_price DECIMAL(10, 2),
                buying_price DECIMAL(10, 2),
                quantity INT,
                description TEXT
            )
        """)

    def fetch_medicine(self):
        self.cursor.execute("SELECT * FROM medicineinfo")
        return self.cursor.fetchall()

    def add_medicine(self, name, selling_price, buying_price, quantity, description):
        sql = "INSERT INTO medicineinfo (name, selling_price, buying_price, quantity, description) VALUES (%s, %s, %s, %s, %s)"
        val = (name, selling_price, buying_price, quantity, description)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def update_medicine(self, id, name, selling_price, buying_price, quantity, description):
        sql = "UPDATE medicineinfo SET name = %s, selling_price = %s, buying_price = %s, quantity = %s, description = %s WHERE id = %s"
        val = (name, selling_price, buying_price, quantity, description, id)
        self.cursor.execute(sql, val)
        self.mydb.commit()

    def delete_medicine(self, id):
        sql = "DELETE FROM medicineinfo WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.mydb.commit()
