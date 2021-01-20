messages_list = []
while True:
    data = input()
    if data == "end":
        break

    data = data.split()
    command = data[0]
    if command == "Chat":
        message = data[1]
        messages_list.append(message)
    elif command == "Delete":
        message = data[1]
        if message in messages_list:
            messages_list.remove(message)
    elif command == "Edit":
        message_to_edit = data[1]
        message_new_ver = data[2]
        if message_to_edit in messages_list:
            index = messages_list.index(message_to_edit)
            messages_list[index] = message_new_ver
    elif command == "Pin":
        message = data[1]
        messages_list.remove(message)
        messages_list.append(message)
    elif command == "Spam":
        message = data[1:]
        for el in message:
            messages_list.append(el)

for el in messages_list:
    print(el)
