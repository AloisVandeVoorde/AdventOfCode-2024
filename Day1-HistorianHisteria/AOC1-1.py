import os

ls1 = []
ls2 = []

with open('input1-1.txt', 'r') as file:
    for line in file:

        linesplit = line.split('   ')
        ls1.append(int(linesplit[0]))
        ls2.append(int(linesplit[1]))

ls2.sort()
ls1.sort()

total = 0
for i in range(len(ls1)):
    total += abs(ls1[i] - ls2[i])

print(total)  # >>1834060

