def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"Discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
