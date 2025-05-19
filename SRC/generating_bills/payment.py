def payment_option():
    print("\nchoose the option:")
    print("1. NetBanking")
    print("2. UPI")
    print("3. Cash")
    choice = input("Option (1/2/3): ")
    if choice == '1':
        return "NetBanking"
    elif choice == '2':
        return "UPI"
    elif choice == '3':
        return "Cash"
    else:
        return "Invalid Option"
