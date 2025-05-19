import json
import os

def login():
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()

    filepath = os.path.join("src", "database", "user_data.json")

    try:
        with open(filepath, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        print("User data file not found.")
        return None

    for user in users:
        if user['name'] == username and user['email'] == email:
            print(f"{user['role'].capitalize()} login successful.")
            return user['role']

    print("Login failed ! please try agin.")
    return None
