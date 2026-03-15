# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

for i in inventory:
    print("Processing started")
    print("Processing:", i)
    item = inventory.get(i)
    current_stock = item[0]
    minimum_stock = item[1]
    restock_quantity = item[2]
    on_sale = item[3]
    while current_stock < minimum_stock:
        current_stock += restock_quantity
    item[0] = current_stock
    if current_stock > discount_threshold:
        if not on_sale:
            on_sale = True
            item[3] = on_sale
    print("Processing Completed")