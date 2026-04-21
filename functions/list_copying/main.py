# List of product prices
x = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    prices_copy = prices.copy()
    for i in range(len(prices_copy)):
        if prices_copy[i] > 2.00:
            prices_copy[i] = prices_copy[i] * (1-0.10)
            
    return prices_copy        

# Call the function and store the updated prices
updated_prices = apply_discount(x)
print(f"Updated product prices: ${updated_prices}")