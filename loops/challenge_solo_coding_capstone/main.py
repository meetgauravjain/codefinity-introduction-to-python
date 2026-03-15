# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item in inventory:
    item_details = inventory.get(item)
    current_stock = item_details[0]
    regular_price = item_details[1]
    discounted_price = item_details[2]
    if current_stock < 30:
        print(f"{item} need restocking.")
    elif current_stock >= 30 and current_stock <= 100:
        print(f"{item} should be sold at the regular price of {regular_price}.")
    else:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")