# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for i in range(len(weekdays)):
    day = weekdays[i]
    prpmotion  = daily_promotions[i]
    print(f"{day}: Promotion on {prpmotion}")
    