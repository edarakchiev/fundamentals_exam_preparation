import re

pattern = r"(?P<sep>@|#)(?P<word_1>[A-Za-z]{3,})(?P=sep){2}(?P<word_2>[A-Za-z]{3,})(?P=sep)"

words = input()

mirror = []
counter = 0
matches = re.finditer(pattern, words)
for match in matches:
    counter += 1
    m = match.groupdict()
    word_1 = m["word_1"]
    word_2 = m["word_2"]
    word_check = word_2[::-1]
    if word_1 == word_check:
        mirror.append(f"{word_1} <=> {word_2}")

if counter > 0:
    print(f"{counter} word pairs found!")
else:
    print("No word pairs found!")
if mirror:
    print("The mirror words are:")
    print(', '.join(mirror))
else:
    print("No mirror words!")
