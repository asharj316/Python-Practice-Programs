def sort2Dlistbycolumn(l1,nl_index):
    for i in range(len(l1) - 1):  
        for j in range(len(l1) - 1 - i):  
            
            if l1[j][nl_index] > l1[j + 1][nl_index]:
                
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
    return l1


l1 = [[1, "Alice"], [3, "Bob"], [2, "Charlie"], [4, "Ashar"], [5, "Anas"], [6, "Qasim"]]


print(sort2Dlistbycolumn(l1, 0))


print(sort2Dlistbycolumn(l1, 1))
