import re

for_real = True

filename = "input.txt" if for_real else "test2.txt"

data = None
with open(filename, "r") as file:
    data = file.read()

lines = data.split("don't()")
total = 0
for i in range(len(lines)):
    line = ""
    if i == 0:
        line = lines[i]
    else:
        parts = lines[i].split("do()",1)
        if len(parts) == 2:
            line = parts[1]

    matches = re.findall(r"mul\([0-9]*,[0-9]*\)", line)
    for match in matches:
        nums = match.replace("mul(","").replace(")","").split(",")
        total += int(nums[0])*int(nums[1])
print(total)
