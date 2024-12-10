def read_input():
    id = 0
    disk = []
    with open('input9.txt') as f:
        data = True
        for c in f.read().strip():
            disk_data = id if data else '.'
            for _ in range(int(c)):
                disk.append(disk_data)
            id += 1 if data else 0
            data = not data
    return disk

print(read_input())


def fragment_disk(disk):
    pointer1 = 0
    pointer2 = len(disk) - 1

    while pointer1 < pointer2:
        if disk[pointer1] != '.':
            pointer1 += 1
        elif disk[pointer2] == '.':
            pointer2 -= 1
        else:
            disk[pointer1], disk[pointer2] = disk[pointer2], disk[pointer1]
            pointer1 += 1
            pointer2 -= 1
    return disk


def count_checksum(disk):
    total = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            return total
        
        total += i*disk[i]


print(count_checksum(fragment_disk(read_input())))
