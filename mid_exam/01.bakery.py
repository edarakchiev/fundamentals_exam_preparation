biscuits_per_day = int(input())
workers = int(input())
competing_factory = int(input())

counter = 0
all_biscuits = 0
fabric_per_day = biscuits_per_day * workers

for day in range(1, 31):
    counter += 1
    if counter % 3 == 0:
        all_biscuits += int(fabric_per_day * 0.75)
        continue
    all_biscuits += fabric_per_day


print(f"You have produced {int(all_biscuits)} biscuits for the past month.")
difference = all_biscuits - competing_factory
percent = difference / competing_factory * 100
if all_biscuits > competing_factory:
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    print(f"You produce {percent*-1:.2f} percent less biscuits.")