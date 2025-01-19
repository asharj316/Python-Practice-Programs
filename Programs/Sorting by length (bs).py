def sortingbylength(l1):
    try:
        k = int(input("How many largest elements do you want? "))
        if k <= 0:
            raise ValueError("Wrong input. Please enter a positive number.")
        elif k > len(l1):
            raise ValueError("Wrong input. Please enter a number smaller than the length of the list.")
    except ValueError as e:
        print(f"Error: {e}")
        
    finally:
   
        l1_sorted = sorted(l1, key=len)  
        
        print(f"Sorted List by Length: {l1_sorted}")
        
        
        largest_elements = l1_sorted[-k:]
        print(f"The {k} largest strings by length: {largest_elements}")
        
        return l1_sorted  


l1 = ["Ashar", "CJ", "Milcolu", "Milky", "Shahsahab", "Jaffery", "Machar", "Jheela", "Spongebob"]

print(sortingbylength(l1))
