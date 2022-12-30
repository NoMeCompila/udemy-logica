class Pelicula {
    constructor(titulo, visto) {
      this.titulo = titulo;
      this.visto = visto;
    }

    wasViwed() {
        if(this.visto){
            console.log(`ya viste ${this.titulo}`);
        }else{
            console.log(`aún no viste ${this.titulo}`);
        }
    }
}

p1 = new Pelicula("Venom", true);
p2 = new Pelicula("Merlina", false);
p3 = new Pelicula("asds", true);

lista = [p1, p2, p3];

function busqueda(lista, titulo){
    for (const peli of lista) {
        if(titulo == peli.titulo){
            peli.wasViwed();
        }       
    }
}

function mostrar(lista, titulo){
    titulos = []
    for (const i of lista) {
        titulos.push(i.titulo);
    }

    if(titulos.includes(titulo)){
        busqueda(lista, titulo);
    }else{
        console.log("no se encuentra esa pelicula en lista");
    }
}

mostrar(lista, "Merlina");