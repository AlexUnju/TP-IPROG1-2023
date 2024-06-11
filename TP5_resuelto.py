#Casos de estudio 
#1 Analizar, realizar la prueba de escritorio y mostrar la salida de los siguientes programas:

# i = 10
i = int(input('i:'))
if (i == 10):
    if (i < 15):
        print('uno')
if (i < 12):
    print('dos')
else:
    print('tres')
    
# a = 7, b = 9, c = 3
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
if (a>b and a>c) and (a != b and a != c):
    print(a)
elif (b>a and b>c) and (b != a and b != c):
    print(b)
elif (c>a and c>b) and (c != a and c != b):
    print(c)
else:
    print("iguales")
    
# a = 3, b = 9, c = 7
a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
x = a != b
y = not c >= a and not b == 0
z = not x or y
if not x or y:
    print('alternativa 1')
elif not x or not y and z:
    print('alternativa 2')
elif not x and not z or y:
    print('alternativa 3')
else:
    print('alternativa 4')
    
#EJERCICIO 2
""" Analizar, realizar la prueba de escritorio y ejecutar en python cada uno de los casos del algoritmo de la serie
par, s = 2 + 4 + 6 + 8 + 10 + 12 + 14 +… Mostrar en cada caso el valor de la suma s y el valor del término i.

a. hasta que la acumulación de términos sea mayor que x, para x=25.
b. hasta el n-ésimo término, para n=4.
c. hasta que el n-ésimo término sea mayor o igual que q, para q=13"""
#serie_par_a
x = int(input('valor a superar:'))
s = 0
i = 0
while s <= x:
    i += 1
    s += 2 * i
print(f'serie = {s}; términos = {i-1}')#-> creo que ponen el -1 porque cuando "i" vale 4
#series es igual a "n", es decir, vale 20. 

#serie_par_b
n = int(input('nro términos: '))
s = 0
for i in range(1, n+1):
    s += 2 * i
n_esimo_termino = 2 * n
print(f'serie = {s} términos = {n} n-ésimo término = {n_esimo_termino}')

#serie_par_c
q = int(input('término a superar:'))
s = 0
i = 1
t = 2 * i
while t < q:
    s += t
    i += 1
    t = 2 * i
print(f'serie={s} términos={i}')

#EJERCICIO 3 HECHO POR MI
"""Los tres lados a, b y c de un triángulo deben satisfacer la desigualdad triangular: cada uno de los lados no
puede ser más largo que la suma de los otros dos. Escriba un programa que reciba como entrada los tres lados
de un triángulo, e indique: si acaso el triángulo es inválido; y si no lo es, qué tipo de triángulo es (equilátero,
isósceles, escaleno"""

def invalido(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True
        
def equilatero(a, b, c):
    if a == b == c:
        print("Es un triangulo equilatero")
        
def isoseles(a, b, c):
    if a == b != c or c == a != b or c == b != a:
        print("Es un triangulo isoseles")
        
def escaleno(a, b, c):
    if a != b != c:
        print("Es un triangulo escaleno")
        
#ORIGINAL
while True:
    print()
    a = int(input("Ingresar lado a: "))
    b = int(input("Ingresar lado b: "))
    c = int(input("Ingresar lado c: "))
    print()
    inv = invalido(a, b, c)
    if inv:
        equilatero(a, b, c)
        isoseles(a, b, c)
        escaleno(a, b, c)
    else:
        print("Triangulo invalido")
    
#HECHO POR CHATGPT

def verificar_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("El triángulo es inválido.")
    elif a == b == c:
        print("El triángulo es equilátero.")
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

# Obtener los lados del triángulo desde la entrada del usuario
a = float(input("Ingrese el lado a: "))
b = float(input("Ingrese el lado b: "))
c = float(input("Ingrese el lado c: "))

# Verificar y determinar el tipo de triángulo
verificar_triangulo(a, b, c)

#EJERCICIO 4
"""Escriba un programa en python que mediante un menú de opciones: ingrese la fecha de nacimiento validando los datos,
muestre la edad del usuario y una opción de despedida con el cierre del programa. El programa debe tener en
cuenta si el cumpleaños ingresado ya pasó durante este año, o si todavía no ocurre."""

import datetime

def obtener_edad(fecha_nacimiento):
    fecha_actual = datetime.date.today()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

def ingresar_fecha_nacimiento():
    while True:
        try:
            dia = int(input("Ingrese el día de nacimiento (1-31): "))
            mes = int(input("Ingrese el mes de nacimiento (1-12): "))
            anio = int(input("Ingrese el año de nacimiento (yyyy): "))
            fecha_nacimiento = datetime.date(anio, mes, dia)
            return fecha_nacimiento
        except ValueError:
            print("Fecha de nacimiento inválida. Por favor, ingrese nuevamente.")

def mostrar_edad():
    fecha_nacimiento = ingresar_fecha_nacimiento()
    edad = obtener_edad(fecha_nacimiento)
    print("Su edad es:", edad, "años")

def despedida():
    print("¡Hasta luego!")

# Menú de opciones
while True:
    print("Menu:")
    print("1. Ingresar fecha de nacimiento y mostrar edad")
    print("2. Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        -()
    elif opcion == "2":
        despedida()
        break
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.")

# def validar_fecha(dia, mes, año):
#     return dia == 19 and mes == 10 and año == 2001

# def edad():
#     if 

# while True:
#     print("\t MENU DE OPCIONES")
#     print("1. Ingrese su fecha de nacimiento")
#     print("2. Salir")
#     print()
#     option = int(input("Elija la acción que desee realizar: "))
#     if option == 1:
#         dia = int(input("Ingrese su dia de nacimiento: "))
#         mes = int(input("Ingrese su mes de nacimiento: "))
#         año = int(input("Ingrese su año de nacimiento: "))
#         true = validar_fecha(dia, mes, año)
#         if true:
#             print()
#             print("¡Usted tiene 21 años! ¡Felicidades!")
#             print()
#     elif option == 2:
#         print("Adiós, cuidese mucho!")
#         break

#EJERCICIO 5 | ¿Puede explicar con sus propias palabras por qué ambos programas imprimen lo mismo?

"""Argumentos posicionales"""
def nombre_persona(nombre, apellido):
    print(f'{nombre} {apellido}')
    
nombre_persona('Lionel', 'Messi')

"""Argumentos de palabras clave"""
def nombre_persona(nombre, apellido):
    print(f'{nombre} {apellido}')
    
nombre_persona(apellido = 'Messi', nombre = 'Lionel')

#EJERCICIO 6 | Analice y realice la prueba de escritorio utilizando el debugger de VSC
#a
def mi_funcion(x, y=50):
    '''Parámetros con valores iniciales'''
    print('x:', x)
    print('y:', y)
    
a = int(input('a:')) #10
mi_funcion(a)
print(mi_funcion.__doc__)
#b
def f1():
    '''Juan Galan: poeta jujeño 1913-1963'''
    s = '''Jujuy le han puesto de nombre,
debe ser cosa de Dios;  
en el idioma del cielo  
así se llama el amor...
'''
    def f2():
        print(s)
    
    f2()
    
f1()
print(f1.__doc__)   

#EJERCICIO 7
"""Realizar la multiplicación de dos números enteros n1 y n2 mediante sumas sucesivas, hacer dos algoritmos uno
con la estructura while y otro con la estructura for. Finalmente haga un algoritmo que multiplique tres factores
mediante sumas sucesivas. ¿Cómo haría un algoritmo que multiplique muchos factores con el mismo método
anterior?"""
#CON WHILE
def multiplicar(n1, n2):
    contador = 0
    suma = 0
    while contador < n2:
        suma += n1
        contador += 1
    return suma

#ORIGINAL
n1 = int(input("Ingresar n1: "))
n2 = int(input("Ingresar n2: "))
resultado = multiplicar(n1, n2)
print(f"El resultado es: {resultado}")

#CON FOR
def multiplicar(n1, n2):
    suma = 0
    for i in range(n2):
        suma += n1
    return suma

#ORIGINAL
n1 = int(input("Ingresar n1: "))
n2 = int(input("Ingresar n2: "))
resultado = multiplicar(n1, n2)
print(f"El resultado es: {resultado}")

def multiplicar(n1, n2):
    suma = 0
    for i in range(n2):
        suma += n1
    return suma

#MULTIPLICANDO 3 NUMEROS CON WHILE
def multiplicacion_while(n1, n2):
    resultado = 0
    contador = 0

    while contador < n2:
        resultado += n1
        contador += 1

    return resultado

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))
 
producto = multiplicacion_while(n1, n2)
resultado = multiplicacion_while(producto, n3)
print("El resultado de la multiplicación de tres factores es:", resultado)

# MULTIPLICANDO TRES NUMEROS CON FOR
def operacion(a,b):
    suma = 0
    for i in range(b):
        suma += a
    return suma

#ORIGINAL
n1 = int(input("Ingresar n1: "))
n2 = int(input("Ingresar n2: "))
n3 = int(input("Ingresar n3: "))
resultado = operacion(n1, n2)
tresNumeros = operacion(resultado, n3)
print(f"el resultado es: {resultado}")
print(f"el resultado de los tres numeros enteros es: {tresNumeros}")

#EJERCICIO 8
"""Escribir un módulo que utiliza tres parámetros que representan un ancho y altura, el tercer parámetro es un
carácter a utilizar en el dibujo de un rectángulo. En el ejemplo siguiente se leen los valores 5 (ancho), 3
(altura) con el carácter “o”, resultando el gráfico:
o o o o o
o o o o o
o o o o o
"""
def parametro(ancho,altura,caracter):
    for _ in range(altura):
        linea = caracter * ancho
        print(linea)
    
#ORIGINAL
ancho = int(input("Ingresar ancho: "))
alto = int(input("Ingresar alto: "))
caracter = input("Ingresar caracter para dibujar el rectangulo: ")
parametro(ancho,alto,caracter) 

#EJERCICIO 9
"""Escribir un programa en python que consulte a una cantidad n de estudiantes, el nombre y las notas de las
asignaturas de un curso (Análisis Matemático, Álgebra, Introducción a la Programación, e Inglés). Pregunte al
usuario la nota que ha obtenido en cada asignatura. Mostrar para cada estudiante, cuántas asignaturas aprobó
(nota mayor a 50 incluido), y si la nota es menor a 30 debe alertar al estudiante que “ES MUY PROBABLE QUE DEBA
RECURSAR”. Al final el programa debe mostrar el nombre del estudiante con el promedio más alto; el nombre
del estudiante y la materia de aquel que tiene la nota mínima de todo el curso."""

def aprobado(nota):
    if nota > 50:
        return "Usted está aprobado"
    elif nota < 30:
        return "ES PROBABLE QUE DEBA RECURSAR"

def promedio(*notas):
    suma = sum(notas)
    return suma / len(notas)

def nota_minima(nombre, *notas):
    min_nota = min(notas)
    return min_nota

def validar_nota(nota):
    while not (0 <= nota <= 100):
        nota = float(input("Ingrese una nota válida (entre 0 y 100): "))
    return nota

max_promedio = 0
min_nota = 100
crack = ""
min_crack = ""

while True:
    print()
    nombre = input("Ingrese el nombre del estudiante: ").capitalize()
    print()
    analisis = validar_nota(float(input("Ingrese la nota de Análisis Matemático: ")))
    algebra = validar_nota(float(input("Ingrese la nota de Álgebra: ")))
    programacion = validar_nota(float(input("Ingrese la nota de Introducción a la Programación: ")))
    ingles = validar_nota(float(input("Ingrese la nota de Inglés: ")))
    print()
    print(f"Nota de Análisis Matemático: {analisis} - {aprobado(analisis)}")
    print(f"Nota de Álgebra: {algebra} - {aprobado(algebra)}")
    print(f"Nota de Programación: {programacion} - {aprobado(programacion)}")
    print(f"Nota de Inglés: {ingles} - {aprobado(ingles)}")
    
    prom = promedio(analisis, algebra, programacion, ingles)
    if prom > max_promedio:
        max_promedio = prom
        crack = nombre
    print()
    print(f"{crack} tiene el promedio más alto, con {max_promedio}%")
    
    nota_min = nota_minima(nombre, analisis, algebra, programacion, ingles)
    if nota_min < min_nota:
        min_nota = nota_min
        min_crack = nombre
    print(f"{min_crack} obtuvo la menor nota de todos, con un: {min_nota}")
    
    opcion = input("¿Desea ingresar los datos de otro estudiante? (s/n): ")
    if opcion.lower() != "s":
        break

#EJERCICIO 10 PENDIENTE

#EJERCICIO 11

"""Realizar un programa modular que muestre un menú de opciones. Debe ingresar inicialmente dos valores que
representan el numerador y denominador de una fracción.

a. sumar_fracciones(n1,d1,n2,d2) calcula la suma de dos fracciones. El resultado es otra fracción cuyo
numerador es n1*d2+d1*n2 y denominador d1*d2. Se debe simplificar la fracción resultado.

b. restar_fracciones(n1,d1,n2,d2) calcula la resta de dos fracciones. El resultado es otra fracción
numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.

c. multiplicar_fracciones(n1,d1,n2,d2) calcula el producto de dos fracciones. El resultado es una fracción
con numerador n1*n2 y denominador d1*d2. Se debe simplificar la fracción resultado.

d. dividir_fracciones(n1,d1,n2,d2) calcula la división de dos fracciones. El resultado es una fracción con
numerador n1*d2 y denominador d1*n2. Se debe simplificar la fracción resultado.

En cada ejecución del programa deberá ingresar la fracción solicitando numerador y denominador. La fracción debe
simplificarse y mostrarse. Al mostrar la fracción se debe mostrar la misma simplificada. En caso de denominador 1,
sólo debe mostrar el numerador. Puede implementar una función simplificar_funcion(n,d) que devuelve 2 nuevos valores
resultados de la simplificación, para ello hay que dividir n y d por el mcd de ambos. Puede implementar una función
mcd(n,d) que devuelve el máximo común divisor de ambos parámetros."""

def menu_de_opciones():
    print()
    print("\t **BIENVENIDO AL MENU DE OPCINES**")
    print()
    print("1. Sumar Fracciones")
    print("2. Restar Fracciones")
    print("3. Multiplicar Fracciones")
    print("4. Dividir Fracciones")
    print()
    opcion = int(input("Ingresar la opción que desee ejecutar: "))
    return opcion

def sumar_fracciones(n1, d1, n2, d2):
    numerador = n1*d2+d1*n2
    denominador = d1*d2
    n, d = simplificar(numerador, denominador)
    return mostrar_fraccion(n, d)

def restar_fracciones(n1, d1, n2, d2):
    numerador = n1*d2-d1*n2
    denominador = d1*d2
    n, d = simplificar(numerador, denominador)
    return mostrar_fraccion(n, d)

def multiplicar_fracciones(n1, n2, d1, d2):
    numerador = n1*n2
    denominador = d1*d2
    n, d = simplificar(numerador, denominador)
    return mostrar_fraccion(n, d)

def dividir_fracciones(n1, n2, d1, d2):
    numerador = n1*d2
    denominador = n2*d1
    n, d = simplificar(numerador, denominador)
    return mostrar_fraccion(n, d)

def simplificar(n, d):
    divisor = mcd(n, d)
    return n // divisor, d // divisor

def mcd(n, d):
    while d != 0:
        n, d = d, n % d
    return n

def mostrar_fraccion(n, d):
    if d == 1:
        return f"{n}"
    else:
        return f"{n}/{d}"

#ORIGINAL
print("Ingrese la primera fracción: ")
n1 = int(input("Ingrese n1: "))
d1 = int(input("Ingrese n1: "))

print("Ingrese la segunda fracción: ")
n2 = int(input("Ingrese n2: "))
d2 = int(input("Ingrese n2: "))
opcion = menu_de_opciones()

if opcion == 1:
    print()
    print("La suma simplificada es:",sumar_fracciones(n1, n2, d1, d2))
    
elif opcion == 2:
    print()
    print("La  resta simplificada es:",restar_fracciones(n1, n2, d1, d2))
    
elif opcion == 3:
    print()
    print("La multiplicación simplificada es:",multiplicar_fracciones(n1, n2, d1, d2))
    
elif opcion == 4:
    print
    print("La división simplificada es:",dividir_fracciones(n1, n2, d1, d2))
    
#EJERCICIO 12
"""Se quiere determinar el importe a facturar a los clientes de unos grandes almacenes según estos criterios:
a. Si pagan con tarjeta oro tendrán un 15% de descuento.
b. Si pagan con tarjeta club tendrán un 5% de descuento.
c. Si la tarjeta (oro o club) es modalidad joven, tendrán un 5% plus de descuento."""

def gold_card(numero):
    return numero*(1 - 0.15)

def club_card(numero):
    return numero*(1 - 0.05) 

def mod_joven(numero):
    return numero*(1 - 0.05)

#ORIGINAL
while True:
    precio = int(input("Ingresar un precio: "))
    cantidad = int(input("Ingresar cantidad: "))
    print()
    print("\t **¿Cúal es su forma de pago?**")
    print("1. Tarjeta de oro (15% de descuento)")
    print("2. Tarjeta club (5% de descuento)")
    print()
    opcion = int(input("Ingrese la forma de pago: "))
    modalidad = input("¿Su tarjeta es de modalidad joven? si/no: ")
    
    if opcion == 1:
        total = gold_card(precio*cantidad)
        
    elif opcion == 2:
        total = club_card(precio*cantidad)
        
    if modalidad == "si":
        total = mod_joven(total)
    print("El total es:",total)
    print()
    
#EJERCICIO 13

"""Se quiere determinar la nómina de los empleados de una empresa de acuerdo con estos criterios:

a. Si el empleado es altamente productivo tendrá en nómina un plus de productividad.
b. Si el empleado es encargado de su grupo tendrá en nómina un plus de encargado.
c. Si el empleado ha cometido una infracción grave durante ese mes le será eliminado cualquier plus que
pudiera tener."""

