let l1 = [1, 2, 3, 4, "a", 5, 1, 2];
let l2 = [];

for (const i of l1) {
    if(!isNaN(i) && !l2.includes(i)){
        l2.push(i);
    }
}

console.log(l2);