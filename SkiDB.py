#Program that uses DBbase to create and run the database program for Kitten Skis

#imports
import DBbase as db
import csv

#Class to control the Skis database
class Skis(db.DBbase):

    # Constructor that simply calls the parent DBbase classes constructor
    def __init__(self):
        super().__init__("skisDB.sqlite")

    # Implementing the reset_database method
    def reset_database(self):

        # Try catch block to catch if an error occurs when executing the sql below to drop the
        # table if it exits and create a new one.
        try:
            sql = """
                    DROP TABLE IF EXISTS Orderline;
                    DROP TABLE IF EXISTS "Return";
                    DROP TABLE IF EXISTS Payment;
                    DROP TABLE IF EXISTS "Order";
                    DROP TABLE IF EXISTS Product;
                    DROP TABLE IF EXISTS Raw_Material;
                    DROP TABLE IF EXISTS Shipping;
                    DROP TABLE IF EXISTS Customer;
                    DROP TABLE IF EXISTS Employee;

                    CREATE TABLE Employee(
                        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        last TEXT NOT NULL,
                        first TEXT NOT NULL,
                        position TEXT);
                    
                    CREATE TABLE Customer(
                        cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first TEXT NOT NULL,
                        last TEXT NOT NULL,
                        address TEXT);
                        
                    CREATE TABLE Shipping(
                        ship_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        order_id INTEGER,
                        ship_date TEXT,
                        delivery_date TEXT,
                        cost REAL,
                        FOREIGN KEY (order_id) REFERENCES "Order"(order_id));
                        
                    CREATE TABLE Raw_Material(
                        material_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cast TEXT, 
                        date_purchased TEXT,
                        quantity INTEGER,
                        material_name TEXT UNIQUE);
                        
                    CREATE TABLE Product(
                        prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        prod_name TEXT UNIQUE NOT NULL,
                        type TEXT,
                        pricing REAL,
                        makeup TEXT,
                        manufacturing_cost REAL,
                        ski_name TEXT,
                        dimensions TEXT);
                    
                    CREATE TABLE "Order"(
                        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        emp_id INTEGER,
                        cust_id INTEGER,
                        date TEXT,
                        total_price REAL,
                        pmt_id TEXT,
                        FOREIGN KEY (emp_id) REFERENCES "Employee"(emp_id),
                        FOREIGN KEY (cust_id) REFERENCES "Customer"(cust_id));
                    
                    CREATE TABLE Payment(
                        pmt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        order_id INTEGER,
                        cust_id INTEGER,
                        credit_card INTEGER,
                        FOREIGN KEY (order_id) REFERENCES "Order"(order_id),
                        FOREIGN KEY (cust_id) REFERENCES "Customer"(cust_id));
                    
                    CREATE TABLE "Return"(
                        return_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        date TEXT,
                        order_id INTEGER,
                        quantity INTEGER,
                        FOREIGN KEY (order_id) REFERENCES "Order"(order_id));
                    
                    CREATE TABLE Orderline(
                        line_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        order_id INTEGER, 
                        prod_id INTEGER,
                        quantity INTEGER,
                        price REAL,
                        FOREIGN KEY (order_id) REFERENCES "Order"(order_id),
                        FOREIGN KEY (prod_id) REFERENCES "Product"(prod_id));
                """
            super().execute_script(sql)
        except Exception as e:
            print("An error occurred.", e)

