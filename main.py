from SRC.authentication.user_auth import UserAuthentication
from SRC.authentication.sign_in import SignIn
from SRC.menumanagement.menu_management import MenuManager
from SRC.menumanagement.admin_auth import admin_login

def login_menu(auth):
    print("\nlogin system")
    print("1 - press for admin login")
    print("2 - press for staff login")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        auth.admin_login()
    elif choice == "2":
        auth.staff_login()
    else:
        print("Invalid choice in login menu!")

def main_menu():
    auth = UserAuthentication()
    sign_in = SignIn()

    while True:
        print("\nrestaurant management system")
        print("1 - press for login")
        print("2 - press for sign in")
        print("3 - exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            login_menu(auth)
        elif choice == "2":
            sign_in.sign_in()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()


def main():
    manager = MenuManager()
    if not admin_login():
        print("Access Denied.")
        return

    actions = {
        '1': manager.view_menu,
        '2': manager.add_item,
        '3': manager.update_item,
        '4': manager.delete_item,
        '5': exit
    }

    while True:
        print("\n1. View Menu\n2. Add Item\n3. Update Item\n4. Delete Item\n5. Exit")
        choice = input("Choice: ").strip()
        if choice == '1':
            manager.view_menu()
        elif choice == '2':
            manager.add_item()
        elif choice == '3':
            manager.update_item()
        elif choice == '4':
            manager.delete_item()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()  
