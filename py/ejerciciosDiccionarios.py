"""
Supongamos que tienes un grupo de estudiantes y quieres almacenar sus calificaciones
en un diccionario. Luego, puedes agregar nuevas calificaciones, actualizar las notas existentes
y eliminar estudiantes del registro.
"""
# calificacion = {
#     "juan" : [3, 2.5, 4],
#     "Maria": [5, 4.6, 2],
#     "katherin": [1.4, 2, 2.9]
# }
# print(calificacion)

# #agregar calificacion
# calificacion["juan"].append(5)
# print(calificacion)

# #actualizar
# calificacion["Maria"] =[5, 3, 4.9]
# print(calificacion)

# calificacion["Maria"][1]= 2

# #eliminar
# del calificacion["katherin"]
# print(calificacion)
#--------------------------------------------------------
"""
Ejemplo Práctico: CRUD para un Directorio de Contactos
Vamos a implementar las operaciones básicas de un CRUD:

Crear: Agregar un nuevo contacto.
Leer: Mostrar los contactos existentes.
Actualizar: Modificar el número de teléfono de un contacto existente.
Eliminar: Borrar un contacto del directorio.
"""
# diccionarioContacto = {
#     "juan": "3333",
#     "Carlos": "8999",
#     "Dario": "89877",
#     "javier": "171652"
# }
# #crear
# diccionarioContacto["Diana"]= "6655"
# print(diccionarioContacto)
# print(f"contacto agregado: Diana {diccionarioContacto["Diana"]}")

# #leer contaco
# print("\nDICCIONARIO CONTACOS")
# for nombre, telefono in diccionarioContacto.items():
#     print(f"{nombre} : {telefono}")

# # actualizar
# diccionarioContacto["juan"]= "1111" 
# print("\nDICCIONARIO CONTACOS")
# for nombre, telefono in diccionarioContacto.items():
#     print(f"{nombre} : {telefono}")

# #eliminar
# del diccionarioContacto["Carlos"]
# print("contacto elimindo exitosamente")

# print("\nDICCIONARIO CONTACOS")
# for nombre, telefono in diccionarioContacto.items():
#     print(f"{nombre} : {telefono}")   

#-------------------------------------------------------------     
"""
Ejercicio: Gestión de Inventario de Productos
El usuario podrá:

Agregar un nuevo producto o actualizar la cantidad de un producto existente.
Eliminar un producto del inventario.
Mostrar el inventario actual.
"""
inventario = {}
continuar = True

while continuar :
    print("\n Opciones")
    print("1. agregar o actualizar un producto: ")
    print("2. Eliminar un producto: ")
    print("3. mostrar el inventario: ")
    print("4. para salir")

    opcion = input("ingrese una opcion entre 1 al 4 :")

    if opcion == "1": 
        #agregar
        producto = input("ingrese el nombre del producto :").lower()
        cantidad = int(input(f"ingrese la cantidad del producto {producto} :"))

        if producto in inventario:
            inventario[producto] += cantidad
            print(f"se agrego {cantidad} unidades de {producto}. total : {inventario[producto]} unidades ")
        else:
            inventario[producto] = cantidad
            print(f"{producto.capitalize()} añadido al inventario con {cantidad} unidades")

    #eliminar
    elif opcion == "2":
        producto = input("ingrese el nombre del producto a eliminar: ").lower()

        if producto in inventario:
            del inventario[producto]
            print(f"{producto} eliminado del inventario ")

        else:
            print(f"producto {producto} No existe en el inventario")

    #mostrar 
    elif opcion == "3":
        print("\n INVENTARIO ACTUAL")
        if inventario :
            for producto, cantidad in inventario.items():
                print(f"{producto} : {cantidad} unidades")

        else:
            print("inventario vacio")       

    #salir
    elif opcion == "4":
        continuar = False
        print("gracias por visitarnos")
    else:
        print("opcion incorrectar")


