#Program file that defines the Product class that represents the Product table. This file also contains the CRUD
#operations relating to the Product table.

#Imports

#Class definition for a Product
class Product:

    #Constructor to get the Database
    def __init__(self, db_obj):
        self.db = db_obj

    #Method for adding a Product to the skis database
    def add_prod(self, prod_name, type, pricing, makeup, manufacturing_cost, ski_name, dimensions):

        #Try-except block to catch exceptions when inserting product
        try:
            #Calling the get cursor and execute functions from the DBbase class to run sql to insert the product into
            #the DB and calling the get_connection and commit functions to commit the change
            self.db.get_cursor.execute("INSERT OR IGNORE into Product (prod_name, type, pricing, makeup, "
                                       "manufacturing_cost, ski_name, dimensions) values(?, ?, ?, ?, ?, ?, ?);",
                                       (prod_name, type, pricing, makeup, manufacturing_cost, ski_name,
                                        dimensions))
            self.db.get_connection.commit()

            #Printing to let the user know the product was added successfully
            print(f"Added Product: {prod_name} successfully.")

        except Exception as ex:

            #Prints a message to let the user know where an error occurred
            print("An error occurred in the Product class when adding product.", ex)

    #Fetch method to retrieve a product from the DB
    def fetch_prod(self, prod_id = None, prod_name = None):

        #Try-except block to catch exceptions when fetching the product from the DB
        try:

            #Checks if a product ID was provided and if it was, that is how the Product is retrieved. If the product
            #name was provided, that is how the Product is retrieved. If neither were provided, the whole Product table
            #is retrieved.
            if prod_id is not None:
                return self.db.get_cursor.execute("SELECT * FROM Product WHERE prod_id = ?", (prod_id,)).fetchone()
            elif prod_name is not None:
                return self.db.get_cursor.execute("SELECT * FROM Product WHERE prod_name = ?", (prod_name,)).fetchone()
            else:
                return self.db.get_cursor.execute("SELECT * FROM Product").fetchall()

        #Prints a message to let the user know what error occurred when retrieving the product.
        except Exception as e:
            print("An error occurred in the Product class when fetching product.", e)

    #Delete method for removing a product from the DB
    def delete_prod(self, prod_id):

        #Try-except block to catch exceptions when deleting a product from the DB
        try:
            #Executes and commits the deletion of the product using the product id and SQL. It then commits it.
            self.db.get_cursor.execute("DELETE FROM Product where prod_id = ?;", (prod_id,))
            self.db.get_connection.commit()

            #Prints a message that the product has been deleted
            print(f"Deleted product {prod_id} successfully")
            return True

        #Prints a message to let the user know what error occurred when deleting the product.
        except Exception as e:
            print("An error has occurred when deleting the product.", e)
            return False

    #Method for updating a product entry in the DB
    def update_prod(self, prod_id, prod_name = None, type = None, pricing = None, makeup = None,
                   manufacturing_cost = None, ski_name = None, dimensions = None):

        #Try-except block to catch exceptions when updating product
        try:
            #If chain that checks what information was provided to update the product and executes SQL to make
            #that update
            if prod_name is not None:
                self.db.get_cursor.execute("UPDATE Product set prod_name = ? WHERE prod_id = ?;", (prod_name, prod_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the product name was updated successfully.
                print(f"Updated Product to {prod_name} successfully.")
            if type is not None:
                self.db.get_cursor.execute("UPDATE Product set type = ? WHERE prod_id = ?;", (type, prod_id))
                # Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the type was updated successfully.
                print(f"Updated Product to {type} successfully.")
            if pricing is not None:
                self.db.get_cursor.execute("UPDATE Product set size_pricing = ? WHERE prod_id = ?;", (pricing,
                                                                                                      prod_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the ricing was updated successfully.
                print(f"Updated Product size pricing to {pricing} successfully.")
            if makeup is not None:
                self.db.get_cursor.execute("UPDATE Product set makeup = ? WHERE prod_id = ?;", (makeup, prod_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the makeup was updated successfully.
                print(f"Updated Product makeup to {makeup} successfully.")
            if manufacturing_cost is not None:
                self.db.get_cursor.execute("UPDATE Product set manufacturing_cost = ? WHERE prod_id = ?;",
                                           (manufacturing_cost, prod_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the manufacturing cost was updated successfully.
                print(f"Updated Product manufacturing cost to {manufacturing_cost} successfully.")
            if ski_name is not None:
                self.db.get_cursor.execute("UPDATE Product set ski_name = ? WHERE prod_id = ?;", (ski_name, prod_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the ski_name was updated successfully.
                print(f"Updated Product ski name to {ski_name} successfully.")
            if dimensions is not None:
                self.db.get_cursor.execute("UPDATE Product set dimensions = ? WHERE prod_id = ?;", (dimensions,
                                                                                                    prod_id))
                #Commits the change to the DB
                self.db.get_connection.commit()

                #Prints a message to let the user know the dimensions was updated successfully.
                print(f"Updated Product dimensions to {dimensions} successfully.")

            #If statement if the proper fields weren't provided
            if (prod_name is None and type is None and pricing is None and makeup is None
                    and manufacturing_cost is None and ski_name is None and dimensions is None):
                print("You must provide a product name, type, price, makeup, manufacturing cost, ski name, or "
                      "dimensions to update the product.")

        #Prints a message to let the user know what error occurred when updating the employee.
        except Exception as e:
            print("An error has occurred when updating the employee.", e)

    #Method that runs when an Employee or Admin chose to access the Product Table
    def run_prod_options(self):

        #Establish the CRUD options for products
        prod_options = {"get_prod": "Get all Products",
                       "getby_prod": "Get Product by ID",
                       "update_prod": "Update Product",
                       "add_prod": "Add Product",
                       "del_prod": "Delete Product",
                       "back": "Go back a page"}

        #Prompt the employee to make a selection about what action they want to do to the Product table
        print("\nPlease choose an action you'd like to take: ")

        #Create a string to store the employee's action selection
        action_selection = ""

        #While loop that keeps prompting the user for
        while action_selection != "back":

            #Print the list of category options by looping through the dictionary items
            print("*** Product Action List ***")
            for action in prod_options.items():
                print(action)

            #Store the employee's selection in a variable to be checked
            action_selection = input("Select an action: ")

            #If-elif-else block that checks which action was selected and runs the appropriate method and logic for it
            if action_selection == "get_prod":

                #Calls the fetch_prod method to get a list of products and stores it in a variable
                results = self.fetch_prod()

                #Print line for formatting
                print("")

                #Loops through each product in the list and prints
                for item in results:
                    print(item)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "getby_prod":

                #Prompts the employee to enter the ID of the product to fetch and stores
                prod_id = input("Enter Product ID: ")

                #Calls fetch method with ID and stores
                results = self.fetch_prod(prod_id)

                #Prints product that was fetched
                print(results)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "update_prod":

                #Prompt the employee to enter the ID of the product they want to update
                prod_id = input("Enter Product ID: ")

                #Establish the attr options for updating the product
                attr_options = {"name": "Update Product Name",
                                "type": "Update Product Type",
                                "price": "Update Product Price",
                                "makeup": "Update Product Size Pricing",
                                "man_cost": "Update Product Manufacturing Cost",
                                "ski_name": "Update Product Ski Name",
                                "dim": "Update Product Dimensions"}

                #Prompt the employee to make a selection about what attribute they want to update
                print("\nPlease choose an attribute you'd like to update: ")

                #Boolean that is changed when a correct attribute has been chosen
                valid_attr = False

                #While loop that keeps prompting the user for an attribute selection
                while not valid_attr:

                    #Print the list of attribute options by looping through the dictionary items
                    print("*** Product Attribute List ***")
                    for attr in attr_options.items():
                        print(attr)

                    #Store the employee's selection in a variable to be checked
                    attr_selection = input("Select an attribute: ")

                    #If-elif-else block that checks which attribute was selected and runs the appropriate method and
                    #logic for it
                    if attr_selection == "name":
                        prod_name = input("Enter updated product name: ")
                        self.update_prod(prod_id, prod_name, type=None, pricing=None, makeup=None,
                                         manufacturing_cost=None, ski_name=None, dimensions=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        # Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "type":
                        prod_type = input("Enter updated product type: ")
                        self.update_prod(prod_id, prod_name=None, type=prod_type, size_pricing=None, makeup=None,
                                         manufacturing_cost=None, ski_name=None, dimensions=None)
                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "price":
                        prod_price = input("Enter updated product pricing: ")
                        self.update_prod(prod_id, prod_name=None, type=None, pricing=prod_price, makeup=None,
                                         manufacturing_cost=None, ski_name=None, dimensions=None)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "makeup":
                        prod_makeup = input("Enter updated product makeup: ")
                        self.update_prod(prod_id, prod_name=None, type=None, pricing=None, makeup=prod_makeup,
                                         manufacturing_cost=None, ski_name=None, dimensions=None)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "man_cost":
                        prod_man_cost = input("Enter updated product manufacturing cost: ")
                        self.update_prod(prod_id, prod_name=None, type=None, pricing=None, makeup=None,
                                         manufacturing_cost=prod_man_cost, ski_name=None, dimensions=None)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "ski_name":
                        prod_ski_name = input("Enter updated product ski name: ")
                        self.update_prod(prod_id, prod_name=None, type=None, pricing=None, makeup=None,
                                         manufacturing_cost=None, ski_name=prod_ski_name, dimensions=None)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    elif attr_selection == "dim":
                        prod_dim = input("Enter updated product dimensions: ")
                        self.update_prod(prod_id, prod_name=None, type=None, pricing=None, makeup=None,
                                         manufacturing_cost=None, ski_name=None, dimensions=prod_dim)

                        #Set boolean to true since correct attribute was selected
                        valid_attr = True

                        #Allow the employee to continue and format output
                        input("Press return to continue")
                        print("")

                    else:

                        print("Invalid selection, please try again\n")

            elif action_selection == "add_prod":

                #Prompt the user for the info of the product to add
                prod_name = input("Enter the product name of the Product to add: ")
                prod_type = input("Enter the type of the Product to add: ")
                prod_price = input("Enter the price of the Product to add: ")
                prod_makeup = input("Enter the makeup of the Product to add: ")
                prod_man_cost = input("Enter the manufacturing cost of the Product to add: ")
                prod_ski_name = input("Enter the ski name of the Product to add: ")
                prod_dim = input("Enter the dimensions of the Product to add: ")

                #Now call the method to add the product
                self.add_prod(prod_name, prod_type, prod_price, prod_makeup, prod_man_cost, prod_ski_name,
                              prod_dim)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            elif action_selection == "del_prod":

                #Prompt the employee for the product ID of the product to delete
                prod_id = input("Please enter the ID of the product to delete: ")

                #Call the method to delete the product
                self.delete_prod(prod_id)

                #Allow the employee to continue and format output
                input("Press return to continue")
                print("")

            else:

                #If the user didn't select "back" let them know that they made an invalid selection
                if action_selection != "back":
                    print("Invalid selection, please try again\n")

        #Line to format output when going back
        print("")