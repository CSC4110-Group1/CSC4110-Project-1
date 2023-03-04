#Revision #1 Alexander Wade 2/02/2023
#Begin Alexander Wade 3/02/2023
from Forestview_Database import Forestview_Database
import pickle
import tkinter as tk
import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("green")  

class App(customtkinter.CTk):
    WIDTH = 1300
    HEIGHT = 800
    DARK_COLOR = '#90ee90'
    LIGHT_COLOR = '#233923'
    def __init__(self, database):
            super().__init__()

            #window setup            
            self.title("Datatree",)
            self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

            
            # load image 
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
            self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "datatree_Logo1.png")), size = (100, 100))


            # frames
            self.nav_frame = customtkinter.CTkFrame(self, width = 200, corner_radius=0,
                                                    fg_color=("#c9c9c9","#212121"))
            self.nav_frame.place(relheight = 2,
                                 x = 0, y = 0,
                                 anchor = 'w')
            
            
            # version
            self.nav_frame_vers = customtkinter.CTkLabel(self.nav_frame, 
                                                         text='v3.3.23', 
                                                         text_color= (App.LIGHT_COLOR, App.DARK_COLOR))
            self.nav_frame_vers.place(relx = 0.4, rely = 0.93)

            # switch mode
            self.switch = customtkinter.CTkSwitch(self.nav_frame, text='', command=self.change_mode)
            self.switch.place(relx = 0.4, rely = 0.95)
            self.switch.select()

            # logo
            self.nav_frame_logo = customtkinter.CTkLabel(self.nav_frame, text='', image=self.logo_image)
            self.nav_frame_logo.place(x = 50, y = 20, rely = 0.5)
            self.nav_frame_label = customtkinter.CTkLabel(self.nav_frame, text='DataTree', 
                                                          text_color = (App.LIGHT_COLOR, App.DARK_COLOR), font = customtkinter.CTkFont(size=22, weight="bold"))
            self.nav_frame_label.place(x = 50, y = 125, rely = 0.5)

            # create home frame
            self.home_frame = customtkinter.CTkFrame(self, corner_radius=0)
            self.home_frame.grid_columnconfigure(0, weight=1)
            self.home_frame.place(x = 200, relwidth=1, relheight=1)

            
            # label 1
            self.label1 = customtkinter.CTkLabel(self.home_frame,text="Datatree Interactive Database", 
                                                 text_color= (App.LIGHT_COLOR, App.DARK_COLOR),
                                                 font=("Arial", 30))
            self.label1.place(relx=0.45, rely=0.05, anchor='center')

            # label 2
            self.label2 = customtkinter.CTkLabel(self.home_frame,
                                                        text="Make your data like tree and leaf the rest to us!!!",
                                                        text_color= (App.LIGHT_COLOR, App.DARK_COLOR),
                                                        font=("Arial", 12))
            self.label2.place(relx=0.45, rely = 0.1, anchor='center')

            # bar
            self.bar = customtkinter.CTkProgressBar(self.home_frame, 
                                                    width=500, 
                                                    height=2,
                                                    progress_color='#426d42')
            self.bar.place(relx=0.45, rely = 0.15, anchor='center')
            self.bar.set(1)

            # label 3
            self.label3 = customtkinter.CTkLabel(self.home_frame,
                                                 text="Please choose from the following options below:",
                                                 text_color= (App.LIGHT_COLOR, App.DARK_COLOR),
                                                 font=("Arial", 12))
            self.label3.place(relx=0.45, rely = 0.20, anchor='center')


            # buttons
            self.button1 = customtkinter.CTkButton(self.home_frame,
                                                   text="Add Data",
                                                   command=lambda: self.new_window(1, self, database))
            self.button1.place(relx=0.3, rely = 0.28, anchor='e')
            self.button2 = customtkinter.CTkButton(self.home_frame,
                                                   text="Delete Last Entry",
                                                   command=lambda: self.new_window(2, self, database))
            self.button2.place(relx=0.45, rely = 0.28, anchor='center')
            self.button3 = customtkinter.CTkButton(self.home_frame,
                                                   text="Add Random Entry",
                                                   command=lambda: self.new_window(3, self, database))
            self.button3.place(relx=0.6, rely = 0.28, anchor='w')
            self.button4 = customtkinter.CTkButton(self.home_frame,
                                                   text="Search Order ID",
                                                   command=lambda: self.new_window(4, self, database))
            self.button4.place(relx=0.3, rely = 0.40, anchor='e')
            self.button5 = customtkinter.CTkButton(self.home_frame,
                                                   text="Search Customer ID",
                                                   command=lambda: self.new_window(5, self, database))
            self.button5.place(relx=0.45, rely = 0.40, anchor='center')
            self.button6 = customtkinter.CTkButton(self.home_frame,
                                                   text="Search Employee ID",
                                                   command=lambda: self.new_window(6, self, database))
            self.button6.place(relx=0.6, rely = 0.40, anchor='w')
            self.button7 = customtkinter.CTkButton(self.home_frame,
                                                   text="Search Order Date",
                                                   command=lambda: self.new_window(7, self, database))
            self.button7.place(relx=0.3, rely = 0.52, anchor='e')
            self.button8 = customtkinter.CTkButton(self.home_frame,
                                                   text="Search Required Date",
                                                   command=lambda: self.new_window(8, self, database))
            self.button8.place(relx=0.45, rely = 0.52, anchor='center')
            self.button9 = customtkinter.CTkButton(self.home_frame,
                                                   text="Search Shipped Date",
                                                   command=lambda: self.new_window(9, self, database))
            self.button9.place(relx=0.6, rely = 0.52, anchor='w')
            self.button10 = customtkinter.CTkButton(self.home_frame,
                                                    text="Search Ship Via",
                                                   command=lambda: self.new_window(10, self, database))
            self.button10.place(relx=0.3, rely = 0.64, anchor='e')
            self.button11 = customtkinter.CTkButton(self.home_frame,
                                                    text="Search Ship Name",
                                                   command=lambda: self.new_window(11, self, database))
            self.button11.place(relx=0.6, rely = 0.64, anchor='w')

    def new_window(self, choice, window, database):
    
        """opens a new window based on what button the user presses.""" 
        global newWindow       
        newWindow = customtkinter.CTkToplevel(self)
        newWindow.attributes("-topmost", True)
        newWindow.title("Datatree")
        newWindow.geometry("450x450")
        
        global entry1
        Button_name=["to add a data entry:",
                     "to delete the last entry:",
                     "to add a random entry:",
                     "search by order ID:",
                     "to search by customer ID:",
                     "to search by employee ID:",
                     "to search by order date:",
                     "to search by required date:",
                     "to search by shipped date:",
                     "to search by ship via:",
                     "to search by ship name:"]
        
        #boolean statment that takes user input based on the button pressed
        if choice==2:
            l1=customtkinter.CTkLabel(master=newWindow, 
                                      text="Click the button below "+Button_name[choice-1],
                                      text_color=(App.LIGHT_COLOR, App.DARK_COLOR),
                                      font=("Arial", 12))
            b1 =customtkinter.CTkButton(master=newWindow,
                                        text="Delete",
                                        text_color=(App.LIGHT_COLOR, App.DARK_COLOR),
                                        command=lambda: self.data(choice, window, database))
            l1.place(relx=0.5,rely=0.05,anchor="center")
            b1.place(relx=0.5,rely=0.13,anchor="center")
        elif choice==3:
        
            l1=customtkinter.CTkLabel(master=newWindow, 
                                      text="Click the button below "+Button_name[choice-1],
                                      text_color=(App.LIGHT_COLOR, App.DARK_COLOR),
                                      font=("Arial", 12))
            b1 =customtkinter.CTkButton(master=newWindow,
                                        text="Add",
                                        text_color=(App.LIGHT_COLOR, App.DARK_COLOR),
                                        command=lambda: self.data(choice, window, database))
            l1.place(relx=0.5,rely=0.05,anchor="center")
            b1.place(relx=0.5,rely=0.13,anchor="center")

        else:
            if choice==1:
                t="Add"
            else:
                t="Search"
            l1=customtkinter.CTkLabel(master=newWindow, 
                                      text="Enter text below " + Button_name[choice-1],
                                      text_color=(App.LIGHT_COLOR, App.DARK_COLOR),
                                      font=("Arial", 12))
            l1.place(relx=0.5,rely=0.05,anchor="center")
            entry1=customtkinter.CTkEntry(master=newWindow)
            entry1.place(relwidth=0.8, relx=0.5,rely=0.12,anchor="center")  
            b1 =customtkinter.CTkButton(master=newWindow,
                                        text=t,
                                        command=lambda: self.data(choice, window, database))
            b1.place(relx=0.5,rely=0.25,anchor="center")
        #Button created to close window
        close_button = customtkinter.CTkButton(master=newWindow,text="Close",command=self.Close)
        close_button.place(relx=0.5,rely=0.90,anchor="center")

        
    def data(self, choice, window, database):
        """Function that recieves user input and executes the users commands """
        search="empty"
        if choice>3 or choice == 1:
            search=entry1.get()
        value = ""
        if choice == 1:
                database.add_order_to_database(search)
                value = "Adding order to end of database...\n Order added was: " + database.return_last_order()
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
                with open("ForestviewApp.pkl", "wb") as F:
                    pickle.dump(database, F)
        if choice == 2:
                value = "Deleting last order...\n Order Deleted was: " + database.delete_last_entry()
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.3,anchor="center")
                with open("ForestviewApp.pkl", "wb") as F:
                    pickle.dump(database, F)
        if choice == 3:
                value = "Adding random order to database..." + "\n Order being added is: " + database.  add_random_entry()
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.3,anchor="center")
                with open("ForestviewApp.pkl", "wb") as F:
                    pickle.dump(database, F)
        if choice == 4:
                value = "Searching for Order ID: " + search + "\n Results: " + database.search_order_id(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
        if choice == 5:
                value = "Searching for Orders with Customer ID: " + search.upper() + "\n Results: " + database. search_customer_id(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
        if choice == 6:
                value = "Searching for Orders filled by ID of Employee : " + search.upper() + "\n Results: " +  database.search_employee_id(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
        if choice == 7:
                value = "Searching for Orders ordered on the date : " + search.upper() + "\n Results: " +   database.search_order_date(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
        if choice == 8:
                value = "Searching for Orders needed by date : " + search.upper() + "\n Results: " + database.  search_required_date(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
        if choice == 9:
                value = "Searching for Orders shipped on date : " + search.upper() + "\n Results: " + database. search_shipped_date(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
        if choice == 10:
                value = "Searching for Orders Shipped via : " + search.upper() + "\n Results: " + database. search_ship_via(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")
        if choice == 11:
                value = "Searching for Orders shipped to : " + search.upper() + "\n Results: " + database.  search_ship_name(search)
                outputLabel = customtkinter.CTkLabel(newWindow, text = value, wraplength=400)
                outputLabel.place(relx=0.5,rely=0.5,anchor="center")  
        print(value)
   
    def change_mode(self):
        if self.switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")
            

    def Close(self):
        """Function that closes newWindow"""
        newWindow.destroy()

    def Exit(self):
        """Function that closes newWindow"""
        newWindow.destroy()
        self.destroy()
if __name__ == "__main__":
    database = Forestview_Database()
    with open("ForestviewApp.pkl", "wb") as F:
        pickle.dump(database, F)
    app = App(database)
    app.mainloop()

#revision 3 3/02/2023
#End Alexander Wade 3/02/2023
