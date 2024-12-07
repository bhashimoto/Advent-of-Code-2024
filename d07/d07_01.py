for_real = True

def run(for_real:bool):
    data = load_data(for_real)
    eqs = build_equations(data)
    result = 0
    for eq in eqs:
        if is_possible(eq[0], 0, eq[1]):
            result += eq[0]
    print(result)


def build_equations(data: list[str]):
    eqs = []
    for line in data:
        parts = line.split(": ")
        result = int(parts[0])
        nums = parts[1].split()
        eqs.append([result, list(map(int,nums))])

    return eqs

def load_data(for_real:bool) -> list[str]:
    filename = "input.txt" if for_real else "test.txt"

    data = None
    with open(filename) as file:
        data = file.readlines()
    return data

def is_possible(target:int, acc:int, eq:list[int]) -> bool:
    if len(eq) == 0:
        return target == acc

    addition = acc + eq[0]
    multiplication = acc * eq[0]

    return is_possible(target, addition, eq[1:]) or is_possible(target, multiplication, eq[1:])


    


run(for_real)
