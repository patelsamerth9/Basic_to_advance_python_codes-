menu = {"Pizza": 120, "Burger": 80, "Pasta": 100}
order = input("Enter item name: ")
if order in menu:
    print(order, "costs", menu[order], "₹")
else:
    print("Item not available")