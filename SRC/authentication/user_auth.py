import uuid
import json
import os

class UserAuthentication:
    def __init__(self):
        
        self.folder = "src/database"
        self.path = self.folder + "/user_data.json"

        
        os.makedirs(self.folder, exist_ok=True)

        
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                self.user_data = json.load(file)
        else:
            self.user_data = []


    def generate_user_data(self, role):
        user = {}

        
        while True:
            name = input("Please enter your name: ")
            if name.replace(" ", "").isalpha():
                user["name"] = name
                break
            else:
                print("Name should contain only letters and spaces!")

        
        while True:
            address = input("Please enter your address: ")
            if address.replace(" ", "").isalnum():
                user["address"] = address
                break
            else:
                print("Invalid address! Use only letters, numbers, and spaces.")

        
        while True:
            contact = input("Please enter your contact number: ")
            if len(contact) == 10 and contact.isdigit():
        
                if "0000" in contact or "1111" in contact or "2222" in contact or \
                 "3333" in contact or "4444" in contact or "5555" in contact or \
                "6666" in contact or "7777" in contact or "8888" in contact or \
                "9999" in contact:
                    print("invalid number! please tyr agin.")
                else:
                    user["contact"] = contact
                    break
            else:
                print("Please enter a 10-digit number only.")

        
        while True:
            email = input("Please enter your email: ")
            if "@" in email and "." in email:
                user["email"] = email
                break
            else:
                print("Invalid email! Please try again ")


        
        user["role"] = role
        user["id"] = f"{role}_{user['name'].split()[0]}_{uuid.uuid4().hex[:6]}"

        
        self.user_data.append(user)
        print(f"{role.capitalize()} account created successfully!\n")
        self.save_to_json()

    def admin_sign_up(self):
        print("\n*** Admin Sign-Up ***")
        self.generate_user_data("admin")

    def staff_sign_up(self):
        while True:
            print("\n*** Staff Sign-Up ***")
            self.generate_user_data("staff")
            another = input("Create another staff? (yes/no): ").lower()
            if another != "yes":
                break

    def save_to_json(self):
        with open(self.path, "w") as f:
            json.dump(self.user_data, f, indent=4)
        print("Data saved successfully to JSON.")