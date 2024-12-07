def read_matrix():
    matrix = []
    with open('input6.txt') as f:
        for line in f:
            row = []
            for char in line.strip():
                row.append(char)
            matrix.append(row)
    return matrix


def on_board(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def find_agent(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            agent_direction = is_agent(matrix[i][j])
            if agent_direction != -1:
                return i, j, agent_direction


def is_agent(char):
    if char == '>':
        return 0
    if char == 'v':
        return 1
    if char == '<':
        return 2
    if char == '^':
        return 3
    return -1


def move_agent(start_x, start_y, agent_dir, matrix):
    total_moves = 0
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x = start_x
    y = start_y

    next_x = start_x + moves[agent_dir][0]
    next_y = start_y + moves[agent_dir][1]

    while on_board(next_x, next_y, matrix):
        if matrix[next_x][next_y] == '#':
            agent_dir = (agent_dir + 1) % 4
        else:
            if matrix[x][y] != 'X':
                matrix[x][y] = 'X'
                total_moves += 1
            x = next_x
            y = next_y
        next_x = x + moves[agent_dir][0]
        next_y = y + moves[agent_dir][1]

    if matrix[x][y] != 'X':
        matrix[x][y] = 'X'
        total_moves += 1

    return total_moves


def main():
    matrix = read_matrix()
    print(f"read matrix of size {len(matrix)}x{len(matrix[0])}")
    start_x, start_y, agent_dir = find_agent(matrix)
    print(f"found agent at {start_x}, {start_y} facing {agent_dir}")
    print(move_agent(start_x, start_y, agent_dir, matrix))
    print_matrix(matrix)


def print_matrix(matrix):
    for row in matrix:
        for char in row:
            print(char, end='')
        print()

main()
