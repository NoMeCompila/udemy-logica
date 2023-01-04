let l1 = [1,2,3,4,5];
let l2 = [1,2,4,5];

let n = 5;


function isPermutation(list, num){
    l3 = [];
    for(let i = 1; i <= num; i++){
        l3.push(i);
    }

    if (l3.length != list.length){
        return false;
    }
    
    for(let i = 0; i <= n; i++){
        if(l3[i] != list[i]){
            return false;
        }
    }
    return true;
}

console.log(isPermutation(l1, n));
console.log(isPermutation(l2, n));