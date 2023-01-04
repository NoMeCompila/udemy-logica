let n1 = 5;
let n2 = 7;
let n3 = 8;
let n4 = 9;
let n5 = 1;
let n6 = 1;

function mayor(x, y){
    let m = "both are equals";

    if(x > y){
        m = x;
    }else if(y > x){
        m = y;
    }
    return m;
}

console.log(mayor(n1, n2));
console.log(mayor(n3, n4));
console.log(mayor(n5, n6));