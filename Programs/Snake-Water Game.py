import random

total = 0
choices = ("snake", "water", "gun")

print("Welcome to Snake, Water, Gun Game!")
print("Enter 'quit' to exit the game.")

while True:
    try:
        u_choice = input("\nEnter your choice (Snake/Water/Gun): ").lower()
        
        if u_choice == "quit":
            print("Thanks for playing! Your final score is:", total)
            break
        
        if u_choice not in choices:
            raise ValueError("Please enter a valid choice (Snake/Water/Gun)!")
        
        c_choice = random.choice(choices)
        print(f"You chose: {u_choice}, I chose: {c_choice}")
        
        if u_choice == c_choice:
            print("It's a tie!")
        elif (u_choice == "water" and c_choice == "snake") or \
             (u_choice == "gun" and c_choice == "water") or \
             (u_choice == "snake" and c_choice == "gun"):
            print("Haha, you lose!")
            total -= 1
        else:
            print("You won!")
            total += 1
        
        print(f"Your current score: {total}")
    
    except ValueError as e:
        print(e)