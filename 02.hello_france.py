items_collections = input().split("|")
budget = float(input())

CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE = 20.50

new_price = []
profit = 0

for el in items_collections:
    item_type, price = el.split("->")
    price = float(price)
    if budget < price:
        continue
    if item_type == "Clothes" and price <= CLOTHES_MAX_PRICE:
        budget -= price
        current_profit = price * 0.4
        profit += current_profit
        current_price = price + current_profit
        new_price.append(current_price)
    elif item_type == "Shoes" and price <= SHOES_MAX_PRICE:
        budget -= price
        current_profit = price * 0.4
        profit += current_profit
        current_price = price + current_profit
        new_price.append(current_price)
    elif item_type == "Accessories" and price <= ACCESSORIES_MAX_PRICE:
        budget -= price
        current_profit = price * 0.4
        profit += current_profit
        current_price = price + current_profit
        new_price.append(current_price)

for el in new_price:
    print(f"{el:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
all_money = sum(new_price) + budget
if all_money >= 150:
    print("Hello, France!")
else:
    print("Time to go.")