let phrase1 = "Hola Como estas";
let phrase2 = "MUCHO MAS CON MAYuscula";

function isUper(char){
    return char.toUpperCase() === char;
}

function isLower(char){
    return char.toLowerCase() === char;
}

function isUpperOrLower(str){
    let l1 = str.split('');
    let m = 0;
    let M = 0; 
    for (const char of l1) {
        if(isUper(char)){
            M++;
        }else if(isLower(char)){
            m++
        }
    }
    if(m > M){
        str.toLowerCase();
    }else{
        str.toUpperCase();
    }
    return str
}

console.log(isUpperOrLower(phrase1));
console.log(isUpperOrLower(phrase2));