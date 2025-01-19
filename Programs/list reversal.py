#list reversal
def reverse_list(lst):
  return lst[::-1]

item_S = input("Enter the items of list (space-separated): ")
lst = item_S.split()
reversed_lst = reverse_list(lst) 
print("Reversed list:", reversed_lst)