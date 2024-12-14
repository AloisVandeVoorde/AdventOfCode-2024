
def read_map():
    mmap = []
    with open("input10.txt") as f:
        for line in f:
            mmap.append([char for char in line.strip()])
    return mmap


def find_starting_points(mmap):
    starting_points = []
    for i in range(len(mmap)):
        for j in range(len(mmap[i])):
            if mmap[i][j] == '0':
                starting_points.append((i, j))

    return starting_points


def return_all_possible_ends(startx, starty, mmap):
    current_height = mmap[startx][starty]
    if current_height == '9':
        return [(startx, starty)]

    possible_paths = find_posible_directions(startx, starty, current_height, mmap)
    result = []
    for path in possible_paths:
        result.extend(return_all_possible_ends(path[0], path[1], mmap))
    return result


def find_posible_directions(x, y, height, mmap):
    possible_paths = []
    if onBoard(x + 1, y, mmap) and mmap[x + 1][y] == str(int(height) + 1):
        possible_paths.append((x + 1, y))
    if onBoard(x - 1, y, mmap) and mmap[x - 1][y] == str(int(height) + 1):
        possible_paths.append((x - 1, y))
    if onBoard(x, y + 1, mmap) and mmap[x][y + 1] == str(int(height) + 1):
        possible_paths.append((x, y + 1))
    if onBoard(x, y - 1, mmap) and mmap[x][y - 1] == str(int(height) + 1):
        possible_paths.append((x, y - 1))
    return possible_paths


def onBoard(x, y, mmap):
    height = len(mmap)
    width = len(mmap[0])
    return 0 <= x < height and 0 <= y < width


def main():
    mmap = read_map()
    starting_points = find_starting_points(mmap)
    result = 0
    for point in starting_points:
        end_points_in_reach = return_all_possible_ends(point[0], point[1], mmap)
        result += len(end_points_in_reach)

    print(result)


def print_end_points(mmap, positions, startx, starty):
    print(f"Start: {startx}, {starty}, End: {positions}")
    for i in range(len(mmap)):
        for j in range(len(mmap[i])):
            if (i, j) in positions:
                print('X', end='')
            elif i == startx and j == starty:
                print('S', end='')
            else:
                print('.', end='')
        print()


main()
