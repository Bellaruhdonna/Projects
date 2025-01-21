bike_money = 100000
saved_money = 0
day = 0

while saved_money < bike_money:
    if day % 2 == 0:  # Even day
        saved_money += 1000
    else:  # Odd day
        saved_money += 500
    day += 1

# Adjusting day to reflect the correct number of days taken


print("Total days required:", day+1)
print("Total money saved:", saved_money)


bike_money = 100000
saving = 0
day = 1

for day in range(1, 100000000):  # A large upper limit to ensure the loop runs until saving >= bike_money
    if day % 2 == 0:  # Even day
        saving += 1000
    else:  # Odd day
        saving += 500

    if saving >= bike_money:  # Break the loop once the goal is achieved
        break

print("Total days required:", day)
print("Total money saved:", saving)


