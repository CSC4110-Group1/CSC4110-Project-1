#Revision #1 Ian Siple 2/02/2023
#Begin Ian Siple 3/02/2023
import csv

class Forestview_OpenOrdersCsv:

    def __init__(self):
        self.orders = []

    def create_list(self): 
        try:
            file = open("orders.csv", "r")
            for line in file:
                line = line.rstrip()
                string1 = line.split(',')
                self.orders.append(string1)
        finally:
            file.close()
                
    def return_orders(self):
        try:
            self.create_list()
            return self.orders
        except:
            print("'orders.csv' did not open correctly.")
            return 1

#revision 1 3/02/2023
#End Ian Siple 3/02/2023
#Group 1/Project #1