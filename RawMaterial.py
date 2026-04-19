#Program file that defines the RawMaterial class that represents the Raw_Material table. This file also contains the
#CRUD operations relating to the Raw_Material table.

#Imports

#Class definition for a Raw Material
class RawMaterial:

    #Constructor to get the Database
    def __init__(self, db_obj):
        self.db = db_obj

    #Method for adding a raw material to the skis database
    def add_rm(self, cast, date_purch, qty, mat_name):

        #Try-except block to catch exceptions when inserting raw material
        try:
            #Calling the get cursor and execute functions from the DBbase class to run sql to insert the raw material
            #into the DB and calling the get_connection and commit functions to commit the change
            self.db.get_cursor.execute("INSERT OR IGNORE into RAW_MATERIAL (cast, date_purchased, quantity, "
                                       "material_name) values(?, ?, ?, ?);", (cast, date_purch, qty, mat_name))
            self.db.get_connection.commit()

            #Printing to let the employee know the raw material was added successfully
            print(f"Added raw material: {mat_name} successfully.")

        except Exception as ex:

            #Prints a message to let the user know where an error occurred
            print("An error occurred in the RawMaterial class when adding raw material.", ex)

    #Fetch method to retrieve a raw material from the DB
    def fetch_rm(self, rm_id = None, rm_name = None):

        #Try-except block to catch exceptions when fetching the raw material from the DB
        try:

            #Checks if a material ID was provided and if it was, that is how the raw material is retrieved. If the
            #material name was provided, that is how the raw material is retrieved. If neither were provided, the whole
            #raw_material table is retrieved.
            if rm_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM Raw_Material WHERE material_id = ?", (rm_id,)).fetchone()
            elif rm_name is not None:
                return self.db.get_cursor.execute("SELECT * FROM Raw_Material WHERE material_name = ?",
                                                  (rm_name,)).fetchone()
            else:
                return self.db.get_cursor.execute("SELECT * FROM Raw_Material").fetchall()

        #Prints a message to let the user know what error occurred when retrieving the raw material.
        except Exception as e:
            print("An error occurred in the RawMaterial class when fetching raw material.", e)

    #Delete method for removing a raw material from the DB
    def delete_rm(self, rm_id):

        #Try-except block to catch exceptions when deleting a raw material from the DB
        try:
            #Executes and commits the deletion of the raw material using the raw material id and SQL. It then commits
            #it.
            self.db.get_cursor.execute("DELETE FROM Raw_Material where material_id = ?;", (rm_id,))
            self.db.get_connection.commit()

            #Prints a message that the raw material has been deleted
            print(f"Deleted raw material {rm_id} successfully")
            return True

        #Prints a message to let the user know what error occurred when deleting the raw material.
        except Exception as e:
            print("An error has occurred when deleting the raw material.", e)
            return False

    #Method for updating a raw material entry in the DB
    def update_rm(self, rm_id, cast=None, date_purch=None, qty=None, mat_name=None):

        #Try-except block to catch exceptions when updating raw material
        try:
            #If chain that checks what information was provided to update the raw material and executes SQL to make
            #that update
            if cast is not None:
                self.db.get_cursor.execute("UPDATE Raw_Material set cast = ? WHERE material_id = ?;", (cast, rm_id))
                # Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the material cast was updated successfully.
                print(f"Updated Raw Material Cast to {cast} successfully.")
            if date_purch is not None:
                self.db.get_cursor.execute("UPDATE Raw_Material set date_purchased = ? WHERE material_id = ?;",
                                           (date_purch, rm_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the material date purchased was updated successfully.
                print(f"Updated Raw Material Date Purchased to {date_purch} successfully.")
            if qty is not None:
                self.db.get_cursor.execute("UPDATE Raw_Material set quantity = ? WHERE material_id = ?;", (qty, rm_id))
                # Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the employee know the material quantity was updated successfully.
                print(f"Updated Raw Material Quantity to {qty} successfully.")
            if mat_name is not None:
                self.db.get_cursor.execute("UPDATE Raw_Material set material_name = ? WHERE material_id = ?;",
                                           (mat_name, rm_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the material name was updated successfully.
                print(f"Updated Raw Material Name to {mat_name} successfully.")

            #If statement for if the proper fields weren't provided
            if cast is None and date_purch is None and qty is None and mat_name is None:
                print("You must provide a cast, date purchased, quantity, or material name to update the raw material.")

        #Prints a message to let the user know what error occurred when updating the raw material.
        except Exception as e:
            print("An error has occurred when updating the raw material.", e)

    #Method that runs when an Employee or Admin chose to access the Raw_Material Table
    def run_rm_options(self):

        #Establish the CRUD options for raw materials
        rm_options = {"get_rm": "Get all Products",
                       "getby_rm": "Get Product by ID",
                       "update_rm": "Update Product",
                       "add_rm": "Add Product",
                       "del_rm": "Delete Product",
                       "back": "Go back a page"}

        #Prompt the employee to make a selection about what action they want to do to the Raw_Material table
        print("\nPlease choose an action you'd like to take: ")

        #Create a string to store the employee's action selection
        action_selection = ""

        #While loop that keeps prompting the user for
        while action_selection != "back":

            #Print the list of category options by looping through the dictionary items
            print("*** Raw Material Action List ***")
            for action in rm_options.items():
                print(action)

            #Store the employee's selection in a variable to be checked
            action_selection = input("Select an action: ")

            #If-elif-else block that checks which action was selected and runs the appropriate method and logic for it
            if action_selection == "get_rm":

                #Calls the fetch_return method to get a list of raw materials and stores it in a variable
                results = self.fetch_rm()

                #Print line for formatting
                print("")

                #Loops through each raw material in the list and prints
                for item in results:
                    print(item)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "getby_rm":

                #Prompts the employee to enter the ID of the raw material to fetch and stores
                rm_id = input("Enter Raw Material ID: ")

                #Calls fetch method with ID and stores
                results = self.fetch_rm(rm_id)

                #Prints raw material that was fetched
                print(results)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "update_rm":

                # Prompt the employee to enter the ID of the raw material they want to update
                rm_id = input("Enter Raw Material ID: ")

                #Establish the attr options for updating the raw material
                attr_options = {"cast": "Update Raw Material Cast",
                                "date": "Update Raw Material Date Purchased",
                                "qty": "Update Raw Material Quantity",
                                "name": "Update Raw Material Name"}

                #Prompt the employee to make a selection about what attribute they want to update
                print("\nPlease choose an attribute you'd like to update: ")

                #Boolean that is changed when a correct attribute has been chosen
                valid_attr = False

                #While loop that keeps prompting the user for an attribute selection
                while not valid_attr:

                    #Print the list of attribute options by looping through the dictionary items
                    print("*** Raw Material Attribute List ***")
                    for attr in attr_options.items():
                        print(attr)

                    #Store the employee's selection in a variable to be checked
                    attr_selection = input("Select an attribute: ")

                    #If-elif-else block that checks which attribute was selected and runs the appropriate method and
                    #logic for it
                    if attr_selection == "cast":
                        rm_cast = input("Enter updated raw material cast: ")
                        self.update_rm(rm_id, cast=rm_cast, date_purch=None, qty=None, mat_name=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "date":
                        rm_date = input("Enter updated raw material date purchased: ")
                        self.update_rm(rm_id, cast=None, date_purch=rm_date, qty=None, mat_name=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "qty":
                        rm_qty = input("Enter updated raw material quantity: ")
                        self.update_rm(rm_id, cast=None, date_purch=None, qty=rm_qty, mat_name=None)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "name":
                        rm_name = input("Enter updated raw material name: ")
                        self.update_rm(rm_id, cast=None, date_purch=None, qty=None, mat_name=rm_name)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    else:

                        print("Invalid selection, please try again\n")

            elif action_selection == "add_rm":

                #Prompt the user for the info of the raw material to add
                rm_cast = input("Enter the cast of the raw material to add: ")
                rm_date = input("Enter the date purchased for the raw material to add: ")
                rm_qty = input("Enter the quantity of the raw material to add: ")
                rm_name = input("Enter the name of the raw material to add: ")

                #Now call the method to add the raw material
                self.add_rm(rm_cast, rm_date, rm_qty, rm_name)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "del_rm":

                #Prompt the employee for the raw material ID of the raw material to delete
                rm_id = input("Please enter the ID of the raw material to delete: ")

                #Call the method to delete the raw material
                self.delete_rm(rm_id)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            else:

                #If the user didn't select "back" let them know that they made an invalid selection
                if action_selection != "back":
                    print("Invalid selection, please try again\n")

        #Line to format output when going back
        print("")