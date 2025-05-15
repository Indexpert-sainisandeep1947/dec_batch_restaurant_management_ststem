import json
import os

class MenuManager:
    def __init__(self, filename="menu_data.json"):
        self.filename = filename
        self.menu = self.load_menu()

    def load_menu(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_menu(self):
        with open(self.filename, 'w') as f:
            json.dump(self.menu, f, indent=4)

    def input_item_details(self):
        item = {}
        item['id'] = input("ID: ").strip()
        if any(i['id'] == item['id'] for i in self.menu):
            print("Item ID already exists.")
            return None 
        item['name'] = input("Name: ").strip()
        item['size'] = input("Size: ").strip()
        try:
            item['price'] = float(input("Price: ").strip())
        except:
            print("Invalid price.")
            return None
        item['category'] = input("Category (veg/nonveg/softdrink): ").strip().lower()
        if item['category'] not in ['veg', 'nonveg', 'softdrink']:
            print("Invalid category.")
            return None
        return item

    def add_item(self):
        item = self.input_item_details()
        if item:
            self.menu.append(item)
            self.save_menu()
            print("Item added.")

    def update_item(self):
        item_id = input("Enter ID to update: ").strip()
        for item in self.menu:
            if item['id'] == item_id:
                item['name'] = input("New Name: ").strip()
                item['size'] = input("New Size: ").strip()
                try:
                    item['price'] = float(input("New Price: ").strip())
                except:
                    print("Invalid price.")
                    return
                category = input("New Category: ").strip().lower()
                if category not in ['veg', 'nonveg', 'softdrink']:
                    print("Invalid category.")
                    return
                item['category'] = category
                self.save_menu()
                print("Item updated.")
                return
        print("Item not found.")

    def delete_item(self):
        item_id = input("Enter ID to delete: ").strip()
        before = len(self.menu)
        self.menu = [item for item in self.menu if item['id'] != item_id]
        if len(self.menu) < before:
            self.save_menu()
            print("Item deleted.")
        else:
            print("Item not found.")

    def view_menu(self):
        if not self.menu:
            print("Menu is empty.")
            return
        for cat in ['veg', 'nonveg', 'softdrink']:
            print(f"\n{cat}")
            print("id\tname\tsize\tprice")
            found = False
            for item in self.menu:
                if item['category'] == cat:
                    print(f"{item['id']}\t{item['name']}\t{item['size']}\t₹{item['price']}")
                    found = True
            if not found:
                print("No items.")

