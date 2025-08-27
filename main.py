# variables, input, and output, integer conversion
name = input("What is your name?\n")

menu = (
    "Our menu for today is:\n"
    "1. Black Coffee\n"
    "2. cappuccino\n"
    "3. Espresso\n"
    "4. Latte\n"
    "5. Mocha\n"
    "6. Tea\n"
    "7. Hot Chocolate\n"
    "8. Iced Coffee\n"
    "9. Smoothie\n"
    "10. Frappuccino"
)

print(f"Hello {name}! Welcome to scriptism!\n{menu}\n")
print("What would you like to order?")
order = input()

price = 3.50  # default price

quantity = input(f"Great choice! How many {order} would you like to order?\n")
total = float(price) * int(quantity)
print(
    f"Thank you {name}! "
    f"You have ordered {quantity} {order}(s). "
    f"Your total is ${total:.2f}. "
    "Your order will be ready soon!"
)