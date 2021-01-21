message = input()

while True:
    data = input()
    if data == "Decode":
        break
    data = data.split("|")
    command = data[0]
    if command == "Move":
        num_letters = int(data[1])
        n_letters = message[:num_letters]
        left_letters = message[num_letters:]
        message = left_letters + n_letters
    elif command == "Insert":
        index = int(data[1])
        value = data[2]
        lef = message[:index]
        right = message[index:]
        message = lef + value + right
    elif command == "ChangeAll":
        sub_str = data[1]
        replacement = data[2]
        if sub_str in message:
            message = message.replace(sub_str, replacement)

print(f"The decrypted message is: {message}")