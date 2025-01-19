trans={"date":["10-Jan-2024","3-Feb-2024"],
        "amount":[25000,10000],
       "category":["Supply Expense","Treat Expense"],
       "descripation":["Maths ki supply me paise lag gai","doston ko treat dedi"]
    }

while True:
    
    choice=input("Do u wish to add more transactions (press any key to add and 'e' to end):")
    
    if choice!='e':
        date=input("Enter the date:")
        trans["date"].append(date)
        amount=int(input("Enter the amount u spent:"))
        trans["amount"].append(amount)
        category=input("Enter the category of Expense:")
        trans["category"].append(category)
        descripation=input("Enter the descripation:")
        trans["descripation"].append(descripation)
    else:
        break     

with open("E:\expenses.txt","w+") as f:
    
    for i in range(len(trans["date"])):
        
        f.write(f"Date: {trans['date'][i]}\n")
        f.write("-" * 100 + "\n")
        f.write(f"{i+1}. Amount: {trans['amount'][i]}\n")
        f.write(f"{i+1}. Category: {trans['category'][i]}\n")
        f.write(f"{i+1}. Description: {trans['descripation'][i]}\n")
        f.write("-" * 100 + "\n")
        
print("Data Written successfully :)")

choice_2=input("Do u wish to see the total amount of money u spent u junkie!(press any key to view and 'n' to not view):")
if choice_2!="n":
    total=0
    for i in trans["amount"]:
        total+=i
    print(total)
        


