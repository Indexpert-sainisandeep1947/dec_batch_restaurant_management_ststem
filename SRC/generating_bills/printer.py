def show_bill(order_list, subtotal, tax, discount, total):
    print("\n--- Bill ---")
    for item in order_list:
        print(f"{item['name']} x{item['qty']} = ₹{item['total']:.2f}")
    print(f"\nSubtotal       : ₹{subtotal:.2f}")
    print(f"Tax (5%)       : ₹{tax:.2f}")
    print(f"Discount (10%) : ₹{discount:.2f}")
    print(f"Total Bill     : ₹{total:.2f}")
