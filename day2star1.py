t = 0
for line in open("input", "r"):
    numbers = list(map(int, line.split()))
    if numbers == sorted(numbers) or numbers[::-1] == sorted(numbers):
        for i in range(1, len(numbers)):
            if not abs(numbers[i-1] - numbers[i]) or abs(numbers[i-1] - numbers[i]) > 3:
                break
        else:
            t += 1

print(t)
