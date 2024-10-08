// """
// if condicion {
//     ejecutece el codigo
// }else {
//     ejecutece el siguiente codigo 
//    }
// """
// let num1 = 8;
// let num2 = 88;

// if (num1 >= num2) {
//     console.log("es TRUE");
// }else{
//     console.log("es FALSE");
// }

//PY
// # num1 = 8
// # num2 = 88

// # if num1 >= num2 :
// #     print("es TRUE")
// # else:
// #     print("es FALSE")

//--------------------------------------------------------
// let edad = prompt("ingrese su edad")

// if (edad >= 18){
//     console.log("eres mayor de edad")
// }else{
//     console.log(`eres menor de edad, la faltan ${18-edad} años para ser mayor de edad`)
// }
//---------------------------------------------------------------------------------------
//calcular precio con descuento
// let precio = parseFloat(prompt("ingrese el precio del producto: "))
// let desceunto = parseFloat(prompt("ingrese el descuento: "))

// let cupon = prompt("si tiene un cupon tendra un desceunto si o no ")

// if (cupon == "si") {
//     descuentoCupon = (precio * desceunto) /100
//     // total = precio - descuentoCupon


//     console.log(" total a pagar con descuento es: ", precio - descuentoCupon)
//     // console.log("total a pagar con descuento es de: ",total)
// }else{
//     console.log("no tiene descuento valor a pagar :", precio)
// }

//-----------------------------------------------------------------------------
// Escribe un programa que reciba la calificación de un estudiante (de 0 a 100) 
// e imprima una clasificación según el rango:

// 90-100: Excelente
// 70-89: Aprobado
// 50-69: Necesita mejorar
// 0-49: Reprobado
let calificacion = prompt("ingrese la calificacion del estudiante de 0 a 100")

if( calificacion === "90" ){
    console.log("Excelente")
}else if (calificacion >= 70 && calificacion <= 89 ){
    console.log("Aprobado")

}else if (calificacion >=50 && calificacion <= 69){
    console.log("necesita mejorar")
}else{
    console.log("Reprobo")
}
//----------------------------------------------------------------------------------
// Escribe un programa que reciba tres números que representan los lados de un triángulo
//  e imprima si el triángulo es Equilátero (todos los lados iguales), Isósceles 
//  (dos lados iguales) o Escaleno (todos los lados diferentes). 
//  Asegúrate de que los números formen un triángulo válido.
let lado1 = prompt("Ingresa la longitud del primer lado:");
let lado2 = prompt("Ingresa la longitud del segundo lado:");
let lado3 = prompt("Ingresa la longitud del tercer lado:");

if (lado1 == lado2 && lado2 == lado3) {
    console.log("El triángulo es Equilátero.");
} else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3) {
    console.log("El triángulo es Isósceles.");
} else {
    console.log("El triángulo es Escaleno.");
}
