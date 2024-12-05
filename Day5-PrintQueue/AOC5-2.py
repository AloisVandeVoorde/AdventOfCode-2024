
def read_input():
    rules = {}
    update_queues = []
    with open('input5.txt') as f:
        for line in f:
            if '|' in line:
                new_rule = line.strip().split('|')
                if new_rule[0] not in rules:
                    rules[new_rule[0]] = []
                if new_rule[1] not in rules:
                    rules[new_rule[1]] = []
                rules[new_rule[0]].append(new_rule[1])
            elif ',' in line:
                new_update = line.strip().split(',')
                update_queues.append(new_update)
    return rules, update_queues

def main():
    total = 0
    rules, update_queues = read_input()
    for update in update_queues:
        if (check_update(rules, update) == 0):
            updated_update = update_update(update, rules)
            total += check_update(rules, updated_update)
    print(total)


def check_update(rules, update):
    prev = []
    for x in update:
        rule = rules[x]
        for p in prev:
            if p in rule:
                return 0
        prev.append(x)
    return int(prev[len(prev)//2])

def update_update(update, rules):
    new_update = []
    for x in update:
        rule = rules[x]
        i = 0
        for y in new_update:
            if y in rule:
                break
            i += 1
        new_update.insert(i, x)
    return new_update

main()
