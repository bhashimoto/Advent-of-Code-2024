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
            if data[i][j] == "A":
                found += find_my_x(data, [i,j])
    print(found)



def find_my_x(table: list[list[str]], center:list[int]) -> int:
    x = len(table[0])
    y = len(table)

    if center[0] <= 0 or center[0] >= y -1:
        return 0
    if center[1] <= 0 or center[1] >= x -1:
        return 0

    diags = 0
    if ((table[center[0]-1][center[1]-1] == "S" and table[center[0]+1][center[1]+1] == "M" ) or  
        (table[center[0]-1][center[1]-1] == "M" and table[center[0]+1][center[1]+1] == "S")):
        diags += 1
    if ((table[center[0]+1][center[1]-1] == "S" and table[center[0]-1][center[1]+1] == "M" ) or 
        (table[center[0]+1][center[1]-1] == "M" and table[center[0]-1][center[1]+1] == "S")):
        diags += 1
    if diags == 2:
        return 1
    else:
        return 0
run()
