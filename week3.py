def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    
    else:
        return price

#Prompting the user for input

original_price = float(input("Enter the original price of the item: "))
dicount_percentage = float(input("Enter the discount percentage: "))

#Calculating the final price
final_price = calculate_discount(original_price, dicount_percentage)

#Printing the final rice or original price if no discount is applied
if final_price < original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")

else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")