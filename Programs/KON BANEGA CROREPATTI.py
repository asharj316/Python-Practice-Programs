reward1=100000
reward2=50000
reward3=10000000
totalreward=0
print("\tWelcome to Kon banangay Corerpati!!")
print("First Guest se shuru kartay hai.To ap ka naam sir?:",end="")
name=input().capitalize()
print("To Mr.",name ,"apkay samnay screen pe sawwal aingay r apnay sahi jawab batana hai.")
#1
print("To phela sawwal hai 1 lakh rupay ka!")
print("Ques1:What is cover song of game NFSUG2?")
answers_=["set fire to the rain","kill yourself iii","1000 blunts","riders on the storm"]
print("The choices are following","1.",answers_[0],"2.",answers_[1],"3.",answers_[2],"4.",answers_[3])
print("To apko kiya lagta hai konsa jawab sahi hai?:",end="")
choice_=input().lower()
if choice_==answers_[3] or choice_=="4":
    print("You are Right")
    print("You won 1 lakh rupees")
    while choice_==answers_[3] or choice_=="4":
        totalreward1=reward1
        print("Your total winning is:",totalreward1)
        break
    
elif choice_==answers_[0] or choice_==answers_[1] or choice_==answers_[2] or choice_=="1" or choice_=="2" or choice_=="3" :
    print("You are Wrong")
    print("You lost 1 lac rupees")
    while choice_==answers_[0] or choice_==answers_[1] or choice_==answers_[2] or choice_=="1" or choice_=="2" or choice_=="3":
        totalreward1=reward1-reward1
        print("Your total winning is:",totalreward1)
        break
    
else:
    print("Wrong spelling maybe try to type correct spelling <3")
#2
print("To dusra sawwal hai 50k rupay ka hai!")
print("Ques2:Who is diddy?")
answers_=["Biggie's killer","Tupac's killer","Naas's friend","Bachabaaz"]
print("The choices are following","1.",answers_[0],"2.",answers_[1],"3.",answers_[2],"4.",answers_[3])
print("To apko kiya lagta hai konsa jawab sahi hai?:",end="")
choice_=input().capitalize()
    
if choice_==answers_[1] or choice_=="2":
    print("You are Right")
    print("You won 50k rupees")
    while choice_==answers_[1] or choice_=="2":
        totalreward2=totalreward1+reward2
        print("Your total winning is:",totalreward2)
        break
    
elif choice_==answers_[0] or choice_==answers_[2] or choice_==answers_[3] or choice_=="1" or choice_=="3" or choice_=="4" :
    print("You are Wrong")
    print("You lost 50k rupees")
    while choice_==answers_[0] or choice_==answers_[2] or choice_==answers_[3] or choice_=="1" or choice_=="3" or choice_=="4" :
        totalreward2=totalreward1
        print("Your total winning is:",totalreward2)
        break
    
else:
    print("Wrong spelling maybe try to type correct spelling <3")
    
#3
print("To teesra sawwal hai 50k rupay ka hai!")
print("Ques3:Who is ghari chor?")
answers_=["Imran khan","Nawaz sharif","Altaf bhai","Zardari"]
print("The choices are following","1.",answers_[0],"2.",answers_[1],"3.",answers_[2],"4.",answers_[3])
print("To apko kiya lagta hai konsa jawab sahi hai?:",end="")
choice_=input().capitalize()
    
if choice_==answers_[0] or choice_=="1":
    print("You are Right")
    print("You won 1 crore rupees")
    while choice_==answers_[0] or choice_=="1":
        totalreward3=totalreward2+reward3
        print("Your total winning is:",totalreward)
        break
    
elif choice_==answers_[1] or choice_==answers_[2] or choice_==answers_[3] or choice_=="2" or choice_=="3" or choice_=="4" :
    print("You are Wrong")
    print("You lost 1 crore rupees")
    while choice_==answers_[1] or choice_==answers_[2] or choice_==answers_[3] or choice_=="2" or choice_=="3" or choice_=="4" :
        totalreward3=totalreward2
        print("Your total winning is:",totalreward3)
        break
else:
    print("Wrong spelling maybe try to type correct spelling <3")
    
Totalreward=totalreward3
print("You won total of :", Totalreward)   

