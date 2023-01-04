let n = 5;

function getFactorial(num){
    if(num == 0 || num == 1){
        return 1;
    }else{
        return getFactorial(num-1) * num;
    }
}

console.log(getFactorial(n));