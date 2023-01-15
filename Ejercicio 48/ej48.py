parragraph = "palabra palabra hola palabra libro libro"
palabras_sin_repetir = list(set(parragraph.split()))
x = ""
for i in palabras_sin_repetir:
    if parragraph.count(i) == 1:
        x = i

print([list(x), list(x)[0]])

