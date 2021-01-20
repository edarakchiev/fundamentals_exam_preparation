series = input().split()

while True:
    data = input()
    if data == "end":
        break

    data = data.split()
    command = data[0]
    if command == "reverse":
        start = int(data[2])
        count = int(data[4])
        stop = start + count
        reverse_part = series[start:stop]
        reverse_part.reverse()
        left_side = series[:start]
        right_side = series[stop:]
        series = left_side + reverse_part + right_side
    elif command == "sort":
        start = int(data[2])
        count = int(data[4])
        stop = start + count
        sort_part = series[start:stop]
        sort_part.sort()
        left_side_sort = series[:start]
        right_side_sort = series[stop:]
        series = left_side_sort + sort_part + right_side_sort
    elif command == "remove":
        count = int(data[1])
        series = series[count:]

str_series = [str(el) for el in series]
print(', '.join(str_series))
