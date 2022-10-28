A = {1,2,3,4,5,6}
B ={0,2,4,6,8}
A.add(10)


print("Union :", A | B)
print("Union :",A.union(B))

print("Intersection :", A & B)
print("Intersection",A.intersection(B))

print("Difference :", A - B)
print("Difference",A.difference(B))
# A U B - A intersec B
print("Symmetric difference :", A ^ B)
print("Symmetric difference :",A.symmetric_difference(B))