#Program that acts as the main project file that runs the program

#imports
import Employee
import Admin
import Customer
import SkiDB as skiDB


class Project:

    #Run method for running the Skis DB program
    def run(self):

        #Create instance of Database
        skidb = skiDB.Skis()

        #Print a welcome message and prompt the user for an employee ID and password
        print("Welcome to the Kitten Factory.")

        #Prompts the user to indicate if they are a customer or employee and stores their answer as a string
        emp_or_cust = input("Please indicate if you are a Customer or Employee(C/E): ").lower()

        #If-else block for employee vs customer options
        if emp_or_cust == "e":

            #Create an instance of the Employee class since the user indicated they are an employee
            employee = Employee.Employee(skidb)

            #Variables that define the indexes of information so that we don't use "magic numbers"
            emp_id_index = 0
            emp_last_index = 1
            emp_first_index = 2

            #Store a list of the employees to check against
            emp_list = employee.fetch_emp()

            while True:
                #Set boolean to false initially to mark if the employee was found
                employee_found = False

                #Prompt the employee to enter their employee ID and name
                print("Please enter your Employee ID and Password")

                #Store the employee ID and password to be checked if the user is an employee or admin
                emp_id = int(input("Employee ID: "))
                emp_password = input("Password: ")

                #Loops through the employee list to check against the provided credentials
                for emp in emp_list:

                    #If-elif that checks if the credentials match an employee or admin
                    if emp_id == emp[emp_id_index] and emp_password == "KT-DBADMIN-801":

                        #Print to welcome the admin to the system
                        print(f"Welcome {emp[emp_first_index]} {emp[emp_last_index]}. Signed in as ADMIN. \n")

                        #Create instance of Admin Object
                        admin = Admin.Admin(skidb)

                        #RUN METHOD FROM ADMIN FILE
                        admin.run_admin()

                        #Employee was found so set boolean for employee_found to True
                        employee_found = True

                    elif emp_id == emp[emp_id_index] and emp_password == "KT-EMPLOYEE":

                        #Print to welcome the employee to the system
                        print(f"Welcome {emp[emp_first_index]} {emp[emp_last_index]}. \n")

                        #RUN METHOD FROM EMPLOYEE FILE
                        employee.run_emp()

                        # Employee was found so set boolean for employee_found to True
                        employee_found = True

                #Runs if an employee wasn't found
                if not employee_found:

                    #If this is reached, the employee wasn't found so print a message
                    print("ACCESS DENIED: Credentials not found. Please try again.\n")

                #Check if the employee was found, if they were, break from the while loop
                if employee_found:
                    break

        #This section is for customers
        else:

            #Create a new instance of the Customer class
            customer = Customer.Customer(skidb)

            #Section that prompts the customer for their customer ID if they know it or not
            cust_id = input("Customer ID (or \"n/a\"): ").lower()

            #If the customer doesn't know their ID, prompt them for their name. Then fetch their ID
            if cust_id == "n/a":
                cust_first = input("First name: ")
                cust_last = input("Last name: ")

                #Assigning index of customer ID to descriptive variable so "magic numbers" are not used
                cust_id_index = 0
                cust_id = customer.fetch_cust(cust_id=None, first=cust_first, last=cust_last)[cust_id_index]

            #If the customer did know their ID, we need to grab their first and last name for the welcome message
            else:

                #Assigning index of customer first and last to descriptive variables so "magic numbers" are not used
                cust_first_index = 1
                cust_last_index = 2
                cust_first = customer.fetch_cust(cust_id=cust_id, first=None, last=None)[cust_first_index]
                cust_last = customer.fetch_cust(cust_id=cust_id, first=None, last=None)[cust_last_index]

            #ADD PASSWORD LOGIC HERE

            #Print to welcome the customer
            print(f"Welcome {cust_first} {cust_last}! \n")
            
            #Once signed in, call the run method from the Customer class
            customer.run_cust(cust_id)

project = Project()
project.run()

# skidb = SkiDB.Skis()
# employee = Employee.Employee(skidb)
# employee.add_emp("Jelovich", "Jacob", "CEO")
