message = input()

while True:
    data = input()
    if data == "Reveal":
        break
    data = data.split(":|:")
    command = data[0]
    if command == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command == "Reverse":
        substring = data[1]
        if substring in message:
            replace_message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message = replace_message + substring
            print(message)
        else:
            print("error")
    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        if substring in message:
            message = message.replace(substring, replacement)
            print(message)
        # else:
        #     print("error")
print(f"You have a new text message: {message}")
