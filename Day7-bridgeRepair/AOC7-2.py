
def read_operations():
    operations = []
    with open('input7.txt') as f:
        for line in f:
            line = line.strip()
            operation = []
            split_on_equals = line.split(':')
            operation.append(split_on_equals[0].strip())
            operation.append(split_on_equals[1].split())
            operations.append(operation)
    return operations


def add(op1, op2):
    return op1 + op2

def multiply(op1, op2):
    return op1 * op2

def concat(op1, op2):
    return int(str(op1) + str(op2))

operands = [add, multiply, concat]

def calculate(result, curr, next_values):
    if len(next_values) == 0:
        return curr == result

    next_value = int(next_values[0])
    for operand in operands:
        if calculate(result, operand(curr, next_value), next_values[1:]):
            return True

    return False

def main():
    total = 0
    operations = read_operations()
    for operation in operations:
        result = int(operation[0])
        values = operation[1]
        if calculate(result, int(values[0]), values[1:]):
            total += result
    print(total)

main()
