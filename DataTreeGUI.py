
#Revision #1 Alexander Wade 2/18/2023
#Begin Alexander Wade 2/18/2023
import tkinter as tk


def data(choice):
    """Function that recieves user input and executes the users commands """
    search="empty"
    if choice>3:
        search=entry1.get()
    print(search)


def Close():
    """Function that closes newWindow"""
    newWindow.destroy()

def new_window(choice):
    
    """opens a new window based on what button the user presses."""
    global newWindow
    newWindow=tk.Toplevel(window)
    newWindow.title("Datatree")
    newWindow.geometry("400x400")
    newWindow.configure(bg='light green')
    global entry1
    Button_name=["add data","delete the last entry","to add a random entry","search by order ID",
                 "to search by customer ID","to search by employee ID",
                 "to search by order date","to search by order ID","to search by required date",
                 "to search by shipped date","to search by ship via","to search by ship name",
                 "to search by ship address","to search by ship city"]

    #boolean statment that takes user input based on the button pressed
    if choice==1:
        l1=tk.Label(master=newWindow, text="Click the button below "+Button_name[choice-1],
                    bg="light green",fg="brown",font=("Arial", 12))
        b1 =tk.Button(master=newWindow,text="Add",bg="brown",fg='white',
                      font="ariel",width="10",command=lambda: data(choice))
        l1.place(x=55,y=10)
        b1.place(x=120,y=35)
    elif choice==2:
       
        l1=tk.Label(master=newWindow, text="Click the button below "+Button_name[choice-1],
                    bg="light green",fg="brown",font=("Arial", 12))
        b1 =tk.Button(master=newWindow,text="Delete",bg="brown",fg='white',
                    font="ariel",width="10",command=lambda: data(choice))
        l1.place(x=55,y=10)
        b1.place(x=120,y=35)

    else: 
        l1=tk.Label(master=newWindow, text="Enter text below "+Button_name[choice-1],
                    bg="light green",fg="brown",font=("Arial", 12))
        entry1=tk.Entry(master=newWindow, width=52)  
        b1 =tk.Button(master=newWindow,text="Search",bg="brown",fg='white',font="ariel",
                      width="10",command=lambda: data(choice))
        l1.place(x=50,y=10)
        entry1.place(x=30,y=35)
        b1.place(x=120,y=60)
    #Button created to exit window
    exit=tk.Button(master=newWindow,text="Close",bg="brown",fg='white',font=("Arial", 9),
                   width="10",command=Close)
    exit.place(x=140,y=372)

    
    
    
    
    
    
    

    
    
  


#window setup
window = tk.Tk()
window.title("Datatree",)
window.geometry("800x400")
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
button1 = tk.Button(master=window,text="Add Data",bg="brown",fg='white',
                    font="ariel",width="18",command=lambda: new_window(1))
button2 = tk.Button(master=window,text="Delete Last Entry",bg="brown",
                    fg='white',font="ariel",width="18",command=lambda: new_window(2))
button3 = tk.Button(master=window,text="Add Random Entry",bg="brown",
                    fg='white',font="ariel",width="18",command=lambda: new_window(3))
button4 = tk.Button(master=window,text="Search Order Id",bg="brown"
                    ,fg='white',font="ariel",width="18",command=lambda: new_window(4))
button5 = tk.Button(master=window,text="Search Customer Id",
                    bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(5))
button6 = tk.Button(master=window,text="Search Employee Id",
                    bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(6))
button7 = tk.Button(master=window,text="Sarch Order Date",
                    bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(7))
button8 = tk.Button(master=window,text="Search Order Id",
                    bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(8))
button9 = tk.Button(master=window,text="Search Required Date",
                    bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(9))
button10 = tk.Button(master=window,text="Search Shipped Date",
                     bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(10))
button11 = tk.Button(master=window,text="Search Ship Via",
                     bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(11))
button12 = tk.Button(master=window,text="Search Ship Name",
                     bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(12))
button13 = tk.Button(master=window,text="Search Ship Address",
                     bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(13))
button14= tk.Button(master=window,text="Search Ship City",
                    bg="brown",fg='white',font="ariel",width="18",command=lambda: new_window(14))

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
button13.place(x=400,y=600)
button14.place(x=750,y=600)


tk.mainloop()
#revision #1 2/18/2023
#End Alexander Wade 2/18/2023
