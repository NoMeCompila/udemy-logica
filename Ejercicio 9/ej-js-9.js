let l1 = [1, 2, 3, 4];
let l2 = [3, 4, 5, 6];

let l3 = [];

for(let i = 0; i < l1.length; i++){
    for(let j = 0; j < l2.length; j++){
        if(l1[i] == l2[j]){
            l3.push(l1[i]);
        }
    }
}

console.log(l3);