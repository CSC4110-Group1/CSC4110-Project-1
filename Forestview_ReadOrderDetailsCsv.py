import csv

class Forestview_OpenOrderDetailsCsv:
    def __init__(self):
        self.order_details = []

    def create_list(self): 
        try:
            file = open("order-details.csv", "r")
            for line in file:
                line = line.rstrip()
                string1 = line.split(',')
                self.order_details.append(string1)
        finally:
            file.close()
                
    def return_order_details(self):
        try:
            self.create_list()
            return self.order_details
        except:
            print("'order-details.csv' did not open correctly")
            return 1

