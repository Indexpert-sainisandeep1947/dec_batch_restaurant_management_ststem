import json
import os

class SignIn:
    def __init__(self):
        self.path = "user_data.json"
        if os.path.exists(self.path):
            with open(self.path, 'r') as file:
                self.user_data = json.load(file)
        else:
            self.user_data = []

    def sign_in(self):
        email = input('Enter your email to sign in: ')
        for user in self.user_data:
            if user["email"] == email:
                print("Welcome back,", user["name"])
                return
        print("Email not found. Please sign up first.")
