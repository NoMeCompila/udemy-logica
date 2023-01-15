l1 = "Fernando Caballero es un profesional del area de la programacion es de Ctes y de Argentina"
lista = l1.split()
diccionario = {}

for i in lista:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1

mayor = max(diccionario, key= diccionario.get)

print(mayor)
print(diccionario.get(mayor))