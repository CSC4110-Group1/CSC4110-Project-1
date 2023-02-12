from Forestview_Database import Forestview_Database
from tkinter import*

def main():
    #Create main window 
    root = Tk()
    root.title("Forestview Orders Database")
    root.geometry("600x600")
    #create label
    title_label = Label(root, text = "Forestview Orders Database", font=("Helvetica", 18))
    title_label.grid(row = 0, column = 0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()