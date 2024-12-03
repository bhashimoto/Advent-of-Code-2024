for_real = True

filename = "input.txt" if for_real else "test.txt"

def run(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(list(map(int,line.split())))

    safe = 0
    for line in data:
        if is_safe(line):
            # print(f"line {line} is safe")
            safe += 1

    return safe

def is_safe(line) -> bool:
    if line[1] > line[0]:
        return is_safe_asc(line)
    if line[1] < line[0]:
        return is_safe_desc(line)
    return False

def is_safe_asc(line) -> bool:
    for i in range(len(line)-1):
        if line[i] >= line[i+1]:
            return False
        if line[i] < line[i+1] - 3:
            return False
    return True

def is_safe_desc(line) -> bool:
    for i in range(len(line)-1):
        if line[i] <= line[i+1]:
            return False
        if line[i] > line[i+1] + 3:
            return False
    return True

print(run(filename))
