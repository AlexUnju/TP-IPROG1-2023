#Realice la prueba de escritorio o traza del algoritmo de Euclides utilizando el debugger de VSC
#---------ENCONTRAR EL MCD----------
#ENCONTRAR EL MCD DE DOS NUMEROS
a = int(input("Ingresar dividendo: "))
b = int(input("Ingresar divisor: "))
#"abs" retorna el valor absoluto de las variables, es decir, su forma positiva
a = abs(a)
b = abs(b)
#Algoritmo Euclides Iterativo
while b != 0:
    r = a % b  #temp = b
    a = b      #b = a % b
    b = r      #a = temp
#mcd = a
print("El MCD es:",a)
#----------------------------------
#ESTE NO RETORNA LOS VALORES NEGATIVOS
a = int(input('a:')) #2366, 55
b = int(input('b:')) #273, 89
i = 0
while b != 0:     #   200-150-> 2
    r = a % b     #   100-75->5
    a = b         #   20-15->5
    b = r         #   4-3->
    i += 1        #   2x5x5=50
print('mcd:', a,"se ejecuto",i,"veces")
#Otra forma (no acepta valores negativos)
a = int(input("Ingresar dividendo: "))
b = int(input("Ingresar divisor: "))

mcd = 1
for i in range(2, b+1):
    if a % i == 0 and b % i == 0:
        mcd = i 

print("El MCD de", a, "y", b, "es:", mcd)
#----------ENCONTRAR EL MCM-----------
a = int(input("a: "))
b = int(input("b: "))
i = 2
while True:
    if i % a == 0 and i % b == 0:
        mcm = i
        break
    i += 1
print("el mcm es:",mcm)
#-----------------------------------------------------------------------------------------
#2
"""En un supermercado se ingresa repetidamente el precio de un producto y el número
de unidades a comprar por cliente (un cliente solo puede comprar un tipo de producto). Validar
que el precio del producto y el número de unidades no debe ser negativo ni cero. A partir de 5
unidades se realiza un descuento del 10% sobre el total de la compra. Los clientes se
identifican por un número de orden consecutivo automático. Muestre el importe de dinero que
debe pagar el cliente. El proceso finaliza al terminar la jornada laboral. Mostrar el número
de orden del cliente que pagó el máximo importe y el total recaudado por el supermercado."""

importe_total = 0
cliente_maximo = 0
importe_maximo = 0
orden = 0
while True: 
    precio_unitario = float(input('Precio unitario: '))
    cantidad = int(input('Cantidad: '))
    
    if precio_unitario <= 0 or cantidad <= 0:
        print('Precio y cantidad deben ser mayores que cero')
        continue
    
    orden += 1
    importe = precio_unitario * cantidad * (0.9 if cantidad >= 5 else 1)
    print(f'El importe del cliente {orden} es ${importe:.2f}')
    
    importe_total += importe

    if importe > importe_maximo:
        importe_maximo = importe
        cliente_maximo = orden
    
    continuar = input('Continuar (s/n): ')
    if continuar.lower() != 's':
        break

print(f'El cliente {cliente_maximo} pagó el máximo importe ${importe_maximo:.2f}')
print(f'El total recaudado por el supermercado es ${importe_total:.2f}')

#EJERCICIOS (1)
"""Analizar y ejecutar los siguientes algoritmos en Python, luego realizar la prueba de escritorio:
manual y automático utilizando el debugger del VSC"""

#PROBAR CON 11
#VERIFICAR SI UN NUMERO ES PRIMO O NO
#FORMA 1 
nro = int(input('Ingrese nro:'))
dsor = 2
es_primo = True

if nro <= 1:
   es_primo = False
while dsor < nro and es_primo:
    resto = nro % dsor
    if resto == 0:
       es_primo = False
    else:
       dsor += 1
print('Es primo:', es_primo)

#FORMA 2 | DETECTAR SI UN NUMERO ES PRIMO O NO
nro = int(input('Ingrese nro:'))
dsor = 2
es_primo = True

if nro <= 1:
   es_primo = False
while nro > dsor:
   if nro % dsor == 0:
       es_primo = False
       break
   else:
      dsor += 1
print(es_primo)

#FORMA 3 USANDO FOR
nro = int(input('Ingrese nro:'))

if nro <= 1:
    es_primo = False
else:
    es_primo = True
    for dsor in range(2, (nro//2)+1):
        if nro % dsor == 0:
            es_primo = False
            break

print('Es primo:', es_primo)

#FORMA 2 
nro = int(input('Ingrese un número: '))
es_primo = True

for dsor in range(2, nro):
    resto = nro % dsor
    if resto == 0:
        es_primo = False
        print(es_primo)
        break
else:
    print(es_primo)
    
#OTRA FORMA DE FINALIZAR LA FORMA 2
nro = int(input('Ingrese un número: '))

es_primo = True

for dsor in range(2, nro):
    resto = nro % dsor
    if resto == 0:
        es_primo = False
        break

if es_primo:
    print(nro, 'es un número primo')
else:
    print(nro, 'no es un número primo')

#PROBANDO CON x = 3
x = int(input('x:'))
y = 0
iter = x
while iter > 0:
    y += x
    iter -= 1
    print(y, iter)
    
#PROBAR CON: 6, 7, 9, 4

contador = 0
suma = 0
logico_max = True
continuar = 's'
while (continuar == 's'):
   nota = float(input('Ingrese nota:'))
   suma += nota
   contador += 1
   if logico_max:
      logico_max = False
      nota_max = nota
      pos_nota_max = contador
else:
   if nota > nota_max:
      nota_max = nota
      pos_nota_max = contador
   continuar = input('Continuar (s/n):')
promedio = suma/contador
print('Promedio: ', promedio)
print('Nota máxima: ', nota_max)
print('Posición Máximo: ', pos_nota_max)

#EJERCICIO 2.a)
"""Analizar y ejecutar los siguientes códigos en Python, luego debe cambiar la sentencia
repetitiva for por la sentencia while"""

#USANDO FOR TABLA DE MULTIPLICAR

tabla = int(input("ingrese el numero a multiplicar: "))
print(f"ESTA ES LA TABLA DEL:{tabla}")

for i in range(1,11):
    print(f"{tabla} x {i} = {tabla*i}")
    
#USANDO WHILE TABLA DE MULTIPLCIAR

tabla = int(input("ingresar un numero para crear la tabla: "))
max_num = int(input("ingresar hasta que numero quiere su tabla: "))
i = 1

while i <= max_num:
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")
    i += 1

#2.b)
vi = int(input('vi:'))
vf = int(input('vf:'))
for ddo in range (vi, vf):
   divisores = 0
   print('')
   print(ddo,': ', end='')
   for dsor in range (2,ddo):
      if ddo % dsor == 0:
         print(dsor, ',', end='')
         divisores += 1
   if divisores == 0:
      print('es un número primo!', end='')
print('\n')

#EJERCICIO 3
"""Escribir un algoritmo que calcule y muestre todos los divisores de un número entero"""
#"""LOGICA: QUE UN NUMERO SEA DIVISOR SIGNIFICA QUE SU RESTO DA CERO, SPRINTEAMOS CADA VEZ QUE
#ESO PASE, LE SUMAMOS 1 AL CONTADOR PARA VERIFICAR Q EN TODOS LOS PASOS PASE ESO"""
numero_entero = int(input("ingrese un numero entero: "))
i = 1
while i <= numero_entero:
    if numero_entero % i == 0:
        print(i)
    i += 1
    
#EJERCICIO 4
"""Escribir un algoritmo que calcule y muestre la división entera de dos números enteros ddo
y dsor mediante restas sucesivas."""

ddo = int(input("ingrese ddo: "))
dsor = int(input("ingrese dsor: "))
i = 0
while ddo >= dsor:
    ddo = ddo - dsor
    i += 1
print(f"La division es igual a {i} y el resto es {ddo}")

#EJERCICIO 5
"""Muestre todos los números primos que hay en un intervalo [inicial, final]"""
#ESTA MAL PORQUE NO MUESTRA EL 2 PERO SI EL 1 
numero_inicial = int(input("ingrese el numero inicial: "))
numero_final = int(input("ingrese el numero final: "))

while numero_inicial <= numero_final:
    if numero_inicial % 2 != 0:
        print(numero_inicial)
    numero_inicial += 1

#FORMA CORRECTA
inicial = int(input("Ingrese número inicial: "))
final = int(input("Ingrese número final: "))

while inicial <= final:
    if inicial > 1:
        es_primo = True
        for i in range(2, inicial):
            if inicial % i == 0:
                es_primo = False
                break
        if es_primo and (inicial % 2 != 0 or inicial == 2):
            print(inicial)
        else:
            print(f"{inicial} no es un número primo")
    else:
        print("El número inicial debe ser mayor que 1")
    inicial += 1
    
#FORMA 2 SIN BREAK | LA DIFERENCIA ES QUE EN LA LINEA DEL FOR SE VERIFICA CONSTANTEMENTE SI EL
#NUMERO ES DIFIVISIBLE POR "I", PERO "ES_PRIMO" UNA VEZ FALSO PERMANECE

inicial = int(input("Ingrese número inicial: "))
final = int(input("Ingrese número final: "))

while inicial <= final:
    if inicial > 1:
        es_primo = True
        for i in range(2,inicial):
            if inicial % i == 0:
                es_primo = False
        if es_primo and (inicial % 2 != 0 or inicial == 2):
            print(inicial) 
    inicial += 1

#EJERCICIO 6
"""Leer números enteros, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria
de todos los números positivos ingresados"""

suma = 0 

while True:
    entero = int(input("Ingrese un numero entero: "))
    suma += entero
    if entero == 0:
        break
print("la sumatoria de los numeros es:",suma)

#EJERICICIO 7
"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
que ha cumplido (desde 1 hasta su edad). Por ejemplo si ingresa: 18, Debe mostrar: 1 año,
2 años, 3 años, …, 18 años"""

edad = int(input("ingrese su edad"))
i = 0

while i <= edad:
   print(i,"año")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
   i += 1
   
#AL REVES

edad = int(input("Ingrese su edad: "))
i = edad

while i >= 0:
    print(i,"año")
    i -= 1
    
#EJERCICIO 8
"""Realizar el código de un programa que solicite al usuario un número entero positivo
(debe validar que cumpla ésta condición) y muestre por pantalla todos los números impares
desde 1 hasta ese número. Resuelto lo anterior, comente las líneas de código y agregue otras
que muestre los impares en forma decreciente desde el número ingresado hasta 1"""

#MUESTRA EN PANTALLA TODOS LOS NUMEROS IMPARES DESDE EL 1 HASTA EL NUMERO INGRESADO

numero = int(input("Ingresar un numero entero positivo: "))
i = 1

while numero >= i:
   if i % 2 != 0:
      print(i)
   i += 1

#MUESTRA EN PANTALLA TODOS LOS NUMEROS IMPARES PERO DE FORMA CRECIENTE
numero = int(input("Ingresar un numero entero positivo: "))
i = numero

while i >= 0:
   if i % 2 != 0:
      print(i)
   i -= 1

#EJERCICIO 9
"""Escribir un programa que solicite ingresar la cantidad de alumnos de un curso y cada nota
de los mismos. Finalmente deberá mostrar cuántos tienen notas mayores o iguales a 7 y cuántos
menores a 7. También calcule y muestre el promedio de todos los valores ingresados."""

alumnos = int(input("Ingresar la cantidad de alumnos: "))
i = 1
mayor_a_7 = 0
menores_a_7 = 0
x = 0
y = 0
while i <= alumnos:
    nota = float(input(f"Ingrese la nota del alumno numero {i}: "))
    i += 1
    if nota >= 7:
        mayor_a_7 = mayor_a_7 + nota
        x += 1 
    if nota < 7:
        menores_a_7 += nota
        y += 1

print(f"Alumnos con nota mayor o igual 7: {x}")
print(f"Alumnos con nota menor a 7: {y}")
promedio = float(input(f"El promedio es: {(menores_a_7 + mayor_a_7) / alumnos}"))

#FORMA 2 
alumnos = int(input("Ingresar la cantidad de alumnos: "))
if alumnos < 0:
    print("imposible")
else:
    i = 1
    mayor_a_7 = 0
    menores_a_7 = 0
    x = 0
    y = 0

    while i <= alumnos:
        nota = float(input(f"Ingrese la nota del alumno numero {i}: "))
        i += 1
        if nota >= 7:
            mayor_a_7 = mayor_a_7 + nota
            x += 1
        if nota < 7:
            menores_a_7 += nota
            y += 1

    print(f"Alumnos con nota mayor o igual 7: {x}")
    print(f"Alumnos con nota menor a 7: {y}")
    promedio = float(input(f"El promedio es: {(menores_a_7 + mayor_a_7) / alumnos}"))

#EJERCICIO 13
""" Mediante un menú de opciones el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción
incorrecta, se debe informar del error. Volver a mostrar las tres opciones luego de ejecutada cada opción,
permitiendo volver a elegir. Si elige las opciones 1 muestre un texto de Bienvenida, 2 mostrar el mayor de
cinco valores numéricos ingresados. Si elige la opción 3, el programa finalizará."""

while True:
    opcion = input("Ingrese: opción 1, opción 2, opcción 3: ")
    if opcion == "1":
        print("¡Bienvenida!")
    elif opcion == "2":
        i = 0
        mayor_numero = 0 
        while i < 5:
            cinco_num  = int(input("Ingrese 5 numeros cualesquiera: "))
            i += 1
            if cinco_num > mayor_numero:
                mayor_numero = cinco_num
        print("-> El número mayor entre los 5 es el:",mayor_numero)
    elif opcion == "3":
        print("El programa finalizó")
        break
    else:
        print("Opción incorrecta")