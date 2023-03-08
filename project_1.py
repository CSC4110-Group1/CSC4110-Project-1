import csv
import random

"""User inputs a value and this function finds and prints customer information"""
def search_customers(customer_Data):
    print("search function prototype")

"""Searches and deletes customer information"""
def delete_customers(customer_Data):

    print("delete function prototype")
    search_customers(customer_Data)
    return customer_Data

"""Function that user inputs values to be inserted in the customer data array"""
def input_customers():
    new_entry=[]
    print("input function prototype")
    
    return new_entry




"""Main Function"""
def main():
     pass
     customer_Data=[]
     #Reads from csv file 
     with open('us-500.csv','r') as read:
          r=csv.reader(read)
    
          for i in r:
            #append file list to a list
            customer_Data.append(i)
     
         
     for i in range(10):
         print(customer_Data[i])




if __name__=="__main__":
  main()
