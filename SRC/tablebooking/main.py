from booking import show_available_tables, book_table, my_bookings, cancel_booking
from datetime import datetime, timedelta

def suggest_dates():
    print("\nSuggested booking dates (every 3 days):")
    today = datetime.today().date()
    for i in range(0, 31, 3):
        d = today + timedelta(days=i)
        print(d.strftime("%Y-%m-%d"))

def menu():
    while True:
        print("\n--- Table Booking System ---")
        print("1. Show Available Tables")
        print("2. Book Table")
        print("3. My Bookings")
        print("4. Cancel Booking")
        print("5. Suggested Dates")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            time = input("Time (HH:MM): ")
            show_available_tables(date, time)
        elif choice == "2":
            book_table()
        elif choice == "3":
            my_bookings()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            suggest_dates()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
