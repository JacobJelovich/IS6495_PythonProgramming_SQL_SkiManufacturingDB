#Program file that defines the Customer class that represents the Customer table. This file also contains the logic for
#the actions that a customer can make when logged into the system as well as CRUD operations relating to the Customer
#table.
from xml.etree.ElementTree import tostring

#Imports
import Order
import OrderLine
import Product
import datetime
import Return


#Class definition for a customer
class Customer:

    #Constructor to get the Database
    def __init__(self, db_obj):
        self.db = db_obj

    #Method for adding a customer to the skis database
    def add_cust(self, first, last, address):

        #Try-except block to catch exceptions when inserting customer
        try:
            #Calling the get cursor and execute functions from the DBbase class to run sql to insert the customer into
            #the DB and calling the get_connection and commit functions to commit the change
            self.db.get_cursor.execute("INSERT OR IGNORE into Customer (first, last, address) "
                                       "values(?, ?, ?);", (first, last, address))
            self.db.get_connection.commit()

            #Printing to let the user know the customer was added successfully
            print(f"Added customer: {first}, {last} successfully.")

        except Exception as ex:

            #Prints a message to let the user know where an error occurred
            print("An error occurred in the Customer class when adding customer.", ex)

    #Fetch method to retrieve a customer from the DB
    def fetch_cust(self, cust_id=None, first=None, last=None):

        #Try-except block to catch exceptions when fetching the customer from the DB
        try:

            #Checks if a customer ID was provided and if it was, that is how the customer is retrieved. If the first
            #and last name was provided, that is how the customer is retrieved. If neither were provided, the whole
            #Customer table is retrieved.
            if cust_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM Customer WHERE cust_id = ?", (cust_id,)).fetchone()
            elif first is not None and last is not None:
                return self.db.get_cursor.execute("SELECT * FROM Customer WHERE first = ? and last = ?",
                                                    (first, last)).fetchone()
            else:
                return self.db.get_cursor.execute("SELECT * FROM Customer").fetchall()

        #Prints a message to let the user know what error occurred when retrieving the customer.
        except Exception as e:
            print("An error occurred in the Customer class when fetching customer.", e)

    #Delete method for removing a customer from the DB
    def delete_cust(self, cust_id):

        #Try-except block to catch exceptions when deleting a customer from the DB
        try:
            #Executes and commits the deletion of the customer using the customer id and SQL. It then commits it.
            self.db.get_cursor.execute("DELETE FROM Customer where cust_id = ?;", (cust_id,))
            self.db.get_connection.commit()

            #Prints a message that the customer has been deleted
            print(f"Deleted customer {cust_id} successfully")
            return True

        #Prints a message to let the user know what error occurred when deleting the customer.
        except Exception as e:
            print("An error has occurred when deleting the customer.", e)
            return False

    #Method for updating a customer entry in the DB
    def update_cust(self, cust_id, first = None, last = None, address = None):

        #Try-except block to catch exceptions when updating customer
        try:
            #If-elif-else chain that checks what information was provided to update the customer and executes SQL to
            #make that update
            if first is not None and last is not None and address is not None:
                self.db.get_cursor.execute("UPDATE Customer set first = ?, last = ?, address = ? WHERE cust_id = ?;",
                                           (first, last, address, cust_id))

                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the first, last, and address were updated successfully.
                print(f"Updated Customer to {first, last, address} successfully.")
            elif first is not None and last is not None and address is None:
                self.db.get_cursor.execute("UPDATE Customer set first = ?, last = ? WHERE cust_id = ?;", (first, last,
                                                                                                         cust_id))

                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the first and last were updated successfully.
                print(f"Updated Customer to {first, last} successfully.")
            elif first is None and last is None and address is not None:
                self.db.get_cursor.execute("UPDATE Customer set address = ? WHERE cust_id = ?;", (address, cust_id))

                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the address was updated successfully.
                print(f"Updated Customer to {address} successfully.")

            #Else statement if the proper fields weren't provided
            else:
                print("You must provide either the first and last name or address to update customer.")

        #Prints a message to let the user know what error occurred when updating the customer.
        except Exception as e:
            print("An error has occurred when updating the customer.", e)

    #Method that runs when an Employee or Admin chose to access the Customer Table
    def run_cust_options(self):

        #Establish the CRUD options for Customer
        cust_options = {"get_cust": "Get all Customers",
                       "getby_cust": "Get Customer by ID",
                       "update_cust": "Update Customer",
                       "add_cust": "Add Customer",
                       "del_cust": "Delete Customer",
                       "back": "Go back a page"}

        #Prompt the user to make a selection about what action they want to do to the Customer table
        print("\nPlease choose an action you'd like to take: ")

        #Create a string to store the user's action selection
        action_selection = ""

        #While loop that keeps prompting the user for
        while action_selection != "back":

            #Print the list of category options by looping through the dictionary items
            print("*** Customer Action List ***")
            for action in cust_options.items():
                print(action)

            #Store the users selection in a variable to be checked
            action_selection = input("Select an action: ")

            #If-elif-else block that checks which action was selected and runs the appropriate method and logic for it
            if action_selection == "get_cust":

                #Calls the fetch_cust method to get a list of customers and stores it in a variable
                results = self.fetch_cust()

                #Print line for formatting
                print("")

                #Loops through each customer in the list and prints
                for item in results:
                    print(item)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "getby_cust":

                #Prompts the employee to enter the ID of the customer to fetch and stores
                cust_id = input("Enter Customer ID: ")

                #Calls fetch method with ID and stores
                results = self.fetch_cust(cust_id)

                #Prints customer that was fetched
                print(results)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "update_cust":

                #Prompt the employee to enter the ID of the customer they want to update
                cust_id = input("Enter Customer ID: ")

                #Prompt the employee for first name to be changed to. They enter n/a if they want to update address
                cust_first = input("Enter updated first name or \"n/a\" if you want to update address: ")

                #Check if the employee entered a first name, if they did, prompt the employee for an updated last name.
                #If they didn't, prompt the employee for an address. Call the update customer method afterward.
                if cust_first != "n/a":
                    cust_last = input("Enter updated last name: ")
                    self.update_cust(cust_id, first=cust_first, last=cust_last)
                    print(self.fetch_cust(cust_id))

                    #Allow the employee to continue and format output
                    input("Press return to continue")
                    print("")
                else:
                    cust_address = input("Enter updated address: ")
                    self.update_cust(cust_id, address=cust_address)
                    print(self.fetch_cust(cust_id))

                    #Allow the employee to continue and format output
                    input("Press return to continue")
                    print("")

            elif action_selection == "add_cust":

                #Prompt the user for the info of the customer to add
                cust_first = input("Enter the first name of the Customer to add: ")
                cust_last = input("Enter the last name of the Customer to add: ")
                cust_address = input("Enter the address of the Customer to add: ")

                #Now call the method to add the customer
                self.add_cust(cust_first, cust_last, cust_address)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "del_cust":

                #Prompt the employee for the customer ID of the customer to delete
                cust_id = input("Please enter the ID of the customer to delete: ")

                #Call the method to delete the customer
                self.delete_cust(cust_id)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            else:

                #If the employee didn't select "back" let them know that they made an invalid selection
                if action_selection != "back":
                    print("Invalid selection, please try again\n")

        #Line to format output when going back
        print("")

    #Method that runs when a customer signs into the system and allows them to access the system
    def run_cust(self, cust_id):

        #Establish the category options for customers
        category_options = {"ord_hist": "View Order History",
                            "get_ord": "View Order",
                            "make_ord": "Make an Order",
                            "up_ord": "Update Payment on Order",
                            "del_ord": "Delete an Order",
                            "ret": "Make a Return",
                            "exit": "Exit Program"}
        
        #Create an instance of Order that the user can interact with
        order = Order.Order(self.db)

        #Prompt the customer to make a selection about what action they'd like to take
        print("Please choose a category you would like to access: ")

        #Create a string to store the customer's action selection
        action_selection = ""
        
        #While loop that keeps prompting the customer for a selection unless they choose "exit"
        while action_selection != "exit":

            #Print the list of category options by looping through the dictionary items
            print("*** Action List ***")
            for category in category_options.items():
                print(category)

            #Store the users selection in a variable to be checked
            action_selection = input("Select an action: ")

            #If-elif-else block that checks which action was selected and runs the appropriate method for it
            if action_selection == "ord_hist":

                #Calls the fetch method to get a list of the customers orders then store them in a list
                results = order.fetch_order(ord_id=None, cust_id=cust_id)

                #Print line for formatting
                print("")

                #Loops through each order in the list and prints
                for item in results:
                    print(item)

                #Allow the customer to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "get_ord":

                #Prompts the customer to enter the ID of the order to fetch and stores
                ord_id = input("Enter Order ID: ")

                #Calls fetch method with ID and stores
                results = order.fetch_order(ord_id)

                #Prints order that was fetched
                print(results)

                #Allow the customer to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "make_ord":

                #Initialize an empty list that will hold the products in the customers cart
                cart = []

                #Initialize the total_price to zero
                total_order_price = 0

                #Create an instance of Product that the customer can use
                product = Product.Product(self.db)

                #Create an instance of Orderline so that we can add the order to it
                orderline = OrderLine.OrderLine(self.db)

                #While loop that keeps prompting the user to enter products they would like until they type "done"
                while True:

                    #Prompt the user to enter the ID of a product they want
                    prod_id = input("Enter the Product ID of a product you would like to add (or \"done\" "
                                    "to be done): ")

                    #Check if the user wanted to be done
                    if prod_id.lower() == "done":
                        break

                    #Store index of price in Product in a variable so we dont use "magic numbers"
                    prod_price_index = 3

                    #Fetch the product price from the Product table
                    prod_price = product.fetch_prod(prod_id=prod_id, prod_name=None)[prod_price_index]

                    #Add that price to the total price
                    total_order_price = total_order_price + float(prod_price)

                    #Add the product ID to the cart
                    cart.append({"prod_id": prod_id, "price": prod_price})

                #Prompt the user for their payment ID
                pmt_id = input("Please enter your payment ID: ")

                #Get current date as string
                date = datetime.date.strftime(datetime.date.today(), "%m/%d/%Y")

                #Call add_order method from the Order class to make an order and store it's ID
                ord_id = order.add_order(emp_id=None, cust_id=cust_id, date=date,
                                         total_price=total_order_price, pmt_id=pmt_id)

                #Iterate through the cart and add each to the orderline
                for prod in cart:
                    orderline.add_line_item(ord_id, prod_id=prod["prod_id"], qty=1, price=prod["price"])

            elif action_selection == "up_ord":

                #Prompt the customer to enter the ID of the order they want to update.
                ord_id = input("Enter Order ID of order you'd like to update: ")

                #Now prompt the user to enter the updated payment ID
                pmt_id = input("Please enter the updated Payment ID you want on this account: ")

                #Update the order
                order.update_order(ord_id=ord_id, emp_id=None, cust_id=None, date=None, total_price=None, pmt_id=pmt_id)

                #Allow the customer to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "del_ord":

                #Prompt the customer to enter the ID of the order they want to delete.
                ord_id = input("Enter Order ID of order you want to delete: ")

                #Call Order method to delte the order
                order.delete_order(ord_id)

                #Allow the customer to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "ret":

                #Create instance of Return to interact with
                ret = Return.Return(self.db)

                #Prompt the customer for the ID of the order they want to make a return for
                ord_id = input("Enter the Order ID of the order you want to return: ")

                #Get current date as string
                date = datetime.date.strftime(datetime.date.today(), "%m/%d/%Y")

                #Call Return method to add return
                ret.add_return(date, ord_id, qty = 1)

                #Allow the customer to continue and format output
                input("Press return to continue")
                print("")

            #This runs if the customer entered something that wasn't an option to print a message to let them know
            else:
                if action_selection != "exit":
                    print("Invalid selection, please try again\n")