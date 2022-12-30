let num = 10;
let divisors = [];

for(let i = 0; i <= num; i++){
    if(num%i == 0){
        divisors.push(i);
    }
}

console.log(divisors);