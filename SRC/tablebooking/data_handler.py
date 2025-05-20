import json

def load_tables():
    with open("tables.json") as f:
        return json.load(f)

def load_bookings():
    with open("bookings.json") as f:
        return json.load(f)

def save_bookings(data):
    with open("bookings.json", "w") as f:
        json.dump(data, f, indent=4)
