#bubble sorting list swapping
def listswapping(l):
    l2=[]
    for i in range(len(l)-1):
        for j in range(0,len(l)-1-i):
            if  l[j]>l[j+1]:
                 temp=l[j] 
                 l[j]=l[j+1] 
                 l[j+1]=temp 
    return l

l=[12,3,1,56,4,7,7,88,79,890,0,-1,5]
print(listswapping(l))

