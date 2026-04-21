def apply_discount(price, discount=0.05):
    discounted_price = price *(1-discount)
    return discounted_price

def apply_tax(price, tax=0.07):
    taxed_price = price + (price * tax)
    return taxed_price
    
def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    total = apply_tax(discounted, tax)
    return total

total_cost = calculate_total(price=120, discount=0.05, tax=0.07)

print(f"Total cost with default discount and tax: ${total_cost}")

discounted_total_cost = calculate_total(price=100, discount=0.10, tax=0.08)

print(f"Total cost with custom discount and tax: ${discounted_total_cost}")





    