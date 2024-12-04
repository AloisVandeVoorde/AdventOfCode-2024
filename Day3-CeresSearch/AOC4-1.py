def get_text_matrix():
    matrix = []
    with open('input4-1.txt', 'r') as file:
        for line in file:
            matrix.append(line)

    return matrix
def check_for_sequence(matrix, sequence, startx, starty, expected):
    max_x = len(matrix[0])
    max_y = len(matrix)

    for i in range(len(sequence)):
        x_pos = startx + sequence[i][0]
        y_pos = starty + sequence[i][1]
        
        if x_pos < 0 or x_pos >= max_x or y_pos < 0 or y_pos >= max_y:
            return False
        if matrix[y_pos][x_pos] != expected[i]:
                return False

    return True


def detect_mas(matrix, startx, starty):
    amount_of_mas = 0
    mask = [
        [(0,1),(0,2),(0,3)],
        [(1,0),(2,0),(3,0)],
        [(1,1),(2,2),(3,3)],
        [(-1,1),(-2,2),(-3,3)],
        [(1,-1),(2,-2),(3,-3)],
        [(-1,-1),(-2,-2),(-3,-3)],
        [(0,-1),(0,-2),(0,-3)],
        [(-1,0),(-2,0),(-3,0)]
    ]

    expected = ['M','A','S']

    for i in range(len(mask)):
        if check_for_sequence(matrix, mask[i], startx, starty, expected):
            amount_of_mas += 1

    return amount_of_mas

def scan_matrix(matrix):
    total = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 'X':
                total += detect_mas(matrix, x, y)
    return total 

def main():
    matrix = get_text_matrix()
    print(scan_matrix(matrix))

if __name__ == '__main__':
    main()
