from pprint import pprint
alumnos = [["Fernando", 8],["Viviana", 10],["Roque", 7],["Evelin", 5],["Victor", 4]]

aprobados = list(filter(lambda x: x[1] >= 6, alumnos))
desaprobados = list(filter(lambda x:x[1] < 6, alumnos))

print(f"aprobados: {len(aprobados)} | desaprobados: {len(desaprobados)}")