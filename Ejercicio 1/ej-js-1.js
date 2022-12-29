function title(n){
    ti = `tabla del ${n} \n`; 
    console.log(ti);
}

function numInput(){
    console.log("ingrese un número: ");
}

function generateTable(n){
    for(let i = 0; i <= 10; i++){
        console.log(`${n} * ${i} = ${n*i}`)
    }
}

function endApp(){
    process.exit();
}

function dataInput(){
    let num;
    numInput();
    process.stdin.on('data', function(data){
        num = data.toString().trim();        
        title(num);
        generateTable(num);
        endApp();
    });
}

dataInput();







