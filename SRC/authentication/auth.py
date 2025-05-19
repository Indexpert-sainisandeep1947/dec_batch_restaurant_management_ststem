from SRC.authentication.user_auth import UserAuthentication
from SRC.authentication.sign_in import SignIn  

def login_menu(auth):
    print("\nSign Up System")
    auth.staff_sign_up()  # You can modify this if you want to offer admin/staff choice

def main_menu():
    auth = UserAuthentication()
    sign_in = SignIn()  # Make sure SignIn is a class with a method called sign_in()

    while True:
        print("\nRestaurant Management System")
        print("1 - Press for Sign Up")
        print("2 - Press for Login")
        print("3 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            login_menu(auth)
        elif choice == "2":
            sign_in.sign_in()  # This should internally check if user is admin or staff
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
