# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = [price * qty for price, qty in zip(prices, quantities_sold)]
    return revenue

def get_product_name(name_revenue):
    return name_revenue[0]

def formatted_output(revenues):
    revenue_sorted = sorted(revenues, key=get_product_name)
    for product, revenue in revenue_sorted:
        print(f"{product.lower()} has total revenue of ${revenue}")

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)



# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")