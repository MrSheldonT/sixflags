function generadorRandomCodigo(digits, max) {
    let randomCode = '';

    for (let i = 0; i < digits; i++) {
        const randomDigit = Math.floor(Math.random() * (max + 1));
        randomCode += randomDigit.toString();
    }

    return randomCode;
}

// Example usage
const code1 = generadorRandomCodigo(20, 9);
console.log('Random Code 1:', code1);

const code2 = generadorRandomCodigo(1, 1);
console.log('Random Code 2:', code2);


// elegir elemento de un arreglo

function elegirElemento(arreglo) {
    let randomIndex = Math.floor(Math.random() *  arreglo.length);
    return arreglo[randomIndex].toString();
}