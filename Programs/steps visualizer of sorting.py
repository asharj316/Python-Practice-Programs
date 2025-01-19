#displaying steps of sorting
def BubbleSortVisualization(l):
    step=1
    print("The initial list is:",l)
    for i in range(len(l)-1):
        for j in range(0,len(l)-1-i):
            if  l[j]>l[j+1]:
                 l[j], l[j+1] = l[j+1], l[j]              
                
        print("step",step,":",l)
        step+=1
    return print("The sorted list is:",l)

l=[12,3,1,56,4,7,7,88,79,890,0,-1,5]
listswapping(l)
