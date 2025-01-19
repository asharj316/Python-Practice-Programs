print("\tWelcome to Contact Management System made by CJ :)")

try:

    contacts = {}

    with open('E:\contacts.txt', 'r') as file:

        for line in file:

            data = line.strip().split(',')

            name = data[0]

            email = data[1]

            phone = data[2]

            contacts[name] = [{"email": email}, {"phno": phone}]

except FileNotFoundError:

    contacts = {"ashar":[{"email":"zheng.pou@gmail.com"},{"phno":"03353246270"}]}


while True:

    choice = input("Hn ballu no.save karna hai update karna hai ya naya daalna hai ya delete karna hia janeman ('s' to save , 'u' to update ,'d' to delete ,'x' to end the loop baby!): ")

    if choice == 'x':

        break


    if choice == 'd':

        username = input("jaan kiska no. delete karna hai?(nahi karna to 'n' daba do): ")

        if username != 'n':

            if username not in contacts:

                print("chanda ye naam se koi no. nhi hai :(")

            if username in contacts:

                del contacts[username]

                with open('E:\contacts.txt', 'w') as file:

                    for name in contacts:

                        file.write(f"{name},{contacts[name][0]['email']},{contacts[name][1]['phno']}\n")

                print(f"{username}'s is deleted :)")

    
    elif choice == 's':

        n_no = input("hn jiger kiska no. save karwana hai?(agar nhi karna to 'n' dabao dasti): ")

        if n_no != 'n':

            if len(n_no) != 11:

                print("11 digits ka number hota hai L!")

            elif len(n_no) == 11:

                name = input("Naam daalo kiska number add karna hai!?: ")

                if name in contacts:

                    print("ye banda phelay hi hai kaliya!")

                elif name not in contacts:

                    email = input("Email daal iski: ")

                    contacts[name] = [{"email": email}, {"phno": n_no}]

                    with open('E:\contacts.txt', 'w') as file:

                        for name in contacts:

                            file.write(f"{name},{contacts[name][0]['email']},{contacts[name][1]['phno']}\n")

                    print(f"{name}'s number and email have been added successfully!")


    elif choice == 'u':

        user = input("kis banday ka update karna hai?: ")

        if user not in contacts:

            print("user hai hi nhi ")

        elif user in contacts:

            user_2 = input("'e' dabao email update karnay ke liye r 'n' number ke liye or agr kuch nhi karna to 'x' dabao: ")

            if user_2 == 'x':

                continue

            elif user_2 == 'e':

                email_1 = input("Enter the new email: ")

                contacts[user][0]["email"] = email_1

                with open('E:\contacts.txt', 'w') as file:

                    for name in contacts:

                        file.write(f"{name},{contacts[name][0]['email']},{contacts[name][1]['phno']}\n")

            elif user_2 == 'n':

                phno_1 = input("Enter the new number: ")

                if len(phno_1) != 11:

                    print("phir wohi b 11 digits ka number daalday!")

                elif len(phno_1) == 11:

                    contacts[user][1]["phno"] = phno_1

                    with open('E:\contacts.txt', 'w') as file:

                        for name in contacts:

                            file.write(f"{name},{contacts[name][0]['email']},{contacts[name][1]['phno']}\n")


else:

                print("1 kaam hai wo to sahi kar sahi input de")
