# variables, input, and output, integer conversion
name = input("What is your name?\n")

menu = (
    "Our menu for today is:\n"
    "1. Black Coffee -$2.00\n"
    "2. cappuccino -$3.50\n"
    "3. Espresso -$2.50\n"
    "4. Latte -$4.00\n"
    "5. Mocha -$4.50\n"
    "6. Tea -$1.50\n"
    "7. Hot Chocolate -$3.00\n"
    "8. Iced Coffee -$4.00\n"
    "9. Smoothie -$4.00\n"
    "10. Frappuccino -$4.50"
)

print(f"Hello {name}! Welcome to scriptism!\n{menu}\n")
print("What would you like to order?")
order = input()

# price 
if order.lower() == "black coffee":
    price = 2.00
elif order.lower() == "cappuccino":
    price = 3.50
elif order.lower() == "espresso":
    price = 2.50
elif order.lower() == "latte":
    price = 4.00
elif order.lower() == "mocha":
    price = 4.50
elif order.lower() == "tea":
    price = 1.50
elif order.lower() == "hot chocolate":
    price = 3.00
elif order.lower() == "iced coffee":
    price = 3.00
elif order.lower() == "smoothie":
    price = 4.00
elif order.lower() == "frappuccino":
    price = 4.50
else:
    print("Sorry, we don't have that item on the menu.")
    exit()

quantity = input(f"Great choice! How many {order} would you like to order?\n")
total = float(price) * int(quantity)
print(
    f"Thank you {name}! "
    f"You have ordered {quantity} {order}(s). "
    f"Your total is ${total:.2f}. "
    "Your order will be ready soon!"
)