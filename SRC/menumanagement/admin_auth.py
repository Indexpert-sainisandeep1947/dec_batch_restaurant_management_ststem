def admin_login():
    username = input("Admin Username: ").strip()
    email = input("Admin email: ").strip()
    return username == "admin" and email == "admin123"
