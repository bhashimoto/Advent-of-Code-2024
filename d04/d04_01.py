for_real = True

filename = "input.txt" if for_real else "test.txt"

def run():
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data.append(list(line)[:-1])


    found = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            found += find_word(data, [i,j], "XMAS")
    print(found)



def find_word(table: list[list[str]], start:list[int], word:str) -> int:
    directions = {
        'N' : [-1, 0],
        'S' : [ 1, 0],
        'E' : [ 0, 1],
        'W' : [ 0,-1],
        'NE': [-1, 1],
        'NW': [-1,-1],
        'SE': [ 1, 1],
        'SW': [ 1,-1],
    }

    x = len(table[0])
    y = len(table)

    count = 0
    for direction in directions:
        pos = start
        found = True
        for letter in word:
            if pos[0] < 0 or pos[0] >= y:
                found = False
                break
            if pos[1] < 0 or pos[1] >= x:
                found = False
                break
            if table[pos[0]][pos[1]] != letter:
                found = False
                break
            pos = [pos[0] + directions[direction][0], pos[1] + directions[direction][1]]
        if found:
            count += 1
    return count

run()
