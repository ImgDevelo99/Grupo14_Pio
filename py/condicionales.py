"""
if condicion :
    ejecutece el codigo
else :
    ejecutece el siguiente codigo   
"""
# num1 = 8
# num2 = 88

# if num1 >= num2 :
#     print("es TRUE")
# else:
#     print("es FALSE")

#--------------------------------------------------------------
"""
crearun programa para indicarle al usuario si es mayor de edad podra conducir, soliciar por
consola la edad y si es colombiano
"""
# edad = int(input("ingrese su edad: "))
# nacionalidad = True

# if edad >= 18 and nacionalidad == True :
#     print("usted puede condicir TRUE")
# else:
#     print("No puede condicir FALSE")

# print("felicitaciones")

#----------------------------------------------
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# password = "admin123"
# passInput = input("ingrese su contraseña: ")

# if password.lower() == passInput.lower() :
#     print("contraseña correcta. Bienvenido")
# else:
#     print("contraseña incorrecta por favor verifique")

#--------------------------------------------------------------------
 # //La entrada a un circo vale  x pesos por persona, 
# 	//sin embargo, si la edad de la persona es menor 
# 	//de 10 años se le da un descuento del 25% en el 
# 	//valor del boleto. Escribir el código que 
# 	//calcule y muestre lo que pagará por la entrada 
# 	//al circo según la edad.
# precioBoleto = float(input("ingrese el precio del boleto: "))
# edad = int(input("ingrese la edad de la persona: "))

# if edad < 10 :
#     descuento = precioBoleto * 0.25
#     print(f"el precio a pagar con descuento del 25 % es: {precioBoleto - descuento}")
# else:
#     print("no tiene descuento, total a pagar" , precioBoleto)

#--------------------------------------------------------------------
#escribir u programa donde al usuario ingrese la calificacion de 0 a 10, el programa debe clasificar
# mayor o igual a 9 = excelente
# 7 y 8.9 = sobresaliente
# 5 y 6.9 = aceptable
# menos de 5 = insuficiente

# calificacion = float(input("ingrese la calificacion entre 0 y 10: "))

# if calificacion >= 9 :
#     print("su nota es Excelente")
# elif calificacion >= 7:
#     print("su nota es sobresaliente")
# elif calificacion >= 5 :
#     print("su nota es aceptable")
# else:
#     print("su nota es insuficiente")

#----------------------------------------------------------------    
#solicitarle al usuario que ingrese un numero del 1 al 7, e indicar que dia de la semana es:

#---------------------------------------------------------------
#escribir un programa donde le solicitemos al usuario que ingres los 3 lados del triangulo, el programa me debe 
#indicar si el triangulo es EQUILATERO(todos los lados iguales),el triangulo es ISOCELES(dos lados iguales
#  y uno diferente) triangulo escaleno (todos los lados son diferentes)...............
#-----------------------------------------------------------------
# lado1 = float(input("ingrese la longitud del primer lado: "))
# lado2 = float(input("ingrese la longitud del segundo lado: "))
# lado3 = float(input("ingrese la longitud del tercer lado: "))

# if lado1 == lado2 and lado1 == lado3 and lado2 == lado3 :
#     print("el triangulo es  EQUILATERO")
# elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
#     print("el triangulo es  ISOCELES")
# else:
#     print("el triangulo es ESCALENO")

#-------------------------------------------------------------------------
# 1. Escribe un programa que solicite al usuario ingresar un año y determine si es un año bisiesto.
# Un año es bisiesto si es divisible por 4, pero no por 100, excepto si también es divisible por 400.      

# 2. Escribe un programa que solicite al usuario ingresar su edad y verifique lo siguiente:

# Si la edad es menor a 12 años, mostrar "Eres un niño".
# Si la edad es mayor o igual a 12 pero menor a 18, mostrar "Eres un adolescente".
# Si la edad es mayor o igual a 18 pero menor a 65, mostrar "Eres un adulto".
# Si la edad es mayor o igual a 65, mostrar "Eres un adulto mayor".

# 3. Escribe un programa que solicite al usuario ingresar una calificación entre 0 y 100.
# El programa debe clasificar la calificación de la siguiente manera:

# Mayor o igual a 90: Sobresaliente
# Entre 80 y 89: Notable
# Entre 70 y 79: Aprobado
# Menor a 70: Suspenso

#4. Desarrolla un programa que solicite al usuario ingresar la hora actual en formato de 24 horas (0-23), 
# si el sistema está activado (sí/no) y el nivel de seguridad (bajo, medio, alto). El programa debe determinar las siguientes condiciones:

# Sistema seguro: Si el sistema está activado y la hora es entre 6 y 18, independientemente del nivel de seguridad.
# Sistema moderadamente seguro: Si el sistema está activado y la hora está fuera de ese rango, pero el nivel de seguridad es medio o alto.
# Sistema no seguro: Si el sistema no está activado, independientemente de la hora o el nivel de seguridad.



