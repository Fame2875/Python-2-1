def findAlphabet(x):
    for i in x:
        if 'a' <= i <= 'z':
            return (ord(i))
    return 0

def sort(inp):
    key = []
    value = []
    for i in inp:
        key.append(findAlphabet(i))
        value.append(i)

    for i in range(len(key)):
        min = i
        for j in range(i+1, len(key)):
            if key[j] < key[min] and key[j] >= 0:
                min = j
        key[min], key[i] = key[i], key[min]
        value[min], value[i] = value[i], value[min]
    return value

inp = input("Enter Input : ").split()
print(*sort(inp))