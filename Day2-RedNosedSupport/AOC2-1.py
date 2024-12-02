
import os

ls1 = []

with open('input2-1.txt', 'r') as file:
    for line in file:
        linesplit = line.split()
        ls1.append(linesplit)

total = 0
for l in ls1:
    asc = True
    desc = True
    prev = int(l[0])
    for li in l[1:]:
        curr = int(li)
        diff = curr - prev
        if diff > 0:
            desc = False
        if diff < 0:
            asc = False
        if abs(diff) < 1 or abs(diff) > 3:
            desc = asc = False
        prev = curr

    if asc or desc:
        total += 1

print(total)  # >>572
