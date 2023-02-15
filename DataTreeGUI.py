import tkinter as tk


#window setup
window = tk.Tk()
window.title("Datatree",)
window.geometry("800x400")
window.configure(bg='light green')
#loads image into logo variable
logo=tk.PhotoImage(file='datatree_Logo.png')

#labels
label1 = tk.Label(master=window,text="Datatree Interactive Database",fg='brown',bg='light green',font=("Arial", 25))
label2 = tk.Label(master=window,text="Make your data like tree and leaf the rest to us!!!",
                  fg='brown',bg='light green',font=("Arial", 9))
label3 = tk.Label(master=window,text="Please choose from the following options bellow:",
                  fg='brown',bg='light green',font=("Arial", 12))
label4=tk.Label(master=window, image=logo)

#button Creation 
button1 = tk.Button(master=window,text="Add Data",bg="brown",fg='white',font="ariel",width="18")
button2 = tk.Button(master=window,text="Delete Last Entry",bg="brown",fg='white',font="ariel",width="18")
button3 = tk.Button(master=window,text="Add Random Entry",bg="brown",fg='white',font="ariel",width="18")
button4 = tk.Button(master=window,text="Search Order Id",bg="brown",fg='white',font="ariel",width="18")
button5 = tk.Button(master=window,text="Search Customer Id",bg="brown",fg='white',font="ariel",width="18")
button6 = tk.Button(master=window,text="Search Employee Id",bg="brown",fg='white',font="ariel",width="18")
button7 = tk.Button(master=window,text="Sarch Order Date",bg="brown",fg='white',font="ariel",width="18")
button8 = tk.Button(master=window,text="Search Order Id",bg="brown",fg='white',font="ariel",width="18")
button9 = tk.Button(master=window,text="Search Required Date",bg="brown",fg='white',font="ariel",width="18")
button10 = tk.Button(master=window,text="Search Shipped Date",bg="brown",fg='white',font="ariel",width="18")
button11 = tk.Button(master=window,text="Search Ship Via",bg="brown",fg='white',font="ariel",width="18")
button12 = tk.Button(master=window,text="Search Ship Name",bg="brown",fg='white',font="ariel",width="18")
button13 = tk.Button(master=window,text="Search Ship Address",bg="brown",fg='white',font="ariel",width="18")
button14= tk.Button(master=window,text="Search Ship City",bg="brown",fg='white',font="ariel",width="18")

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
