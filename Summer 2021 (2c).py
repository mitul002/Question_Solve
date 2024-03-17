user_name = ["healthMin", "reliefMin", "FoodMin"]
password = ["123health", "456 relief", "789food"]

admin = {'imadmin': '123'}


# Convert user_name and password lists into pairs using zip
user_info = dict(zip(user_name, password))


def user_login():
    username = input("Enter username: ")
    passwd = input("Enter password: ")
    if username in user_info and user_info[username] == passwd:
        print("User Login Successful\n")
    else:
        print("Invalid Username or Password\n")


def admin_login():
    username = input("Enter admin username: ")
    passwd = input("Enter admin password: ")
    if username in admin and admin[username] == passwd:
        print("Admin Login Successful\n")
        return True
    else:
        print("Invalid Admin Username or Password\n")
        return False


def add_user():
    if admin_login():
        new_username = input("Enter new username: ")
        new_password = input("Enter new password: ")
        user_info[new_username] = new_password
        print("New user added successfully\n")
    else:
        print("Only admin can add new users\n")


def print_user():
    if admin_login():
        print("Existing Users:")
        print(user_info)
        print('\n')
    else:
        print("Only admin can see this details.")


while True:
    print("Options:")
    print("1.User login")
    print("2.Admin login")
    print("3.Add User")
    print("4.Print existing users")
    print("5.Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        user_login()
    elif choice == '2':
        admin_login()
    elif choice == '3':
        add_user()
    elif choice == '4':
        print_user()
    elif choice == '5':
        print("Thank you..\n")
        break
    else:
        print("Invalid choice.Please enter again\n")