import re

for_real = True

filename = "input.txt" if for_real else "test.txt"

data = None
with open(filename, "r") as file:
    data = file.read()


matches = re.findall("mul\([0-9]*,[0-9]*\)", data)
total = 0
for match in matches:
    nums = match.replace("mul(","").replace(")","").split(",")
    total += int(nums[0])*int(nums[1])
print(total)
