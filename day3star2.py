import re
z = True
t = 0
for line in open("input", "r"):
    for i in re.findall("do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)", line):
        if i == "don't()":
            z = False
        if i == "do()":
            z = True
        if i.startswith("mul("):
            comma = i.index(",")
            firstnum = i[4:comma]
            secondnum = i[comma+1:-1]
            if z:
                t += int(firstnum)*int(secondnum)

print(t)