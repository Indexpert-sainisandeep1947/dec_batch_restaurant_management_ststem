import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from menu_management import MenuManager
from auth_login import login

def admin_panel(menu):
    while True:
        print("\nAdmin Panel")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Menu")

        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            menu.add_item()
        elif choice == "2":
            menu.update_item()
        elif choice == "3":
            menu.delete_item()
        elif choice == "4":
            menu.view_menu()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

def staff_panel(menu):
    print("\nStaff Menu")
    menu.view_menu()

def main():
    user_role = login()
    if not user_role:
        return

    menu = MenuManager()

    if user_role == "admin":
        admin_panel(menu)
    elif user_role == "staff":
        staff_panel(menu)
    else:
        print("Invalid role found.")

if __name__ == "__main__":
    main()


