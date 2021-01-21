import re

pattern = r"(?P<separator>::|\*{2})(?P<emoji>[A-Z][a-z]{2,})(?P=separator)"

data = input()
threshold = re.findall(r"\d", data)
threshold = [int(el) for el in threshold]

cool_threshold = 1
for num in threshold:
    cool_threshold *= num

matches = re.finditer(pattern, data)
match_check = re.match(pattern, data)
print(f"Cool threshold: {cool_threshold}")
match_list = []
match_for_print = {}
for match in matches:
    m = match.groupdict()
    match_list.append(m['emoji'])
    sum_point = 0
    for el in m['emoji']:
        sum_point += ord(el)
    if sum_point >= cool_threshold:
        match_for_print[m['emoji']] = m['separator']

print(f"{len(match_list)} emojis found in the text. The cool ones are:")
for key, value in match_for_print.items():
    print(f"{value}{key}{value} ")