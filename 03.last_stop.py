def is_exist(collection, item):
    if item in collection:
        return True


collection = list(map(int, input().split()))
while True:
    data = input()
    if data == "END":
        break
    data = data.split()
    instruction = data[0]

    if instruction == "Change":
        p_num = int(data[1])
        c_num = int(data[2])
        if is_exist(collection, p_num):
            i = collection.index(p_num)
            collection[i] = c_num
    elif instruction == "Hide":
        p_num = int(data[1])
        if is_exist(collection, p_num):
            collection.remove(p_num)
    elif instruction == "Switch":
        c_num = int(data[2])
        p_num = int(data[1])
        if is_exist(collection, p_num) and is_exist(collection, c_num):
            i_p_num = collection.index(p_num)
            i_c_num = collection.index(c_num)
            collection[i_p_num], collection[i_c_num] = collection[i_c_num], collection[i_p_num]
    elif instruction == "Insert":
        c_num = int(data[2])
        index = int(data[1])
        if index < len(collection):
            collection.insert(index + 1, c_num)
    elif instruction == "Reverse":
        collection.reverse()

print(' '.join(str(el) for el in collection))