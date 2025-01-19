#negative number remover
def negremover(l1):
    for i in range(len(l1)):
        if l1[i] < 0:
            n_no=l1[i]
            print("the negative number is:",n_no)

l1=[-9,-10,-5,-1,1,5,6,7]
negremover(l1)