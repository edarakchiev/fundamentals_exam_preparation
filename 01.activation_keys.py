def contains(act_key, sub_str):
    if sub_str in act_key:
        print(f"{act_key} contains {sub_str}")
    else:
        print("Substring not found!")


def flip(act_key, upper_low, start, stop):
    left = act_key[:start]
    center = act_key[start:stop]
    right = act_key[stop:]
    if upper_low == "Upper":
        center = center.upper()
    elif upper_low == "Lower":
        center = center.lower()
    act_key = left + center + right
    print(act_key)
    return act_key


def slice_str(act_key, start, stop):
    left = act_key[:start]
    right = act_key[stop:]
    act_key = left + right
    print(act_key)
    return act_key


activation_key = input()

while True:
    data = input()
    if data == "Generate":
        break
    data = data.split(">>>")
    command = data[0]
    if command == "Contains":
        substring = data[1]
        contains(act_key=activation_key, sub_str=substring)
    elif command == "Flip":
        up_low = data[1]
        start_i = int(data[2])
        stop_i = int(data[3])
        activation_key = flip(act_key=activation_key, upper_low=up_low, start=start_i, stop=stop_i)
    elif command == "Slice":
        start_i = int(data[1])
        stop_i = int(data[2])
        activation_key = slice_str(act_key=activation_key, start=start_i, stop=stop_i)

print(f"Your activation key is: {activation_key}")