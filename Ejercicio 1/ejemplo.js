var nombre;

console.log("ingrese nombre: ")

process.stdin.on('data', function(data){
    nombre = data.toString().trim();
    console.log(`Hola ${nombre}! \n`);
    process.exit();
});