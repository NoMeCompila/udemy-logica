let p1 = 0;
let p2 = 1;
let n = 10;


for(let i = 0; i <= n; i = i +1){
    let x = p2
    p2 += p1
    p1 = x;
    console.log(p2);
}