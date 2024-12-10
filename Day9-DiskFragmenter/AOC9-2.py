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


def compact_disk(disk):
    current_data_segment = []
    current_segment_id = '.'
    for i in range(len(disk) - 1):
        pointer = len(disk) - 1 - i
        print(pointer)
        if current_segment_id != '.':
            if disk[pointer] == current_segment_id:
                current_data_segment.append(disk[pointer])
            else:
                find_open_segment(disk, current_data_segment, pointer + 1)

        if disk[pointer] != current_segment_id:
            current_data_segment = [disk[pointer]]
            current_segment_id = disk[pointer]

    return disk


def find_open_segment(disk, data_segment, end):
    open_length = 0
    for i in range(end):
        if disk[i] == '.':
            open_length += 1
            if open_length == len(data_segment):
                swap_disk_segment(disk, len(data_segment), i - len(data_segment) + 1, end)
                return
        else:
            open_length = 0


def swap_disk_segment(disk, segment_length, pos1, pos2):
    for i in range(segment_length):
        disk[pos1 + i], disk[pos2 + i] = disk[pos2 + i], disk[pos1 + i]


def count_checksum(disk):
    total = 0
    for i in range(len(disk)):
        if disk[i] != '.':
            total += i * disk[i]

    return total


print(count_checksum(compact_disk(read_input())))
