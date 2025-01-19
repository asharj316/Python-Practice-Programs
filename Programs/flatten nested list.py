#Flatten nested list 
def fnl(l1):
    l2=[]
    for sublist in l1:
        for item in sublist:
            l2.append(item)
    print(l2) 
            
        
l1=[[1,2,3,4],
    [5,6,7,8]]
fnl(l1)