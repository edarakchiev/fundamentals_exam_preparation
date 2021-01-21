city_dict = {}
while True:
    data = input()
    if data == "Sail":
        break
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)
    if city not in city_dict:
        city_dict[city] = {"population": 0, "gold": 0}
    city_dict[city]["population"] += population
    city_dict[city]["gold"] += gold

while True:
    command_data = input()
    if command_data == "End":
        break
    command_data = command_data.split("=>")
    command = command_data[0]
    town = command_data[1]
    if command == "Plunder":
        people = int(command_data[2])
        gold_amount = int(command_data[3])
        city_dict[town]["population"] -= people
        city_dict[town]["gold"] -= gold_amount
        print(f"{town} plundered! {gold_amount} gold stolen, {people} citizens killed.")
        if city_dict[town]["population"] == 0 or city_dict[town]["gold"] == 0:
            del city_dict[town]
            print(f"{town} has been wiped off the map!")
    elif command == "Prosper":
        gold_increase = int(command_data[2])
        if gold_increase < 0:
            print(f"Gold added cannot be a negative number!")
            continue
        city_dict[town]["gold"] += gold_increase
        print(f"{gold_increase} gold added to the city treasury. {town} now has {city_dict[town]['gold']} gold.")

sorted_city = sorted(city_dict.items(), key=lambda x: (-x[1]["gold"], x[0]))
print(f"Ahoy, Captain! There are {len(sorted_city)} wealthy settlements to go to:")
for key, value in sorted_city:
    print(f"{key} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")

