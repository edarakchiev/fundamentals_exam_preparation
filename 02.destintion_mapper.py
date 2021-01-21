import re

pattern = r"(?P<sep>=|/)(?P<destination>[A-Z][A-Za-z]{2,})(?P=sep)"
points = 0
data = input()
destination = []
matches = re.finditer(pattern, data)
for m in matches:
    match = m.groupdict()
    length = len(match["destination"])
    points += length
    destination.append(match['destination'])

print("Destinations:", end="")
print(f" {', '.join(destination)}", end="")
print()
print(f"Travel Points: {points}")