
// let contador = 1;

// while (contador <= 10){
//     console.log(contador)
//     contador ++; //+= 1
// }
// console.log("fin del bucle")

// # while contador >= 1:
// #     print(contador) 
// #     contador -= 1
// # print("fin del bucle")
//-------------------------------------------------------------------------
// # 1. Escribir un programa que solicite ingresar 10 notas de alumnos 
// y nos informe cuántos tienen notas mayores o iguales a 7
// y cuántos menores.  

let aprobados = 0;
let reprobados = 0;
let contador = 1;

while (contador <= 10){
    let nota = parseFloat(prompt("ingrese las notas "+ contador + ":"))

    if (nota >= 7 ){
        aprobados ++;// 0 +1 =  1 +1 = 2+ 1 = 3
    }else{
        reprobados++;
    }
    contador ++;
}
console.log("la cantidad de alumnos con notas iguales o mayor a 7 es: ", aprobados)
console.log("la cantidad de alumnos con notas menor a 7 es: ", reprobados)