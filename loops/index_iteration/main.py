prices = [29.99, 45.50, 12.75, 38.20]

for index in range(len(prices)):
    if index == 0:
        prices[index] = prices[index] - prices[index]/10 
    if index == 1:
        prices[index] = prices[index] - prices[index]/5
    if index == 2:
        prices[index] = prices[index] - prices[index]*15/100
    if index == 3:
        prices[index] = prices[index] - prices[index]*5/100
    print(f'Updated price for item {index}: ${prices[index]:.2f}')    