target = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if index < len(target):
        value = target[index]
        target[index] = -1
        for i in range(len(target)):
            if target[i] == -1:
                continue
            if target[i] > value:
                target[i] -= value
            elif target[i] <= value:
                target[i] += value

print(f"Shot targets: {target.count(-1)} -> {' '.join(str(el) for el in target)}")
