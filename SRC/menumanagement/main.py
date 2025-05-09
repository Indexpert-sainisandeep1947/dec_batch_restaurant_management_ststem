from menu import MenuManager

menu = MenuManager()

while True:
    print("\n--- MENU ---")
    print("1. View Menu")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        menu.view_menu()
    elif choice == '2':
        item_id = int(input("ID: "))
        name = input("Name: ")
        price = float(input("Price: "))
        category = input("Category (veg/nonveg/softdrink): ")
        menu.add_item(item_id, name, price, category)
    elif choice == '3':
        item_id = int(input("ID to update: "))
        name = input("New name: ")
        price = float(input("New price: "))
        category = input("New category: ")
        menu.update_item(item_id, name, price, category)
    elif choice == '4':
        item_id = int(input("ID to delete: "))
        menu.delete_item(item_id)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
