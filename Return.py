#Program file that defines the Return class that represents the Return table. This file also contains the
#CRUD operations relating to the Return table.

#Imports

#Class definition for a Return
class Return:

    #Constructor to get the Database
    def __init__(self, db_obj):
        self.db = db_obj

    #Method for adding a Return to the skis database
    def add_return(self, date, order_id, qty):

        #Try-except block to catch exceptions when inserting Return
        try:
            #Calling the get cursor and execute functions from the DBbase class to run sql to insert the Return into the
            #DB and calling the get_connection and commit functions to commit the change
            self.db.get_cursor.execute("INSERT OR IGNORE into Return (date, order_id, quantity) values(?, ?, ?);",
                                       (date, order_id, qty))
            self.db.get_connection.commit()

            #Printing to let the employee know the return was added successfully
            print(f"Added Return for order: {order_id} successfully.")

        except Exception as ex:

            #Prints a message to let the user know where an error occurred
            print("An error occurred in the Return class when adding return.", ex)

    #Fetch method to retrieve a return from the DB
    def fetch_return(self, ret_id = None, ord_id = None):

        #Try-except block to catch exceptions when fetching the return from the DB
        try:

            #Checks if a return ID was provided and if it was, that is how the return is retrieved. If the order_id was
            #provided, that is how the return is retrieved. If neither were provided, the whole
            #return table is retrieved.
            if ret_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM Return WHERE return_id = ?", (ret_id,)).fetchone()
            elif ord_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM Return WHERE order_id = ?",
                                                  (ord_id,)).fetchone()
            else:
                return self.db.get_cursor.execute("SELECT * FROM Return").fetchall()

        #Prints a message to let the user know what error occurred when retrieving the return.
        except Exception as e:
            print("An error occurred in the Return class when fetching return.", e)

    #Delete method for removing a return from the DB
    def delete_return(self, ret_id):

        #Try-except block to catch exceptions when deleting a return from the DB
        try:
            #Executes and commits the deletion of the return using the return id and SQL. It then commits
            #it.
            self.db.get_cursor.execute("DELETE FROM Return where return_id = ?;", (ret_id,))
            self.db.get_connection.commit()

            #Prints a message that the return has been deleted
            print(f"Deleted return {ret_id} successfully")
            return True

        #Prints a message to let the user know what error occurred when deleting the return.
        except Exception as e:
            print("An error has occurred when deleting the return.", e)
            return False

    #Method for updating a return entry in the DB
    def update_return(self, ret_id, date=None, ord_id=None, qty=None):

        #Try-except block to catch exceptions when updating return
        try:
            #If chain that checks what information was provided to update the return and executes SQL to make
            #that update
            if date is not None:
                self.db.get_cursor.execute("UPDATE Return set date = ? WHERE return_id = ?;", (date, ret_id))
                # Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the return date was updated successfully.
                print(f"Updated Return Date to {date} successfully.")
            if ord_id is not None:
                self.db.get_cursor.execute("UPDATE Return set order_id = ? WHERE return_id = ?;",
                                           (ord_id, ret_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the return order id was updated successfully.
                print(f"Updated Order ID on Return to {ord_id} successfully.")
            if qty is not None:
                self.db.get_cursor.execute("UPDATE Return set quantity = ? WHERE return_id = ?;", (qty, ret_id))
                # Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the return quantity was updated successfully.
                print(f"Updated Return Quantity to {qty} successfully.")

            #If statement for if the proper fields weren't provided
            if date is None and ord_id is None and qty is None:
                print("You must provide a date, order ID, or quantity to update the return.")

        #Prints a message to let the user know what error occurred when updating the return.
        except Exception as e:
            print("An error has occurred when updating the return.", e)

    #Method that runs when an Employee or Admin chose to access the Return Table
    def run_ret_options(self):

        #Establish the CRUD options for returns
        ret_options = {"get_ret": "Get all Returns",
                       "getby_ret": "Get Return by ID",
                       "update_ret": "Update Return",
                       "add_ret": "Add Return",
                       "del_ret": "Delete Return",
                       "back": "Go back a page"}

        #Prompt the employee to make a selection about what action they want to do to the Return table
        print("\nPlease choose an action you'd like to take: ")

        #Create a string to store the employee's action selection
        action_selection = ""

        #While loop that keeps prompting the user for
        while action_selection != "back":

            #Print the list of category options by looping through the dictionary items
            print("*** Return Action List ***")
            for action in ret_options.items():
                print(action)

            #Store the employee's selection in a variable to be checked
            action_selection = input("Select an action: ")

            #If-elif-else block that checks which action was selected and runs the appropriate method and logic for it
            if action_selection == "get_ret":

                #Calls the fetch_return method to get a list of returns and stores it in a variable
                results = self.fetch_return()

                #Print line for formatting
                print("")

                #Loops through each return in the list and prints
                for item in results:
                    print(item)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "getby_ret":

                #Prompts the employee to enter the ID of the return to fetch and stores
                ret_id = input("Enter Return ID: ")

                #Calls fetch method with ID and stores
                results = self.fetch_return(ret_id)

                #Prints return that was fetched
                print(results)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "update_ret":

                #Prompt the employee to enter the ID of the return they want to update
                ret_id = input("Enter Return ID: ")

                #Establish the attr options for updating the return
                attr_options = {"date": "Update Return Date",
                                "ord_id": "Update Return Order ID",
                                "qty": "Update Return Quantity"}

                #Prompt the employee to make a selection about what attribute they want to update
                print("\nPlease choose an attribute you'd like to update: ")

                #Boolean that is changed when a correct attribute has been chosen
                valid_attr = False

                #While loop that keeps prompting the user for an attribute selection
                while not valid_attr:

                    #Print the list of attribute options by looping through the dictionary items
                    print("*** Return Attribute List ***")
                    for attr in attr_options.items():
                        print(attr)

                    #Store the employee's selection in a variable to be checked
                    attr_selection = input("Select an attribute: ")

                    #If-elif-else block that checks which attribute was selected and runs the appropriate method and
                    #logic for it
                    if attr_selection == "date":
                        ret_date = input("Enter updated return date: ")
                        self.update_return(ret_id, date=ret_date, ord_id=None, qty=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "ord_id":
                        ord_id = input("Enter updated return order ID: ")
                        self.update_return(ret_id, date=None, ord_id=ord_id, qty=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "qty":
                        qty = input("Enter updated return quantity: ")
                        self.update_return(ret_id, date=None, ord_id=None, qty=qty)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    else:

                        print("Invalid selection, please try again\n")

            elif action_selection == "add_ret":

                #Prompt the user for the info of the return to add
                ret_date = input("Enter the date of the return to add: ")
                ret_order_id = input("Enter the order ID of the return to add: ")
                ret_qty = input("Enter the quantity of the return to add: ")

                #Now call the method to add the return
                self.add_return(ret_date, ret_order_id, ret_qty)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "del_ret":

                #Prompt the employee for the return ID of the return to delete
                ret_id = input("Please enter the ID of the return to delete: ")

                #Call the method to delete the return
                self.delete_return(ret_id)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            else:

                #If the user didn't select "back" let them know that they made an invalid selection
                if action_selection != "back":
                    print("Invalid selection, please try again\n")

        #Line to format output when going back
        print("")