let word = "invisible";
let json = {};

for (const elem of word){
    //console.log(elem);

    if(elem in json){
        json[elem] += 1;
    }else{
        json[elem] = 1;
    }
}

// Convertir el objeto en una matriz de tuplas
const entries = Object.entries(json);

// Ordenar la matriz por el valor de cada tupla
const sortedEntries = entries.sort((a, b) => b[1] - a[1]);

// Obtener la primera tupla de la matriz ordenada (que será la tupla con el mayor valor)
const [letter, value] = sortedEntries[0];
console.log(letter);
console.log(sortedEntries);
