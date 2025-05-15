def order_menu(order_manager):
    while True:
        print("\n1. Manage Orders\n2. View Orders\n3. Back")
        choice = input("Choose option: ")
        if choice == '1':
            print("\n--- Manage Orders ---")
            print("1. Place New Order")
            print("2. Update Existing Order")
            print("3. Cancel Order")
            sub = input("Select: ")
            if sub == '1':
                name = input("Customer name: ")
                order_manager.create_order(name)
            elif sub == '2':
                order_id = input("Enter Order ID to update: ")
                order_manager.update_order(order_id)
            elif sub == '3':
                order_id = input("Enter Order ID to cancel: ")
                order_manager.cancel_order(order_id)
            else:
                print("Invalid option.")
        elif choice == '2':
            order_manager.view_all_orders()
        elif choice == '3':
            break
        else:
            print("Invalid input.")
