def Toppi(choice,apna_adda):
        while True:
         if choice in apna_adda:
             print("On scene hai")
         elif choice not in apna_adda:
             print("Jana hai jani kaam hai samajha kar!")
         else:
             print("Chala ja bsdk")
            
  
choice=input("han lala kidher bethna hai:")
apna_adda=("Quetta Hotel")
Toppi(choice,apna_adda)