#student score tracker
def average(l1):
    total=len(l1)
    s_total=sum(l1)
    avg=s_total/total
    print("avg is:",avg)
def mxmn(l1):
    mx=l1[0]
    for i in range(len(l1)):
        if l1[i]>mx:
            mx=l1[i]
    print("maximum value is:",mx)
    mn=l1[0]
    for i in range(len(l1)):
        if l1[i]<mn:
            mn=l1[i]
    print("minimum value is:",mn)
        
l1=[1,2,3,4,5,10,12]
mxmn(l1)
average(l1)

        
        
        
        
        
        
        
        
        
        
        
        