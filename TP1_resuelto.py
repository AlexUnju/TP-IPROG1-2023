#"string", 'string',: el tipo de dato que es texto le decimos string, significa cadena, viene de cadena de texto
#'''Calcular el volumen de una esfera cuya fórmula es v = 4/3*PI*r**3=43'''

#CASO DE ESTUDIO 1
radio = float(input("ingrese el valor de radio: ")) #INPUT SIEMPRE NOS DEVUELVE UN TEXTO
pi = 3.1416
volumen = 4/3 * pi * radio ** 3
print('volumen: ', volumen)
#------------------------------------------------------------------------------------------------------
#CASO DE ESTUDIO 1 PERO DE OTRA FORMA MÁS COMPLEJA
import os
from math import pi

os.system('cls') #window: cls; mac y linux: clear

print('hola mundo bienvenido a mi primer programa')
r = float(input("ingrese el radio: "))
print('Usted ingreso ', r)
v = 4 / 3 * pi * r ** 3
print('El volumen es: ', v) 
#------------------------------------------------------------------------------------------------------
#CASO DE ESTUDIO 2
precio = float(input("ingrese el precio unitario del producto: "))
numero_de_productos = float(input("ingrese la cantidad de productos: "))
importe = precio*numero_de_productos
print("total a pagar: ", importe)
#------------------------------------------------------------------------------------------------------
#EJERCICIO 1
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n+" entre "+m+" da un cociente "+str(int(n)//int(m)) + " y un resto " + str(int(n) % int(m)))
#● Muestre el resultado con n = 2 y m = 5 Rta: 2 entre 5 da un cociente 0 y un resto 2
#● ¿Puede obtener un resultado para cualquier valor de m? Si
#● ¿Qué operador utiliza para calcular el resto? El Operador del Modulo
#● Modifique el código quitando str() en la 3er línea, ¿qué sucede?  Da un error de tipeo (TypeError)
#-----------------------------------------------------------------------------------------------------
#EJERCICIO 2
PI = 3.14   
x = int(input("ingresar el valor de X: "))
y = int(input("ingresar el valor de Y: "))
z = int(input("ingresar el valor de Z: "))
e1 = 3*(x/y) + (-y/z)*5
e2 = PI*x**2-(1/2)*(x/(y-z))**1/3
print("El resultado de la 1ra formila es: ", e1)
print("El resultado de la 1ra formila es: ", e2)
#-----------------------------------------------------------------------------------------------------
#EJERCICIO 3
capital_inicial = float(input("Ingrese el capital inicial: "))
interes_anual = 0.04
ahorro_anual = capital_inicial * interes_anual
#
primer_año = capital_inicial + ahorro_anual
segundo_año = primer_año + ahorro_anual
tercer_año = segundo_año + ahorro_anual
print('primer_año: ', primer_año, 'segundo_año: ', segundo_año, 'tercer_año: ', tercer_año)
#--------------------------------------------------------------------------------------------------------
#EJERCICIO 4 perimero = 2(b*h), area = b*a

#FORMA 1
b = int(input("base del rectangulo: "))
a = int(input("altura del rectangulo: "))
perimetro = 2(b*a)
area = b*a
print("El primetro del rectangulo es de: ", perimetro)
print("El area del rectangulo es de: ", area)
#FORMA 2
LA = float(input("Ingresar cuanto mide la altura del rectangulo: "))
LB = float(input("Ingresar cuanto mide la base del rectangulo: "))
Perimetro = LA * 2 + LB * 2
Superficie = LA * LB
print("El perimetro del cuadrado es ", str(float(Perimetro)) + " y su Superficie es de", str(float(Superficie)))
#--------------------------------------------------------------------------------------------------------
#EJERCICIO 5
from math import sqrt

cateto_1 = float(input("El cateto 1 vale: "))
cateto_2 = float(input("El cateto 2 vale: "))
hipotenusa = sqrt(cateto_1**2 + cateto_2**2)
print("La hipotenusa es de: ",hipotenusa,"cm.")
#FORMA 2 a = int(input("El cateto 1 vale: "))
b = int(input("El cateto 2 vale: "))
h = (a**2 + b**2)**0.5
print("El valor de la hipotenusa es: ", h)
#--------------------------------------------------------------------------------------------------------
#EJERCICIO 6
#Solicite el ingreso de una cantidad de pesos Argentinos, dar su equivalente en dólares y en euros. Se sabe que
#1 dólar = 202,30 pesos y 1 euro = 214,30 pesos (formatee los resultados a 3 decimales).

pesos_argentinos= float(input("Ingrese los pesos para la conversión: "))
conversion_dolar = pesos_argentinos / 202.30
conversion_euro =  pesos_argentinos / 214.30
print("en euros: ",str(round(conversion_euro, 3)),"en dolares: ", str(round(conversion_dolar)))
#--------------------------------------------------------------------------------------------------------
#EJERCICIO 7

#Solicite el valor de un ángulo en Radianes conviértalo a grados Sexagesimales y luego a Centesimales. Muestre los
#resultados en pantalla.
#Fórmula de conversiones: sexadecimal = valorEnRadian * 180 / Pi, centesimal = valorEnRadian * 200 / Pi

PI = 3.14
valorEnRadian = float(input("Ingrese el valor en radianes: "))
sexadecimal = valorEnRadian * 180 / PI
centesimal = valorEnRadian * 200 / PI
print("El valor en sexadecimal es: ", sexadecimal)
print("El valor en centesimal es:  ",  centesimal)
#--------------------------------------------------------------------------------------------------------
#EJERCICIO 8 Determine la distancia entre dos puntos en el espacio. Punto 1: (x1, y1, z1) y Punto 2: (x2, y2, z2).

#FORMA 1
print("~~~VALORES DEL PUNTO 1~~~")
x1 = float(input("ingrese x1"))
y1 = float(input("ingrese y1"))
z1 = float(input("ingrese z1"))
print("~~~VALORES DEL PUNTO 2~~~")
x2 = float(input("ingrese x2"))
y2 = float(input("ingrese y2"))
z2 = float(input("ingrese z2"))
d = ((x1-x2)**2 + (y1-y2)**2 +(z1-z2)**2)**0.5
print("La distancia entre el punto 1 y el punto 2 es: ", d)

#FORMA 2
from math import sqrt

print("~~~VALORES DEL PUNTO 1~~~")
x1 = float(input("ingrese x1: "))
y1 = float(input("ingrese y1: "))
z1 = float(input("ingrese z1: "))
print("~~~VALORES DEL PUNTO 2~~~")
x2 = float(input("ingrese x2: "))
y2 = float(input("ingrese y2:"))
z2 = float(input("ingrese z2: "))
d = sqrt((x1-x2)**2 + (y1-y2)**2 +(z1-z2)**2)
print("La distancia entre el punto 1 y el punto 2 es: ", d)
#--------------------------------------------------------------------------------------------------------
#EJERCICIO 9
#Diseñar un programa que permita calcular el índice de masa corporal de una persona. IMC: kg/m**2

peso_en_kg = float(input("Ingrese su peso en kg: "))
altura_en_metro = float(input("Ingrese su altura en metro: "))
masa_corporal = peso_en_kg / altura_en_metro ** 2
print("Su pasa corporal es de: ",masa_corporal)
#--------------------------------------------------------------------------------------------------------

