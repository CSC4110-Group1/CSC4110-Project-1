#Revision #1 Alexander Wade 2/18/2023
#Begin Alexander Wade 2/18/2023
from Forestview_Database import Forestview_Database
import tkinter as tk

def data(choice, window, database):
    """Function that recieves user input and executes the users commands """
    search="empty"
    if choice>3:
        search=entry1.get()
    value = ""
    match(choice):
        case 1:
            value = "Adding order to end of database...\n Order added was: " + 0
            outputLabel = tk.Label(newWindow, text = value, bg = 'white', fg = 'black', wraplength=400)
            outputLabel.place(x=150,y=100)
        case 2:
            value = "Deleting last order...\n Order Deleted was: " + database.delete_last_entry()
            outputLabel = tk.Label(newWindow, text = value, bg = 'white', fg = 'black', wraplength=400)
            outputLabel.place(x=150,y=100)
        case 3:
            value = "Adding random order to database..." + "\n Order being added is: " + database.add_random_entry()
            outputLabel = tk.Label(newWindow, text = value, bg = 'white', fg = 'black', wraplength=400)
            outputLabel.place(x=150,y=100)
        case 4:
            value = "Searching for Order ID: " + search + "\n Results: " + database.search_order_id(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black', wraplength=400)
            outputLabel.place(x=150, y=100)
        case 5:
            value = "Searching for Orders with Customer ID: " + search.upper() + "\n Results: " + database.search_customer_id(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black',wraplength=400)
            outputLabel.place(x=100, y=100)
        case 6:
            value = "Searching for Orders filled by ID of Employee : " + search.upper() + "\n Results: " + database.search_employee_id(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black', wraplength=400)
            outputLabel.place(x=100, y=100)
        case 7:
            value = "Searching for Orders ordered on the date : " + search.upper() + "\n Results: " + database.search_order_date(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black', wraplength=400)
            outputLabel.place(x=100, y=100)
        case 9:
            value = "Searching for Orders needed by date : " + search.upper() + "\n Results: " + database.search_required_date(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black', wraplength=400)
            outputLabel.place(x=100, y=100)
        case 10:
            value = "Searching for Orders shipped on date : " + search.upper() + "\n Results: " + database.search_shipped_date(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black', wraplength=400)
            outputLabel.place(x=100, y=100)
        case 11:
            value = "Searching for Orders Shipped via : " + search.upper() + "\n Results: " + database.search_ship_via(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black', wraplength=400)
            outputLabel.place(x=100, y=100)
        case 12:
            value = "Searching for Orders shipped to : " + search.upper() + "\n Results: " + database.search_ship_name(search)
            outputLabel = tk.Label(newWindow, text= value, bg='white', fg='black', wraplength=400)
            outputLabel.place(x=100, y=100)   
    print(value)

def Close():
    """Function that closes newWindow"""
    newWindow.destroy()

def new_window(choice, window, database):
    
    """opens a new window based on what button the user presses."""
    global newWindow
    newWindow=tk.Toplevel(window)
    newWindow.title("Datatree")
    newWindow.geometry("400x400")
    newWindow.configure(bg='light green')
    global entry1
    Button_name=["to add a data entry:","to delete the last entry:","to add a random entry:","search by order ID:",
                 "to search by customer ID:","to search by employee ID:",
                 "to search by order date:","to search by order ID:","to search by required date:",
                 "to search by shipped date:","to search by ship via:","to search by ship name:",
                 ]

    #boolean statment that takes user input based on the button pressed
    if choice==2:
        l1=tk.Label(master=newWindow, text="Click the button below "+Button_name[choice-1],
                    bg="light green",fg="brown",font=("Arial", 12))
        b1 =tk.Button(master=newWindow,text="Delete",bg="brown",fg='white',
                      font="ariel",width="10",command=lambda: data(choice, window, database))
        l1.place(x=30,y=10)
        b1.place(x=120,y=35)
    elif choice==3:
       
        l1=tk.Label(master=newWindow, text="Click the button below "+Button_name[choice-1],
                    bg="light green",fg="black",font=("Arial", 12))
        b1 =tk.Button(master=newWindow,text="Add",bg="brown",fg='black',
                    font="ariel",width="10",command=lambda: data(choice, window, database))
        l1.place(x=30,y=10)
        b1.place(x=120,y=35)

    else:
        if choice==1:
            t="Add"
        else:
            t="Search"
        l1=tk.Label(master=newWindow, text="Enter text below "+Button_name[choice-1],
                    bg="light green",fg="brown",font=("Arial", 12))
        entry1=tk.Entry(master=newWindow, width=52)  
        b1 =tk.Button(master=newWindow,text=t,bg="brown",fg='black',font="ariel",
                      width="10",command=lambda: data(choice, window, database))
        l1.place(x=50,y=10)
        entry1.place(x=30,y=35)
        b1.place(x=120,y=60)
    #Button created to exit window
    exit=tk.Button(master=newWindow,text="Close",bg="brown",fg='black',font=("Arial", 9),
                   width="10",command=Close)
    exit.place(x=140,y=372)

def main(database):
    #window setup
    window = tk.Tk()
    window.title("Datatree",)
    window.geometry("1200x800")
    window.configure(bg='light green')
    #loads image into logo variable
    logo=tk.PhotoImage(file='datatree_Logo1.png')



    #labels
    label1 = tk.Label(master=window,text="Datatree Interactive Database",fg='brown',bg='light green',font=("Arial", 25))
    label2 = tk.Label(master=window,text="Make your data like tree and leaf the rest to us!!!",
                    fg='brown',bg='light green',font=("Arial", 9))
    label3 = tk.Label(master=window,text="Please choose from the following options bellow:",
                    fg='brown',bg='light green',font=("Arial", 12))
    label4=tk.Label(master=window, image=logo,bg='light green')

    #button Creation 
    button1 = tk.Button(master=window,text="Add Data",bg="brown",fg='black',
                        font="ariel",width="18",command=lambda: new_window(1, window, database))
    button2 = tk.Button(master=window,text="Delete Last Entry",bg="brown",
                        fg='black',font="ariel",width="18",command=lambda: new_window(2, window, database))
    button3 = tk.Button(master=window,text="Add Random Entry",bg="brown",
                        fg='black',font="ariel",width="18",command=lambda: new_window(3, window, database))
    button4 = tk.Button(master=window,text="Search Order Id",bg="brown"
                        ,fg='black',font="ariel",width="18",command=lambda: new_window(4, window, database))
    button5 = tk.Button(master=window,text="Search Customer Id",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(5, window,database))
    button6 = tk.Button(master=window,text="Search Employee Id",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(6, window, database))
    button7 = tk.Button(master=window,text="Sarch Order Date",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(7, window, database))
    button8 = tk.Button(master=window,text="Search Order Id",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(8, window, database))
    button9 = tk.Button(master=window,text="Search Required Date",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(9, window, database))
    button10 = tk.Button(master=window,text="Search Shipped Date",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(10, window, database))
    button11 = tk.Button(master=window,text="Search Ship Via",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(11, window. database))
    button12 = tk.Button(master=window,text="Search Ship Name",
                        bg="brown",fg='black',font="ariel",width="18",command=lambda: new_window(12, window, database))



    #output to the screen
    label4.place(x=0,y=0)
    label1.place(x=450,y=0)
    label2.place(x=550,y=50)
    label3.place(x=500, y=160)
    button1.place(x=350,y=200)
    button2.place(x=600,y=200)
    button3.place(x=850,y=200)
    button4.place(x=350,y=300)
    button5.place(x=600,y=300)
    button6.place(x=850,y=300)
    button7.place(x=350,y=400)
    button8.place(x=600,y=400)
    button9.place(x=850,y=400)
    button10.place(x=350,y=500)
    button11.place(x=600,y=500)
    button12.place(x=850,y=500)



    tk.mainloop()

if __name__ == "__main__":
    database = Forestview_Database()
    main(database)

#revision #1 2/18/2023
#End Alexander Wade 2/18/2023