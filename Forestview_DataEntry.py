class Forestview_DataEntry:

    def __init__(self, dataEntry):
        try:
            self.dataEntry = dataEntry
        except:
            print("Invalid Data Entry... ERROR RETRIEVING DATA")

    def reverse_data_entry(self):
        try:
            self.dataEntry.reverse()
        except:
            return "Invalid Data Entry... ERROR REVERSING DATA ENTRY"
    def return_data_entry(self):
        try:
            return self.dataEntry
        except:
            return "Invalid Data Entry... ERROR RETURNING DATA ENTRY"
    def print_data_entry(self):
        print(self.dataEntry)
    
    def get_order_id(self):
        try:
            return self.dataEntry[0]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING ORDER ID"
    def get_customer_id(self):
        try:
            return self.dataEntry[1]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING CUSTOMER ID"
    def get_employee_id(self):
        try:
            return self.dataEntry[2]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING EMPLOYEE ID"
    def get_order_date(self):
        try:
            return self.dataEntry[3]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING ORDER DATE"
    def get_required_date(self):
        try:
            return self.dataEntry[4]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING REQUIRED DATE"
    def get_shipped_date(self):
        try:
            return self.dataEntry[5]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIPPED DATE"
    def get_ship_via(self):
        try:
            ship_via = self.dataEntry[6]
            if ship_via == '1':
                return "Truck"
            if ship_via == '2':
                return "Plane"
            if ship_via == '3':
                return "UPS"
            else:
                return "Cargo Ship"
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIP VIA"
    def get_freight(self):
        try:
            return self.dataEntry[7]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING FREIGHT"
    def get_ship_name(self):
        try:
            return self.dataEntry[8]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIP NAME"
    