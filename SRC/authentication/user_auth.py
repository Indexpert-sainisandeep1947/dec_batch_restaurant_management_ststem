import uuid
import json
import os

class UserAuthentication:
    def __init__(self):
        self.path = "user_data.json"
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                self.user_data = json.load(file)
        else:
            self.user_data = []

    def generate_user_data(self, role):
        user = {}
        user["name"] = input('Please enter your name: ')
        if user["name"].replace(" ", "").isalpha():
            pass
        else:
            print("name should be letter and space!")
            return
        
        user["address"] = input('Please enter your address: ')
        if user["address"].replace(" ","").isalnum():
            pass
        else:
            print("invalid address!")
            return
        
        
        user["contact"] = input('Please enter your contact number: ')
        if user["contact"].isdigit() and len(user["contact"]) == 10:
            pass
        else:
            print("invalid number! please enter valid number(only 10 degit)")
            return
    
        user["email"] = input('Please enter your email: ')
        user["role"] = role

        user["id"] = f"{role}_{user['name'].split()[0]}_{uuid.uuid4().hex[:6]}"
        self.user_data.append(user)
        print(f"{role.capitalize()} account created successfully!\n")
        self.save_to_json()

    def admin_login(self):
        while True:
            print("\n*** Admin Sign-Up ***")
            self.generate_user_data("admin")
            another = input("Create another admin? (yes/no): ").lower()
            if another != "yes":
                break

    def staff_login(self):
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
