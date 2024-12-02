filename = "input.txt"

def run(filename:str) -> int:
    left = []
    right = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            left.append(int(data[0]))
            right.append(int(data[1]))

    frequency = {}
    for item in right:
        if item not in frequency:
            frequency[item] = 0
        frequency[item] += 1

    similarity = 0
    for item in left:
        if item in frequency:
            similarity += frequency[item]*item
    return similarity

result = run(filename)
print(result)

