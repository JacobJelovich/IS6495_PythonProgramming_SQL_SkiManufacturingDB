#Program file that defines the Employee class that represents the Employee table. This file also contains the logic for
#the actions that an employee can make when logged into the system as well as CRUD operations relating to the Employee
#table.

#Imports
import Customer
import Product
import RawMaterial
import Return
import Order

#Class definition for an employee
class Employee:

    #Constructor to get the Database
    def __init__(self, db_obj):
        self.db = db_obj

    #Method for adding an employee to the skis database
    def add_emp(self, last, first, position):

        #Try-except block to catch exceptions when inserting employee
        try:
            #Calling the get cursor and execute functions from the DBbase class to run sql to insert the employee into the DB and
            #calling the get_connection and commit functions to commit the change
            self.db.get_cursor.execute("INSERT OR IGNORE into Employee (last, first, position) "
                                       "values(?, ?, ?);", (last, first, position))
            self.db.get_connection.commit()

            #Printing to let the user know the employee was added successfully
            print(f"Added employee: {last}, {first} successfully.")

        except Exception as ex:

            #Prints a message to let the user know where an error occurred
            print("An error occurred in the Employee class when adding employee.", ex)

    #Fetch method to retrieve an emp from the DB
    def fetch_emp(self, emp_id = None, last = None, first = None):

        #Try-except block to catch exceptions when fetching the employee from the DB
        try:

            #Checks if an employee ID was provided and if it was, that is how the Employee is retrieved. If the first
            #and last name was provided, that is how the Employee is retrieved. If neither were provided, the whole
            #employee table is retrieved.
            if emp_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM Employee WHERE emp_id = ?", (emp_id,)).fetchone()
            elif last is not None and first is not None:
                return self.db.get_cursor.execute("SELECT * FROM Employee WHERE last = ? and first = ?", (last, first)).fetchone()
            else:
                return self.db.get_cursor.execute("SELECT * FROM Employee").fetchall()

        #Prints a message to let the user know what error occurred when retrieving the employee.
        except Exception as e:
            print("An error occurred in the Employee class when fetching employee.", e)

    #Delete method for removing an employee from the DB
    def delete_emp(self, emp_id):

        #Try-except block to catch exceptions when deleting an employee from the DB
        try:
            #Executes and commits the deletion of the employee using the employee id and SQL. It then commits it.
            self.db.get_cursor.execute("DELETE FROM Employee where emp_id = ?;", (emp_id,))
            self.db.get_connection.commit()

            #Prints a message that the employee has been deleted
            print(f"Deleted employee {emp_id} successfully")
            return True

        #Prints a message to let the user know what error occurred when deleting the employee.
        except Exception as e:
            print("An error has occurred when deleting the employee.", e)
            return False

    #Method for updating an employee entry in the DB
    def update_emp(self, emp_id, last = None, first = None, position = None):

        #Try-except block to catch exceptions when updating employee
        try:
            #If-elif-else chain that checks what information was provided to update the employee and executes SQL to make
            #that update
            if last is not None and first is not None and position is not None:
                self.db.get_cursor.execute("UPDATE Employee set last = ?, first = ?, position = ? WHERE emp_id = ?;",
                                           (last, first, position, emp_id))

                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the last, first, and position were updated successfully.
                print(f"Updated Employee to {last, first, position} successfully.")
            elif last is not None and first is not None and position is None:
                self.db.get_cursor.execute("UPDATE Employee set last = ?, first = ? WHERE emp_id = ?;", (last, first,
                                                                                                         emp_id))

                # Commits the change to the DB
                self.db.get_connection.commit()

                # Prints a message to let the user know the last and first were updated successfully.
                print(f"Updated Employee to {last, first} successfully.")
            elif last is None and first is None and position is not None:
                self.db.get_cursor.execute("UPDATE Employee set position = ? WHERE emp_id = ?;", (position, emp_id))

                # Commits the change to the DB
                self.db.get_connection.commit()

                # Prints a message to let the user know the position was updated successfully.
                print(f"Updated Employee to {position} successfully.")

            #Else statement if the proper fields weren't provided
            else:
                print("You must provide either the last and first name or position to update employee.")


        #Prints a message to let the user know what error occurred when updating the employee.
        except Exception as e:
            print("An error has occurred when updating the employee.", e)

    #Method that runs when an employee signs in to allow them access to the system
    def run_emp(self):

        #Establish the category options for employees
        category_options = {"emp": "Employee Access",
                            "cust": "Customer Access",
                            "prod": "Product Access",
                            "rm": "Raw Material Access",
                            "ret": "Return Access",
                            "ord": "Order Access",
                            "exit": "Exit Program"}

        #Prompt the user to make a selection about what category they want to access
        print("Please choose a category you would like to access: ")

        #Create a string to store the user's catagory selection
        category_selection = ""

        #While loop that keeps prompting the user for a selection unless they choose "exit"
        while category_selection != "exit":

            #Print the list of category options by looping through the dictionary items
            print("*** Category List ***")
            for category in category_options.items():
                print(category)

            #Store the users selection in a variable to be checked
            category_selection = input("Select a category: ")

            #If-elif-else block that checks which category was selected and runs the appropriate method for it
            if category_selection == "emp":
                self.run_emp_options()

            elif category_selection == "cust":
                customer = Customer.Customer(self.db)
                customer.run_cust_options()

            elif category_selection == "prod":
                product = Product.Product(self.db)
                product.run_prod_options()

            elif category_selection == "rm":
                rm = RawMaterial.RawMaterial(self.db)
                rm.run_rm_options()

            elif category_selection == "ret":
                ret = Return.Return(self.db)
                ret.run_ret_options()

            elif category_selection == "ord":
                order = Order.Order(self.db)
                order.run_ord_options()

            #This runs if the employee entered something that wasn't an option to print a message to let them know
            else:
                if category_selection != "exit":
                    print("Invalid selection, please try again\n")

    #Method that runs when an Employee or Admin chose to access the Employee Table
    def run_emp_options(self):

        #Establish the CRUD options for employees
        emp_options = {"get_emp": "Get all Employees",
                       "getby_emp": "Get Employee by ID",
                       "update_emp": "Update Employee",
                       "add_emp": "Add Employee",
                       "del_emp": "Delete Employee",
                       "back": "Go back a page"}

        #Prompt the user to make a selection about what action they want to do to the Employee table
        print("\nPlease choose an action you'd like to take: ")

        #Create a string to store the user's action selection
        action_selection = ""

        #While loop that keeps prompting the user for
        while action_selection != "back":

            #Print the list of category options by looping through the dictionary items
            print("*** Employee Action List ***")
            for action in emp_options.items():
                print(action)

            #Store the users selection in a variable to be checked
            action_selection = input("Select an action: ")

            #If-elif-else block that checks which action was selected and runs the appropriate method and logic for it
            if action_selection == "get_emp":

                #Calls the fetch_emp method to get a list of employees and stores it in a variable
                results = self.fetch_emp()

                #Print line for formatting
                print("")

                #Loops through each employee in the list and prints
                for item in results:
                    print(item)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "getby_emp":

                #Prompts the employee to enter the ID of the employee to fetch and stores
                emp_id = input("Enter Employee ID: ")

                #Calls fetch method with ID and stores
                results = self.fetch_emp(emp_id)

                #Prints employee that was fetched
                print(results)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "update_emp":

                #Prompt the employee to enter the ID of the employee they want to update
                emp_id = input("Enter Employee ID: ")

                #Prompt the user for last name to be changed to. They enter n/a if they want to update position
                emp_last = input("Enter updated last name or \"n/a\" if you want to update position: ")

                #Check if the user entered a last name, if they did, prompt the user for an updated first name. If they
                #didn't, prompt the user for a position. Call the update employee method afterward.
                if emp_last != "n/a":
                    emp_first = input("Enter updated first name: ")
                    self.update_emp(emp_id, last=emp_last, first=emp_first)
                    print(self.fetch_emp(emp_id))

                    #Allow the employee to continue and format output
                    input("Press return to continue")
                    print("")
                else:
                    emp_position = input("Enter updated position: ")
                    self.update_emp(emp_id, position=emp_position)
                    print(self.fetch_emp(emp_id))

                    #Allow the employee to continue and format output
                    input("Press return to continue")
                    print("")

            elif action_selection == "add_emp":

                #Prompt the user for the info of the employee to add
                emp_last = input("Enter the last name of the Employee to add: ")
                emp_first = input("Enter the first name of the Employee to add: ")
                emp_position = input("Enter the position of the Employee to add: ")

                #Now call the method to add the employee
                self.add_emp(emp_last, emp_first, emp_position)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "del_emp":

                #Prompt the user for the employee ID of the employee to delete
                emp_id = input("Please enter the ID of the employee to delete: ")

                #Call the method to delete the employee
                self.delete_emp(emp_id)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            else:

                #If the user didn't select "back" let them know that they made an invalid selection
                if action_selection != "back":
                    print("Invalid selection, please try again\n")

        #Line to format output when going back
        print("")