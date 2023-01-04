let word1 = "Lapicero";
let word2 = "Copiarle";

let word3 = "Fer";
let word4 = "Asd";

function limpiar(p){
    return p.toLowerCase();
}

function transformToList(p){
    return p.split('').sort().join('');
}

function areAnagrams(p1, p2){
    if(transformToList(limpiar(p1)) == transformToList(limpiar(p2))){
        console.log("son anagramas");
    }else{
        console.log("no son anagramas");
    }
}

areAnagrams(word1, word2);
areAnagrams(word3, word4);

