for_real = True

def run(for_real:bool) -> None:
    blinks = 25
    data = str("9759 0 256219 60 1175776 113 6 92833") if for_real else str("125 17")
    stones = data.split()
    if not for_real:
        print(stones)
    for i in range(1, blinks + 1):
        stones = apply_rules(stones)
        if not for_real:
            print(f"After blink #{i}: {stones}")
    print(len(stones))


def apply_rules(stones: list[str]) -> list[str]:
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            listed = list(stone)
            left = str(int("".join(listed[:len(stone)//2])))
            right = str(int("".join(listed[len(stone)//2:])))
            new_stones.extend([left, right])
        else:
            new_stones.append(str(int(stone)*2024))
    return new_stones

run(for_real)
