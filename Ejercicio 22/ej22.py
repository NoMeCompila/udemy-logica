n1 = 5
n2 = 7
n3 = 8
n4 = 9
n5 = 1
n6 = 1

def mayor(x, y):
    z = "both are equals"
    if x > y:
        z = x
    elif x < y:
        z = y
    return z

print(mayor(n1,n2))
print(mayor(n3,n4))
print(mayor(n5,n6))
