def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(price, discount_percent)
    
    # Provide feedback to the user
    if discount_percent < 20:
        print("Discount does not apply as it is below 20%. The price remains the same.")
    
    # Print the result
    print(f"Final price after discount: ksh{final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
