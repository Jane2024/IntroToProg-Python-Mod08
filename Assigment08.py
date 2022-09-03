# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MBruce,8.31.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# start of Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """This class stores data about a product:

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    methods:
        to_string():    (string)This returns a string
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MBruce,8.31.2022,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class

    # -- Constructor --
    ###############################################
    def __init__(self, product, price):
        self.product_name = product             # uses the property to create attribute for product_name
        self.product_price = price              # uses the property to create attribute for product_price

    # -- Properties --
    ################################################
    # product_name
    @property
    def product_name(self):                                 # Getter property for product_name
        return str(self.__product_name).title()             # converts to title case and returns product_name

    @product_name.setter
    def product_name(self, productX):                       # Setter property for product_name
        if str(productX).isnumeric() == False:              # Check if entry is numeric
            self.__product_name = productX                  # If string, assign name to attribute
        else:
            raise Exception("Names cannot be numbers")      # Else inform user entry in invalid

    # product_price
    @property
    def product_price(self):                                # Getter property for product_price
        return str(self.__product_price)                    # returns product_price

    @product_price.setter
    def product_price(self, priceX):                        # Setter property for product_price
        try:
            if float(priceX):                               # Check if entry is float
                self.__product_price = float(priceX)        # If float, assign price to attribute
        except ValueError:
            raise Exception("Price needs to be a number")   # Else inform user entry in invalid


    # -- Methods --
    #################################################
    def to_string(self):
        return self.__str__()                                # Overrides defualt str() method and converts class data to string

    def __str__(self):
        return self.product_name + ", " + self.product_price # Returns product_name and product price as a string


# End of Data -------------------------------------------------------------------- #

# Start of Processing  ------------------------------------------------------------- #
class FileProcessor:
    """ This class processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects):
        add_data_to_list(product, price, list_of_products) - Adds news product to list:

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MBruce,8.31.2022,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):                     # reads a list of product objects from file
        """ Reads a list of product objects from a file

            :param file_name: (string) name of file to open and read
            :return: list_of_products: (list) returns list of products read from file
        """

        list_of_products=[]                                 # Initialize list of product to empty set
        try:
            file = open(file_name, "r")                     # Try to open file to read list of products
            for line in file:                               # loop through each line in file
                item = line.split(",")                      # separate the product and price items in each line
                row = Product(item[0],item[1])              # assign each pair of product and price to a row
                list_of_products.append(row)                # append it to the list
            file.close()
        except IOError:                                     # If file was not found, then except clause executes and informs the user.
            print("ERROR...cannot locate", file_name, "file.")
        return list_of_products                             # returns list of product objects


    ########################################################
    # Added additional method #
    @staticmethod
    def add_data_to_list(product, price, list_of_products):
        """ Adds new data to a list of product objects

            :param product: (string) name of product:
            :param price: (float) price of product:
            :param list_of_products: (list) the list of products:
            :return: (list) appended list of products
        """
        p= Product(str(product).strip(), float(price))       # create a new product object with new product name and price
        list_of_products.append(p)                           # append the new product instance to the list


        return list_of_products                              # return the appended list of products

    ########################################################

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves a list of product objects to file

            :param file_name: (string) name of file
            :param list_of_product_objects: (list) a list containing product objs
            :return: write_status: (bool) return true or false based if it successfully wrote to file
        """
        write_status = False                            # initialize write status to False
        try:
            objFile = open(file_name, "w")              # Open file for write
            for row in list_of_product_objects:         # Loop through rows in list
                objFile.write(str(row) + "\n")          # Write each row to file
            objFile.close()
            write_status =True                          # set the status to true- It Worked!!!
        except Exception as e:                          # Inform user if could not open file
            print("Could not write to file")
        return write_status                             # Need to return if the write to file was successful or not


# End of Processing  ------------------------------------------------------------- #

# Start of Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ This class handles the presentation of the data:

        methods:
            :output_menu():
            :input_menu_choice(int):  gets user's menu choice
            :output_current_list(list): shows users current data in list
            :add_product(product_name, product_price): adds new products to list
            :exit_program(int): exits program


        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            MBruce,8.31.2022,Modified code to complete assignment 8
        """

    # TODO: Add code to show menu to user
    @staticmethod
    def output_menu():
        """  Display a menu of choices to the user

            :return: nothing
        """
        print('''
            Menu of Options
            ----------------------------
            1) Show current data in list
            2) Add a new product to list
            3) Save list to File        
            4) Exit Program
            ''')
        print()  # Add a line to beautify

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

            :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add a line to beautify
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_list(list_of_rows):
        """ Shows the current products and their prices in the list of Products

            :param list_of_rows: (list) of rows you want to display
            :return: nothing
        """
        print("******* The current product list is: *******")
        for row in list_of_rows:
            print(row.product_name + " -  $" + row.product_price )
        print("********************************************")
        print()  # Add a line to beautify


    # TODO: Add code to get product data from user
    @staticmethod
    def input_new_product_and_price():
        """  Gets product and price data to be added to the list

            :return: (string, string) with product and price
        """
        str_product = input("Please input a new product name: ") # Prompt user for new product- assign to string "str_product"
        flt_price = input("Please input its price: ")            # Prompt user for price- assign to string "flt_price"

        return (str_product, flt_price)  # Return user entered product and price values


# End of Presentation (Input/Output)  -------------------------------------------- #


#############################################################################
# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts
try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while (True):

        # Show user a menu of options
        IO.output_menu()

        # Get user's menu option choice
        choice_str = IO.input_menu_choice()

        # Show user current data in the list of product objects
        if choice_str.strip() == '1':  # show current data in list
            IO.output_current_list(lstOfProductObjects)
            continue

        # Let user add data to the list of product objects
        elif choice_str.strip() == '2':  # add product to list
            str_product, flt_price = IO.input_new_product_and_price()
            lstOfProductObjects = FileProcessor.add_data_to_list(product=str_product, price=flt_price, list_of_products=lstOfProductObjects)
            continue  # to show the menu

        # let user save current data to file
        elif choice_str == '3':  # Save Data to File
            table_lst = FileProcessor.save_data_to_file(file_name=strFileName, list_of_product_objects=lstOfProductObjects)
            print("Data Saved!")
            continue  # to show the menu

        # exit program
        elif choice_str == '4':  # Exit Program
            print("Goodbye!")
            break  # by exiting loop

except Exception as e:
    print("Dude, you got an file error!")
    print(e,e.__doc__,sep="\n")

# End of Main Body of Script  --------------------------------------------------- #




