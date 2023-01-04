let num1 = 2002;
let num2 = 1234;

function capi(num){
    let reversed = num.toString().split('').reverse().join("");
    //console.log(reversed);
    return reversed === num
}

console.log(capi(num1));
console.log(capi(num2));
