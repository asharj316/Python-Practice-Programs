#tuple duplicate remover
def tdr(t1,t2):
    t3=t1+t2
    l1=list(t3)
    l1.sort()
    for item in l1:
        if l1.count(item) >1:
            print("duplicate value:",item)  
    s1=set(l1)
    print(s1)

t1=(21,3,1,31,1,1,3)
t2=(3,43,1,3,5,6,869,64)
tdr(t1,t2)

            
