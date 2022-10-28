def BSTH(l, r, arr, x):
    if r >= l:
        mid = (r + l) // 2

        if arr[mid] == x:
         return "Found"
        elif arr[mid] > x:
         return BSTH(l, mid - 1, arr, x)
        else:
         return BSTH(mid + 1, r, arr, x)

    else:
        return "Not Found"




a = input('Enter Input : ').split('/')
arr, k = list(map(int, a[0].split())), int(a[1])
print(BSTH(0, len(arr) - 1, sorted(arr), k))
