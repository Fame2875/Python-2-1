inp = list(map(int, input("Enter Input : ").split()))
for x in range(len(inp)):
    min = x
    if inp[x] < 0:
        continue
    for y in range(x + 1, len(inp)):
        if inp[y] < inp[min] and inp[y] >= 0:
            min = y
    inp[min], inp[x] = inp[x], inp[min]
print(*inp)