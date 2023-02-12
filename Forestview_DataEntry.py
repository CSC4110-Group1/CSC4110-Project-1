
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
            return self.dataEntry[6]
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
    def get_ship_address(self):
        try:
            return self.dataEntry[9]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIPPING ADDRESS"
    def get_ship_city(self):
        try:
            return self.dataEntry[10]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIPPING CITY"
    def get_ship_region(self):
        try:
            return self.dataEntry[11]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIPPING REGION"
    def get_ship_postal_code(self):
        try:
            return self.dataEntry[12]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIPPING POSTAL CODE"
    def get_ship_country(self):
        try:
            return self.dataEntry[13]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING SHIPPING COUNTRY"
    def get_product_id(self):
        try:
            return self.dataEntry[14]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING PRODUCT ID"
    def get_unit_price(self):
        try:
            return self.dataEntry[15]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING UNIT PRICE"
    def get_quantity(self):
        try:
            return self.dataEntry[16]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING QUANTITY ORDERED"
    def get_discount(self):
        try:
            return self.dataEntry[17]
        except:
            return "Invalid Data Entry... ERROR RETRIEVING DISCOUNT"