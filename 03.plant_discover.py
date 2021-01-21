n = int(input())
plants = {}
for _ in range(n):
    plant_data, rarity_data = input().split("<->")
    if plant_data not in plants:
        plants[plant_data] = {"rarity": 0, "rating": []}
    plants[plant_data]['rarity'] = int(rarity_data)

while True:
    data = input()
    if data == "Exhibition":
        break
    data = data.split(": ")
    command = data[0]
    plant_data = data[1]
    plant_data = plant_data.split(" - ")
    plant = plant_data[0]

    if plant not in plants:
        print("error")
        continue
    if command == "Rate":
        rating = int(plant_data[1])
        plants[plant]["rating"].append(rating)
    elif command == "Update":
        new_rarity = int(plant_data[1])
        plants[plant]['rarity'] = new_rarity
    elif command == "Reset":
        plants[plant]["rating"] = []
    else:
        print("error")
plant_discovery = {}
for key in plants:
    if sum(plants[key]['rating']) > 0:
        average = sum(plants[key]['rating']) / len(plants[key]['rating'])
    else:
        average = 0
    plant_discovery[key] = {'rarity': plants[key]['rarity'], 'average': average}

print("Plants for the exhibition:")
sorted_plants = sorted(plant_discovery.items(), key=lambda x: (-x[1]['rarity'], -x[1]['average']))
for key, value in sorted_plants:
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {value['average']:.2f}")
