from Forestview_DataEntry import Forestview_DataEntry
from Forestview_ReadOrdersCsv import Forestview_OpenOrdersCsv
import random
"""
Combines order and user oder data
"""
import string
class Forestview_Database:
    #Method to create data structure
    def __init__(self):
        #Empty dictionary to store data based off of order id as key
        self.forestview_datastructure = {}
        #Store data from csv files into variables
        self.order_data = Forestview_OpenOrdersCsv().return_orders()
        #Create data structure
        self.create_data_structure()
        #Variable to keep track of last order... mainly used to add order to database
        self.LAST_ORDER = Forestview_DataEntry(self.forestview_datastructure[self.order_data[-1][0]])
    
    #Creates database
    def create_data_structure(self):
        for i in range(len(self.order_data)):
            self.forestview_datastructure[self.order_data[i][0]] = self.order_data[i]

    #Deletes last order from database
    def delete_last_entry(self):
        item_deleted = list(self.forestview_datastructure)[-1]
        self.forestview_datastructure.popitem()
        return item_deleted
        
    
    
    #Method to generate random order and order details and then adds it to dictionary
    def add_random_entry(self):
        order = []
        order_id = str(int(self.LAST_ORDER.get_order_id()) + 1)
        customer_id = "SAMPL"
        employee_id = random.choice(range(10))
        order_date = self.LAST_ORDER.get_order_date()
        required_date = self.LAST_ORDER.get_order_date()
        shipped_date = self.LAST_ORDER.get_shipped_date()
        ship_via = self.LAST_ORDER.get_ship_via()
        freight = self.LAST_ORDER.get_freight()
        ship_name = self.LAST_ORDER.get_ship_name()

        #Create new random order
        order = [order_id, customer_id, employee_id, order_date, required_date, shipped_date,
                 ship_via, freight, ship_name]
        self.forestview_datastructure[order_id] = order
        self.LAST_ORDER = Forestview_DataEntry(order)
        #Returns newly added order
        return "Adding Randomly Generated Data... \n" + "Randomly Generated data is:\n" + list(self.forestview_datastructure)[-1]
    def return_last_order(self):
        order_id = self.LAST_ORDER.get_order_id()
        dataEntry = Forestview_DataEntry(self.forestview_datastructure[order_id])
        order = "Order ID: " + str(dataEntry.get_order_id()) + "\n" \
            + "Customer ID: " + str(dataEntry.get_customer_id()) + "\n" \
            + "Employee ID: " + str(dataEntry.get_employee_id()) + "\n" \
            + "Order Date: " + str(dataEntry.get_order_date()) + "\n" \
            + "Required Date: " + str(dataEntry.get_required_date()) + "\n" \
            + "Shipped Date: " + str(dataEntry.get_shipped_date()) + "\n" \
            + "Shipped Via: " + str(dataEntry.get_ship_via()) + "\n" \
            + "Freight: " + str(dataEntry.get_freight()) + "\n" \
            + "Shipped To: " + str(dataEntry.get_ship_name())
        return order
    def add_order_to_database(self, data):
        try:
            val = ""
            for char in data:
                if str.isalnum(char) or char == "," or char == "-":
                    val = val + char
            list_of_vals = val.split(",")
            order_id = str(int(self.LAST_ORDER.get_order_id()) + 1)
            customer_id = list_of_vals[0]
            employee_id = list_of_vals[1]
            order_date = list_of_vals[2]
            required_date = list_of_vals[3]
            shipped_date = list_of_vals[4]
            ship_via = list_of_vals[5]
            freight = list_of_vals[6]
            ship_name = list_of_vals[7]
            self.forestview_datastructure[order_id] = [order_id,customer_id, employee_id, order_date, required_date, shipped_date, ship_via, freight, ship_name]
            order = [order_id, customer_id, employee_id, order_date, required_date, shipped_date, ship_via, freight, ship_name]
            self.LAST_ORDER = Forestview_DataEntry(order)

        except:
            print("ERROR: Make sure strings are seperated by commas!")

    #================================================================================================================================#
    #===================================================Search engine================================================================#
    #================================================================================================================================#
    
    #Search by order id returns order data as list
    def search_order_id(self, order_id):
        try:
            val = ""
            for char in order_id:
                if str.isalnum(char):
                    val = val + char
            #return str(self.forestview_datastructure[order_id])
            dataEntry = Forestview_DataEntry(self.forestview_datastructure[str(val)])
            order = "Order ID: " + str(dataEntry.get_order_id()) + "\n" \
            + "Customer ID: " + str(dataEntry.get_customer_id()) + "\n" \
            + "Employee ID: " + str(dataEntry.get_employee_id()) + "\n" \
            + "Order Date: " + str(dataEntry.get_order_date()) + "\n" \
            + "Required Date: " + str(dataEntry.get_required_date()) + "\n" \
            + "Shipped Date: " + str(dataEntry.get_shipped_date()) + "\n" \
            + "Shipped Via: " + str(dataEntry.get_ship_via()) + "\n" \
            + "Freight: " + str(dataEntry.get_freight()) + "\n" \
            + "Shipped To: " + str(dataEntry.get_ship_name())
            return order
        except KeyError:
            return "ERROR... NO ORDERS WERE FOUND WITH THAT ORDER ID"
        
    #Search orders by customer id returns all orders from that customer
    def search_customer_id(self, customer_id):
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            val = ""
            for char in customer_id:
                if str.isalnum(char):
                    val = val + char
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][1] == val.upper():
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND WITH THE CUSTOMER ID: " + customer_id
    
    #Search orders by employee id returns all orders completed by that employee
    def search_employee_id(self, employee_id):
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            val = ""
            for char in employee_id:
                if str.isalnum(char):
                    val = val + char
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][2] == val:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND WITH THE EMPLOYEE ID: " + employee_id

    #Search orders by order date returns orders ordered on that date
    def search_order_date(self, order_date):
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            val = ""
            for char in order_date:
                if str.isalnum(char) or char == "-":
                    val = val + char
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][3][:10] == val:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND THAT WERE ORDERED ON: " + order_date
    
    #Search orders by required date delivered returns list of orders required to be delivered that day
    def search_required_date(self, required_date):
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            val = ""
            for char in required_date:
                if str.isalnum(char) or char == "/" or char == "-":
                    val = val + char
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][4][:10] == val:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND WITH A REQUIRED DATE OF: " + required_date
    
    #Search orders by when they were shipped returns list of orders shipped on that date
    def search_shipped_date(self, shipped_date):
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            val = ""
            for char in shipped_date:
                if str.isalnum(char) or char == "/" or char == "-":
                    val = val + char
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][5][:10] == val:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE SHIPPED ON: " + shipped_date
    
    #Search orders by way of shipment returns list of orders shipped the same way
    def search_ship_via(self, ship_via):
        #assuming 1 is ground, 2 is ship, 3 is plane
        orders = []
        val = ""
        for char in ship_via:
            if str.isalnum(char):
                val = val + char
        ship_via = val.lower()
        trans = val.upper()
        try:
            if ship_via == "ship":
                ship_via = "1"
            if ship_via == "plane":
                ship_via = "2"
            if ship_via == "truck":
                ship_via = "3"

            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][6] == ship_via:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE SHIPPED BY: " + trans
    
    #Search orders by customer name returns all orders ordered from that customer
    def search_ship_name(self, ship_name):
        orders = []
        #List to keep track of order ids... returns order ids
        ship_name = ship_name.upper()
        try:
            val = ""
            for char in ship_name:
                if str.isalnum(char) or char == " ":
                    val = val + char
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][8].upper() == val.upper():
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE SHIPPED TO SOMEONE WITH NAME: " + ship_name
    