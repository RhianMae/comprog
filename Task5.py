#User Management System

users = []

while True:
    print("\n=== USER MANAGEMENT SYSTEM ===")
    print("1. Show User")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        if not users:
            print("No users found.")
        else:
            print("Users list: ")
            for i, user in enumerate(users):
                
                print(f"{i + 1}. {user}")

    elif choice == "2":
        name = input("Enter new user name: ")
        users.append(name)
        print("User added.")

    elif choice == "3":
        try:
            index = int(input("Enter user index to update: "))
            if 0 <= index < len(users):
                new_name = input("Enter new name: ")
                users[index] = new_name
                print("User updated.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        try:
            index = int(input("Enter user index to delete: "))
            if 0 <= index < len(users):
                users.pop(index)
                print("User deleted.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Exiting system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
