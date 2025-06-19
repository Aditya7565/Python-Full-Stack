# Simulate a restaurant order system.
# Menu has items with prices ()
# Customer orders multiple items ()
# Tasks:


# Show menu to the user.

# Let them choose 5 items (with quantity), and store the order.

# Calculate total bill.

# Create a of unique ordered items.
# Convert the final order summary to a for record-keeping.
# : Update the menu dynamically (e.g., add a new item or change price).



menu={
    'Pizza':250,
    'Burger':100,
    'Pasta':50,
    'Coke':70,
    'Fries':110
}
print("------ MENU ------")
for item,price in menu.items():
    print(f"{item}: ₹ {price}")
print("------------------")
order=[]
for i in range(3):
    item=input("Enter item name:").title()
    if item not in menu:
        print("item not in menu ")
        continue
    qty=int(input(f"Enter quantity of {item}: "))
    order.append((item,qty))
print(order)
    
total = 0
order_dict = {}
for item, qty in order:
    total += menu[item] * qty
    if item in order_dict:
        order_dict[item] += qty
    else:
        order_dict[item] = qty
print(total)

unique_items=set(order_dict.keys())

print("\n---- ORDER SUMMARY ----")
for item, qty in order_dict.items():
    print(f"{item} x {qty} = ₹{menu[item] * qty}")
print(f"Total Bill: ₹{total}")
print(f"Unique Items: {unique_items}")
print(f"Order Record (Dictionary): {order_dict}")

choice = input("\nDo you want to update the menu? (yes/no): ").lower()
if choice == "yes":
    action = input("Add new item or change price? (add/change): ").lower()
    name = input("Enter item name: ").title()
    price = int(input("Enter item price: "))
    menu[name] = price
    print("Menu updated.")

print("\n------ UPDATED MENU ------")
for item, price in menu.items():
    print(f"{item}: ₹{price}")