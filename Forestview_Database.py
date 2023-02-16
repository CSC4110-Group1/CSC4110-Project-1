
#Revision #1-20 IanSiple 2/XX/2023
#Revision #X AliChowdhury 2/16/2023
from Forestview_DataEntry import Forestview_DataEntry
from Forestview_ReadOrdersCsv import Forestview_OpenOrdersCsv
from Forestview_ReadOrderDetailsCsv import Forestview_OpenOrderDetailsCsv
import random
"""
Combines order and user oder data
"""
import string
class Forestview_Database:
    #Method to create data structure
    def __init__(self):
        """Creates the initial data structure"""
        #Empty dictionary to store data based off of order id as key
        self.forestview_datastructure = {}
        #Store data from csv files into variables
        self.order_data = Forestview_OpenOrdersCsv().return_orders()
        self.order_detail_data = Forestview_OpenOrderDetailsCsv().return_order_details()
        #Create data structure
        self.create_data_structure()
        #Variable to keep track of last order... mainly used to add order to database
        self.LAST_ORDER = Forestview_DataEntry(self.forestview_datastructure[self.order_data[-1][0]])
    
    #Creates database
    def create_data_structure(self):
        """Iterates through the data structure"""
        for i in range(len(self.order_data)):
            self.forestview_datastructure[self.order_data[i][0]] = self.order_data[i] + self.order_detail_data[i]

    #Deletes last order from database
    def delete_last_entry(self):
        """Deletes last entry of the file"""
        self.forestview_datastructure.pop()
    
    
    #Method to generate random order and order details and then adds it to dictionary
    def add_random_entry(self):
        """Perpetually creates and returns a random user"""
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
        ship_address = self.LAST_ORDER.get_ship_address()
        ship_city = self.LAST_ORDER.get_ship_city()
        ship_region = self.LAST_ORDER.get_ship_region()
        ship_postal = self.LAST_ORDER.get_ship_postal_code()
        ship_country = self.LAST_ORDER.get_ship_country()

        product_id = self.LAST_ORDER.get_product_id()
        unit_price = self.LAST_ORDER.get_unit_price()
        quantity = self.LAST_ORDER.get_quantity()
        discount = self.LAST_ORDER.get_discount()
        #Create new random order
        order = [order_id, customer_id, employee_id, order_date, required_date, shipped_date,
                 ship_via, freight, ship_name, ship_address, ship_city, ship_region, ship_postal,
                 ship_country, product_id, unit_price, quantity, discount]
        self.LAST_ORDER = Forestview_DataEntry(order)
        self.forestview_datastructure[order_id] = self.LAST_ORDER
        #Returns newly added order
        return "Adding Randomly Generated Data... \n" + "Randomly Generated data is:\n" + str(self.LAST_ORDER.return_data_entry())

    #Reverses data structure
    def reverse_data(self):
        """Reverses data structure"""
        self.forestview_datastructure = dict(reversed(list(self.forestview_datastructure.items())))
    #================================================================================================================================#
    #===================================================Search engine================================================================#
    #================================================================================================================================#
    
    #Search by order id returns order data as list
    def search_order_id(self, order_id):
        """Searches through the data structure and returns order data as a list"""
        try:
            return str(self.forestview_datastructure[order_id])
        except KeyError:
            return "ERROR... NO ORDERS WERE FOUND WITH THAT ORDER ID"
        
    #Search orders by customer id returns all orders from that customer
    def search_customer_id(self, customer_id):
        """Searches through the data structure and returns all orders from that specific customer"""
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][1] == customer_id.upper():
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND WITH THE CUSTOMER ID: " + customer_id
    
    #Search orders by employee id returns all orders completed by that employee
    def search_employee_id(self, employee_id):
        """Searches the data structure and returns all orders completed by that employee"""
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][2] == employee_id:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND WITH THE EMPLOYEE ID: " + employee_id

    #Search orders by order date returns orders ordered on that date
    def search_order_date(self, order_date):
        """Searches orders by order date and returns orders that were ordered on that date"""
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][3][:10] == order_date:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND THAT WERE ORDERED ON: " + order_date
    
    #Search orders by required date delivered returns list of orders required to be delivered that day
    def search_required_date(self, required_date):
        """Searches orders that are promised on the specific date"""
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][4][:10] == required_date:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE FOUND WITH A REQUIRED DATE OF: " + required_date
    
    #Search orders by when they were shipped returns list of orders shipped on that date
    def search_shipped_date(self, shipped_date):
        """Searches orders via shipped date, returns list of orders shipped on that date"""
        #List to keep track of order ids... returns order ids
        orders = []
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][5][:10] == shipped_date:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE SHIPPED ON: " + shipped_date
    
    #Search orders by way of shipment returns list of orders shipped the same way
    def search_ship_via(self, ship_via):
        """Searches orders via shipping method and returns list of orders via that method"""
        #assuming 1 is ground, 2 is ship, 3 is plane
        orders = []
        ship_via = ship_via.lower()
        trans = ship_via.upper()
        try:
            if ship_via == "ship":
                ship_via = "1"
            if ship_via == "plane":
                ship_via = "2"
            if ship_via == "ground":
                ship_via = "3"
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
        """Searches orders by customer name and returns all orders from that customer"""
        orders = []
        #List to keep track of order ids... returns order ids
        ship_name = ship_name.upper()
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][8].upper() == ship_name:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE SHIPPED TO SOMEONE WITH NAME: " + ship_name
    
    #NEEDS WORKKKKK
    def search_ship_address(self, ship_address):
        """Searches the data structure for the shipping address and returns orders made to that address"""
        orders = []
        #List to keep track of order ids... returns order ids
        ship_address = ship_address.upper()
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][9].upper() == ship_address:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE SHIPPED TO ADDRESS AT: " + ship_address
        
    def search_ship_city(self, ship_city):
        """Searches the data structure for the shipping address and returns orders made to that city"""
        orders = []
        #List to keep track of order ids... returns order ids
        ship_city = ship_city.upper()
        try:
            for keys in self.forestview_datastructure:
                if self.forestview_datastructure[keys][10].upper() == ship_city:
                    orders.append(keys)
            orders[0]
            return str(orders)
        except IndexError:
            return "ERROR... NO ORDERS WERE SHIPPED TO: " + ship_city

#Revision Number # 2/2X/2023
##End Ali Chowdhury 2/16/2023