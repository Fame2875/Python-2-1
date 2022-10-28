import math
x, y = map(float, input().split())
z = math.sqrt((x*x)+(y*y))
ans = "{:.6f}".format(z)
print(ans)
