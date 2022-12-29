let parragraph = "soy la palabra en una frase llena de PALABRA";
let word = "palabra";
let nums = 0; 
let list = [];

list = parragraph.split(' ');
//console.log(list);

list.forEach(elem => {
    //console.log(elem);
    if(elem.toLocaleLowerCase() === word){
        nums++;
    }
});

console.log(nums);