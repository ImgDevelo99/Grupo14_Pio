"""
son tipos de datos nos permite almacenar cualquier tipo de dato  multiples
- ordenarlas
- indexadas
- se puede anidar
- mutables
- dinamicas (CRUD  crear, mostrar, actualizar, eliminar)
"""
# lista = [ 12, 34, 3, "hola", 3.4, 45.67 , "python", True, [ 34, "bienvenidos"]]

# print(lista)

# numeros = [2, 5, 6, 7 ,8 ] 
# print(numeros)
# print(numeros[3])

#--------------------METODOS DE LISTAS----------------
# frutas = ["piña", "sandia", "manzana", "manzana"]
# #metodo append(elemnto) : agrega un elemento a la lista
# frutas.append("uvas")
# print(frutas)

# #insert(posicion, elemento) : insertar un elemento en la posicion especifica
# frutas.insert(1, "bananos")
# print(frutas)

# #remove(elemento).  elimina un elemento de la lista
# frutas.remove("uvas")
# print(frutas)

# #pop : elimina de la lista un elemento, pero me lo almacenar en una variable

# elemento = frutas.pop(0)
# print("se elimino de la lista esta fruta",elemento)
# print(frutas)

# print(frutas[:2])
# print(frutas)

# #------------------------------------------------------------------------------------
# contador = frutas.count("manzana")
# print(contador)

# print(len(frutas))#contar los elementos
#---------------------------------------------------------------------------------------
#solicitar al usuario que ingrese 3 precio y se almacenne en una lista, luego mostrar los precio
# precio = []

# nombre1 = input("ingrese el primer nombre: ")
# precio.append(nombre1)

# nombre2 = input("ingrese el primer nombre: ")
# precio.append(nombre2)

# nombre3 = input("ingrese el primer nombre: ")
# precio.append(nombre3)

# print("los precio qu usted ingreso son: ",precio)
#---------------------------------------------------------------------------------------
# Pide al usuario que ingrese el precio de tres productos y almacénalos en una lista.
# Luego, muestra la lista y el precio total sumado.
# precio = []

# precio1 = float(input("ingrese el primer precio: "))
# precio.append(precio1)

# precio2= float(input("ingrese el primer precio: "))
# precio.append(precio2)

# precio3 = float(input("ingrese el primer precio: "))
# precio.append(precio3)

# print("la suma total es: ",sum(precio))

#------------------------------------------------------------------------------------------
## Escribe un programa en Python que permita al usuario crear una lista de compras. 
# El programa debe solicitar al usuario que ingrese el nombre de los productos uno por uno 
# y los agregue a la lista. Una vez que el usuario haya terminado de agregar productos, 
# el programa debe imprimir la lista completa de compras en orden.
# Requisitos:
# El programa debe permitir al usuario ingresar productos hasta que decida detenerse.
# Después de ingresar cada producto, el usuario debe ser preguntado si desea agregar otro producto.
# Si el usuario decide que no quiere agregar más productos, el programa debe mostrar la lista completa de compras.

# listaCompras = []

# while True:
#     producto = input("ingrese el nombre del producto a la lista: ")
#     listaCompras.append(producto)

#     continuar = input("quiere agregar mas productos? (si/no): ").lower()
#     if continuar == "no":
#         break
# print(f"\n-----LISTA DE PRODUCTOS------")

# for i in listaCompras:
#     print(i)

#----------------------------------------------------------------------------------------
# Escribe un programa en Python para gestionar una lista de contactos. 
# El programa debe permitir al usuario realizar las siguientes operaciones:

# Agregar un contacto a la lista, incluyendo un nombre y un número de teléfono.
# Eliminar un contacto de la lista especificando el nombre del contacto.
# Mostrar todos los contactos en la lista, con el formato "Nombre: Número de teléfono".
# El programa debe mostrar un menú con las opciones disponibles y seguir funcionando hasta 
# que el usuario elija salir. Asegúrate de manejar situaciones en las que el usuario intente
# eliminar un contacto que no está en la lista y que el programa informe adecuadamente al usuario.

# Requisitos:
# El programa debe permitir al usuario ingresar contactos con un nombre y un número de teléfono.
# Debe ser posible eliminar un contacto buscando por el nombre.
# Debe mostrar todos los contactos en la lista en un formato claro.
# El programa debe seguir ejecutándose hasta que el usuario decida salir.


