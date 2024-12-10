t = 0
for line in open("input", "r"):
    numbers = list(map(int, line.split()))
    for j in range(len(numbers)):
        nnumbers = numbers[:j] + numbers[j + 1:]
        if nnumbers == sorted(nnumbers) or nnumbers[::-1] == sorted(nnumbers):
            for i in range(1, len(nnumbers)):
                if not abs(nnumbers[i-1] - nnumbers[i]) or abs(nnumbers[i-1] - nnumbers[i]) > 3:
                    break
            else:
                t += 1
                break

print(t)
