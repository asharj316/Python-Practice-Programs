def sorting(l1):
    k=int(input("how many largest number do you want:"))
    l2=[]
    for i in range(len(l1)-1):
        for j in range(len(l1)-1-i):
            if l1[j]>l1[j+1]:
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp
    l2.append(l1[-k:])
    print(f"The largest {k} number are:",l2)
    return l1
    

l1=["Ashar","CJ","Milcolu","Milky","Shahsahab","Jaffery","Machar","Jheela","Spongebob"]
print(sorting(l1))


    