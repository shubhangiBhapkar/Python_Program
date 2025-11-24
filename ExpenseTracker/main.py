expenses = []

print("Welcome to Expense Tracker :")

print("========MENU========")

while True :
    print("[1] Add Expense")
    print("[2] View All Expenses")
    print("[3] Total Expenses")
    print("[4] Exit")

    choice = int(input("Enter your Choice : "))

    # 1.Add expense

    if choice == 1:
        date = input("Enter a date :")
        category = input("which type of category of expense :")
        description = input("more details :")
        amount = float(input("Enter the amount :"))

        expense =[
            {
                "date" :date,
                "category":category,
                "description" :description,
                "amount":amount
            }
        ]

        expenses.append(expenses)
        print("\nExpenses Added Successfully!!")
    
    # 2. VIEW ALL EXPENSES

    elif choice == 2:
        if(len(expenses)==0):
            print("No expenses ")
        else :
            print("=========Your Expenses=========")
            count =1
            for eachExpense in expenses :
                # print(f" expense No.{count} : {eachExpense['date']}, {eachExpense['category']}, {eachExpense['description']},{eachExpense['amount']}")
                print(f" Expense No.{count} :")
                print(f" Date : {eachExpense['date']}")
                print(f" Category : {eachExpense['category']}")
                print(f" Description : {eachExpense['description']}")
                print(f" Amount : {eachExpense['amount']}")
                count+=1

    # 3.view Tatal spending
    elif choice == 3:
        print("========Total spending upto today=======")
        total = 0
        for expense in expenses :
            total += expense['amount'] 
        print(f"Total : {total} Rs.")
        
    # 4.Exit
    elif choice == 4:
        print("thank you! Come soon..")
        break

    else :
        print("Invalid Choice")



