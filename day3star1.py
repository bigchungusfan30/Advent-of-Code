import re
t = 0
for line in open("input", "r"):
    for i in re.findall("mul\([0-9]+,[0-9]+\)", line):
        comma = i.index(",")
        firstnum = i[4:comma]
        secondnum = i[comma+1:-1]
        t += int(firstnum)*int(secondnum)

print(t)
