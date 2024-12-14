for_real = True

def run(for_real):
    data = load_file() if for_real else "2333133121414131402"
    print("data:", data)
    disk_map = make_disk_map(data)
    print("disk map:\t", "".join(disk_map))
    compressed = compress(disk_map)
    print("compressed:\t", "".join(compressed))
    checksum = calculate_checksum(compressed)
    print("checksum:",checksum)

def load_file(filename:str="input.txt") -> str:
    with open(filename) as file:
        return file.read()[:-1]

def make_disk_map(data:str) -> list[str]:
    disk_map = []
    is_file = True
    file_id = 0
    for i in range(len(data)):
        c = "."
        if is_file:
            c = str(file_id)
            file_id += 1
        for _ in range(int(data[i])):
            disk_map.append(c)
        is_file = not is_file
    return disk_map

def compress(disk_map:list[str]) -> list[str]:
    empty_spaces = disk_map.count(".")
    compressed = disk_map
    curr = len(disk_map) - 1
    while empty_spaces:
        if compressed[curr] != '.':
            i = compressed.index('.')
            compressed[i], compressed[curr] = compressed[curr], compressed[i]
        curr -= 1
        empty_spaces -= 1

    return compressed

def calculate_checksum(compressed:list[str]) -> int:
    checksum = 0
    for i in range(len(compressed)):
        if compressed[i] == ".":
            break
        checksum += i*int(compressed[i])
    return checksum

run(for_real)
