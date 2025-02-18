def subject():
    sub=int(input("Enter no. of subjects:"))
    marksheet(sub)
    
def marksheet(sub):
    total=0
    for i in range(1,sub+1):
        print("Enter the marks",i,":",end="")
        marks=int(input())
        total+=marks
    percentage(total,sub)
        
def percentage(total,sub):
    per=total/(sub*100)*100
    print("percentage is:",per)

subject()


    
    