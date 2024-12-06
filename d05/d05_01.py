for_real = True
filename = "input.txt" if for_real else "test.txt"

file = open(filename, "r")
data = file.read()
file.close()

parts = data.split("\n\n")
rules = {}
temp = parts[1].split("\n")[:-1]
updates = []
for i in range(len(temp)):
    updates.append(list(map(int,temp[i].split(','))))

for line in parts[0].split("\n"):
    rule = list(map(int, line.split("|")))
    if rule[0] not in rules:
        rules[rule[0]] = set()
    rules[rule[0]].add(rule[1])

valid_updates = []
for update in updates:
    valid = True
    for i in range(len(update)):
        if update[i] in rules and valid:
            intersection = set(update[:i]).intersection(rules[update[i]])
            if len(intersection) > 0:
                valid = False
    if valid:
        print(f"update {update} is valid")
        valid_updates.append(update)

result = 0
for up in valid_updates:
    mid = int(up[len(up)//2])
    result += mid

print(result)

    
