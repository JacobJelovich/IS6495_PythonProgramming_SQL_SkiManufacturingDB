#File used to import everything in the DB using a csv parsing script

import csv
import SkiDB
import Employee
import Customer
import Order
import OrderLine
import Return
import RawMaterial
import Product

#Method that populates the db
def populate_everything():
    #Initialize the database connection
    db = SkiDB.Skis()

    #Initialize all classes with the db baton
    emp = Employee.Employee(db)
    cust = Customer.Customer(db)
    order_obj = Order.Order(db)
    ordline = OrderLine.OrderLine(db)
    ret = Return.Return(db)
    rm = RawMaterial.RawMaterial(db)
    prod = Product.Product(db)

    try:
        #Employees
        with open("employees.csv", mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                emp.add_emp(row["first"], row["last"], row["position"])

        #Customers
        with open("customers.csv", mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                cust.add_cust(row["first"], row["last"], row["address"])

        #Orders
        with open("orders.csv", mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                order_obj.add_order(row["emp_id"], row["cust_id"], row["date"], row["total_price"], row["pmt_id"])

        #Orderlines
        with open("orderline.csv", mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ordline.add_line_item(row["ord_id"], row["prod_id"], 1, row["price"])

        #Returns
        with open("returns.csv", mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ret.add_return(row["date"], row["ord_id"], 1)

        #Raw Materials
        with open("rawmaterials.csv", mode="r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rm.add_rm(row["cast"], row["date_purch"], row["qty"], row["mat_name"])

        #Products
        with open("products.csv", mode="r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        prod.add_prod(row["prod_name"], row["type"], row["price"], row["makeup"], row["man_cost"],
                                      row["ski_name"], row["dim"])

        print("Database populated successfully from CSV files!")

    except FileNotFoundError as e:
        print(f"Error: Could not find file {e.filename}. Check your file names!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


skis = SkiDB.Skis()
skis.reset_database()
populate_everything()