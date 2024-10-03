# nombre = input("escriba su nombre:")
# print("su nombre es: ",nombre)
# print(type(nombre))

# edad = int(input("ingrese su edad: "))# edad = "30" "true", "3.2456" 
# print(type(edad))

# estatura = float(input("ingrese su estatura: "))
# print(type(estatura))

#---------------------------------------------------------------------
"""
solicitar al usuario que ingrese 3 notas y scar el promedio de las mismas
mostrar el resultado
"""
nota1 = float(input("ingrese la primera nota: "))
nota2 = float(input("ingrese la segunda nota nota: "))
nota3 = float(input("ingrese la tercera nota: "))

notafinal = (nota1 * 0.6) + (nota2 * 0.2) + (nota3 * 0.2)

print(f"la primera nota que ustes ingreso es {nota1}, la segunda nota es: {nota2}, y la tercera nota es: {nota3}, y el promedio es: {notafinal} ")

#----------------------------------------------------------------------
"""
Escribe un programa en Python que convierta una temperatura 
dada en grados Celsius a grados Fahrenheit. La fórmula de conversión es: F = C * 9/5 + 32
"""
celcius = float(input("ingrese la temperatura en grados celcius"))

fahrenheit = celcius * 9/5 + 32

print("la convercion a grados F es: ",fahrenheit)

#------------------------------------------------------------------------
"""
1.scribe un programa en Python que tome una cadena de texto como entrada 
y la convierta en tres formatos diferentes: todo en mayúsculas, todo en minúsculas
y en formato título (donde cada palabra empieza con mayúscula).

2.Crea un programa que pida al usuario el ancho y la altura de un rectángulo y calcule el área.
La fórmula del área es: Área = ancho * altura.
"""
#------------------------------------operadores aritmeticos----------------------------------------------------
"""
+  suma     12+3 = 15
-  resta    5-2  = 3
*  multip   2*5  = 10
/  div      10/2  = 5 
%  modulo   16%3  = 1
** potenciacion 12**3 = 1728
"""
#------------------------------------operadores relacionales----------------------------------------------------
"""
> mayor que    12 > 3 True
< menor que    12 < 3 False
== igualdad    12 == 3 False
>= mayor o igual que 19 >= 12 True
<= menor o igual que 12 <= 3  false
!= distinto     12 != 3 True
"""
#------------------------------------operadores logicos----------------------------------------------------
"""
and  devuelve true si ambos opereradores son true
or   devuelve true si alguno de los dos operadores es true
not  devuelve true si alguno de los dos operadores es false

v and v  = true
v or f   = true
f or v   = true
v not f  = true
f not v  = true

"""
# edad = 20
# ciudadanoColombiano = True

# puedeVotar =  edad != 18 and ciudadanoColombiano

# if puedeVotar:
#     print("TRUE")
# else:
#     print("FALSE")

# print(puedeVotar)

#---------------------------Operadores de asignacion-------------------------------------------------
"""
=           var = "hola"
+=          x+=2 =7                 x=x+2 =7    5=5+2 =7           // x = 5
-=          x-=2                    x=x-2
*=          x*=2                    x=x*2 
/=          x/=2                    x=x/2
%=          x%=2                    x=x%2
**=         x**2                    x=x**2    
"""
#-------------------------------------------------------------