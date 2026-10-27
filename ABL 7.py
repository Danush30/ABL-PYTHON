def smart_canteen_management():
    stock = {
        "Burger": 20,
        "Pizza": 10,
        "Sandwich": 15,
        "Juice": 25
    }

    prices = {
        "Burger": 80,
        "Pizza": 150,
        "Sandwich": 60,
        "Juice": 30
    }

    orders = [
        ("Burger", 2),
        ("Pizza", 3),
        ("Juice", 4),
        ("Sandwich", 20),
        ("Burger", 1)
    ]

    total_sales = 0

    for item, quantity in orders:
        print(f"\nOrder: {quantity} {item}")

        if item not in stock:
            print("Rejected: Item unavailable")
        elif quantity <= 0:
            print("Rejected: Invalid quantity")
        elif quantity > stock[item]:
            print("Rejected: Insufficient stock")
        else:
            bill = prices[item] * quantity
            stock[item] -= quantity
            total_sales += bill

            print("Order accepted")
            print("Bill: ₹", bill)
            print("Remaining stock:", stock[item])

    print("\nTotal daily sales: ₹", total_sales)
    print("Remaining stock:")
    for item, quantity in stock.items():
        print(f"{item}: {quantity}")


if __name__ == "__main__":
    smart_canteen_management()