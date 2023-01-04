let n = 920

function get_dates(d){
    let años = Math.floor(d / 365);
    //console.log(`años: ${años}`);
    let remmaning_days = d % 365;
    let meses = Math.floor(remmaning_days / 30)
    //console.log(meses);
    let days = remmaning_days % 30
    console.log(`años: ${años} meses: ${meses} días: ${days}`);
} 

get_dates(n);