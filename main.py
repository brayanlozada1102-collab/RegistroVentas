# Importing functions to be used
from salesregister import sales_register , show_summary

#Initial configuration and system startup
print("Welcome to the sales registration system \n -----------------------")
start = True
daily_revenue = 0
daily_sales = []

#Product data collection and processing cycle
while start :

  name_product = input("Add the name of the product you are going to sell: ")
  
  try:
    quantity = int(input("Add the quantity of product you are going to sell: "))
    unit_value = float(input("Add the unit price of the product you are going to sell: "))
  except ValueError:
      print("Error try again")
      continue
      

  sales_register(name_product,quantity,unit_value,daily_sales)
 
  daily_revenue = daily_revenue + (quantity*unit_value)
  try:
       switch = input("Do you want to continue recording sales? Yes/No: ").lower()
       if switch != "yes":
           start = False
  except ValueError:
      print("Error try again")
      
#Show the total sales revenue for the day
print("\nSummary of the day \n-----------------------")
show_summary(daily_sales)
print(f"The total amount collected that day was: ${daily_revenue}")
        