def listswapping(l):
    l2=[]
    for i in range(len(l)-1):
        for j in range(0,len(l)-1-i):
            if  l[j]<l[j+1]:
                 l[j+1], l[j] = l[j], l[j+1]
    return l

l=["Ashar","CJ","Milcolu","Milky","Shahsahab","Jaffery","Machar","Jheela","Spongebob"]
print(listswapping(l))


