temp=[34,5,90,45,56]
t_n=list(map(lambda x: (x*9/5)+32,temp))
print(t_n)

no=[2,13,12,321,3,21,31,3,1,50,4523,6,56,5,86,9,66,56,47,5,10]
n_n=list(filter(lambda x: x%2==0,no))
print(n_n)

from functools import reduce
lno=[5,34,534,53,45,34,534,5,3,53,76,568,67,9,86,89,9]
l_n=reduce(lambda x,y: x+y,lno)
print(l_n)



            
            
        
    