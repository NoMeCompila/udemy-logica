function horizon(n){
    let stars = "";
    for(let i = 0; i < n; i++){
        stars += "*";
    }
    return stars;
}

function vert(n){
    count = -1;
    stars = "";
    for(let i = 0; i <= n-2; i++){
        count++;
        if(i == 0){
            stars+="*";
        }
        if(count == n-2){
            stars+="*";
        }

        stars+=" ";
    }
    return stars;
}

function square(n){
    console.log(horizon(n));    
    for(i = 0; i < n-2; i++){
        console.log(vert(n));
    }
    console.log(horizon(n));
}

square(7);
//square(4);