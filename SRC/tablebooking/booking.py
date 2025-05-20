from data_handler import load_tables, load_bookings, save_bookings
from utils import time_diff, is_valid_date

def show_available_tables(date, time):
    tables = load_tables()
    bookings = load_bookings()
    available = []

    for table in tables:
        conflict = False
        for b in bookings:
            if b["table"] == table["id"] and b["date"] == date:
                if time_diff(b["time"], time) < 2:
                    conflict = True
                    break
        if not conflict:
            available.append(table)

    if available:
        print("\nAvailable Tables:")
        for t in available:
            print(f"Table {t['id']} (Seats: {t['seats']})")
    else:
        print("\nNo tables available at this time.")

def book_table():
    name = input("Your Name: ")
    date = input("Booking Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")

    if not is_valid_date(date):
        print("Only 1 month advance booking is allowed.")
        return

    show_available_tables(date, time)
    try:
        table_id = int(input("Enter table ID to book: "))
    except ValueError:
        print("Invalid table ID.")
        return

    bookings = load_bookings()
    for b in bookings:
        if b["table"] == table_id and b["date"] == date:
            if time_diff(b["time"], time) < 2:
                print("This table is already booked around that time.")
                return

    new_booking = {
        "name": name,
        "table": table_id,
        "date": date,
        "time": time
    }
    bookings.append(new_booking)
    save_bookings(bookings)
    print("Booking confirmed!")

def my_bookings():
    name = input("Enter your name: ")
    bookings = load_bookings()
    found = False
    for b in bookings:
        if b["name"].lower() == name.lower():
            print(f"Table {b['table']} on {b['date']} at {b['time']}")
            found = True
    if not found:
        print("No bookings found.")

def cancel_booking():
    name = input("Your Name: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    try:
        table_id = int(input("Table ID: "))
    except ValueError:
        print("Invalid table ID.")
        return

    bookings = load_bookings()
    updated = [b for b in bookings if not (
        b["name"].lower() == name.lower() and
        b["date"] == date and
        b["time"] == time and
        b["table"] == table_id
    )]

    if len(updated) == len(bookings):
        print("No matching booking found.")
    else:
        save_bookings(updated)
        print("Booking cancelled.")
