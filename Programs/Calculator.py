#MUHAMMAD ASHAR(Calculator)
print("\t!!!Welcome to the Calculator!!!")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
operation=(input("Choose your operation('+''-''/''*'):"))
if operation =='+':
  print(a+b)
elif operation == '-':
  print(a-b)
elif operation =='/':
  print(a/b)
elif operation == "*":
  print(a*b)
else:
  print("Invalid Input")