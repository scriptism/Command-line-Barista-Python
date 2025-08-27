name = input("What is your name?\n")

menu = (
    "The menu for today is:\n"
    "1. Pizza\n"
    "2. Pasta\n"
    "3. Qabuli\n"
    "4. Salad"
)

print(f"Hello {name}! Welcome to scriptism!\n{menu}\n")
print("What would you like to order?")
order = input()

quantity = input(f"Great choice! How many {order} would you like to order?\n")
print(
    f"Thank you {name}! "
    f"You have ordered {quantity} {order}(s). "
    "Your order will be ready soon!"
)