
import os

ls1 = []
ls2 = []

with open('input1-1.txt', 'r') as file:
    for line in file:

        linesplit = line.split('   ')
        ls1.append(int(linesplit[0]))
        ls2.append(int(linesplit[1]))

ls2.sort()

dict2 = {}
for li in ls2:
    if li in dict2:
        dict2[li] += 1
    else:
        dict2[li] = 1


ls1.sort()

total = 0
for li in ls1:
    if li in dict2:
        total += li * dict2[li]

print(total)  # >>21607792
