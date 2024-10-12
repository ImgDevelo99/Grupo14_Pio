"""
se utiliza iterar sobre una secuencia (lista, tuplas, diccionarios, un conjunto de cadenas)

"""
#for variable in secuencia
#variable : tomara el valor de cada uno de los  elementos de la secuencia en cada iteracion
#secuencia: secuencia de elementos que se van a recorrer (lista)


# nombres = ["ana", "pablo", "juan", "carlos"]
# for i in nombres:
#     print(f"bienvenido, {i}")

# #--------------------------------------------------------
# numeros = [1, 23,2, 45, 677, 888, 6 ,10]
# for i in numeros:
#     if i % 2 == 0:
#         print(f"{i} es par")    

# #--------------------------------------------------------        
# cadena = " estoy aprEndiendO a prOgramar En python utIlizando El bUcle for"
# vocales = "aeiouAEIOU"
# contador = 0

# for letra in cadena :
#     if letra in vocales:
#         contador += 1

# print(f"el numero de vocales en la cadena es: {contador}")     

#---------------------------------------------------------------------------
# numero = int(input("ingrese un numero del 1 al 10 para saber la tabla  de multiplicar : "))

# for i in range(1, 11):
#     print(f"{numero} X {i} = {numero * i}" )


# # for i in range(1, 11):
# #     print(i)
#--------------------------------------------------------------------------------------------
# for i in range(1, 11):
#     for x in range(1,11):
#         print(f"{i} X {x} = {i * x}")

#     print("-" * 15)  

#--------------------------------------------------------------------------

filas = int(input("ingrese el numero de filas: "))
for i in range (1, filas, + 1):
    for z in range (i):
        print("*", end= "")
    print()    




