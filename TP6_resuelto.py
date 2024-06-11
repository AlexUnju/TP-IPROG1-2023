#CASO DE ESTUDIO 1
""" Analice, diseñe y codifique los siguientes enunciados en Python (usando listas)

1. Mediante un menú de opciones realizar el siguiente programa modular para gestionar
el listado de notas de un examen para los estudiantes de una institución educativa:

a. Registrar estudiantes: para cada uno se debe solicitar DNI, nombre y nota. Validar 
que la nota se encuentre entre 0 y 10. El proceso finaliza cuando el dni es igual a cero.
b. Mostrar el listado de estudiantes con sus respectivas notas.
c. Buscar a un estudiante por su DNI y mostrar su nombre y nota.
d. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).
e. Eliminar a un estudiante buscando por DNI. Emitir un mensaje de confirmación.
f. Mostrar el promedio de las notas ingresadas
g. Salir"""

# s = 'foobar'

# print(s[0] + s[-1])
# print(s[::-5])
# print(s[::-1][::-5])
# print(s[::5])
# print(s[::-1][-1] + s[len(s)-1])

def menu():
    estudiantes = {}
    while True:
        print()
        print("\t**MENU DE OPCIONES**")
        print("a. Registrar estudiantes")
        print("b. Mostrar el listado de estudiantes")
        print("c. Buscar estudiante por su DNI")
        print("d. Modificar la nota de un estudiante")
        print("e. Eliminar a un estudiante por su DNI")
        print("f. Mostrar el promedio general")
        print("g. Salir del menú")
        opcion = input("Ingresa la opción que desees realizar: ")
        if opcion == "a":
            registrar_estudiantes(estudiantes)
        elif opcion == "b":
            mostrar_listado(estudiantes)
        elif opcion == "c":
            buscar_estudiante(estudiantes)
        elif opcion == "d":
            modificar_nota(estudiantes)
        elif opcion == "e":
            eliminar_estudiante(estudiantes)
        elif opcion == "f":
            promedio(estudiantes)
        
            
def registrar_estudiantes(estudiantes):
    while True:
        dni = input("Ingrese su DNI (0 para salir): ")
        if dni == "0":
            break
        nombre = input("Ingrese su nombre completo: ")
        nota = int(input("Ingrese la nota correspondiente: "))
        while nota < 0 and nota > 10:
            nota = float(input("Ingrese la nota: "))
            print("Ingrese una nota valida (del 1 al 10)")
        estudiantes[dni] = {"nombre":nombre, "nota":nota}

def mostrar_listado(estudiantes):
    for clave, valor in estudiantes.items():
        print()
        print(F'DNI:{clave}')
        print(f'Nombre:{valor["nombre"]}')
        print(f'Nota:{valor["nota"]}')

def buscar_estudiante(estudiantes):
    dni_b = input("Ingrese el DNI que desea encontrar: ")
    if dni_b in estudiantes:
        estudiante = estudiantes[dni_b]
        print()
        print("DNI: {}".format(dni_b))
        print("Nombre: {}".format(estudiante["nombre"]))
        print("Nota: {}".format(estudiante["nota"]))
    else:
        print("Estudiante no registrado")
 
def modificar_nota(estudiantes):
    dni_b = input("Ingrese el DNI del estudiante para modificar la nota: ")
    nota = float(input("Ingrese la nueva nota: "))
    while nota < 0 and nota > 10:
        print("Ingrese una nota valida (del 1 al 10)")
        nota = float(input("Ingrese la nueva nota: "))
    if dni_b in estudiantes:
        print(f'Nombre actual:{estudiantes[dni_b]["nombre"]}')
        estudiante = estudiantes[dni_b]
        estudiante["nota"] = nota
        print("La nueva nota ha sido modificada correctamente. Revise el listado")
    else:
        print("DNI no encontrado en el sistema")

def eliminar_estudiante(estudiantes):
    dni_b = input("Ingrese el DNI del estudiando ha eliminar: ")
    if dni_b in estudiantes:
        del estudiantes[dni_b]
        print("Estudiante eliminado exitosamente! ")
    else:
        print("No existe el estudiante en el sistema")
        
def promedio(estudiantes):
    total_notas = sum(estudiante['nota'] for estudiante in estudiantes.values())
    cantidad_estudiantes = len(estudiantes)
    promedio_total = total_notas / cantidad_estudiantes
    print(f"El promedio total es de {promedio_total}")

#ORIGINAL
menu()

#OTRA FORMA CON CHATGPT
def menu():
    estudiantes = {}
    while True:
        print("\t**MENU DE OPCIONES**")
        print("a. Registrar estudiantes")
        print("b. Mostrar el listado de estudiantes")
        print("c. Buscar estudiante por su DNI")
        print("d. Modificar los datos de un estudiante")
        print("e. Eliminar a un estudiante por su DNI")
        print("f. Mostrar el promedio de las notas")
        print("g. Salir")
        print()
        opcion = input("Ingresar la opción que desea realizar: ")
        if opcion == "a":
            registrar_estudiantes(estudiantes)
        elif opcion == "b":
            mostrar_listado(estudiantes)
        elif opcion == "c":
            buscar_estudiante(estudiantes)
        elif opcion == "d":
            modificar_datos(estudiantes)
        elif opcion == "e":
            eliminar_estudiante(estudiantes)
        elif opcion == "f":
            mostrar_promedio(estudiantes)
        elif opcion == "g":
            print("Gracias por usar nuestro sistema!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def registrar_estudiantes(estudiantes):
    while True:
        dni = input("Ingrese el DNI del estudiante (0 para finalizar): ")
        if dni == "0":
            print()
            break
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = validar_nota()
        estudiantes[dni] = {"nombre": nombre, "nota": nota}

def validar_nota():
    while True:
        nota = input("Ingrese la nota del estudiante (0-10): ")
        if nota.isdigit() and 0 <= int(nota) <= 10:
            return int(nota)
        else:
            print("Ingrese una nota válida (0-10).")

def mostrar_listado(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("Listado de estudiantes:")
    for dni, datos in estudiantes.items():
        print("DNI:", dni)
        print("Nombre:", datos["nombre"])
        print("Nota:", datos["nota"])
        print()

def buscar_estudiante(estudiantes):
    dni_b = input("Ingrese el DNI del estudiante que desea buscar: ")
    estudiante = estudiantes.get(dni_b)
    if estudiante:
        print("Nombre:", estudiante["nombre"])
        print("Nota:", estudiante["nota"])
    else:
        print("No existe este DNI en nuestro sistema.")

def modificar_datos(estudiantes):
    dni_b = input("Ingrese el DNI del estudiante que desea modificar: ")
    estudiante = estudiantes.get(dni_b)
    if estudiante:
        print("Nombre actual:", estudiante["nombre"])
        nueva_nota = validar_nota()
        estudiantes[dni_b]["nota"] = nueva_nota
        print()
        print("Estudiante modificado correctamente.")
    else:
        print("No existe este DNI en nuestro sistema.")

def eliminar_estudiante(estudiantes):
    dni_b = input("Ingrese el DNI del estudiante que desea eliminar: ")
    if dni_b in estudiantes:
        del estudiantes[dni_b]
        print("Estudiante eliminado correctamente.")
    else:
        print("No existe este DNI en nuestro sistema.")

def mostrar_promedio(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    total_notas = sum(estudiante["nota"] for estudiante in estudiantes.values())
    promedio = total_notas / len(estudiantes)
    print("Promedio de notas:", promedio)

# Ejecutar el menú principal
menu()

#USANDO LISTAS
def menu():
    estudiantes = []
    while True:
        print("\t**MENU DE OPCIONES**")
        print("a. Registrar estudiantes")
        print("b. Mostrar el listado de estudiantes")
        print("c. Buscar estudiante por su DNI")
        print("d. Modificar los datos de un estudiante")
        print("e. Eliminar a un estudiante por su DNI")
        print("f. Mostrar el promedio de las notas")
        print("g. Salir")
        print()
        opcion = input("Ingresar la opción que desea realizar: ")
        if opcion == "a":
            registrar_estudiantes(estudiantes)
        elif opcion == "b":
            mostrar_listado(estudiantes)
        elif opcion == "c":
            buscar_estudiante(estudiantes)
        elif opcion == "d":
            modificar_datos(estudiantes)
        elif opcion == "e":
            eliminar_estudiante(estudiantes)
        elif opcion == "f":
            mostrar_promedio(estudiantes)
        elif opcion == "g":
            print("Gracias por usar nuestro sistema!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def registrar_estudiantes(estudiantes):
    while True:
        dni = input("Ingrese el DNI del estudiante (0 para finalizar): ")
        if dni == "0":
            print()
            break
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = float(input("Ingrese la nota del estudiante (0-10): "))
        while nota < 0 or nota > 10:
            nota = float(input("Ingrese una nota válida (0-10): "))
        estudiantes.append({"dni": dni, "nombre": nombre, "nota": nota})

def mostrar_listado(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("Listado de estudiantes:")
    for estudiante in estudiantes:
        print("DNI:", estudiante["dni"])
        print("Nombre:", estudiante["nombre"])
        print("Nota:", estudiante["nota"])
        print()

def buscar_estudiante(estudiantes):
    dni_b = input("Ingrese el DNI del estudiante que desea buscar: ")
    for estudiante in estudiantes:
        if estudiante["dni"] == dni_b:
            print("Nombre:", estudiante["nombre"])
            print("Nota:", estudiante["nota"])
            return
    print("No existe este DNI en nuestro sistema.")

def modificar_datos(estudiantes):
    dni_b = input("Ingrese el DNI del estudiante que desea modificar: ")
    for estudiante in estudiantes:
        if estudiante["dni"] == dni_b:
            print("Nombre actual:", estudiante["nombre"])
            nueva_nota = float(input("Ingrese la nueva nota del estudiante: "))
            while nueva_nota < 0 or nueva_nota > 10:
                nueva_nota = float(input("Ingrese una nota válida (0-10): "))
            estudiante["nota"] = nueva_nota
            print()
            print("Estudiante modificado correctamente.")
            return
    print("No existe este DNI en nuestro sistema.")

def eliminar_estudiante(estudiantes):
    dni_b = input("Ingrese el DNI del estudiante que desea eliminar: ")
    for estudiante in estudiantes:
        if estudiante["dni"] == dni_b:
            estudiantes.remove(estudiante)
            print("Estudiante eliminado correctamente.")
            return
    print("No existe este DNI en nuestro sistema.")

def mostrar_promedio(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    total_notas = sum(estudiante["nota"] for estudiante in estudiantes)
    promedio = total_notas / len(estudiantes)
    print("Promedio de notas:", promedio)

# Ejecutar el menú principal
menu()

#EJERCICIO 1
"""Considerando las listas del cuadro de la izquierda y en forma manual sin usar la computadora, indique cuál es
el resultado y el tipo de las siguientes expresiones. A continuación, verifique sus respuestas en la
computadora."""

a = [5, 1, 4, 9, 0]
b = list(range(3, 10)) + list(range(20, 23)) #[3, 4, 5, 6, 7, 8, 9, 20, 21, 22]
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]

print(a[2]) #4
print(b[9]) #-> 22 | Crea dos listas y las suma, imprime el elemento 9 de la lista
print(c[1][2]) #5
print(e[0] == e[1]) #-> False | Devuelve valor booleano, porque es falso que e[0] sea igual a e[1]
print(len(c)) #3 | Devuelve la longitud de toda la lista
print(len(c[0])) #2 | Devuelve la longitud de la primera sublista "[1, 2]"
print(len(e)) #3
print(c[-1]) #[6,7]
print(c[-1][+1]) #-> 7 #el "+" es redundante, también se podria acceder a 7 asi: print(c[-1][-1])
print(c[2:] + d[2:]) #->[[6, 7], 'jirafa', 'elefante'] | se suman las dos listas y se crea una nueva lista
print(a[3:10]) #-> [9, 0] | Incluye al 9 y al 0
print(a[3:10:2]) #->[9] | Incluye al 9 pero no al 0 porque salta de 2 en 2
print(d.index('jirafa')) #-> 2 | Index busca la primera aparición del argumento q se le da e imprime su indice
print(e[c[0][1]].count(5)) # -> 2 | indexación, es la acción de buscar un elemento x su indice

#EJERCICIO 2
"""Escriba la función mayores_que(x, lista_valores) que cuente cuántos valores en la lista "valores" son mayores que
x, por ejemplo mayores_que(5, [7, 3, 6, 0, 4, 5, 10]) devuelve el valor 3"""

def mayores_que(x, lista_valores):
    contador = 0
    for i in lista_valores:
        if i > x:
            contador += 1
    return contador
#ORIGINAL
lista = [7, 3, 6, 0, 4, 5, 10]
x = 5
print(mayores_que(x, lista))

#OTRA FORMA CON WHILE
def mayores_que(x, lista_valores):
    contador = 0
    i = 0
    while i < len(lista_valores):
        if lista_valores[i] > x:
            contador += 1
        i += 1
    return contador

valores = [7, 3, 6, 0, 4, 5, 10]
x = 5
resultado = mayores_que(x, valores)
print(resultado)

#OTRA FORMA
def mayores_que(x, lista_valores):
    contador = sum(1 for valor in lista_valores if valor > x)
    return contador

valores = [7, 3, 6, 0, 4, 5, 10]
x = 5
resultado = mayores_que(x, valores)
print(resultado)

#EJERCICIO 3
"""Diseñar un algoritmo en python que permita realizar lo siguiente:
● Cargar una lista con N números enteros
● Mostrar los números ingresados y su posición
● Mostrar si los elementos de la lista se encuentran ordenados en forma descendente
● Mostrar los valores que superen el promedio de los valores ingresados
● Mostrar el mínimo de los valores ingresados y su posición
● Indicar qué elementos son valores primos
● El algoritmo debe considerar que si no se cargó la lista previamente, no se pueda realizar alguna de las
acciones solicitadas."""

def menu():
    lista = []  # Inicializar la lista vacía

    while True:
        print()
        print("\t**BIENVENIDO AL MENU**")
        print("a. Cargar una lista con números enteros")
        print("b. Mostrar los números ingresados y su posición")
        print("c. Mostrar si se encuentran en forma descendente")
        print("d. Mostrar los valores que superan el promedio de los valores ingresados")
        print("e. Mostrar el mínimo de los valores ingresados y su posición")
        print("f. Mostrar qué elementos son valores primos")
        print("q. Salir del programa")
        opcion = input("Ingrese la tarea a realizar: ")
        print()

        if opcion == "a":
            cargar_lista(lista)
        elif opcion == "b":
            mostrar_lista(lista)
        elif opcion == "c":
            forma_descendente(lista)
        elif opcion == "d":
            promedio(lista)
        elif opcion == "e":
            minimo_valor(lista)
        elif opcion == "f":
            verificar_primos(lista)
        elif opcion == "q":
            print("¡Hasta luego!")
            break  # Salir del bucle y finalizar el programa
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def cargar_lista(lista):
    try:
        n = int(input("¿Cuántos valores quiere cargar?: "))
        for i in range(n):
            try:
                cargar = int(input("Ingrese el número que quiere cargar: "))
                lista.append(cargar)
            except ValueError:
                print("Error: Ingrese un número entero válido.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        
# def cargar_lista():
#     lista = []
#     while True:
#         n = int(input("Ingrese el número que quiere cargar a la lista (0 para salir): "))
#         if n != 0:
#             lista.append(n)
#         else:
#             break
#     return lista

def mostrar_lista(lista):
    for indice, valor in enumerate(lista):
        print(f"Número: {valor}, Posición: {indice}")
        
# def mostrar_lista(lista):
#     contador = 0
#     for i in lista:
#         print(f"Numero: {i} posicion: {contador}")
#         contador += 1

def forma_descendente(lista):
    if sorted(lista, reverse=True) == lista:
        print("Su lista esta ordenada de forma descendente!")
    else:
        print("No esta ordenada de forma descendente")

def promedio(lista):
    promedio = sum(lista) / len(lista)
    superan_promedio = [numero for numero in lista if numero > promedio]
    print(f"Valores superiores al promedio ({promedio}): {superan_promedio}")
    #ESTOY USANDO COMPRESION DE LISTA:
    #nueva_lista = [expresion for elemento in secuencia if condicion]
    
def minimo_valor(lista):
    minimo = min(lista)
    posicion = lista.index(minimo)
    print(f"Mínimo: {minimo}, Posición: {posicion}")    

def verificar_primos(lista):
    primos = []
    for numero in lista:
        if numero > 1:
            for i in range(2, int(numero/2)+1):
                if (numero % i) == 0:
                    break
            else:
                primos.append(numero)
    print("Elementos que son valores primos:", primos)
    
#ORIGINAL
menu()

#EJERCICIO 4
"""Diseñar un algoritmo que permita realizar lo siguiente:
● Cargar una lista con valores de tipo caracter a pedido del operador.
● Mostrar la lista desde el último valor ingresado hasta el primero.
● Solicitar un valor al usuario y buscar en la lista devolviendo la posición del primer valor encontrado. En
caso que no se encuentre devolver -1
● Indicar la cantidad de vocales de la lista."""


def menu():
    lista = []
    while  True:
        print()
        print("\t **MENU DE OPCIONES**")
        print("a. Cargar caracteres")
        print("b. Mostrar la lista desde el ultimo valor hasta el primero")
        print("c. Buscar un valor para saber su posicion (el primer valor que aparezca en la lista)")
        print("d. Indicar la cantidad de vocales en la lista")
        print("e. Salir")
        opcion = input("Ingrese la opción que quiere ejecutar: ")
        print()
        if opcion == "a":
            cargar(lista)
        elif opcion == "b":
            mostrar_lista(lista)
        elif opcion == "c":
            buscar_valor(lista)
        elif opcion == "d":
            vocales(lista)
        elif opcion == "e":
            print("Gracias por usar nuestro programa!")
            break
            
def cargar(lista):
    try:
        cantidad = int(input("¿Cuantos caracteres quiere cargar?: "))
        print()
        for i in range(cantidad):
            caracter = input("Ingrese los caracteres que quiere cargar a la lista: ")
            lista.append(caracter)
    except ValueError:
        print("Por favor, ingresar una cantidad entera.")

def mostrar_lista(lista):
    lista_invertida = list(reversed(lista))
    print(lista_invertida)
    
# def mostrar_lista_inversa(lista):
#     inversa = lista[::-1]
#     print("La lista en orden inverso:")
#     for valor in inversa:
#         print(valor)

def buscar_valor(lista):
    valor = input("Ingrese el valor que desea buscar: ")
    try:
        elemento = lista.index(valor)
        if lista[elemento] == valor:
            print(f"{valor} se encuentra en la posicion {elemento}")
    except ValueError:
        print(f"-1")
        
def vocales(lista):
    contador = 0
    for i in lista:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            contador += 1
    print(f"En la lista hay {contador} vocales")
    
# def contar_vocales(lista):
#     contador = 0
#     for valor in lista:
#         if valor.lower() in 'aeiou':
#             contador += 1
#     return contador

#ORIGINAL
menu()

#EJERCICIO 5
"""Diseñar un algoritmo que permita realizar lo siguiente:

● Cargar una lista con valores numéricos hasta que el usuario ingrese cero. No debe permitir que se
carguen valores duplicados en la lista.
● Mostrar la lista completa con la cantidad de elementos
● Agregar un elemento al final de la lista
● Insertar un elemento preguntando la posición al usuario. Valide que el valor no se encuentre cargado.
● Eliminar un elemento indicado por el usuario. Si no se encuentra debe informar con un mensaje.
● Copiar los valores pares a otra lista de nombre listaPares. Mostrar ambas listas."""

def menu():
    lista = []
    while True:
        print()
        print("\t **MENU**")
        print("a. Cargar numeros enteros a la lista")
        print("b. Mostrar la lista completa con la cantidad de elementos")
        print("c. Agregar elemento al final de la lista")
        print("d. Insertar elemento en una posicion especifica")
        print("e. Eliminar un elemento indicado por el usuario")
        print("f. Crear una lista nueva con los valores pares de la original")
        print("g. Salir del menú")
        opcion = input("Ingrese la opcion que quiere ejecutar: ")
        
        if opcion == "a":
            cargar_lista(lista)
        elif opcion == "b":
            mostrar_lista(lista)
        elif opcion == "c":
            agregar(lista)
        elif opcion == "d":
            insertar(lista)
        elif opcion == "e":
            eliminar_elemento(lista)
        elif opcion == "f":
            lista_pares(lista)
        elif opcion == "g":
            print("Gracias por usar nuestro programa!")
            break
    
def cargar_lista(lista):
    cargar = 1
    while True:
        try:
            cargar = int(input("Ingrese el valor númerico que quiere cargar (0 para salir): "))
        except ValueError:
            print("Por favor, ingrese un numero entero.")
        if cargar == 0:
            break
        if cargar in lista:
            print("Este valor ya se encuentra en la lista!")
        else:
            lista.append(cargar)
    
def mostrar_lista(lista):
    print()
    print("Elementos de la lista: ")
    for valor in lista:
        print(valor, end=" ")
    print("\nCantidad de elementos:", len(lista))

def agregar(lista):
    try:
        add = int(input("Ingrese el elemento que desea agregar a la lista: "))
        lista.append(add)
        print("Elemento agregado con exito!")
    except ValueError:
        print("Por favor, ingresar un valor entero")
        
        
def insertar(lista):
    while True:
        posicion = int(input("Ingrese la posición del elemento: "))

        if posicion < 0 or posicion > len(lista): #len es 3, porque "len" retorna la cantidad de elem, no el indice
            print("Posición inválida. Intente nuevamente.") #suponiendo que agregamos 3 elementos
        else:
            add = int(input("Ingrese el elemento que desea insertar en la lista: "))
            if add in lista:
                print("Este elemento ya se encuentra en la lista. Por favor, ingrese otro elemento.")
            else:
                lista.insert(posicion, add)
                print("Elemento agregado con éxito!")
                break
        
def eliminar_elemento(lista):
    eliminar = int(input("Ingrese el elemento que quiere eliminar: "))
    if eliminar in lista:
        lista.remove(eliminar)
        print("Elemento eliminado con exito!")
    else:
        print("Este elemento no se encuentra en la lista")

def lista_pares(lista):
    lista_pares = []
    for valor in lista:
        if valor % 2 == 0:
            lista_pares.append(valor)
    print(f"Listas entera {lista}")
    print(f"Listas con numeros pares {lista_pares}")
    #lista_pares = [valor for valor in lista if valor % 2 == 0]
    #Forma simplificada, compresión de lista!. No usa append
    
#ORIGINAL
menu()

#EJERCICIO 6
"""Escribir el código en python que permita:

● Cargar una lista con N valores aleatorios (random.randint(a,b)), los valores aleatorios deben
encontrarse entre 0 y 100. El valor N es el tamaño de la lista ingresado por el usuario.
● Mostrar el sector de la lista deseada, ingresar el inicio el fin y el paso.
● Copiar la lista a una denominada listaInversa en donde el orden de los elementos se encuentra en
orden inverso a la lista original. Muestre ambas listas.
● Eliminar de listaInversa los valores duplicados. Mostrar ambas listas
● Salir"""
def cargar(N):
    lista = []
    for i in range(N):
        random_list = random.randint(0, 100)
        lista.append(random_list)
    return lista

def sector(lista, start, end, step):
    new_list = lista[start:end:step]
    print(f"Section of the list: {new_list}")
    print()
    
def reverse_list(lista): #lista inversa | ruivers lest
    listaInversa = lista.copy()
    listaInversa.reverse()
    return listaInversa

def delete_duplicate(listaInversa): #Delit tupleket.s
    no_duplicate = list(set(listaInversa))
    return no_duplicate
    
#ORIGINAL
import random
N = int(input("Enter how many values you want to load ")) #load = cargar
lista = cargar(N)
print(f"Original list: {lista}")

start = int(input("Enter the start to define a sector: ")) #Introduzca el inicio para definir un sector
end = int(input("Enter the end of the sector: ")) #Ingresar el final del sector
step = int(input("Enter sector step: ")) #Ingresar paso del sector
sector(lista, start, end, step)

listaInversa = reverse_list(lista)
print(f"The original list is: {lista}")
print(f"The reverse list is: {listaInversa}")

no_duplicate = delete_duplicate(listaInversa)
print()
print(f"Reverse list: {listaInversa}")
print(f"List without duplicates: {no_duplicate}") #Lista sin duplicados | without(wedaut): sin

#EJERCICIO 8
"""Escriba un algoritmo para simular un campeonato de tenis.

Primero, debe pedir al usuario que ingrese los
nombres de ocho tenistas.
A continuación, debe pedir los resultados de
los partidos juntando los jugadores de dos en
dos. El ganador de cada partido avanza a la
ronda siguiente. El algoritmo debe continuar
preguntando por los ganadores de partidos
hasta que quede un único jugador, que es el
campeón del torneo. ¿Puede hacerlo de
manera aleatoria?

Ronda 1
a.Nadal - b.Melzer: a
a.Murray - b.Soderling: b
a.Djokovic - b.Berdych: a
a.Federer - b.Ferrer: a
Ronda 2
a.Nadal - b.Soderling: a
a.Djokovic - b.Federer: a
Ronda 3
a.Nadal - b.Djokovic: b
Campeón: Djokovic"""

import random

#Función para simular un partido entre dos tenistas y determinar el ganador
def simular_partido(jugador1, jugador2):
    ganador = random.choice([jugador1, jugador2])
    return ganador

#Pedir nombres de los tenistas
tenistas = []
for i in range(8):
    nombre = input(f"Ingrese el nombre del tenista {i+1}: ")
    tenistas.append(nombre)
    
#Rondas del campeonato
ronda = 1
while len(tenistas) > 1:
    print(f"Ronda {ronda}")
    ganadores = []
    for i in range(0, len(tenistas), 2):
        jugador1 = tenistas[i]
        jugador2 = tenistas[i+1]
        resultado = simular_partido(jugador1, jugador2)
        ganadores.append(resultado)
        print(f"{jugador1} - {jugador2}: {resultado}")
    tenistas = ganadores
    ronda += 1

#Campeón del torneo
campeon = tenistas[0]
print(f"Campeón: {campeon}")    