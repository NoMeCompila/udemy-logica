class Empelado:
    def  __init__(self, nombre, apellido, sueldo, horario, cliente) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
        self.horario = horario
        self.cleinte = cliente

e1 = Empelado("Roque", "San", 250000, "8 hs", "Meta")

def get_attributs(obj: object) -> list:
    l1 = []
    for i in dir(obj):
        if not i.startswith('__'):
            l1.append(i)
    return l1

print(get_attributs(e1))