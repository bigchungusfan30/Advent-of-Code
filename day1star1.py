t = 0
left, right = [], []
for a in open("input", "r"):
    numbers = a.split("   ")
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))
left.sort()
right.sort()
for (left, right) in zip(left, right):
    t += abs(left - right)

print(t)
