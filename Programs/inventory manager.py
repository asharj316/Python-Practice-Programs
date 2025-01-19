
inventory_data = {
    "rx 580": 30,
    "rx 570": 25,
    "gtx 1660 super": 30,
    "gtx 1650 super": 25
}


def manage_inventory():
    choice = input(
        "Do you wish to view the inventory? Press 'v' to view.\n"
        "If you want to update the inventory, press 'u'.\n"
        "If you want to clear the inventory, press 'c'.\n: "
    )

    if choice == "v":
        print("Current Inventory:")
        for product, quantity in inventory_data.items():
            print(f"{product}: {quantity} units")

    elif choice == "u":
        choice_2 = input("Which GPU's stock do you want to update? ")

        if choice_2 in inventory_data:
            print(f"The current quantity of {choice_2} is: {inventory_data[choice_2]}")
            choice_3 = input("Do you want to add ('a') the quantity or subtract ('s') the quantity? ")

            if choice_3 == 'a':
                choice4 = int(input("How many units of the GPU do you want to add? "))
                inventory_data.update({choice_2: inventory_data[choice_2] + choice4})
                print(f"Updated quantity of {choice_2}: {inventory_data[choice_2]}")

            elif choice_3 == 's':
                choice4 = int(input("How many units of the GPU do you want to subtract? "))
                if choice4 <= inventory_data[choice_2]:  # Ensure we don't subtract more than available
                    inventory_data.update({choice_2: inventory_data[choice_2] - choice4})
                    print(f"Updated quantity of {choice_2}: {inventory_data[choice_2]}")
                else:
                    print("Error: Cannot subtract more than the available quantity.")
            else:
                print("Invalid choice. Please enter 'a' or 's'.")
        else:
            print("Error: Product not found in inventory.")

    elif choice == "c":
        confirm = input("Are you sure you want to clear the entire inventory? (yes/no): ")
        if confirm.lower() == "yes":
            inventory_data.clear()
            print("The inventory has been cleared.")
        else:
            print("Clear operation canceled.")

    else:
        print("Invalid input. Please enter 'v', 'u', or 'c'.")


manage_inventory()
