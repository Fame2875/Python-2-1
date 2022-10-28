def sortAscending(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
def sortDescending(lst):
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
def duplicate(lst):
    s = set()
    for x in lst:
        if x in s:
            return True
        s.add(x)
    return False

inp = list(map(int, list(input("Enter Input : "))))
if len(set(inp)) == 1:
    print("Repdrome")
elif sortAscending(inp):
    if duplicate(inp):
        print("Plaindrome")
    else:
        print("Metadrome")
elif sortDescending(inp) :
    if duplicate(inp):
        print("Nialpdrome")
    else:
        print("Katadrome")
else:
    print("Nondrome")