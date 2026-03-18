Total_cash = int(input("Input Total amount of cash: "))
food = []
transportation = []
bills_utilities = []
entertainment = []
others = []


def food_func():
    a = 0
    for x in range(len(food)):
        a += 1
        print(f"{a}. {food[x]}")
        
        
def transportation_func():
    b = 0
    for y in range(len(transportation)):
        b += 1
        print(f"{b}. {transportation[y]}")
        
        
def bills_utilities_func():
    d = 0
    for z in range(len(bills_utilities)):
        d += 1
        print(f"{d}. {bills_utilities[z]}")
        
    
def entertainment_func():
    e = 0
    for v in range(len(entertainment)):
        e += 1
        print(f"{e}. {entertainment[v]}")
        
        
def others_func():
    f = 0
    for u in range(len(others)):
        f += 1 
        print(f"{f}. {others[u]}")
        
        
def all_func():
    print(" --- Food --- ")
    food_func()
                
    print(" --- Transportation --- ")
    transportation_func()
                
    print(" --- Bills/Utilities --- ")
    bills_utilities_func()
                
    print(" --- Entertainment --- ")
    entertainment_func()
                
    print(" --- Others --- ")
    others_func()
                
    
while True:
    print("\n --- MENU ---")
    print("[1] Add Money")
    print("[2] Deduct Expense")
    print("[3] Classify Expense")
    print("[4] See list")
    print("[5] Exit")
    
    choice = int(input("What would you like to do? \n"))
    
    if choice == 1:
        addAmount = int(input("Enter amount to add: "))
        Total_cash += addAmount
        print(f"New Balance; {Total_cash} \n")
        continue
    if choice == 2:
        expense = int(input("Enter amount of expense: "))
        Total_cash -= expense
        print(f"New Balance: {Total_cash} \n")
        continue
    if choice == 3:
        itemName = str(input("Enter what you bought: "))
        
        print("\n --- MENU ---")
        print("[1] Food")
        print("[2] Transportation")
        print("[3] Bills/Utilities")
        print("[4] Entertainment")
        print("[5] Others \n")
        
        while True:
            choice2 = input("Enter a classfication: ")
            if choice2 == '1':
                food.append(itemName)
                break
            elif choice2 == '2':
                transportation.append(itemName)
                break
            elif choice2 == '3':
                bills_utilities.append(itemName)
                break
            elif choice2 == '4':
                entertainment.append(itemName)
                break
            elif choice2 == '5':
                others.append(itemName)
                break
            else:
                print("Invalid input!")
                

            print("\n[1] Food")
            print("[2] Transportation")
            print("[3] Bills/Utilities")
            print("[4] Entertainment")
            print("[5] Others")
            print("[6] All of the above")
            choice4 = input("Enter the classification") 
             
            if choice4 == '1':
                print(" --- Food --- ")
                food_func()
                continue
                
            elif choice4 == '2':
                print(" --- Transportation --- ")
                transportation_func()
                continue
                
            elif choice4 == '3':
                print(" --- Bills/Utilities --- ")
                bills_utilities_func()
                continue
                
            elif choice4 == '4':
                print(" --- Entertainment --- ")
                entertainment_func()
                continue
                
            elif choice4 == '5':
                print(" --- Others --- ")
                others_func()
                continue 
            
            elif choice4 == '6':
                print(" --- Food --- ")
                food_func()
                
                print(" --- Transportation --- ")
                transportation_func()
                
                print(" --- Bills/Utilities --- ")
                bills_utilities_func()
                
                print(" --- Entertainment --- ")
                entertainment_func()
                
                print(" --- Others --- ")
                others_func()
                
                continue
                
            else:
                print("Invalid input!") 
                continue  
                
                
           
        continue
    
    if choice == 4:
            print("\n[1] Food")
            print("[2] Transportation")
            print("[3] Bills/Utilities")
            print("[4] Entertainment")
            print("[5] Others")
            print("[6] All of the above")
            choice4 = input("Enter the classification") 
             
            if choice4 == '1':
                print(" --- Food --- ")
                food_func()
                continue
                
            elif choice4 == '2':
                print(" --- Transportation --- ")
                transportation_func()
                continue
                
            elif choice4 == '3':
                print(" --- Bills/Utilities --- ")
                bills_utilities_func()
                continue
                
            elif choice4 == '4':
                print(" --- Entertainment --- ")
                entertainment_func()
                continue
                
            elif choice4 == '5':
                print(" --- Others --- ")
                others_func()
                continue 
            
            elif choice4 == '6':
                all_func()
                continue
        
        
        
        
    if choice == 5:
        
        print(f"\n Keep track, the total you ended up with is {Total_cash}")
        print("\n And the updated list are the following: \n")
        
        print("Food".ljust(10, " "))
        food_func()
        
        print("\nTransportation".ljust(14, " "))
        transportation_func()
        
        print("\nBills/Utilities".ljust(14, " "))
        bills_utilities_func()
        
        print("\nEntertainment".ljust(9, " "))
        entertainment_func()
        
        print("\nOthers".ljust(10, " "))
        others_func()
        break

print("Thank you for using our app")