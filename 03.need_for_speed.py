car_num = int(input())
cars = {}
for _ in range(car_num):
    car_data = input().split("|")
    mark = car_data[0]
    mileage = int(car_data[1])
    fuel = int(car_data[2])
    cars[mark] = {"mileage": mileage, "fuel": fuel}
while True:
    data = input()
    if data == "Stop":
        break
    data = data.split(" : ")
    command = data[0]
    car = data[1]
    if command == "Drive":
        distance = int(data[2])
        fuel_need = int(data[3])
        if fuel_need > cars[car]["fuel"]:
            print("Not enough fuel to make that ride")
            continue
        else:
            cars[car]["fuel"] -= fuel_need
            cars[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel_need} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")
    elif command == "Refuel":
        re_fuel = int(data[2])
        needed_fuel = 75 - cars[car]["fuel"]
        if re_fuel >= needed_fuel:
            cars[car]["fuel"] = 75
            print(f"{car} refueled with {needed_fuel} liters")
        else:
            cars[car]["fuel"] += re_fuel
            print(f"{car} refueled with {re_fuel} liters")
    elif command == "Revert":
        kilometers = int(data[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
            continue
        print(f"{car} mileage decreased by {kilometers} kilometers")

sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))
for key, value in sorted_cars:
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
