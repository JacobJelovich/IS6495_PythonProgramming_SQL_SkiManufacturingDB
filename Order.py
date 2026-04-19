#Program file that defines the Order class that represents the Order table. This file also contains the CRUD
#operations relating to the Order table.


#Class definition for an Object
class Order:

    #Constructor to get the Database
    def __init__(self, db_obj):
        self.db = db_obj

    #Method for adding an Order to the skis database
    def add_order(self, emp_id, cust_id, date, total_price, pmt_id):

        #Try-except block to catch exceptions when inserting Order
        try:
            #Calling the get cursor and execute functions from the DBbase class to run sql to insert the Order into the
            #DB and calling the get_connection and commit functions to commit the change
            self.db.get_cursor.execute("INSERT OR IGNORE into \"Order\" (emp_id, cust_id, date, total_price, pmt_id) "
                                       "values(?, ?, ?, ?, ?);", (emp_id, cust_id, date, total_price, pmt_id))
            self.db.get_connection.commit()

            #Printing to let the user know the employee was added successfully
            print(f"Added Order for Customer: {cust_id} with Date: {date} and price: {total_price} successfully. \n")

            #Return the last ID
            return self.db.get_cursor.lastrowid

        except Exception as ex:

            #Prints a message to let the user know where an error occurred
            print("An error occurred in the Order class when adding Order. ", ex)

    #Fetch method to retrieve an order from the DB
    def fetch_order(self, ord_id = None, cust_id = None):

        #Try-except block to catch exceptions when fetching the order from the DB
        try:

            #Checks if an order ID was provided and if it was, that is how the order is retrieved. If the cust_id was
            #provided, that is how the order or orders are retrieved. If neither were provided, the whole
            #Order table is retrieved.
            if ord_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM \"Order\" WHERE order_id = ?", (ord_id,)).fetchone()
            elif cust_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM \"Order\" WHERE cust_id = ?", (cust_id,)).fetchall()
            else:
                return self.db.get_cursor.execute("SELECT * FROM \"Order\"").fetchall()

        #Prints a message to let the user know what error occurred when retrieving the order.
        except Exception as e:
            print("An error occurred in the Order class when fetching order.", e)

    #Delete method for removing an order from the DB
    def delete_order(self, ord_id):

        #Try-except block to catch exceptions when deleting an order from the DB
        try:
            #Executes and commits the deletion of the order using the order id and SQL. It then commits
            #it.
            self.db.get_cursor.execute("DELETE FROM \"Order\" where order_id = ?;", (ord_id,))
            self.db.get_connection.commit()

            #Prints a message that the order has been deleted
            print(f"Deleted order {ord_id} successfully")
            return True

        #Prints a message to let the user know what error occurred when deleting the order.
        except Exception as e:
            print("An error has occurred when deleting the order.", e)
            return False

    #Method for updating an order entry in the DB
    def update_order(self, ord_id, emp_id=None, cust_id=None, date=None, total_price=None, pmt_id=None):

        #Try-except block to catch exceptions when updating order
        try:
            #If chain that checks what information was provided to update the order and executes SQL to make
            #that update
            if emp_id is not None:
                self.db.get_cursor.execute("UPDATE \"Order\" set emp_id = ? WHERE order_id = ?;", (emp_id, ord_id))
                # Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the order employee ID was updated successfully.
                print(f"Updated Employee ID on order to {emp_id} successfully.")
            if cust_id is not None:
                self.db.get_cursor.execute("UPDATE \"Order\" set cust_id = ? WHERE order_id = ?;", (cust_id, ord_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the order customer ID was updated successfully.
                print(f"Updated Customer ID on order to {cust_id} successfully.")
            if date is not None:
                self.db.get_cursor.execute("UPDATE \"Order\" set date = ? WHERE order_id = ?;", (date, ord_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the order date was updated successfully.
                print(f"Updated Order Date to {date} successfully.")

            if total_price is not None:
                self.db.get_cursor.execute("UPDATE \"Order\" set total_price = ? WHERE order_id = ?;",
                                           (total_price, ord_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the order total price was updated successfully.
                print(f"Updated Order total price to {total_price} successfully.")

            if pmt_id is not None:
                self.db.get_cursor.execute("UPDATE \"Order\" set pmt_id = ? WHERE order_id = ?;", (pmt_id, ord_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the order payment ID was updated successfully.
                print(f"Updated Order payment ID to {pmt_id} successfully.")

            #If statement for if the proper fields weren't provided
            if emp_id is None and cust_id is None and date is None and total_price is None and pmt_id is None:
                print("You must provide an employee ID, customer ID, date, total price, or payment ID to update the "
                      "order.")

        #Prints a message to let the user know what error occurred when updating the order.
        except Exception as e:
            print("An error has occurred when updating the order.", e)

    #Method that runs when an Employee or Admin chooses to access the Order Table
    def run_ord_options(self):

        #Establish the CRUD options for orders
        ord_options = {"get_ord": "Get all Orders",
                       "getby_ord": "Get Order by ID",
                       "update_ord": "Update Order",
                       "add_ord": "Add Order",
                       "del_ord": "Delete Order",
                       "back": "Go back a page"}

        #Prompt the employee to make a selection about what action they want to do to the Order table
        print("\nPlease choose an action you'd like to take: ")

        #Create a string to store the employee's action selection
        action_selection = ""

        #While loop that keeps prompting the user for
        while action_selection != "back":

            #Print the list of category options by looping through the dictionary items
            print("*** Order Action List ***")
            for action in ord_options.items():
                print(action)

            #Store the employee's selection in a variable to be checked
            action_selection = input("Select an action: ")

            #If-elif-else block that checks which action was selected and runs the appropriate method and logic for it
            if action_selection == "get_ord":

                #Calls the fetch_order method to get a list of returns and stores it in a variable
                results = self.fetch_order()

                #Print line for formatting
                print("")

                #Loops through each order in the list and prints
                for item in results:
                    print(item)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "getby_ord":

                #Prompts the employee to enter the ID of the order to fetch and stores
                ord_id = input("Enter Order ID: ")

                #Calls fetch method with ID and stores
                results = self.fetch_order(ord_id)

                #Prints order that was fetched
                print(results)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "update_ord":

                #Prompt the employee to enter the ID of the order they want to update
                ord_id = input("Enter Order ID: ")

                #Establish the attr options for updating the order
                attr_options = {"emp_id": "Update Employee ID on Order",
                                "cust_id": "Update Customer ID on Order",
                                "date": "Update Date on Order",
                                "tot_price": "Update Order Total Price",
                                "pmt_id": "Update Order Payment ID"}

                #Prompt the employee to make a selection about what attribute they want to update
                print("\nPlease choose an attribute you'd like to update: ")

                #Boolean that is changed when a correct attribute has been chosen
                valid_attr = False

                #While loop that keeps prompting the user for an attribute selection
                while not valid_attr:

                    #Print the list of attribute options by looping through the dictionary items
                    print("*** Order Attribute List ***")
                    for attr in attr_options.items():
                        print(attr)

                    #Store the employee's selection in a variable to be checked
                    attr_selection = input("Select an attribute: ")

                    #If-elif-else block that checks which attribute was selected and runs the appropriate method and
                    #logic for it
                    if attr_selection == "emp_id":
                        emp_id = input("Enter updated employee ID: ")
                        self.update_order(ord_id, emp_id=emp_id, cust_id=None, date=None, total_price=None, pmt_id=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "cust_id":
                        cust_id = input("Enter updated customer ID: ")
                        self.update_order(ord_id, emp_id=None, cust_id=cust_id, date=None, total_price=None,
                                          pmt_id=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "date":
                        date = input("Enter updated order date: ")
                        self.update_order(ord_id, emp_id=None, cust_id=None, date=date, total_price=None, pmt_id=None)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "tot_price":
                        total_price = input("Enter updated order total price: ")
                        self.update_order(ord_id, emp_id=None, cust_id=None, date=None, total_price=total_price,
                                          pmt_id=None)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "pmt_id":
                        pmt_id = input("Enter updated order payment ID: ")
                        self.update_order(ord_id, emp_id=None, cust_id=None, date=None, total_price=None, pmt_id=pmt_id)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    else:

                        print("Invalid selection, please try again\n")

            elif action_selection == "add_ord":

                #Prompt the user for the info of the order to add
                ord_emp_id = input("Enter the employee ID on the order to add: ")
                ord_cust_id = input("Enter the customer ID on the order to add: ")
                ord_date = input("Enter the date on the order to add: ")
                ord_price = input("Enter the total price on the order to add: ")
                ord_pmt_id = input("Enter the payment ID on the order to add: ")

                #Now call the method to add the order
                self.add_order(ord_emp_id, ord_cust_id, ord_date, ord_price, ord_pmt_id)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "del_ord":

                #Prompt the employee for the order ID of the order to delete
                ord_id = input("Please enter the ID of the order to delete: ")

                #Call the method to delete the return
                self.delete_order(ord_id)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            else:

                #If the user didn't select "back" let them know that they made an invalid selection
                if action_selection != "back":
                    print("Invalid selection, please try again\n")

        #Line to format output when going back
        print("")