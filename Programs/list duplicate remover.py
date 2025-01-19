def remove_duplicates(lst):
  result = []
  for item in lst:
    if lst.count(item) == 1:
      result.append(item)
    if lst.count(item)>1:
        print("the duplicate element is :",item)
  return result

user_input = input("Enter the values of list (space-separated): ")
l1 = user_input.split()
unique_list = remove_duplicates(l1)
print("List with duplicates removed:", unique_list)
        
    

    
