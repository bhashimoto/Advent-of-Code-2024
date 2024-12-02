filename = "input.txt"

def run(filename:str) -> int:
    left = []
    right = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            left.append(int(data[0]))
            right.append(int(data[1]))

    left.sort()
    right.sort()

    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    return distance

result = run(filename)
print(result)

