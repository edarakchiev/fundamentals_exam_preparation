def shoot(target_list, index, value):
    if 0 <= index < len(target_list):
        target_list[index] -= value
        if target_list[index] <= 0:
            target_list.pop(index)


def add(target_list, index, value):
    if 0 <= index < len(target_list):
        target_list.insert(index, value)
    else:
        print("Invalid placement!")


def strike(target_list, index, value):
    left_radius = index - value
    right_radius = index + value
    if left_radius < 0 or right_radius > len(target_list):
        print("Strike missed!")
        return target_list
    else:
        left_side = target_list[:left_radius]
        right_side = target_list[right_radius + 1:]
        target_list = left_side + right_side
        return target_list


target_list = list(map(int, input().split()))

while True:
    data = input()
    if data == "End":
        break
    command, index, value = data.split()
    index = int(index)
    value = int(value)
    if command == "Shoot":
        shoot(target_list, index, value)
    elif command == "Add":
        add(target_list, index, value)
    elif command == "Strike":
        target_list = strike(target_list, index, value)

str_list = [str(el) for el in target_list]
print('|'.join(str_list))
