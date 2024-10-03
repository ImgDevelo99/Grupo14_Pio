print("Bienvenidos a PY") #es para pintar mostrar en consola
#esto es para comentar una linea
#para limpiar consola con el comando cls
"""
esto me sirve para comentar}
varias lines en
mi codigo
"""
#para comentar muchas lineas utilizo las teclas ctrl k c
# para descomentar todas las lines seleccionadas ctrl k u
#------------------------TIPOS DE DATOS---------------------------
# print(type("es un tipo de dato string seria una cadena de caracteres 56 78.89 TRUE "))# str =string
# print(type(56))# int
# print(type(3.67))# float = decimales
# print(3.67)
# print(type(True)) #bool
# print(type('a5srss'))#str

#-----------------VARIABLES----------------------------------------
# texto = "estoy aprendiendo py"
# print(texto)
# texto = "para poder realizar mi priyecto"
# print(texto)
# numero = 565
# print(numero)
# texto= "hola mundo"
# print(texto)

# edad = 20
# print(edad)
# precio = 45.9000
# print(precio)
# pregunta = True
# print(pregunta)

#------------errores al momento de declara variables-----------------
# 2edad =
# %texto =
# mi edad = 20
# def = 454
# print = 766
# bool = "hoooe"
# _variable = 333

#------------decalracion orrecta---------------------
# saludar = "hola"
# precioUnitario = 3444.666
# miEdad = 23
# precio_unitario = 445.654
# mi_edad = 30
# nombre = "diego"
# print("bienvenido",nombre)

# #-------------metodos string--------------------
# saludar = "   hola a Todos Ya Terminamos estE moduLo FelIcitaCiones"# " "
# cantidadCAracteres = len(saludar) # devuelve la longitud de la cadena
# print(cantidadCAracteres)

# saludarMayuscula = saludar.upper()# me convierte el texto en mayuscula
# print(saludarMayuscula)

# saludarMinuscula = saludar.lower() # me convierte el texto en minuscula
# print(saludarMinuscula)

# capital = saludar.capitalize()#convertir la primera letra del texto en mayuscula
# print(capital)

# titulo = saludar.title()# convierte el primer caracter de cada palabra en mayuscula
# print(titulo)

# nuevoTexto = saludar.replace("FelIcitaCiones", "programando")# remplaza el texto
# print(nuevoTexto)
# print(saludar)

# eliminarEspacio = saludar.strip()#elimina los espacios en blanco al inicio
# print(eliminarEspacio)

#--------------metodos INT---------------------------------
# num = -10
# print(num)
# valorDevuelto = abs(num) #delvuelve el valor positivo
# print(valorDevuelto)

# precio = 3.4
# redondear = round(precio)#nos aproxima el valor de la variable
# print(redondear)

#----------------------metodos float-------------------
# import math
# calcularRaiz = math.sqrt(64678)
# print(calcularRaiz)

# maximo = max(2,4,6,1,9,4,49,3,0)
# minimo = min(2,4,6,1,9,4,49,3,0)
# print(maximo)
# print(minimo)
#------------------------------------------------------
# num1 = 10
# num2 = 30
# num3 = 50
# total = num1 + num2 + num3
# print("la suma de los 3 numeros es: ",total) 

# palabra1 = "hola"
# palabra2 = "mundo"
# palabra3 = "py"
# frase = palabra1 +" "+ palabra2 +" " + palabra3
# print(frase)
# espacio = ""
# print(type(espacio))

# #------------formas de concatenar en print------------------------------------
# print("la frase unida es: ",frase)
# print("las variables son: ",palabra1,"para escrbnir texto", palabra2,"para escribir otro texto", palabra3)
# print(f"la variables son {palabra1} y luego paso la otra variable q es: {palabra2} y pormultimo es:{palabra3}")

# nombre = "Diego"
# ciudad = "Medellin"
# telefono = "23324"
# print(f"el nombre del profesor es: {nombre} y es de la ciudad de {ciudad} y su telefono es:{telefono}")

# #--------------------------------import fecha-------------------------------
# import datetime
# fechaActual = datetime.datetime.now()#imprime la fecha actual
# print(fechaActual)

# formatoFecha = fechaActual.strftime("%d/%m/%Y %H:%M:%S")# me permite darle formato
# print("la fecha y la hora actual es: ",formatoFecha)

#------------------ import random----------------
import random
numeroAleatorio1 = random.randint(2,63)
numeroAleatorio2 = random.randint(2,63)
numeroAleatorio3 = random.randint(2,63)
numeroAleatorio4 = random.randint(2,63)
print(f"ustedes fueron seleccionados para que nos hagan una exposicion sobre py o un resumen sobre lo visto en clase el dia de mañana, los afortudados son los siquientes:{numeroAleatorio1},{numeroAleatorio2},{numeroAleatorio3},{numeroAleatorio4}")