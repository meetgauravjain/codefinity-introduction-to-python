# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


def calculate_revenue(prices, quantities_sold):
    revenue = [p * q for p, q in zip(prices, quantities_sold)]
    return revenue

def formatted_output(revenues):
    revenues.sort()  # sort by product name
    for product, revenue in revenues:
        print(f"{product} has total revenue of ${revenue}")
    
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = sorted(zip(products, revenue))

formatted_output(revenue_per_product)