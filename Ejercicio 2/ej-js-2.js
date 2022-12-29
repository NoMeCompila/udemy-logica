function endApp(){
    process.exit();
}

function reverseWord(w){
    return w.split('').reverse().join('');
}

function isPalindrome(w){
    if (reverseWord(w) === w){
        console.log("Es un palíndromo");
    }else{
        console.log("No es un palíndromo");
    }
}

console.log("Ingrese una palabra: ")
process.stdin.on('data', function(data){
    let word = data.toString().trim();        
    isPalindrome(word);
    endApp();
});