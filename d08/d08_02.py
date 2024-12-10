for_real = True


def run():
    filename = 'input.txt' if for_real else "test.txt"
    data = load(filename)
    antennas = get_antennas(data)
    antinodes = get_antinodes_positions(data, antennas)
    print(len(set(antinodes)))

def load(filename):
    with open(filename) as file:
        data = list(map(lambda x: list(x)[:-1], file.readlines()))
    return data

def get_antennas(data: list[list[str]]):
    antennas = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] not in antennas:
                antennas[data[i][j]] = []
            antennas[data[i][j]].append((i,j))
    antennas.pop(".")
    return antennas

def get_antinodes_positions(data, antennas):
    antinodes = set()
    for a in antennas:
        for i in range(len(antennas[a])-1):
            for j in range(i+1, len(antennas[a])):
                nodes = calculate_antinodes_with_harmonics(data, antennas[a][i], antennas[a][j])
                for node in nodes:
                    antinodes.add(node)
    return antinodes



def calculate_antinodes(data, n1, n2):
    antinodes = []
    I = range(len(data))
    J = range(len(data[0]))

    dist = get_distance(n1, n2)
    p1 = (n1[0] - dist[0], n1[1] - dist[1])
    p2 = (n2[0] + dist[0], n2[1] + dist[1])

    if p1[0] in I and p1[1] in J:
        antinodes.append(p1)
    if p2[0] in I and p2[1] in J:
        antinodes.append(p2)
    return antinodes

def calculate_antinodes_with_harmonics(data, n1, n2):
    antinodes = []
    I = range(len(data))
    J = range(len(data[0]))

    dist = get_distance(n1, n2)
    antinodes += get_harmonics(I, J, n1, dist)
    antinodes += get_harmonics(I, J, n2, dist)

    return antinodes


def get_distance(n1, n2):
    return (n2[0] - n1[0], n2[1] - n1[1])

def get_harmonics(I, J, node, dist):
    an = [node]
    curr = node
    while curr[0] in I and curr[1] in J:
        an += [curr]
        new_node = (curr[0] + dist[0], curr[1] + dist[1])
        curr = new_node
    curr = node
    while curr[0] in I and curr[1] in J:
        an += [curr]
        new_node = (curr[0] - dist[0], curr[1] - dist[1])
        curr = new_node
    return an

run()
