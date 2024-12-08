antinodes = []


def read_matrix_and_antennas():
    matrix = []
    antennas = {}

    with open('input8.txt') as f:
        x = 0
        for line in f:
            y = 0
            row = []
            for c in line.strip():
                if c != '.':
                    save_antenna(antennas, c, x, y)
                row.append(c)
                y += 1
            x += 1
            matrix.append(row)
            antinodes.append([0] * y)
        return matrix, antennas


def save_antenna(antennas, freq, x, y):
    if freq in antennas:
        antennas[freq].append((x, y))
    else:
        antennas[freq] = [(x, y)]


def get_distance(ant1, ant2):
    return ant1[0] - ant2[0], ant1[1] - ant2[1]


def place_antinode(x, y, matrix):
    if not (0 <= x < len(matrix) and 0 <= y < len(matrix[0])):
        return
    if antinodes[x][y] == '#':
        return

    antinodes[x][y] = '#'


def place_antinodes(antennas, matrix):
    antenna_queue = list(antennas)
    for ant1 in antennas:
        antenna_queue = antenna_queue[1:]
        for ant2 in antenna_queue:
            dx, dy = get_distance(ant1, ant2)
            place_antinode(ant1[0] + dx, ant1[1] + dy, matrix)
            place_antinode(ant2[0] - dx, ant2[1] - dy, matrix)


def count_antinodes():
    count = 0
    for row in antinodes:
        for c in row:
            if c == '#':
                count += 1
    return count


def main():
    matrix, antenna_list = read_matrix_and_antennas()
    for antenna_freq in antenna_list:
        antennas = antenna_list[antenna_freq]
        place_antinodes(antennas, matrix)
        # print(f'-------------{antenna_freq}----------------')
        # print_matrix(matrix)
    print(count_antinodes())
    # print_matrix(matrix)


def print_matrix(matrix):
    x = 0
    for row in matrix:
        y = 0
        for c in row:
            if antinodes[x][y] == '#' and c == '.':
                print('#', end='')
            else:
                print(c, end='')
            y += 1
        x += 1
        print()


main()
