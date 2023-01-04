let sentence = "fernando juan antonio caballero";

let a = "fernando";
let c = a[0] = a.charAt(0).toUpperCase() + a.slice(1,);

console.log(c);
let lista1 = sentence.split(" ");

let lista2 = lista1.map(a => a[0] = a.charAt(0).toUpperCase() + a.slice(1,))

console.log(lista2.join(" "))