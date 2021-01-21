text = input()

while True:
    data = input()
    if data == "Travel":
        break
    data = data.split(":")
    command = data[0]
    max_valid_index = len(text) - 1
    if command == "Add Stop":
        index = int(data[1])
        string = data[2]
        if 0 <= index <= max_valid_index:
            left = text[:index]
            right = text[index:]
            text = left + string + right
        print(text)
    elif command == "Remove Stop":
        start_index = int(data[1])
        stop_index = int(data[2])
        if 0 <= start_index <= max_valid_index and 0 <= stop_index <= max_valid_index:
            left = text[:start_index]
            right = text[stop_index+1:]
            text = left + right
        print(text)
    elif command == "Switch":
        old_str = data[1]
        new_str = data[2]
        if old_str in text:
            text = text.replace(old_str, new_str)
        print(text)
print(f"Ready for world tour! Planned stops: {text}")