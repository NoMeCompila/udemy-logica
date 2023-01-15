l1 = [10,9,9,8,8,10,10]

def get_average1(l: list):
    suma = 0
    cant = 0
    for i in l:
        suma += i
        cant += 1
    return suma / cant

def get_average2(l: list):
    return sum(l) / len(l)

print(get_average1(l1))
print(get_average2(l1))