#Program file that defines the Admin class that represents the Admin table. This file also contains the logic for
#the actions that an admin can make when logged into the system as well as CRUD operations relating to the Employee
#table.

#imports
import Employee
import Customer
import Product
import RawMaterial
import Return
import Order
import pandas as pd
import matplotlib.pyplot as plt

#Class definition for an admin
class Admin(Employee.Employee):

    #Constructor to get the Database
    def __init__(self, db_obj):
        super().__init__(db_obj)

    #Method that runs when an employee signs in as an admin to allow them access to the system
    def run_admin(self):

        #Create an instance of the Employee class
        employee = Employee.Employee(self.db)

        #Establish the category and action options for admins
        cat_act_options = {"emp": "Employee Access",
                            "cust": "Customer Access",
                            "prod": "Product Access",
                            "rm": "Raw Material Access",
                            "ret": "Return Access",
                            "ord": "Order Access",
                            "gen_sales": "Generate Sales Over Time",
                            "gen_prods": "Generate Most/Least Popular Products",
                            "exit": "Exit Program"}

        #Prompt the admin to make a selection about what category they want to access
        print("Please choose a category or action you would like to access: ")

        #Create a string to store the admin's category or action selection
        cat_act_selection = ""

        #While loop that keeps prompting the admin for a selection unless they choose "exit"
        while cat_act_selection != "exit":

            #Print the list of category options by looping through the dictionary items
            print("*** Category/Action List ***")
            for category in cat_act_options.items():
                print(category)

            #Store the users selection in a variable to be checked
            cat_act_selection = input("Select a category/action: ")

            #If-elif-else block that checks which category or action was selected and runs the appropriate method for it
            if cat_act_selection == "emp":
                employee.run_emp_options()

            elif cat_act_selection == "cust":
                customer = Customer.Customer(self.db)
                customer.run_cust_options()

            elif cat_act_selection == "prod":
                product = Product.Product(self.db)
                product.run_prod_options()

            elif cat_act_selection == "rm":
                rm = RawMaterial.RawMaterial(self.db)
                rm.run_rm_options()

            elif cat_act_selection == "ret":
                ret = Return.Return(self.db)
                ret.run_ret_options()

            elif cat_act_selection == "ord":
                order = Order.Order(self.db)
                order.run_ord_options()

            elif cat_act_selection == "gen_sales":
                self.gen_sales_over_time()

            elif cat_act_selection == "gen_prods":
                self.gen_prod_pop_report()

            #This runs if the admin entered something that wasn't an option to print a message to let them know
            else:
                if cat_act_selection != "exit":
                    print("Invalid selection, please try again\n")

    def gen_sales_over_time(self):

        #Extracting dates and prices from orders
        sql = 'SELECT date, total_price FROM "Order"'

        #Load the data into a data frame
        df = pd.read_sql_query(sql, self.db.get_connection)

        #Convert the date data into datetime objects
        df['date'] = pd.to_datetime(df['date'])

        #Set the date as the index
        df = df.set_index('date')

        #Grouping by month and summing the total_price
        monthly_sales = df.resample('ME').sum(numeric_only=True)

        #Plot
        if not monthly_sales.empty:
            monthly_sales['total_price'].plot(kind='line', marker='o')
            plt.title("Monthly Sales Report")
            plt.xlabel("Month")
            plt.ylabel("Total Revenue")
            plt.show()
        else:
            print("No sales data found for the report.")

    #Method for generating the product popularity report.
    def gen_prod_pop_report(self):

        #Try-except block for catching exceptions when producing the report
        try:
            #sql to join Orderline (sales) with Product (names) and Employee (who sold it)
            sql = """
            SELECT p.prod_name, ol.quantity, e.first || ' ' || e.last AS emp_name
            FROM Product p
            LEFT JOIN Orderline ol ON p.prod_id = ol.prod_id
            LEFT JOIN "Order" o ON ol.order_id = o.order_id
            LEFT JOIN Employee e ON o.emp_id = e.emp_id
            """

            df = pd.read_sql_query(sql, self.db.get_connection)

            # If a product hasn't sold, quantity will be NaN. Fill with 0.
            df['quantity'] = df['quantity'].fillna(0)

            # Group by product name to get total units sold
            popularity = df.groupby('prod_name')['quantity'].sum().sort_values(ascending=False)

            # Create a figure with two subplots (1 row, 2 columns)
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

            # Plot 1: Most Popular (Top 5)
            popularity.head(5).plot(kind='bar', ax=ax1, color='skyblue')
            ax1.set_title("Top 5 Most Popular Products")
            ax1.set_ylabel("Units Sold")

            # Plot 2: Least Popular (Bottom 5)
            popularity.tail(5).plot(kind='bar', ax=ax2, color='salmon')
            ax2.set_title("5 Least Popular Products")
            ax2.set_ylabel("Units Sold")

            plt.tight_layout()
            plt.show()

            # Print a quick leaderboard for the Admin in the console
            print("\n--- Sales Leaderboard (Units Sold by Employee) ---")
            emp_leaderboard = df.groupby('emp_name')['quantity'].sum().sort_values(ascending=False)
            print(emp_leaderboard)

        except Exception as e:
            print("An error occurred generating product reports:", e)