 #Combining the features into application
from features import search_by_date_linear,sort_amount,add_data,delete_data_date,sum_amount

#List of dictonary in variable transactions
transactions = [
 {"date": "2024-08-01", "amount": 50, "description": "Groceries"},
  {"date": "2024-08-02", "amount": 20, "description": "Bus fare"},
  {"date": "2024-08-03", "amount": 300, "description": "Electricity bill"},
  {"date": "2024-08-04", "amount": 200, "description": "New shoes"},
  ]
flag=True
while flag:
  print("Expense Tracker App:\n 1.Adding\n 2.Searching\n 3.Sorting\n 4.Deleting\n 5.display\n 6.Stop Application\n 7.Sum Amount")
  choice=int(input("Choose feature: "))
  if choice==1:
    print("-"*50)
    print("adding data")
    print("-"*50)
    print(add_data(transactions))
    print("-"*50)
  elif choice==2:
    print("-"*50)
    print("Searching Data")
    print("-"*50)
    print(search_by_date_linear(transactions))
    print("-"*50)
  elif choice==3:
    print("-"*50)
    print("Sorting data")
    print("-"*50)
    print(sort_amount(transactions))
    print("-"*50)
  elif choice==4:
    print("-"*50)
    print("deleting data")
    print("-"*50)
    print(delete_data_date(transactions))
    print("-"*50)
  elif choice==5:
    print("-"*50)
    print(transactions)
    print("-"*50)
  elif choice==6:
    print("-"*50)
    print("Application Stopped")
    flag=False
    print("-"*50)
  elif choice==7:
    print("_"*50)
    print("sum of amount of given year")
    print(sum_amount(transactions))
    print("_"*50)
  else:
    print("-"*50)
    print("Please enter correct feature")
