from cart import add_item
from calculater import calculate_bill
from printer import show_bill
from payment import payment_option

def main():
    order_list = []
    print("=== Welcome to Billing System ===")
    
    while True:
        add_item(order_list)
        cont = input("Aur item add karein? (y/n): ")
        if cont.lower() != 'y':
            break

    subtotal, tax, discount, total = calculate_bill(order_list)
    show_bill(order_list, subtotal, tax, discount, total)

    method = payment_option()
    print(f"\nPayment Method: {method}")
    print("\nShukriya! Aapka bill ban gaya hai.\n")

if __name__ == "__main__":
    main()
