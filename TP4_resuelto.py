#CASOS DE ESTUDIO
'''Diseñar un algoritmo que ordene tres números a, b, c en forma ascendente utilizando
un módulo denominado menorMayor que tiene dos parámetros y que devuelve en el primer
parámetro el valor menor y en el segundo el valor mayor de los parámetros respectivamente.'''

def menor_mayor(a, b):
    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a
    return menor, mayor

def leer():
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    return a, b, c

#principal
a, b, c = leer()
a, b = menor_mayor(a, b)
b, c = menor_mayor(b, c)
a, b = menor_mayor(a, b)
print(f'{a}, {b}, {c}')

#OTRA FORMA SIN USAR 2 FUNCIONES
def menorMayor(a, b):
    if a < b:
        menor = a
        mayor = b
    else:
        menor = b
        mayor = a
    return menor, mayor

#ORIGINAL
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
a, b = menorMayor(a, b)
b, c = menorMayor(b, c)
a, b = menorMayor(a, b)
print(f"{a}, {b}, {c}")

#CASO DE ESTUDIO
def modulo_uno():
    global a  #2
    a = 7     #3
    print(a)  #4
    return #-> no es necesario el return

a = 2
modulo_uno()
print(a)

#CASO DE ESTUDIO ->>>>>> ANALIZAR CON PROFUNDIDAD
def modulo_uno():
    def modulo_dos():
        global a   
        print(a)
        a = 1
        return

    a = 3    
    modulo_dos()
    print(a)
    return

a = 4
modulo_uno()    
print(a)

#EJERCICIO 2
"""Escribir un módulo denominado PMS que tiene dos parámetros formales base y exponente. Calcular la base
elevada al exponente, siendo la base un número real cualquiera y exponente un valor entero positivo o nulo.
Utilizar las multiplicaciones sucesivas de la base. Si el cálculo no puede realizarse debe devolver cero (0)."""

def PMS(base, exponente):
    if exponente < 0:
        return 0
    resultado = 1
    for i in range(exponente):
        resultado *= base
    return resultado

#ORIGINAL
resultado = PMS(2,5)
print(resultado)

#EJERCICIO 3

"""Mediante un menú de opciones resolver:"""

#a. Ingresar dos valores a y b validando que estén en el intervalo [0,9] ->
#-> y mostrarlos en letras separados por una serie de asteriscos
#b. Si a y b son pares intercambiar los valores y mostrarlos en letras
#c. Salir

# Función para convertir un número en letra
def convertir_numero_letra(numero):
    numeros_letras = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    return numeros_letras[numero]

# Función para validar que un número esté en el intervalo [0,9]
def validar_numero(numero):
    return numero >= 0 and numero <= 9

# Función para intercambiar dos valores
def intercambiar_valores(a, b):
    return b, a

# Función para imprimir una serie de asteriscos
def imprimir_asteriscos():
    print("**********")

# Menú de opciones
while True:
    print("Menú de opciones:")
    print("a. Ingresar dos valores a y b y mostrarlos en letras separados por asteriscos")
    print("b. Intercambiar valores si son pares y mostrarlos en letras")
    print("c. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "a":
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        
        if validar_numero(a) and validar_numero(b):
            letra_a = convertir_numero_letra(a)
            letra_b = convertir_numero_letra(b)
            imprimir_asteriscos()
            print(f"{letra_a} * {letra_b}")
            imprimir_asteriscos()
        else:
            print("Error: los números deben estar en el intervalo [0,9]")
    
    elif opcion == "b":
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de b: "))
        
        if a % 2 == 0 and b % 2 == 0:
            a, b = intercambiar_valores(a, b)
            letra_a = convertir_numero_letra(a)
            letra_b = convertir_numero_letra(b)
            imprimir_asteriscos()
            print(f"{letra_a} * {letra_b}")
            imprimir_asteriscos()
        else:
            print("Error: ambos números deben ser pares")
    
    elif opcion == "c":
        break
    
    else:
        print("Error: opción inválida")
        
#OPCION 2 HECHA POR MI

def validar(numero):
        return numero >= 0 and numero <= 9

def string(numero):
    numero_letras = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    return numero_letras[numero]
    
def pares(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return b, a
    else:
        print("Numeros inpares")
        
while True:
    print("A. Ingresa dos valores del [0,9] para convertirlos en string")
    print("B. Si a y b son valores pares se intercambian y se muestran en string")
    print("C. Salir")
    opcion = input("Ingresa la opción que consideres: ")
    
    if opcion == "C":
        break
    a = int(input("Ingresar a: "))
    b = int(input("Ingresar b: "))
    
    if opcion == "A":
        if validar(a) and validar(b):
            letra_a = string(a)
            letra_b = string(b)
            print(f"{letra_a}, {letra_b}")
            
    elif opcion == "B":
        a, b = pares(a, b)
        letra_a = string(a)
        letra_b = string(b)
        print(f"{letra_a} * {letra_b}")

#EJERCICIO 4
"""Analizar, ejecutar, realizar la prueba de escritorio en forma manual y con el debugger del VSC"""
#Pruebe para s = 1
def dos(s):
    s = s + 5
    print('Dos:', s)
def uno(s):
    s = s + 10
    dos(s)
    print('Uno:', s)
    return s
#Principal
s = int(input('Inicial:'))#1
s = s + uno(s)
print('Global:',s)

"""Pruebe para v = 10, luego elimine el # de la última línea,
debe mostrar el tiempo. ¿Cómo evita utilizar global v?  """ #HECHO

def acelerar(v):
    global tiempo
    tiempo = 1
    v+= 5
    return v
#PRINCIPAL
v = float(input('Velcidad?:'))
print(f'Velocidad: {v} km/h')
print('Aumento la velocidad!')
v = acelerar(v)
print(f'Velocidad: {v} km/h')
print('Tiempo:', tiempo)

#EJERCICIO 5
""" Diseñar un algoritmo que simule una calculadora básica debe utilizar un módulo denominado calcular(op,a,b)
dónde los parámetros a y b son variables de tipo float y representan los operandos de la expresión aritmética y
op es un parámetro de tipo cadena de caracteres que puede ser: ‘suma’, ‘resta’, ‘multiplicación’ y ‘división’,
y se realiza la operación correspondiente. Mediante un menú de opciones el operador debe ingresar los datos
de a y b y luego debe poder seleccionar una operación aritmética."""

def calculadora(op, a , b):
    if op == "1":
        return a + b
    elif op == "2":
        return a - b
    elif op == "3":
        return a * b
    elif op == "4":
        if b == 0:
            return "Error, division por 0"
        else:
            return a / b
    else:
        return "Error: operador invalido"
    
#ORIGINAL
op = input("¿Qué operación desea realizar?: \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n Quiero la numero: ")
a = float(input("ingrese a: "))
b = float(input("ingrese b: "))
resultado = calculadora(op, a, b)
print(resultado)

# Definir la función para calcular la operación aritmética | OTRA FORMA DE CHATGPT
# def calcular(op, a, b):
#     if op == 'suma':
#         return a + b
#     elif op == 'resta':
#         return a - b
#     elif op == 'multiplicación':
#         return a * b
#     elif op == 'división':
#         if b == 0:
#             return "Error: división por cero"
#         else:
#             return a / b
#     else:
#         return "Error: operador inválido"

# # Programa principal
# while True:
#     # Mostrar menú de opciones
#     print("Menú de opciones:")
#     print("1. Suma")
#     print("2. Resta")
#     print("3. Multiplicación")
#     print("4. División")
#     print("5. Salir")

#     # Pedir al usuario que seleccione una opción
#     opcion = int(input("Seleccione una opción (1-5): "))

#     # Salir del programa si la opción es 5
#     if opcion == 5:
#         break

#     # Pedir al usuario que ingrese los valores de a y b
#     a = float(input("Ingrese el valor de a: "))
#     b = float(input("Ingrese el valor de b: "))

#     # Realizar la operación aritmética seleccionada
#     if opcion == 1:
#         resultado = calcular('suma', a, b)
#     elif opcion == 2:
#         resultado = calcular('resta', a, b)
#     elif opcion == 3:
#         resultado = calcular('multiplicación', a, b)
#     elif opcion == 4:
#         resultado = calcular('división', a, b)
#     else:
#         resultado = "Error: opción inválida"

#     # Mostrar el resultado
#     print("El resultado es:", resultado)

#EJERCICIO 6 
"""Escribir un algoritmo que simule las operaciones que se realizan en un cajero automático de acuerdo al
esquema jerárquico de los módulos que se nota en la figura:""" 

# Módulo de lectura y validación de clave
def validar_clave():
    clave = input("Ingrese su clave: ")
    # Lógica de validación de clave
    if clave == "1234":
        return True
    else:
        return False

# Módulo de consulta de saldo
def consultar_saldo():
    # Lógica de consulta de saldo
    saldo = 10000
    print(f"Su saldo actual es de ${saldo}")

# Módulo de retiro de efectivo
def retirar_efectivo():
    # Lógica de retiro de efectivo
    cantidad = int(input("Ingrese la cantidad a retirar: "))
    if cantidad > 0 and cantidad % 100 == 0:
        print(f"Retire su dinero: ${cantidad}")
    else:
        print("La cantidad ingresada no es válida")

# Módulo de depósito
def depositar():
    # Lógica de depósito
    cantidad = int(input("Ingrese la cantidad a depositar: "))
    if cantidad > 0:
        print(f"Depósito realizado por ${cantidad}")
    else:
        print("La cantidad ingresada no es válida")

# Menú principal
def menu():
    while True:
        print("1. Consultar saldo")
        print("2. Retirar efectivo")
        print("3. Depositar")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            consultar_saldo()
        elif opcion == 2:
            retirar_efectivo()
        elif opcion == 3:
            depositar()
        elif opcion == 4:
            print("Operación finalizada")
            break
        else:
            print("Opción inválida")

# Programa principal
if validar_clave():
    menu()
else:
    print("Clave incorrecta. Intente nuevamente")
    
#EJERCICIO 7

"""Un tanque de agua tiene una capacidad fija en litros que no puede cambiar. Se puede cargar y vaciar un
volumen determinado de agua en litros. No se puede llenar más de su capacidad así como tampoco se puede
vaciar más del volumen que posee. Se pide implementar un algoritmo en python que mediante un menú de opciones y de
manera modular que permita cargar o descargar una cantidad permitida de agua solicitado por el operador,
también se debe poder consultar el volumen de agua en el tanque."""

# Función para cargar el tanque de agua
def cargar_tanque(tanque, cantidad):
    if tanque['volumen'] + cantidad > tanque['capacidad']:
        print('No se puede cargar más agua, el tanque está lleno.')
    else:
        tanque['volumen'] += cantidad
        print(f'Se han cargado {cantidad} litros de agua en el tanque.')
    return tanque

# Función para descargar el tanque de agua
def descargar_tanque(tanque, cantidad):
    if tanque['volumen'] - cantidad < 0:
        print('No se puede descargar más agua, el tanque está vacío.')
    else:
        tanque['volumen'] -= cantidad
        print(f'Se han descargado {cantidad} litros de agua del tanque.')
    return tanque

# Función para consultar el volumen de agua en el tanque
def consultar_volumen(tanque):
    print(f'El tanque tiene un volumen de {tanque["volumen"]} litros.')
    return

# Programa principal
tanque = {'capacidad': 1000, 'volumen': 500}

while True:
    print('\n--- MENÚ DE OPCIONES ---')
    print('1. Cargar agua en el tanque')
    print('2. Descargar agua del tanque')
    print('3. Consultar volumen de agua en el tanque')
    print('4. Salir')

    opcion = input('\nIngrese una opción (1-4): ')
    
    if opcion == '1':
        cantidad = int(input('Ingrese la cantidad de agua a cargar: '))
        tanque = cargar_tanque(tanque, cantidad)
    elif opcion == '2':
        cantidad = int(input('Ingrese la cantidad de agua a descargar: '))
        tanque = descargar_tanque(tanque, cantidad)
    elif opcion == '3':
        consultar_volumen(tanque)
    elif opcion == '4':
        print('¡Hasta luego!')
        break
    else:
        print('Opción inválida, intente de nuevo.')
        
#PUNTO 8    
"""Existe una plataforma donde se colocan tanques de agua. Para esta plataforma se quiere implementar un
algoritmo denominado: controlador_de_tanques que realiza las mismas operaciones que el algoritmo del punto
anterior. Al crearse el controlador_de_tanques se debe determinar la cantidad máxima de tanques que puede
controlar de 2 a 4. El controlador_de_tanques permite agregar y quitar tanques de agua. Se desea saber
cuántos tanques de agua hay, el volumen ocupado con agua y la capacidad vacía que tiene cada tanque."""
