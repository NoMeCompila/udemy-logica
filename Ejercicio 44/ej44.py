l1 = ["Fernando Caballero", "San Francisco", "Hola", "Fer", "Think Big"]
l2 = list(filter(lambda x:len(x.split()) > 1, l1))
print(l2)