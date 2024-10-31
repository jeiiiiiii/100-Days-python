target = int(input("Input number: "))

total = 0

for num in range(2, target + 1, 2):
    total += num
    print(total)