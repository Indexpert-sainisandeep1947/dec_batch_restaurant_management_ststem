import json
import os

class MenuManager:
    def __init__(self):
        self.filename = "menu_data.json"
        self.menu = self.load_menu()

    def load_menu(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_menu(self):
        with open(self.filename, 'w') as f:
            json.dump(self.menu, f, indent=4)

    def add_item(self, item_id, name, price, category):
        if category.lower() not in ['veg', 'nonveg', 'softdrink']:
            print("Invalid category. Use veg, nonveg or softdrink.")
            return

        for item in self.menu:
            if item['id'] == item_id:
                print("ID already exists.")
                return

        self.menu.append({
            'id': item_id,
            'name': name,
            'price': price,
            'category': category.lower()
        })
        self.save_menu()
        print("Item added.")

    def update_item(self, item_id, name, price, category):
        for item in self.menu:
            if item['id'] == item_id:
                item['name'] = name
                item['price'] = price
                item['category'] = category.lower()
                self.save_menu()
                print("Item updated.")
                return
        print("Item not found.")

    def delete_item(self, item_id):
        original = len(self.menu)
        self.menu = [item for item in self.menu if item['id'] != item_id]
        if len(self.menu) < original:
            self.save_menu()
            print("Item deleted.")
        else:
            print("Item not found.")

    def view_menu(self):
        if not self.menu:
            print("Menu is empty.")
            return

        print("\n MENU (Grouped):")
        for category in ['veg', 'nonveg', 'softdrink']:
            print(f"\n {category.upper()}:")
            found = False
            for item in self.menu:
                if item['category'] == category:
                    print(f"  ID: {item['id']} | {item['name']} - ₹{item['price']}")
                    found = True
            if not found:
                print("  No items.")

                