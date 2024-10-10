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
# El programa debe seguir ejecutándose hasta que el usuario decida salir..
# contactos = []#nombre: diego, telefono: 234234

# print("--------AGENDA TELEFONICA-----------")

# while True :
#     print("\n1. agregar contacto")
#     print("\n2. eliminar contacto")
#     print("\n3. mostrar contacto")
#     print("\n4. salir")

#     opcion = input("íngrese una opcion: ")

#     if opcion == "1" :
#         nombre = input("nombre de contacto: ")
#         telefono = input("numero telefonico: ")
#         contactos.append([nombre, telefono])
#         print("contacto agregado")

#     elif opcion == "2" :
#         nombre = input("nombre del contacto a eliminar: ")
#         for i in contactos:
#             if i[0] == nombre:
#                 contactos.remove(i)
#                 print("contacto eliminado exitosamente")
#                 break
#         else:
#             print("contacto no existe")    

#     elif opcion == "3":
#         if contactos:     
#             for i in contactos:
#                 print(f"Nombre :{i[0]}, telefono :{i[1]}")
#         else:
#             print("no hay contactos en la lista")

#     elif opcion == "4":
#         print("gracias saliendo del programa")
#         break        

#--------------------------------------------------------------------
# #Escribe un programa en Python que permita al usuario crear una lista de sus películas favoritas.
# El programa debe permitir al usuario realizar las siguientes acciones:

# Agregar una película a la lista.
# Eliminar una película especificando su nombre.
# Mostrar todas las películas en la lista.
# Buscar si una película específica está en la lista.
# El programa debe ofrecer estas opciones en un menú y continuar funcionando hasta que el usuario decida salir.

# elif opcion =="4":
#     pelicula = input("ingrese la pelicula que dea buscar")
#         if pelicula in listaPeliculas:
#     print(f" la pelicula {pelicula} esta en la lista")
# else:
#     print("pelicula {pelicula} no encontrada")

#------------------------------------------------------------------
"""Escribe un programa en Python para gestionar una lista de tareas pendientes. El programa debe implementar un CRUD 
(Crear, Leer, Actualizar, Eliminar) para las tareas y permitir al usuario realizar las siguientes acciones:

Crear una nueva tarea: Añadir una tarea a la lista con una descripción y una fecha de vencimiento.
Leer todas las tareas: Mostrar todas las tareas actuales, incluyendo su descripción y fecha de vencimiento.
Actualizar una tarea: Modificar la descripción y/o la fecha de vencimiento de una tarea existente especificando 
su número de identificación.
Eliminar una tarea: Eliminar una tarea de la lista especificando su número de identificación.
El programa debe ofrecer un menú de opciones y seguir funcionando hasta que el usuario decida salir. Asegúrate 
de manejar situaciones en las que el usuario intente realizar acciones sobre tareas que no existen y proporciona
mensajes adecuados.

Requisitos:
El programa debe permitir al usuario ingresar una descripción y una fecha de vencimiento para cada nueva tarea.
Cada tarea debe tener un identificador único que se utiliza para actualizar o eliminar la tarea.
El programa debe mostrar todas las tareas en un formato claro.
El usuario debe poder actualizar la descripción y/o la fecha de vencimiento de una tarea.
El usuario debe poder eliminar una tarea especificando su identificador."""
tareas = []
idTarea = 1

while True :
    print("---\n MENU DE TAREAS----")
    print("1. Nueva tarea")
    print("2. Leer todas las tarea")
    print("3. Actualizar una tarea")
    print("4. Eliminar una tarea")
    print("5. salir")

    opcion = input("Elige la opcion deseada: ")

    #crear tarea-----------------------------------
    if opcion == "1":
        descripcion = input("Descripcion de la tarea :")
        fechaVencimiento = input("Fecha de vencimiento (dd/mm/aaa): ")

        tareas.append({"id": idTarea, "descripcion": descripcion, "fechaVencimiento": fechaVencimiento})
        print(f"Tarea {idTarea} creada con exito \n")
        idTarea += 1

    #leer las tareas-----------------------    
    elif opcion == "2":
        if len(tareas)== 0:
            print("No hay tareas..")
        else:
            print("-LISTA DE TAREAS-")
        for i in tareas:
            print(f"ID: {i["id"]} descripcion: {i["descripcion"]} fecha de vencimiento: {i["fechaVencimiento"]}")
            print()

    #Actualizar tarea----------------------
    elif  opcion == "3":
        tareEncontrada = False
        idActualizar = int(input("Ingrese el ID que quiere actualizar: "))
        for i in tareas :
            if i ["id"] == idActualizar :
                nuevaDescripcion = input("ingrese la nueva descripcion (dejar en blanco si no quiere modificar la descriocion): ")
                nuevaFecha = input("Ingrese una nueva fecha (dejar en blanco si no quiere modificar la fecha): ")
                if nuevaDescripcion :
                    i["descripcion"] = nuevaDescripcion
                if nuevaFecha :
                    i["fechaVencimiento"] = nuevaFecha    
                    print(f"Tarea {idActualizar} actualizado con exito\n")
                    tareEncontrada = True
                    break
        if not tareEncontrada :
            print(f"No se encontro la tarea con el ID: {idActualizar}\n")

    #Eliminar tarea-------------------------------------     
    elif opcion == "4":
        idEliminar = int(input("Ingrese el ID a eliminar: "))
        tareEncontrada = False
        for i in tareas :
            if i ["id"] == idEliminar:  
                tareas.remove(i) 
                print(f"Tarea {idEliminar} eliminada exitosamente ")
                tareEncontrada = True
                break
        if not tareEncontrada :
            print(f" No se encontro la tarea con el ID {idEliminar}")     

    #-salir de la tarea-------
    elif opcion == "5":
        print("Salir del programa")
        break
    else:
        print("opcion invalida por favor verifique")         













