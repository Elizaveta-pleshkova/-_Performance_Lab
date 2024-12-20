from itertools import cycle

n = int(input())
m = int(input())

array = []

for i in range(n):
    array.append(i + 1)

circular_array = cycle(array)

full_intervals = []
last_elem = 0
new_m = m

while last_elem != array[0]:
    interval = []
    if last_elem != 0:
        interval.append(last_elem)
        new_m = m - 1
    for i in range(new_m):
        last_elem = next(circular_array)
        interval.append(last_elem)
    full_intervals.append(interval)

resulting_path = []
for i in full_intervals:
    resulting_path.append(str(i[0]))

print("".join(resulting_path))
