l1 = [1, 2, 3, 4, "a", 5, 1, 2]
print(l1)
l2 = []
for i in l1:
    if type(i) == int:
        l2.append(i)
print(l2)
c = set(l2)
print(list(c))