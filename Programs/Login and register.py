# Define user credentials
user1 = ["email=zhengpou@gmail.com", "password=cjinthehood", "username=muhammad.ashar"]
user2 = ["email=abbax.momi@gmail.com", "password=Cjinthehood316716", "username=muhammad.abbas"]

# Parse user credentials into dictionaries
users = [
    {"email": "zhengpou@gmail.com", "password": "cjinthehood", "username": "muhammad.ashar"},
    {"email": "abbax.momi@gmail.com", "password": "Cjinthehood316716", "username": "muhammad.abbas"}
]

print("\tWelcome Mofo")

# Ask user for choice
choice = input("If you already have an account press ('L') and if you want to register press ('R'): ").upper()

if choice == "L":
    while True:
        # Ask user for email or username
        email_or_username = input("Enter your email (press 'u' to continue with username): ")

        if email_or_username == 'u':
            # Ask user for username
            username_ = input("Enter your username: ")
            # Check if username exists
            for user in users:
                if user["username"] == username_:
                    # Ask user for password
                    password_ = input("Enter your password: ")
                    # Check if password is correct
                    if user["password"] == password_:
                        print(f"Welcome back {username_}")
                    else:
                        print("Incorrect credentials")
                    break
            else:
                print("Invalid username")
        else:
            # Check if email exists
            for user in users:
                if user["email"] == email_or_username:
                    # Ask user for password
                    password_ = input("Enter your password: ")
                    # Check if password is correct
                    if user["password"] == password_:
                        print(f"Welcome back {user['username']}")
                    else:
                        print("Incorrect credentials")
                    break
            else:
                print("No account with such credentials")
                


if choice=='R':
    
    while True:
        
        email :
        
        
            






