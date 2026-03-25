def apply_discount(price, discount=0.05):
    return price - price*discount

def apply_tax(price, tax=0.07):
    return price + price*tax

def calculate_total(price, discount=0.05, tax=0.07):
    price = apply_discount(price, discount)
    price  = apply_tax(price,tax)
    return price

total_price_default  = calculate_total(120)

print(f'Total cost with default discount and tax: ${total_price_default}')

total_price_custom  = calculate_total(100, discount=0.10, tax=0.08)

print(f'Total cost with custom discount and tax: ${total_price_custom}')