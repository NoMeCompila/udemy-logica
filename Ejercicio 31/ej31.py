l1 = [1 , 2, 3, 4, 'Fer', True]
def only_quad_nums(l: list): 
    return list(map(lambda x: x**2,list(filter(lambda x: type(x) == int, l))))
print(only_quad_nums(l1))