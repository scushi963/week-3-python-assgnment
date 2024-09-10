def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount and subtract it from the original price
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if final_price == original_price:
    print(f"No discount applied. The original price is: {original_price}")
else:
    print(f"The final price after applying the discount is: {final_price}")
