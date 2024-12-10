t = 0
left, right = [], []
for a in open("input", "r"):
    numbers = a.split("   ")
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))
for l in left:
    c = right.count(l)
    t += c*l

print(t)
