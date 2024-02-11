s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])

print(s1 | s2)
print(s1.union(s2))

print(s1 & s2)
print(s1.intersection(s2))

print(s1 - s2)
print(s1.difference(s2))
print(s2 - s1)
print(s2.difference(s1))