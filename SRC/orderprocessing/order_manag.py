import json
import os
from datetime import datetime

ORDERS_FILE = "data/orders.json"

class OrderManager:
    def __init__(self, menu_manager):
        self.menu_manager = menu_manager
        if not os.path.exists(ORDERS_FILE):
            with open(ORDERS_FILE, 'w') as f:
                json.dump([], f)

    def _load_orders(self):
        with open(ORDERS_FILE, 'r') as f:
            return json.load(f)

    def _save_orders(self, orders):
        with open(ORDERS_FILE, 'w') as f:
            json.dump(orders, f, indent=4)

    def _generate_order_id(self):
        orders = self._load_orders()
        return f"ORD{len(orders)+1:03d}"

    def create_order(self, customer_name):
        menu = self.menu_manager.load_menu()
        if not menu:
            print("Menu is empty.")
            return

        self.menu_manager.display_menu(menu)
        items = []
        while True:
            item_id = input("Enter Item ID to order (or 'done'): ")
            if item_id.lower() == "done":
                break
            item = next((m for m in menu if m["id"] == item_id), None)
            if item:
                try:
                    qty = int(input(f"Quantity for {item['name']}: "))
                    items.append({
                        "id": item['id'],
                        "name": item['name'],
                        "price": item['price'],
                        "quantity": qty
                    })
                except ValueError:
                    print("Invalid quantity.")
            else:
                print("Invalid item ID.")

        if not items:
            print("No items selected.")
            return

        order = {
            "order_id": self._generate_order_id(),
            "customer": customer_name,
            "items": items,
            "total": sum(i['price'] * i['quantity'] for i in items),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        orders = self._load_orders()
        orders.append(order)
        self._save_orders(orders)
        print(f"\nOrder {order['order_id']} placed successfully.")

    def update_order(self, order_id):
        orders = self._load_orders()
        order = next((o for o in orders if o["order_id"] == order_id), None)
        if not order:
            print("Order not found.")
            return

        print(f"\nCurrent items in {order_id}:")
        for i, item in enumerate(order["items"], 1):
            print(f"{i}. {item['name']} x{item['quantity']}")

        try:
            index = int(input("Enter item number to update quantity: ")) - 1
            if 0 <= index < len(order["items"]):
                new_qty = int(input("New quantity: "))
                order["items"][index]["quantity"] = new_qty
                order["total"] = sum(i['price'] * i['quantity'] for i in order["items"])
                self._save_orders(orders)
                print("Order updated.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input.")

    def cancel_order(self, order_id):
        orders = self._load_orders()
        updated_orders = [o for o in orders if o["order_id"] != order_id]
        if len(orders) == len(updated_orders):
            print("Order not found.")
        else:
            self._save_orders(updated_orders)
            print(f"Order {order_id} cancelled.")

    def view_all_orders(self):
        orders = self._load_orders()
        if not orders:
            print("No orders available.")
            return

        for order in orders:
            print(f"\nOrder ID: {order['order_id']}")
            print(f"Customer: {order['customer']}")
            print(f"Time: {order['time']}")
            for item in order["items"]:
                print(f" - {item['name']} x{item['quantity']} = ₹{item['price'] * item['quantity']}")
            print(f"Total: ₹{order['total']}")
