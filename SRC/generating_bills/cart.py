def add_item(order_list):
    name = input("Item ka naam: ")
    qty = int(input("Kitni quantity: "))
    price = float(input("Ek ka price (₹): "))
    total = qty * price
    order_list.append({'name': name, 'qty': qty, 'price': price, 'total': total})
