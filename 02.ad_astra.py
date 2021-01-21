import re

text = input()
pattern = r"(?P<sep>#|\|)(?P<item>[A-Za-z ]+)(?P=sep)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=sep)(?P<calories>\d+)(?P=sep)"
sum_calories = 0
matches = re.finditer(pattern, text)
items = []
for m in matches:
    match = m.groupdict()
    sum_calories += int(match["calories"])
    items.append(f"Item: {match['item']}, Best before: {match['date']}, Nutrition: {match['calories']}")
days = sum_calories // 2000
print(f"You have food to last you for: {days} days!")
for el in items:
    print(el)