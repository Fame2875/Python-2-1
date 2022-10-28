i = 0
while i < 10:
    x = int(input())
    x %= 42
    x = str(x)
    i += 1
    if i == 1:
        Input = [x]
    else:
        Input.append(x)
else:
    Set = set(Input)
    print(len(Set))
