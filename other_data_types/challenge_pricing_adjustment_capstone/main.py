

grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
                     "Eggs": ("Dairy", 5.50, 30),
                     "Bread": ("Bakery", 2.99, 15),
                     "Apples": ("Produce", 1.50, 50)
    
}

cat, price, stock = grocery_inventory["Eggs"]
if price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    price -=1
else:
    print("The price of Eggs is reasonable.")

grocery_inventory ["Eggs"] = (cat, price, stock)
    

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)


cat, price, stock = grocery_inventory["Milk"]
if stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    stock += 20
else:
    print("Milk has sufficient stock.")

grocery_inventory["Milk"] = (cat, price, stock)
    
    
cat, price, stock = grocery_inventory ["Apples"]
if price > 2:
    del grocery_inventory ["Apples"]
    print("Apples removed from inventory due to high price.")

print("Updated inventory:", grocery_inventory)




    
        
    
    



