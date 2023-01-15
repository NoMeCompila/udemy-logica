class Persona:
    def __init__(self, nombre: str, hobbies: list) -> None:
        self.nombre = nombre
        self.hobbies = hobbies

p1 = Persona("Fernando", ["Programación", "Música", "Videojuegos"])
p2 = Persona("Juan", ["Futbol", "Música", "Natación"])
p3 = Persona("Fernando", ["Boxeo", "Futbol", "Política"])
p4 = Persona("Fernando", ["Teatro", "Running", "Futbol"])

# cual es el hobbie que mas se repite
lista_personas = [p1, p2, p3, p4]

lista_hobbies = []
for p in lista_personas:
    lista_hobbies += p.hobbies

cant_hobbies = {}

for i in lista_hobbies:
    if i in cant_hobbies:
        cant_hobbies[i] += 1
    else:
        cant_hobbies[i] = 1

#print(cant_hobbies)
maximo_hobbie = max(cant_hobbies, key = cant_hobbies.get)
print(f"El hobbie que mas se repite es: {maximo_hobbie} con un total de {cant_hobbies.get(maximo_hobbie)} veces")