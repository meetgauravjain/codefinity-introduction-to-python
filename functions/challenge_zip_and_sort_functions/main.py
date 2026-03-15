# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

combined_list = list(zip(products, prices, quantities_sold))
sorted_products = sorted(combined_list,reverse=False)

for i in sorted_products:
    product_name = i[0]
    product_price = i[1]
    quantity_sold = i[2]
    print(f"Product: {product_name}, Price: {product_price}, Quantity Sold: {quantity_sold}")