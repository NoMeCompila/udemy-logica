let parragraph = "La programación es el proceso de escribir y diseñar código informático para decirle a una"
+ "computadora qué debe hacer. Los programadores utilizan lenguajes de programación para escribir código, "
+ "que es un conjunto de instrucciones que le dicen a la computadora qué hacer. El código puede ser utilizado" 
+ "para crear programas informáticos, juegos, aplicaciones móviles, sitios web y mucho más.";
let word = "código";
let new_word = "-[CENSURADO]-";

let censored = parragraph.replace(new RegExp(word, "gi"), new_word);

console.log(censored);