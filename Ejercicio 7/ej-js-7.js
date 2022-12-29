let x = 1;
let y = 10;

function do_list(init, end){
    let l = [];
    for(let i = init; i <= end; i++){
        l.push(i);
    }
    return l;
}

function get_odds(x,y){
    return do_list(x,y).filter(x => x%2 != 0).length;
}

console.log(get_odds(x, y));