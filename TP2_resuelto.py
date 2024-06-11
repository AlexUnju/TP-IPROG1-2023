#CASOS DE ESTUDIO
#Utilizando la estructura selectiva simple
#FORMA 1

regimen = input("De que regimen eres? (vespertino/diurno): ")
nota = int(input("Cual es tu nota? [0, 10]: "))

if nota < 3.5: #va al ultimo pero lo puse primero
   print("Estás desaprobado")
if regimen == "vespertino" and nota >= 6:
   print("Estás eximido papu")
if regimen == "vespertino" and nota >= 3.5:
   print("Rindes examen")
if regimen == "diurno" and nota >= 3.5 and nota <= 10:
   print("Rindes examen quieras o no")


#Utilizando la estructura selectiva compuesta (anidada)
#FORMA 2

regimen = input('Ingrese el régimen (d)iurno o (v)espertino: ')
notaPresentacion = float(input('Ingrese nota de presentación [0, 10]: '))

if notaPresentacion < 3.5:
   print('Reprueba')
else:
   if regimen == 'v':
       if notaPresentacion < 6:
           print('Rinde examen')
       else:
           print('Se exime')
   else:
       if notaPresentacion >= 3.5:
           print('Rinde examen')
#FORMA 3
regimen = input("Ingrese su regimen vespertino/diurno: ")
nota = float(input("Ingrese su nota [0, 10]: "))

if nota < 3.5:
    print("reprueba")
elif regimen == "v":
    if nota >= 6:
        print("se exime")
    else:
        print("rinde examen")
elif regimen == "d":
    if nota >= 3.5:
        print("rinde examen, no hay posibilidad de eximirse")
else:
    print("el regimen es invalido")
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIOS 
#EJERCICIO 1
r = 10
s = 0

resultado = (r != 10) or not (s == -r) or not((True or r >= 10) and not (s <= 0 and True))
print(resultado)
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 2
"""Dadas v, w, z variables de tipo numérico entero escribir las expresiones lógicas correspondientes a los
siguientes enunciados:
A. v es no positivo y w es no menor o igual a cero.
B. v, w, z son diferentes entre sí.
C. v es no nulo y w no es mayor a z.
D. w está estrictamente entre v y z.
E. v es igual a w o z es no negativo pero no ambos a la vez."""

v = int(input("INGRESE V: "))
w = int(input("INGRESE W: "))
z = int(input("INGRESE Z: "))

if not v == "positivo" and not w <= 0: #NECESITO QUE ME EXPLIQUEN!!!!!!!!!!!
    print("1ra",True or False)
if v != w != z:
    print("2da",True or False)
if v == 0 and not w > z:
    print("3ra",True or False)
if w is v and z:
    print("4ta",True or False)
if v == w or not(not z<0):
    print("5ta",True or False)
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 3
clave = "iprog1"
contraseña = input("Introduce la contraseña: ")
if clave == contraseña.lower(): #lo que hace "lower" es tomar el string y lo convierte en minuscula
    print("La contraseña coincide")  
else:
    print("La contraseña NO coincide")
    
#¿Cuándo se visualizará en la pantalla el mensaje “coincide”?
#Se vizualizará cuando la entrada (input) coincida  con la variable clave
 
#Si ingresa en la variable contraseña iProg1, ¿Qué mensaje se verá en la pantalla?
#El mesaje será "La contraseña NO coincide" debido a que esta está con 'P' mayuscula

#Mejore la sentencia en la línea 3 utilizando alguna función que salve la situación anterior.
#Se podría mejorar usando la  función/metodo lower que convierte el «string» de la variable de entrada en minusculas

#¿Qué sucede si ingresa un número?
#La contraseña NO coincide
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 4

precio = 35
edad_cliente = int(input("INGRESE SU EDAD: "))
cantidad_fichas = int(input("INGRESE LA CANTIDAD DE FICHAS QUE DESEE COMPRAR: "))

if (edad_cliente >= 4) and (edad_cliente < 7):
    total = cantidad_fichas * precio
    descuento = total * 20 / 100 #tambien se puede multiplicar el total por 0.20
    descuento_total = total - descuento
    print("TIENE QUE PAGAR:",descuento_total)
    print("LE REGALAMOS 5 FICHAS",cantidad_fichas + 5)
else:
    if (edad_cliente >= 7) and (edad_cliente < 10):
        total = cantidad_fichas * precio
        aumento = total * 15 / 100 #tambien se puede multiplicar el total por 0.15
        aumento_total = total + aumento
        print("DEBE PAGAR:",aumento_total)
    else:
        print("NO SE PERMITE EL INGRESO")
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 5
#Diseñar un algoritmo que permita leer 3 números y escribir en la pantalla si están en “orden creciente” o
#“decreciente” o “no están en orden”.

numero1 = int(input("ingrese un nùmero1: "))
numero2 = int(input("ingrese un nùmero2: "))
numero3 = int(input("ingrese un nùmero3: "))

if numero1 < numero2 < numero3:
    print("ESTA EN ORDEN CRECIENTE")
elif numero1 > numero2 > numero3:
    print("ESTA EN ORDEN DECRECIENTE")
elif numero1 == numero2 == numero3:
    print("LOS NUMEROS SON IGUALES")
else:
    print("NO ESTA EN ORDEN")
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 6
#Diseñar un algoritmo que ordene en forma creciente tres valores diferentes a, b, c
#FORMA 1
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

if a !=b and a != c and b !=c:
    if a < b:
        if a < c:
            if (b < c):
                print(a,b,c)
            else:
                print(a,c,b)
        else:
            print(c,a,b)
    else:
        if b < c:
            if c < a:
                print(b,c,a)
            else:
                print(b,a,c)
        else:
            print(c,b,a)
else:
    print("Los numeros deben ser diferentes: ")
#FORMA 2
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

if (a<b<c):
    print("EL ORDEN ES A,B,C") #1 2 3
elif (a<c<b):
    print("EL ORDEN ES A, C, B") #1 3 2
elif (b<a<c):
    print("EL ORDEN ES B, A, C") #2 1 3
elif (b<c<a):
    print("EL ORDEN ES B, C, A") #2 3 1
elif (c<a<b):
    print("EL ORDENES C, A , B") #3 1 2
elif (c<b<a):
    print("EL ORDEN ES C, B, A") #3 2 1 
else:
    print("NO FUE POSIBLE EL ORDEN")
#FORMA 3
print("Ingresar el primer número: ")
num1 = int(input())
print("Ingresar el segundo número")
num2 = int(input())
print("Ingresar el tercer número")
num3 = int(input())

if(num1<num2 and num2<num3):
    print("",num1," - ",num2," - ",num3)
elif(num1<num3 and num3<num2):
    print("",num1," - ",num3," - ",num2)
elif(num2<num1 and num1<num3):
    print("",num2," - ",num1," - ",num3)
elif(num2<num3 and num3<num1):
    print("", num2," - ",num3," - ",num1)
elif(num3<num1 and num1<num2):
    print("",num3," - ",num1," - ",num2)
elif(num3<num2 and num2<num1):
    print("",num3," - ",num2," - ",num1)
else:
    "Los numeros son iguales"
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 7 #IDENTAR BIEN
print("Este programa mezcla dos colores.")
print(" r. Rojo a. Azul")
primera = input(" Elija un color (r o a): ")
if primera == "r":
    print(" a. Azul v. Verde")
else:
    print(" v. Verde r. Rojo")
    
segunda = input(" Elija otro color (a o v): ")
if segunda == "a":
    print("La mezcla de Rojo y Azul producen Magenta.")
else:
    print("La mezcla de Rojo y Verde producen Amarillo.")
    

segunda = input(" Elija otro color (v o r): ")
if segunda == "v":
    print("La mezcla de Azul y Verde producen Cian.")
else:
    print("La mezcla de Azul y Rojo producen Magenta.")
    
print("¡Hasta la próxima!")
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 8
#Sin ejecutar el código en la computadora, ¿Cuál es la salida por la pantalla? Para los siguientes valores:
#EDAD: 12 y 18
edad = int(input("Ingrese la edad (0, 110]:"))
if edad > 0 and edad <= 12:
    print("Es un niño")
elif edad >12 and edad <= 18:
    print("Es un adolescente")
elif edad >18 and edad <= 80:
    print("Es un adulto")
else:
    print("Es un anciano")
#Si ingreso "12" la salida es «Es un niño»; si ingreso "18" la salida  es «Es un adolecente»

#NÚMERO: -5, 0 y 10
numero = int(input('Ingrese un número entero:'))

print('#')
if numero < 0:
    print('negativo')
if numero < 0 and numero >= -10:
    print(numero)
if numero > 0:
    print('positivo')
if numero > 0 and numero >= 10:
    print(numero)
print('#')
#Si ingreso "-5" la salida es «negativo»; si ingreso "0" no tiene salida, no está definido; si ingreso "10" la salida es positivo
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 9
#Realizar un programa que permita averiguar si un año es bisiesto. Considera que para que un año sea bisiesto
#debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

year = int(input("ingrese el año: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year,"es un año bisiesto.")
else:
    print(year,"no es un año bisiesto.")
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 10
#Diseñar dos programas que utilicen la sentencia selectiva simple y la sentencia encadenada if…elif…else…, el
#programa debe pedir la edad y en función del valor recibido mostrará un mensaje diferente.
#● si el valor de la edad es negativo, se trata de un error
#● si el valor de la edad está entre 0 y 17, se trata de un menor de edad
#● si el valor de la edad es superior o igual a 18, se trata de un mayor de edad

#SENTENCIA SELECTIVA SIMPLE
edad = int(input("Ingrese la edad: "))

if edad < 0:
    print("El número es negativo")
if edad >= 0 and edad <= 17:
    print("Sos menor de edad")
if edad >= 18:
    print("Sos mayor de edad")

#SENTENCIA SELECTIVA ENCADENADA
edad = int(input("Ingrese la edad: "))

if edad < 0:
    print("Es un número negativo, error.")
elif edad <= 17:
    print("Sos menor de edad")
else:
    print("Sos mayor de edad")
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 11
#Hacer dos programas que utilicen la sentencia selectiva compuesta (anidada) y la sentencia if…elif…else…, el
#programa debe pedir un número y mostrará:
#● si es múltiplo de dos,
#● si es múltiplo de cuatro (y de dos)
#● si no es múltiplo de dos
#Nota: El valor 0 se considerará múltiplo de 4 y de 2.

#SENTENCIA SELECTIVA COMPUESTA (ANIDADA)

numero = int(input("Escribe un número: "))

if numero % 2 == 0:
    if numero % 4 == 0:
        print(numero,"es multiplico de 2 y 4")
    else:
        print(numero,"solo es multiplo de 2")
else:
    print(numero,"no es multiplo de 2")
#SENTENCIA SELECTIVA ENCADENADA
#FORMA 1
numero = int(input("Escribe un número: "))

if numero % 2 == 0 and numero % 4 == 0:
    print("Es multiplo de 2 y 4")
elif numero % 2 == 0 and numero % 4 != 0:
    print("Solo es multiplo de 2")
else:
    print("no es multiplo de 2")
    
#FORMA 2
numero = int(input("Ingrese un número entero: "))

if numero == 0 or numero % 4 == 0:
    print(numero, "es múltiplo de cuatro (y de dos)")
elif numero % 2 == 0:
    print(numero, "es múltiplo de dos")
else:
    print(numero, "no es múltiplo de dos")
#-----------------------------------------------------------------------------------------------------------------------
#EJERCICIO 12
"""Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones
sobre las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases
en un día de la semana diferente: los lunes se dicta el Nivel Inicial, los martes el Nivel Intermedio, los
miércoles el Nivel Avanzado, los jueves son para Práctica Hablada y los viernes se dicta Inglés para Viajeros.
El usuario ingresa la fecha actual en formato “día, DD/MM", donde [día] es un día de la semana
(lun-mar-mie-jue-vie), DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la
semana inexistente o una fecha cuyo día supere el rango 1-31 o el mes de 1 a 12, indique que se produjo un
error. Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente.
Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron exámenes, pero eso sólo si se
trata de los niveles Inicial, Intermedio o Avanzado, ya que las Prácticas Habladas y el Inglés para Viajeros no
tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el
programa le mostrará el porcentaje de Aprobados.
Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de asistencia a
clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la
mayoría" si no es así.
Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 de cualquier mes, se deberá imprimir
"Comienzo de nuevo ciclo"."""

# lunes: nivel inicial (examen)
# martes: nivel intermedio (examen)
# miercoles: nivel avanzado (examen)
# jueves: para practica hablada (sin examen)
# viernes: ingles para viajeros (sin examen)

# variables
# #"el formato es: "dia, DD/MM = lunes/05/3"
# DIA: (lun-mar-mie-jue-vie) [1,31]
# DD: numero de dia
# MM: numero de mes [1,12]

# fecha_formato = int(input("ingrese la fecha en formato: «día/DD/MM"))
# dia =
# DD 