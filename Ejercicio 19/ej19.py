class Pelicula:
    def __init__(self, titulo="", visto=False):
        self.titulo = titulo
        self.visto = visto

    def was_viwed(self):
        if(self.visto):
            print(f"Ya viste {self.titulo}")
        else:
            print(f"Aún no viste {self.titulo}")

title1 = "Venom"
title2 = "Cyberpunk"
title3 = "asda"
title4 = "Top Gun"

p1 = Pelicula("Venom", True)
p2 = Pelicula("Merlina", True)
p3 = Pelicula("Cyberpunk", False)
p4 = Pelicula("WoW", False)
p5 = Pelicula("Top Gun", True)

films = [p1, p2, p3, p4, p5]

def mostrar(films : list, tit : str):
    titulos = [x.titulo for x in films]
    if tit in titulos:
        busqueda(films,tit)
    else:
        print(f"{tit} no se encuentra en la lista")

def busqueda(films, tit):
    for f in films:
        if(f.titulo == tit):
            f.was_viwed()
            
mostrar(films, title1)