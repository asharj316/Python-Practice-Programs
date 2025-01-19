vegetables=[]
fruits=[]
frozenitems=[]

while True:
    choice=input("Which item did you bought vegetables,fruits,or frozen items (press 'e' to end this junk):")
    
    choice=choice.lower()
    
    a_choices=["vegetables","fruits","frozen items","e"]
    
    if choice not in a_choices:
        
        print("Please give the input from the given options as asked")
        
    elif choice == 'e':
        break
    
    else:
        
        if choice=="vegetables":
            choice_2=input("daalo jo sabzi daalni hai:)")
            vegetables.append(choice_2)
            
        elif choice=="fruits":
            choice_2=input("daalo jo fruit daalna hai:)")
            fruits.append(choice_2)
            
        elif choice=="frozen items":
            choice_2=input("daalo jo frozen item daalna hai:)")
            frozenitems.append(choice_2)


    
    for i in range(len(vegetables)):
        for j in range(len(vegetables)-1):
            if vegetables[j]>vegetables[j+1]:
                vegetables[j],vegetables[j+1] = vegetables[j+1],vegetables[j]
                
    for k in range(len(fruits)):
        for l in range(len(fruits)-1):
            if fruits[l]>fruits[l+1]:
                fruits[l],fruits[l+1] = fruits[l+1],fruits[l]
                
    for m in range(len(frozenitems)):
        for n in range(len(frozenitems)-1):
            if frozenitems[m] > frozenitems[m+1]:
                frozenitems[m],frozenitems[m+1] = frozenitems[m+1],frozenitems[m]
                
    while True:
        
        choice_3=input("Which item of list u wish to c (v for vegetables,f for fruits,i for frozen items):")
        
        if choice_3=="v":
            print(vegetables)
            break
        
        elif choice_3=="f":
            print(fruits)
            break
        
        elif choice_3=="i":
            print(frozenitems)
            break
        
        else:
            print("paizan please sahi cheez daldo")
                
        
    