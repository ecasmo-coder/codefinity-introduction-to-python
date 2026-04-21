# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100

print("Processing started")

for item, num in inventory.items():
    stock, minimun_stock, restock_qty, on_sale = num
    print(f"Processing {item}")
    while stock < minimun_stock:
        stock += restock_qty       
    inventory[item][0] = stock

    if stock > discount_threshold and not on_sale:
        inventory[item][3] = True
print("Processing completed")
        

    
    
    
    
    
  
        
   