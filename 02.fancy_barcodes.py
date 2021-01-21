import re

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

n = int(input())

for _ in range(n):
    data = input()
    if re.match(pattern, data):
        match = re.findall(r"\d+", data)
        if match:
            print(f"Product group: {''.join(match)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")

