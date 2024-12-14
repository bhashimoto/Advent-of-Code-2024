for_real = True

ans = {}

def run(for_real:bool) -> None:
    blinks = 75
    data = str("9759 0 256219 60 1175776 113 6 92833") if for_real else str("0")
    stones = data.split()
    if not for_real:
        print(stones)
    stone_count = apply_rules(stones, blinks)
    print(stone_count)


def apply_rules(stones: list[str], blinks:int) -> int:
    if (tuple(stones), blinks) in ans:
        return ans[(tuple(stones), blinks)]

    if blinks == 0:
        ans[(tuple(stones), blinks)] = len(stones)
        return len(stones)

    stone_count = 0
    for stone in stones:
        new_stones = []
        if stone == "0":
            new_stones = ["1"]
        elif len(stone) % 2 == 0:
            new_stones = [str(int(stone[:int((len(stone)/2))])), str(int(stone[int(len(stone)/2):]))]
        else:
            new_stones = [str(int(stone)*2024)]
        stone_count += apply_rules(new_stones, blinks-1)
    ans[(tuple(stones),blinks)] = stone_count
    return stone_count

run(for_real)
