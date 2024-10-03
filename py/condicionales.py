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

calificacion = float(input("ingrese la calificacion entre 0 y 10: "))

if calificacion >= 9 :
    print("su nota es Excelente")
elif calificacion >= 7:
    print("su nota es sobresaliente")
elif calificacion >= 5 :
    print("su nota es aceptable")
else:
    print("su nota es insuficiente")

#----------------------------------------------------------------    
#solicitarle al usuario que ingrese un numero del 1 al 7, e indicar que dia de la semana es:

#---------------------------------------------------------------
#escribir un programa donde le solicitemos al usuario que ingres los 3 lados del triangulo, el programa me debe 
#indicar si el triangulo es EQUILATERO(todos los lados iguales),el triangulo es ISOCELES(dos lados iguales
#  y uno diferente) triangulo escaleno (todos los lados son diferentes)...............
#-----------------------------------------------------------------




