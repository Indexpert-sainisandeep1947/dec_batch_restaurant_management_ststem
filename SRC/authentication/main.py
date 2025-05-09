from user_auth import UserAuthentication
from sign_in import SignIn

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

