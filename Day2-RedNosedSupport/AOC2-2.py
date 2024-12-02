
def main():
    ls1 = []
    
    with open('input2-1.txt', 'r') as file:
        for line in file:
            linesplit = line.split()
            ls1.append(linesplit)
    
    total = 0
    for l in ls1:
        if checkAllSafe(l):
            total += 1
        elif checkAllSafeDamped(l):
            total += 1

    return total

def checkAllSafeDamped(report):
    for i in range(0, len(report)):
        newReport = report.copy()
        newReport.pop(i)
        if checkAllSafe(newReport):
            return True
    return False

def checkAllSafe(report):
    return checkSafty(report, asc) or checkSafty(report, desc)

def checkSafty(report, checker):
    safe = True

    prev = int(report[0])
    for level in report[1:]:
        curr = int(level)
        diff = curr - prev
        
        if checker(diff):
                safe = False
        if abs(diff) < 1 or abs(diff) > 3:
                safe = False
        
        prev = curr
    return safe

def asc(diff):
    return diff < 0

def desc(diff):
    return diff > 0

print(main())  # >>612
