produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
#combined two lists
groceries = [produce, dairy]

#for loop to iterate with every item
for x in groceries:
    section = x
    print(section)
    for i in section:
        item_name = i
        print(item_name)


