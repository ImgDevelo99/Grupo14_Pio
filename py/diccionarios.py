"""
es una estructura de datos que almacena pares, clave , valor. cada clave esta asociada a un valor, se conoce como:
"par clave-valor". son mutables que se pueden cambiar,
"""
# milista =[ 23, 3,45,67,89 []]

# nombreDiccionario = {
#     "clave1": "valor1", # calve1 = "un valor"
#     "calve2": "valor2",
#     "calve3": "valor3"
# }

# informacionPersonal = {
#     "nombre": "gabriela",
#     "edad": 8,
#     "ciudad": "medellin"
# }
# print(informacionPersonal)

# nombres = {
#     "nombre": "carlos",
#     "edad" : 30,
#     "cursos": ["py","js","nodejs","java"]

# }
# print(nombres)
# print(nombres["nombre"])
# print(nombres["edad"])
# print(nombres["cursos"][1])

#----------AGREGAR-----------------------------
miDiccionario ={
    "nombre" : "sara",
    "edad" : 30
}
miDiccionario["profesion"] = "Desarrollador"
print(miDiccionario)

#--------------EDITAR----------------------
miDiccionario["edad"] = 32
print(miDiccionario)

#------------Eliminar--------------------
del miDiccionario["edad"]
print(miDiccionario)

#pop eliminar del diccionario y almacenarse en una variable
texto = miDiccionario.pop("nombre")
print(miDiccionario)
print(texto)

#----------agregar multiples valores----------
nuevosDatos = {
    "ciudad" : "Cali",
    "telefono": 21323,
    "direccion": "calle 34 #45-90"
}
for clave, valor in nuevosDatos.items():
    miDiccionario[clave] = valor

print(miDiccionario)    

#---------------multiples valores----------------------------

claveEliminar = ["profesion", "ciudad"]

for clave in claveEliminar :
    if clave in miDiccionario:
        del miDiccionario[clave]

print(miDiccionario)

#---------------ejemplo--------------------------------------
estudiante = {}#estudiante = {"nombre": "diego"}

nombre = input("ingrese su nombre")#

estudiante["datos"] = nombre# agrego al diccionario

print(f"el nombre es {estudiante["datos"]}")#imprimo

#-------------------------------------------------------------------


