from Forestview_Database import Forestview_Database
from Forestview_ReadOrderDetailsCsv import Forestview_OpenOrderDetailsCsv
from Forestview_ReadOrdersCsv import Forestview_OpenOrdersCsv
from Forestview_DataEntry import Forestview_DataEntry

#File to test database side of application
orders = Forestview_OpenOrdersCsv().return_orders()
order_details = Forestview_OpenOrderDetailsCsv().return_order_details()

data = Forestview_Database()

print(data.search_ship_city("Münster"))


