for_real = True
size = [101, 103] if for_real else [11, 7]

def run(for_real):
    robots = load_file(for_real)

    steps = 0
    while True:
        steps += 1
        [robot.move() for robot in robots]
        if are_unique(robots):
            visualize(robots)
            print(steps)
            return


def are_unique(robots):
    positions = set([(r.position['x'], r.position['y']) for r in robots])
    return len(positions) == len(robots)


class Robot:
    def __init__(self, position, velocity):
        self.position = {'x': position[0], 'y': position[1]}
        self.velocity = {'x': velocity[0], 'y': velocity[1]}

    def move(self):
        self.position['x'] = (self.position['x'] + self.velocity['x']) % size[0]
        self.position['y'] = (self.position['y'] + self.velocity['y']) % size[1]
    
    def __str__(self):
        return f"p={self.position['x']},{self.position['y']} v={self.velocity['x']},{self.velocity['y']}"


def load_file(for_real):
    filename = "input.txt" if for_real else "test.txt"
    data = []
    with open(filename) as file:
        for line in file:
            parts = line.split()
            position = list(map(int,parts[0][2:].split(',')))
            velocity = list(map(int,parts[1][2:].split(',')))
            data.append(Robot(position, velocity))
    return data


def visualize(robots):
    mmap = [[0 for _ in range(size[0])] for _ in range(size[1])]
    for robot in robots:
        mmap[robot.position['y']][robot.position['x']] += 1
    for line in mmap:
        print("".join(list(map(str,line))).replace("0","."))


run(for_real)
