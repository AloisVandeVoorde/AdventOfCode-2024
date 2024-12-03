

def read_input():
    input_string = ''
    with open('input3-1.txt', 'r') as file:
        for line in file:
            input_string += line
    
    return input_string


def find_mul(input_string):
    total = 0
    expected = ['m', 'u', 'l','(']
    state = 0

    while input_string != '':
        char = input_string[0]
        input_string = input_string[1:]
        if char == expected[state]:
            state += 1
            if state == 4:
                gotNumbers, num1, num2, input_string = parse_numbers(input_string)
                if gotNumbers:
                    total += num1 * num2
                state = 0 
        else:
            state = 0
    
    return total

def parse_numbers(input_string):
    num1 = ''
    num2 = ''
    gotNumbers = False
    state = 0
    while input_string != '' and not gotNumbers:
        char = input_string[0]
        input_string = input_string[1:]
        if char.isdigit():
            if state == 0 or state == 1:
                num1 += char
                state = 1
            elif state == 2 or state == 3:
                num2 += char
                state = 3
        elif char == ',' and state == 1:
            state = 2
            num1 = int(num1)
        elif char == ')' and state == 3:
            gotNumbers = True
            num2 = int(num2)
        else:
            break;

    return gotNumbers, num1, num2, input_string


def main():
    input_string = read_input()
    print(find_mul(input_string))


main() # >>> 178538786

