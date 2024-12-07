matrix_casche = {}
possible_loop_positions = []


def read_matrix():
    matrix = []
    with open('input6.txt') as f:
        i = 0
        for line in f:
            j = 0
            row = []
            for char in line.strip():
                row.append(char)
                matrix_casche[f"{i}_{j}"] = []
                j += 1
            matrix.append(row)
            i += 1

    return matrix


def on_board(x, y, matrix):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


def find_agent(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            agent_direction = is_agent(matrix[i][j])
            if agent_direction != -1:
                return i, j, agent_direction


def possible_loop(matrix, x, y, start_dir, block_x, block_y):
    if matrix[block_x][block_y] == '#' or not on_board(block_x, block_y, matrix) or matrix[block_x][block_y] == 'X':
        return False

    temp = matrix[block_x][block_y]

    matrix[block_x][block_y] = '0'
    loop_possible = run_loop(matrix, x, y, (start_dir + 1) % 4)
    matrix[block_x][block_y] = temp

    return loop_possible


def run_loop(matrix, x, y, move_dir):
    true_path = []
    path = []
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    next_x = x + moves[move_dir][0]
    next_y = y + moves[move_dir][1]

    while on_board(next_x, next_y, matrix):
        if (x, y, move_dir) in true_path:
            return True
        if matrix[next_x][next_y] == '#':
            move_dir = (move_dir + 1) % 4
        elif matrix[next_x][next_y] == '0':
            path = []
            move_dir = (move_dir + 1) % 4
        else:
            path.append((x, y, move_dir))
            true_path.append((x, y, move_dir))
            x = next_x
            y = next_y
        next_x = x + moves[move_dir][0]
        next_y = y + moves[move_dir][1]

    return False


def add_path_to_cache(path):
    for x, y, move_dir in path:
        add_move_to_cache(x, y, move_dir)


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


def add_move_to_cache(x, y, move_dir):
    if move_dir not in matrix_casche[f"{x}_{y}"]:
        matrix_casche[f"{x}_{y}"].append(move_dir)


def move_agent(start_x, start_y, agent_dir, matrix):
    i = 0
    total_possible_loop = 0
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x = start_x
    y = start_y

    next_x = start_x + moves[agent_dir][0]
    next_y = start_y + moves[agent_dir][1]

    while on_board(next_x, next_y, matrix):
        add_move_to_cache(x, y, agent_dir)
        if matrix[next_x][next_y] == '#':
            agent_dir = (agent_dir + 1) % 4
        else:
            if matrix[x][y] == '.':
                matrix[x][y] = 'X'

            add_move_to_cache(x, y, agent_dir)
            if possible_loop(matrix, x, y, agent_dir, next_x, next_y):
                total_possible_loop += 1
            x = next_x
            y = next_y
            print(i, total_possible_loop)
            i += 1
        next_x = x + moves[agent_dir][0]
        next_y = y + moves[agent_dir][1]

    return total_possible_loop


def main():
    print("starting")
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
