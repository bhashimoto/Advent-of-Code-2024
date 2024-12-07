for_real = True

filename = "input.txt" if for_real else "test.txt"

data = []
with open(filename) as file:
    def load(line):
        return list(line)[:-1]
    data = list(map(load,file.readlines()))

counter = 0

directions = {
    'N': [-1, 0],
    'S': [ 1, 0],
    'E': [ 0, 1],
    'W': [ 0,-1]
}


def look_ahead(matrix, position, direction):
    next_i = position[0] + directions[direction][0]
    next_j = position[1] + directions[direction][1]
    if next_i < 0:
        return 'end'
    if next_i >= len(matrix):
        return 'end'
    if next_j < 0:
        return 'end'
    if next_j >= len(matrix[0]):
        return 'end'

    if matrix[next_i][next_j] == "#":
        return 'turn'

    return 'walk'

def turn(position):
    pos = ['N', 'E', 'S', 'W']
    next = pos[(pos.index(position)+1) % len(pos)]
    return next

def walk(position, direction):
    return [position[0] + directions[direction][0], position[1] + directions[direction][1]]

def get_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                return [i,j]
    return []

position = get_position(data)
direction = 'N'
visits = 1
while True:
    instruction = look_ahead(data, position, direction)
    if instruction == 'end':
        break
    elif instruction == 'turn':
        direction = turn(direction)
    else:
        data[position[0]][position[1]] = 'X'
        position = walk(position, direction)
        if data[position[0]][position[1]] != 'X':
            visits += 1



print(visits)
