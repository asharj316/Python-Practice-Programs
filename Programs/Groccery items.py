g_items=[]
while True:
    try:
        choice=input("add any item in your grocerry list (press 'c' to clear the list or press 'e' to end the loop and press 'a' to add a item):")
        if choice not in ['a','c','e']:
            raise ValueError("Wrong input please (press 'c' to clear the list or press 'e' to end the loop and press 'a' to add a item)")
    except ValueError as x:
            print("Wrong input please (press 'c' to clear the list or press 'e' to end the loop and press 'a' to add a item)")
            continue
    if choice=='a':
            i_choice=input("Enter the item u want to add:")
            g_items.append(i_choice)
    elif choice=='c':
            g_items.clear()
    elif choice=='e':
            print(g_items)
    break

   
        
    
    
