#Casos de Estudio
"""Analice, diseñe y codifique los siguientes enunciados en Python

1. Diseñar un programa que, mediante un menú de opciones nos permite realizar:
1. Generar N ternas de valores en forma aleatoria y agregarlas a una lista. Validar que los valores dentro
de cada terna no se repitan.
2. Mostrar la lista de valores generados
3. Calcular la suma de todos los valores generados
4. Calcular la suma de los valores de una terna a elección del usuario
5. Calcular el promedio de una columna (primera, segunda o tercera) de las ternas a elección del usuario
6. Salir""" 

def menu():
    terna = []
    while True:
        print()
        print("\t **MENU**")
        print("1. Generar N ternas de valores en forma aleatoria ")
        print("2. Mostrar la lista de valores generados")
        print("3. Calcular la suma de todos los valores generados")
        print("4. Calcular la suma de los valores de una terna")    
        print("5. Calcular el promedio de una columna (primera, segunda o tercera)")
        print("6. Salir")
        opcion = input("Ingrese la opcion a ejecutar: ")
        if opcion == "1":
            generar_ternas(terna)
        elif opcion == "2":
            mostrar_ternas(terna)
        elif opcion == "3":
            suma_general(terna)
        elif opcion == "4":
            una_terna(terna)
        elif opcion == "5":
            promedio_columna(terna)
        elif opcion == "6":
            print()
            print("Gracias por usar nuestro programa! Adios!")
            break
        
def generar_ternas(terna):
    cantidad = int(input("¿Cuantas ternas quiere generar?: "))
    if cantidad > 0:
        for _ in range(cantidad):
            lista = []
            while len(lista) < 3:
                valor = random.randint(1, 100)
                if valor not in terna:
                    lista.append(valor)
            terna.append(lista)
        print()
        print("Ternas generadas con exito!")

def mostrar_ternas(terna):
    for valor in terna:
        print(valor)
        
def suma_general(terna):
    suma = 0
    for valor in terna:
        suma += sum(valor)
    print()
    print(f"La suma general es: {suma}")
    
def una_terna(terna):
    indice = int(input("Indique el indice de la terna que quiere calcular: "))
    if indice >= 0 and indice < len(terna):
        suma = sum(terna[indice])
        print()
        print(f"La suma es: {suma}")
    else:
        print()
        print("El indice esta fuera del rango")
        
def promedio_columna(terna):
    columna = int(input("Ingrese la columna que desea sumar (0 - 2): "))
    suma_total = 0
    for valor  in terna:
        suma_total += valor[columna]
    print()
    print(f"La suma total de esa columna es de: {suma_total}")
    
#ORIGINAL
import random
menu()

#EJERCICIO 1
"""Realizar un programa modular en python que permita cargar en forma aleatoria una matriz cuadrada (número de filas
igual a número de columnas ingresado por el usuario) con valores enteros entre 100 a 200 incluidos. Mostrar el
valor máximo de cada columna, el valor mínimo de cada fila, el promedio de los valores que componen la
diagonal principal, finalmente, pase a una lista los valores que se repiten y muestre las mismas."""
#SI QUEREMOS RECORRER UNA COLUMNA EL PRIMER INDICE ES EL CAMBIANTE, SI QUEREMOS RECORRER UNA FILA EL SEGUNDO INDICE ES EL CAMBIANTE

def generar_matriz(n):
    matriz = []
    for _ in range(n):
        lista = []
        for _ in range(n):
            valor = random.randint(100, 200)
            lista.append(valor)
        matriz.append(lista)
    return matriz

def max_columna(matriz):
    maximos = []
    for i in range(len(matriz)): #Cantidad de sublistas dentro de la matriz. "Indice de la fila"
        maximo = float("-inf") #Preguntar
        for j in range(len(matriz[0])): #Se refiere a la longitud del primer elemento, q es igual al numero de columnas. "Indice de la columna"
            if matriz[j][i] > maximo:
                maximo = matriz[j][i] 
        maximos.append(maximo)
    return maximos

def minimo_fila(matriz):
    minimos = []
    for i in range(len(matriz)):
        minimo = float("inf")
        for j in range(len(matriz[0])):
            if matriz[i][j] < minimo:
                minimo = matriz[i][j]
        minimos.append(minimo)
    return minimos

def promedio_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    promedio = suma / len(matriz)
    #print(f"El promedio es {suma / len(matriz)}")
    return promedio

    # suma = 0
    # for i in range(len(matriz)):
    #     for j in range(len(matriz[0])):
    #         if i == j:
    #             suma += matriz[i][j]
    # return suma / len(matriz)

def valores_repetidos(matriz):
    repetidos = []
    valores = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            valor = matriz[i][j]
            if valor in valores and valor not in repetidos:
                repetidos.append(valor)
            else:
                valores.append(valor)
    return repetidos
            
def mostrar(mostrar):
    for elemento in mostrar:
        print(elemento, end=" ")
    print()
    
#ORIGINAL
import random
n = int(input("Ingrese numero de filas y columnas de la matriz cuadrada: "))
matriz = generar_matriz(n)
print("Matriz generada:")
for fila in matriz:
    mostrar(fila)

print()
print("Los valores maximos de cada columna:")
maximos = max_columna(matriz)
mostrar(maximos)

print()
print("Valores minimos de cada fila:")
minimos = minimo_fila(matriz)
mostrar(minimos)

print()
promedio = promedio_diagonal(matriz)
print(f"El promedio de la diagonal principal es de: {promedio}")

print()
repetidos = valores_repetidos(matriz)
print(f"Los valores que se repiten en la matriz:")
mostrar(repetidos)

#EJERCICIO 2
"""Realizar la traza del siguiente algoritmo y graficar el recorrido resultante de la matriz cuadrada de tamaño NxN."""

#EJERCICIO 3
"""Cargar una matriz de NxN aleatoriamente y mostrar los valores de la diagonal principal."""
def matrizNxN(n):
    matriz = []
    for i in range(n):
        lista = []
        for j in range(n):
            valor = random.randint(0,200)
            lista.append(valor)
        matriz.append(lista)
    return matriz

def diagonal_p(matriz):
    diagonal = []
    for i in range(len(matriz)):
        valor = matriz[i][i]
        diagonal.append(valor)
    return diagonal

def mostrar(matriz):
    for elemento in matriz:
        print("{:6}".format(elemento), end=" ") #{:8.2f} "8" representa los espacios; "2"representa decimales y "f" que sea flotante
    print()

#ORIGINAL
import random
n = int(input("Ingresar el valor de la matriz NxN: "))
matriz = matrizNxN(n)
print("Matriz Generada:")
for valor in matriz:
    mostrar(valor)

print()
diagonal = diagonal_p(matriz)
print("Valores de la diagonal principal:")
mostrar(diagonal)

#EJERCICIO 4
"""Realizar los recorridos de las siguientes matrices de NxN, donde N es par, tal como se indica en las siguientes figuras"""

def matriz_cuadrada(N, matriz):
    for i in range(N):
        lista = []
        for j in range(N):
            valor = random.randint(0,200)
            lista.append(valor)
        matriz.append(lista)

def mostrar(matriz):
    for i in range(len(matriz)):
        for j in range((len(matriz))):#tiene un parentesis mas, preguntar
            valor = matriz[i][j]
            print("{:6}".format(valor), end=" ")
        print()

#MODO A
# def recorriendo(matriz):
#     j = 0
#     while j < len(matriz):
#         for i in range(len(matriz)):
#             valor = matriz[i][j]
#             print(valor)
#         j += 1
#         print()


#MODO B
# def recorriendo(matriz):
#     for i in range(len(matriz)):
#         #lista = []
#         for j in range(len(matriz)):
#             valor = matriz[j][i]
#             print(valor, end=" ")
#         print()

#MODO D | ESTUDIAR
# def recorriendo(matriz):  
#     for j in range(len(matriz)):
#         if j % 2 == 0:  # Si la columna es par, se recorre de arriba hacia abajo
#             for i in range(len(matriz)):
#                 valor = matriz[i][j]
#                 print(valor)
#         else:  # Si la columna es impar, se recorre de abajo hacia arriba
#             for i in range(len(matriz) - 1, -1, -1):
#                 valor = matriz[i][j]
#                 print(valor)

#MODO C
def recorriendo(matriz):  
    j = 0
    while j < len(matriz):
        valor = len(matriz)
        revertido = valor.reverse()
        
        for i in range(revertido):
            print(matriz[j][i])

#ORIGINAL      
import random
N = int(input("Ingrese la longitud de la matriz cuadrada: "))
matriz = []
matriz_cuadrada(N, matriz)
mostrar(matriz)
recorriendo(matriz)

#EJERCICIO 5
"""Realizar un módulo suma_fc_mat(tabla, c, k) que devuelve un número que es la suma de una fila o columna y
es del mismo tipo de dato de la matriz, los parámetros son una lista de listas denominada tabla, un parámetro
de tipo string denominado c que si tiene el valor ‘f’ se sumará una fila y si tiene el valor ‘c’ se sumará una
columna, finalmente hay un parámetro entero denominado k que indica qué fila o columna se desea sumar."""

def suma_fc_mat(tabla, c, k):
    suma = 0 
    if c == "f":
        suma = sum(tabla[k])
    elif c == "c":
        for i in range(len(tabla)):
            suma += tabla[i][k]
    return suma 

# Código corregido
tabla = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = input("Ingrese 'c' o 'f': ")
k = int(input("Indique la fila o columna que desea sumar: "))
suma = suma_fc_mat(tabla, c, k)
print("La suma es:", suma)

#EJERCICIO 6
"""Un club de pescadores realizó una competencia de pesca. Por cada participante se registrará la cantidad total
de peces atrapados. Para ello, se tiene dos listas que almacenan el nombre del participante y las cantidades de
peces por participante. Diseñar un algoritmo modular, que mediante un menú de opciones resuelve:
1. Dar la bienvenida al concurso de pesca
2. Cargar las listas con una cantidad n de participantes. La mínima cantidad de participantes es 10 y la
máxima es 50. La cantidad de peces debe ser mayor o igual a 0.
3. Mostrar el promedio de peces capturados.
4. Mostrar la mayor cantidad de peces capturados y el nombre del ganador (pueden haber empates).
5. Disminuir x peces al participante que está en la posición z.
6. Despedirse y salir"""

#ORIGINAL
def menu():
    participantes = []
    peces_atrapados = []
    while True:
        print()
        print("\t**MENÚ DE OPCIONES**")
        print("1. Información sobre el concurso de pesca.")
        print("2. Cagar participantes (10 - 50)")
        print("3. Mostrar el promedio de peces capturados.")
        print("4. Mostrar la mayor cantidad de peces capturados y el nombre del ganador.")
        print("5. Disminuir x peces al participante que está en la posición z.")
        print("6. Despedirse y salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            informacion()
        elif opcion == "2":
            cargar_participantes(participantes, peces_atrapados)
        elif opcion == "3":
            mostrar_promedio(peces_atrapados)
        elif opcion == "4":
            mostrar_ganador(participantes, peces_atrapados)
        elif opcion == "5":
            disminuir_peces(participantes, peces_atrapados)
        elif opcion == "6":
            print()
            print("Gracias por usar nuestro programa!")
            break
def informacion():
    print()
    print("Hola, bienvenido al concurso de pesca!")
    
def cargar_participantes(participantes, peces_atrapados):
    
    cantidad = int(input("¿Cuantos participantes quiere cargar?: "))

    while cantidad < 10 or cantidad > 50:
        print("Cantidad fuera del rango, por favor, ingrese nuevamente")
        cantidad = int(input("¿Cuantos participantes quiere cargar?: "))
        
    for _ in range(cantidad):
        nombre = input("Ingrese su nombre completo: ")
        peces = int(input("¿Cuantos peces atrapo?: "))
        if peces >= 0:
            participantes.append(nombre)
            peces_atrapados.append(peces)
        else:
            print("Cantidad invalida de peces. Debe ser >= 0")
    
def mostrar_promedio(peces_atrapados):
    if len(peces_atrapados) >= 0:
        valor = sum(peces_atrapados)
        print(f"El promedio de peces atrapados es de: {valor//len(peces_atrapados)}")
    else:
        print("NO hay registro de peces atrapados")

def mostrar_ganador(participantes, peces_atrapados):
    mayor_peces_cap = float("-inf")
    for i in peces_atrapados:
        
        if i > mayor_peces_cap:
            mayor_peces_cap = i
            indice = peces_atrapados.index(i) #"Index" retorna el indice
            ganador = participantes[indice]
    print(f"La mayor cantidad de peces atrapados es {mayor_peces_cap} y el ganador es {ganador}!")

# def mostrar_ganador(participantes, peces_atrapados):
#     if len(peces_atrapados) > 0:
#         max_peces_cap = max(peces_atrapados) -> max
#         indice = peces_atrapados.index(max_peces_cap)
#         ganador = participantes[indice]
#         print(f"La mayor cantidad de peces atrapados es {max_peces_cap} y el ganador es {ganador}!")
#     else:
#         print("No hay registro de peces atrapados.")
        
def disminuir_peces(participantes, peces_atrapados):
    nombre = input("Ingrese el nombre del participante: ")
    disminuir = int(input("¿Cuantos peces quiere disminuir?: "))
    if nombre in participantes:
        clave = participantes.index(nombre)
    else:
        print("El nombre no existe en la base de datos")
    if disminuir >= 0:
        peces_atrapados[clave] -= disminuir
        print(f"Se disminuyeron {disminuir} peces a {nombre}")
    else:
        print("No se puede dismunir un numero negativo")
        
# def disminuir_peces(participantes, peces_atrapados):
#     if len(participantes) == 0:
#         print("No hay participantes cargados.")
#         return
    
#     posicion = int(input("Ingrese la posición del participante a modificar: "))
#     if posicion < 0 or posicion >= len(participantes):
#         print("Posición inválida.")
#         return
    
#     cantidad = int(input("Ingrese la cantidad de peces a disminuir: "))
#     if cantidad < 0:
#         print("Cantidad inválida. Debe ser >= 0")
#         return
    
#     peces_atrapados[posicion] -= cantidad
#     if peces_atrapados[posicion] < 0:
#         peces_atrapados[posicion] = 0
#     print(f"Se han disminuido {cantidad} peces al participante en la posición {posicion}.")
    
#ORIGINAL
menu()

#EJERCICIO 7
"""Diseñar un programa modular que permita gestionar los productos de un comercio, las funcionalidades
solicitadas son:
1. Registrar productos: para cada uno se debe solicitar, código, descripción, precio y stock. Agregar las
siguientes validaciones:
a. El código no se puede repetir
b. Todos los valores son obligatorios
c. El precio y el stock no pueden ser negativos
2. Mostrar el listado de productos
3. Mostrar los productos cuyo stock sea menor a un valor dado
4. Incrementar el stock de un producto
5. Mostrar el producto de menor precio
6. Buscar el precio más alto de la lista de productos y a continuación listar los productos que lo poseen.
7. Salir"""
def menu():
    productos = {}
    while True:
        print("\t === MENU DE OPCIONES ==")
        print("1. Registrar producto")
        print("2. Mostrar el listado de productos")
        print("3. Mostrar los productos con bajo stock")
        print("4. Incrementar el stock de un producto")
        print("5. Mostrar el producto de menor precio")
        print("6. Buscar el precio más alto de la lista de productos")
        print("7. Salir")
        opcion = input("Ingrese una opción [1,7]: ")
        print()
        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            mostrar_listado(productos)
        elif opcion == "3":
            mostrar_stock_menor(productos)
        elif opcion == "4":
            incrementar_stock(productos)
        elif opcion == "5":
            mostrar_menor_precio(productos)
        elif opcion == "6":
            mostrar_mayor_precio(productos)
        elif opcion == "7":
            print("Gracias por usar nuestro programa!")
            break
        
def registrar_producto(productos):
    codigo = input("Ingrese el código del producto: ") #Es mejor dejar el codigo como str
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    
    if codigo in productos:
        print("El código no se puede repetir. ")
        return
    if not codigo or not descripcion or precio < 0 or stock < 0:
        print("Error: Todos los valores son obligatorios, por favor, verifique.")
        return
    
    productos[codigo]  = {'descripcion': descripcion, 'precio': precio, 'stock': stock}
    print("Producto cargado con exito!")
    print()
    
    
def mostrar_listado(productos):
    if not productos:
        print("No hay productos en la base de datos")
        return
    
    for clave, valor in productos.items():
        print("Listado de productos:")
        print(f"Codigo: {clave}")
        print(f"Descripción: {valor['descripcion']}")
        print(f"Precio: {valor['precio']}")
        print(f"Stock: {valor['stock']}")
        print("\t=====================")
        
def mostrar_stock_menor(productos):
    limite_stock = int(input("Ingrese el limite de stock: "))
    
    print("Productos con stock menor a", limite_stock)
    for clave, valor in productos.items():
        if valor['stock'] < limite_stock:
            print(f"Codigo: {clave}")
            print(f"Descripción: {valor['descripcion']}")
            print(f"Precio: {valor['precio']}")
            print(f"Stock: {valor['stock']}")
            print("\t-----------------")
            
def incrementar_stock(productos):
    buscar = input("Ingrese el codigo del producto que desea incrementar: ")
    if buscar not in productos:
        print("El codigo no existe")
        
    cantidad = int(input("Ingrese la cantidad a incrementrar: "))
    if cantidad >= 0:
        productos[buscar]['stock'] += cantidad
        print("Stock añadido con exito!")
        print()
    else:
        print("Error: La cantidad no puede ser negativa")
    
def mostrar_menor_precio(productos):
    menor = float("inf")
    for clave, valor in productos.items():
        if valor['precio'] < menor:
            menor = valor
            codigo = clave
    print("Producto de menor precio:")
    print(f"Codigo: {codigo}")
    print(f"Descripción: {menor['descripcion']}")
    print(f"Precio: {menor['precio']}")
    print(f"Stock: {menor['stock']}")

# def mostrar_producto_menor_precio(productos):
#     if not productos:
#         print("No hay productos registrados.")
#         return

    producto_menor_precio = min(productos.values(), key=lambda p: p["precio"])
#     print("Producto con menor precio:")
#     print("Código:", producto_menor_precio)
#     print("Descripción:", producto_menor_precio["descripcion"])
#     print("Precio:", producto_menor_precio["precio"])
#     print("Stock:", producto_menor_precio["stock"])
    
def mostrar_mayor_precio(productos):
    menor = float("-inf")
    for clave, valor in productos.items():
        if valor['precio'] > menor:
            mayor = valor
            codigo = clave
    print("Producto de mayor precio:")
    print(f"Codigo: {codigo}")
    print(f"Descripción: {mayor['descripcion']}")
    print(f"Precio: {mayor['precio']}")
    print(f"Stock: {mayor['stock']}")

# def buscar_precio_mas_alto(productos):
#     if not productos:
#         print("No hay productos registrados.")
#         return

#     precio_maximo = max(p["precio"] for p in productos.values())

#     print("Productos con el precio más alto:")
#     for codigo, producto in productos.items():
#         if producto["precio"] == precio_maximo:
#             print("Código:", codigo)
#             print("Descripción:", producto["descripcion"])
#             print("Precio:", producto["precio"])
#             print("Stock:", producto["stock"])
#             print("------------------------")

#ORIGINAL
if __name__ == "__main__": #Sirve para asegurarse de que el código dentro de este bloque se ejecute solo cuando el archivo se ejecuta
        menu()             #directamente y no cuando se importa como un módulo en otro archivo. Si estamos en otro script se lo importa y llama
        
#EJERCICIO 8
"""
Realizar un programa que permita mediante un menú de opciones, las siguientes operaciones:

a. Cargar 3 listas paralelas: nombre, legajo y nota que son los registros de los estudiantes hasta que el
operador no quiera ingresar más datos, validar que las notas estén en el intervalo [0, 100]. El legajo no
puede estar repetido. Utilice sub algoritmos para la validación.
b. Mostrar los registros en el orden en que fueron ingresados u ordenados por nombre a opción del
operador.
c. Mostrar los registros cuyas notas superan al promedio ordenados de mayor a menor.
d. Mostrar la nota máxima y mínima y cuántos estudiantes las obtuvieron.
e. Agregar un nuevo registro.
f. Agregar una nueva nota para todos los estudiantes.
g. Modificar un registro ingresando el legajo del estudiante.
h. Eliminar un estudiante ingresando el legajo.
i. Salir
Consideración: para poder realizar las opciones b, c, d, f, g,h se debe verificar que haya al menos un registro
cargado, en caso contrario mostrar el mensaje "Debe cargar registros antes de realizar esta operación".
También debe limpiar la pantalla cada vez que se termine de procesar una opción."""

#continue #Ignora todo el resto del codigo e itera de nuevo el bucle

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    
    nombre_lista = []
    legajo_lista = []
    nota_lista = []
    
    while True:
        limpiar_pantalla()
        print("\t**Bienvenido al menú**")
        print("a. Cargar listas")
        print("b. Mostrar registros")
        print("c. Mostrar registros que superan el promedio de mayor a menor")
        print("d. Mostrar la nota maxima y minima")
        print("e. Agregar un nuevo registro")
        print("f. Agregar una nueva nota para todos los estudiantes")
        print("g. Modificar un registro usando el legajo de un estudiante")
        print("h. Eliminar un estudiante ingresando el legajo")
        print("i. Salir")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "a":
            cargar_listas(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "b":
            mostrar_registro(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "c":
            superan_elpromedio(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "d":
            mostrar_nota_maxima_minima(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "e":
            agregar_nuevo_registro(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "f":
            agregar_nota_general(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "g":
            modificar_registro(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "h":
            eliminar_estudiante(nombre_lista, legajo_lista, nota_lista)
        elif opcion == "i":
            print
            print("Gracias por usar nuestro programa!")
            break
        
        input("Presione Enter para continuar...")
            
#VALIDACIONES
def legajo_repetido(legajo_lista):
    legajo = input("Ingrese legajo: ")
    while legajo in legajo_lista:
        print("El legajo no puede estar repetido")
        legajo = input("Ingrese legajo: ")
    legajo_lista.append(legajo)

def validar_nota(nota_lista):
    try:
        nota = int(input("Ingrese nota: "))
        while nota < 0 or nota > 100:
            print("La nota debe estar en el intervalo [0, 100]")
            nota = int(input("Ingrese nota: "))
        nota_lista.append(nota)
    except ValueError:
        print("Por favor, ingrese un numero entero.")   

#CARGAR LISTA
def cargar_listas(nombre_lista, legajo_lista, nota_lista):
    while True:
        nombre = input("Ingrese nombre completo: ")
        nombre_lista.append(nombre)
        
        legajo_repetido(legajo_lista)
        
        validar_nota(nota_lista)
        print()
        
        operador = input("¿Desea continuar? si/no: ")
        print()
        if operador.lower() != "si":
            break
        
# Función para mostrar registros
def mostrar_registro(nombre_lista, legajo_lista, nota_lista):
    if len(nombre_lista) == 0:
        print("No hay registros para mostrar.")
    else:
        print("== Estudiantes registrados ==")
        for nombre, legajo, nota in zip(nombre_lista, legajo_lista, nota_lista):
            print(f"Nombre: {nombre}")
            print(f"Legajo: {legajo}")
            print(f"Nota: {nota}")
            print("---")
            
# def mostrar_registro(nombre, legajo, nota):
#     if nombre and legajo and nota:
#         print("== Estudiantes registrados ==\n")
#         for i in range(len(nombre)):
#             print(f"Nombre: {nombre[i]}")
#             print(f"Legajo: {legajo[i]}")
#             print(f"Nota: {nota[i]}")
#             print("\t---")
#     else:
#         print("Error: Registro invalido")
        
#NOTAS QUE SUPERAN EL PROMEDIO
def superan_elpromedio(nombre, legajo, nota):
    if nombre and legajo and nota:
        promedio = sum(nota) / len(nota)    #key=lambda argumento: expresión
        ordenados = sorted(enumerate(nota), key=lambda x: x[1], reverse=True)
        print("== Estudiantes que superan el promedio ==")
        for indice, valor in ordenados:
            if valor > promedio:
                print(f"Nombre: {nombre[indice]}")
                print(f"Legajo: {legajo[indice]}")
                print(f"Nota: {nota[indice]}")
                print("\t---")
    else:
        print("Error: Registro invalido")
        
# def mostrar_registros_superan_promedio(nombre_lista, legajo_lista, nota_lista):
#     if len(nombre_lista) == 0:
#         print("No hay registros para mostrar.")
#     else:
#         promedio = sum(nota_lista) / len(nota_lista)
#         registros_superan_promedio = [
#             (nombre, legajo, nota) for nombre, legajo, nota in zip(nombre_lista, legajo_lista, nota_lista)
#             if nota > promedio
#         ]

#         if len(registros_superan_promedio) == 0:
#             print("No hay estudiantes que superen el promedio.")
#         else:
#             print("== Estudiantes que superan el promedio ==")
#             for nombre, legajo, nota in registros_superan_promedio:
#                 print(f"Nombre: {nombre}")
#                 print(f"Legajo: {legajo}")
#                 print(f"Nota: {nota}")
#                 print("---")

#MOSTRAR LA NOTA MAXIMA Y MINIMA
def mostrar_nota_maxima_minima(nombre_lista, legajo_lista, nota_lista):
    if len(nombre_lista) == 0:
        print("Debe cargar registros antes de realizar esta operación.")
    else:
        maxima_nota = max(nota_lista)
        minima_nota = min(nota_lista)
        cantidad_maxima = nota_lista.count(maxima_nota)
        cantidad_minima = nota_lista.count(minima_nota)
        
        print("== Nota máxima y mínima ==")
        print(f"Nota máxima: {maxima_nota} (Cantidad de estudiantes: {cantidad_maxima})")
        print(f"Nota mínima: {minima_nota} (Cantidad de estudiantes: {cantidad_minima})")

# def nota_maxima_minima(nombre, legajo, nota):
#     if nombre and legajo and nota:
#         maximo = max(nota)
#         minimo = min(nota)
#         indice_max = nota.index(maximo)
#         indice_min = nota.index(minimo)
#         if indice_max >= 0:
#             print("== El estudiante con la mayor nota es ==")
#             print(f"Nombre: {nombre[indice_max]}")
#             print(f"Legajo: {legajo[indice_max]}")
#             print(f"Nota: {nota[indice_max]}")
#             print("\t---")
#         if indice_min >= 0:
#             print("== El estudiante con la menor nota es ==")
#             print(f"Nombre: {nombre[indice_min]}")
#             print(f"Legajo: {legajo[indice_min]}")
#             print(f"Nota: {nota[indice_min]}")

def agregar_nuevo_registro(nombre_lista, legajo_lista, nota_lista):
    nombre = input("Ingrese nombre: ")
    nombre_lista.append(nombre)
    legajo_repetido(legajo_lista)
    validar_nota(nota_lista)
    print("Estudiante agregado con exito!")
    print()
    return
    
def agregar_nota_general(nombre_lista, legajo_lista, nota_lista):
    if nombre_lista and legajo_lista and nota_lista:
        cambiar = int(input("Ingrese la nueva nota general: "))
        if cambiar < 0 or cambiar > 100:
            print("Nota fuera del rango")
        else:
            for indice, valor in enumerate(nota_lista):
                nota_lista[indice] = cambiar
            print("Notas cambiadas con exito!")

# def agregar_nota_general(nota_lista):
#     if len(nota_lista) == 0:
#         print("No hay registros para modificar.")
#     else:
#         nueva_nota = int(input("Ingrese la nueva nota general: "))
#         while nueva_nota < 0 or nueva_nota > 100:
#             print("Respeta el intervalo [0, 100]")
#             nueva_nota = int(input("Ingrese la nueva nota general: "))

#         nota_lista[:] = [nueva_nota] * len(nota_lista)
#         print("Notas cambiadas con éxito!")

def modificar_registro(nombre_lista, legajo_lista, nota_lista):
    legajo = input("Ingrese el legajo del estudiante a modificar: ")
    if legajo in legajo_lista:
        nombre = input("Ingrese nuevo nombre: ")
        legajo = input("Ingrese nuevo legajo: ")
        nota = int(input("Ingrese nueva nota: "))
        indice = legajo_lista.index(legajo)
        nombre_lista[indice] = nombre
        legajo_lista[indice] = legajo
        nota_lista[indice] = nota
        print("Registro modificado correctamente! ")

# def modificar_registro(registros):
#     if not registros:
#         print("Debe cargar registros antes de realizar esta operación.")
#         return

#     legajo = input("Ingrese el legajo del estudiante a modificar: ")

#     for registro in registros:
#         if registro["legajo"] == legajo:
#             nueva_nota = float(input("Ingrese la nueva nota: "))
#             if not validar_nota(nueva_nota):
#                 print("Error: La nota debe estar en el intervalo [0, 100].")
#                 return
#             registro["nota"] = nueva_nota
#             print("Registro modificado con éxito.")
#             return

def eliminar_estudiante(nombre_lista, legajo_lista, nota_lista):
    legajo = input("Ingrese el legajo del estudiante a eliminar: ")
    if legajo in legajo_lista:
        indice = legajo_lista.index(legajo)
        del nombre_lista[indice]
        del legajo_lista[indice]
        del nota_lista[indice]
    else:
        print("No se encontro ningun estudiante!")
    print("Estudiante eliminado con exito!")

# def eliminar_registro(registros, legajos):
#     if not registros:
#         print("Debe cargar registros antes de realizar esta operación.")
#         return

#     legajo = input("Ingrese el legajo del estudiante a eliminar: ")

#     for registro in registros:
#         if registro["legajo"] == legajo:
#             registros.remove(registro)
#             legajos.remove(legajo)
#             print("Registro eliminado con éxito.")
#             return
        
#     print("No se encontró ningún registro con el legajo especificado.")

#ORIGINAL
import os
if __name__ == "__main__":
    main()
    
#EJERCICIO 9
"""Dos medicinas se aplican a pares de ratones de laboratorio por vez, a tantos pares como se requiera hacer las
pruebas. Luego se registra la tolerancia que tienen los ratones a las medicinas, que son valores reales en el
intervalo [0, 1]. Mostrar la medicina que en promedio representa la más alta tolerancia. Mostrar que prueba en
suma da el menor valor"""

#EJERCICIO 10
"""Mediante un menú de opciones, realizar el siguiente algoritmo en forma modular:
Un comercio de tecnología se dedica a la venta de tres líneas de productos: celulares, tabletas y notebooks. El
comercio cuenta con el registro de los importes de las ventas anuales de los períodos (2012, 2013, 2014, 2015,
2016) de estos productos, y desea realizar un análisis que consiste en lo siguiente:
1. Cargar las ventas realizadas de los tres productos para los períodos citados. Para agilizar el caso de
estudio cargue una matriz de 5 filas por 3 columnas con números aleatorios. Los productos y los
períodos deben cargarse en vectores que están relacionados con las filas o columnas según
corresponda.
2. Mostrar los datos generados de forma tal que gráficamente se vea como una matriz de productos y
períodos.

3. Indicar en qué año se produjo la venta máxima y a que producto correspondió.
4. Insertar un nuevo período (fila) a elección del operador.
5. Eliminar el producto (columna) cuya suma sea la menor de todas.
6. Salir emitiendo un mensaje de despedida."""

import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def menu():
    matriz = []
    productos = ["celulares", "tabletas", "netbooks"]
    periodos = [2012, 2013, 2014, 2015, 2016]
    while True:
        limpiar_pantalla()
        print("\tMENÚ")
        print("1. Cargar ventas para todos los periodos")
        print("2. Mostrar los datos en forma de matriz")
        print("3. Indicar en qué año se produjo la venta máxima y a que producto correspondió.")
        print("4. Insertar un nuevo período (fila) a elección.")
        print("5. Eliminar el producto (columna) cuya suma sea la menor de todas.")
        print("6. Salir.")
        opcion = input("¿Qué opcion quiere ejecutar?: ")
        if opcion == "1":
            cargar_periodos(matriz, productos, periodos)
        elif opcion == "2":
            mostrar_matriz(matriz, productos, periodos)
        elif opcion == "3":
            venta_maxima(matriz, productos, periodos)
        elif opcion == "4":
            insertar_fila(matriz, productos, periodos)
        elif opcion == "5":
            eliminar_columna(matriz, productos, periodos)
        elif opcion == "6":
            print()
            print("Gracias por usar nuestro programa!")
            break
        input("Presione enter para continunar...")
            
def cargar_periodos(matriz, productos, periodos):
    
    for i in range(len(periodos)):
        lista = []
        for j in range(len(productos)):
            valor = random.randint(1000, 10000)
            lista.append(valor)
            #lista = [random.randint(1000, 10000) for _ in range(len(productos))] TODA LA FUNCION SE PUEDE HACER EN UNA LINEA XDXD
        matriz.append(lista) 
    print("Matriz cargada exitosamente!")

def mostrar_matriz(matriz, productos, periodos):
    print("\tBASE DE DATOS")
    print("\t", end="\t")
    for periodo in periodos:
        print(periodo, end="\t")
    print()
    print()
    for i, producto in enumerate(productos):
        print(producto, end="\t")
        for j, _ in enumerate(periodos):
            print(matriz[j][i], end="\t")
        print()
    print()

def venta_maxima(matriz, productos, periodos):
    venta_max = 0
    periodo_max = 0
    productos_max = ""
    for i, valor in enumerate(periodos):
        for j, elemento in enumerate(productos):
            recorriendo = matriz[i][j]
            if recorriendo > venta_max:
                venta_max = recorriendo
                periodo_max = valor
                productos_max = elemento
    print(f"La venta maxima se produjo en el año {periodo_max} y corresponde a {productos_max}: ({venta_max})$")

def insertar_fila(matriz, productos, periodos):
    año = int(input("Ingresar periodo: "))
    insertar = []
    for _ in range(len(productos)):
        valor = random.randint(1000, 10000)
        insertar.append(valor)
        #nueva_fila = [random.randint(1000, 10000) for _ in range(len(productos))] SE PUEDE SIMPLIFICAR XD
    periodos.append(año)
    matriz.append(insertar)
    print("Periodo añadido con exito!")
        
def eliminar_columna(matriz, productos, periodos):
    comparador = float("inf")
    for i in matriz:
        suma = sum(i)
        if suma < comparador:
            comparador = suma
            indice = matriz.index(i)
    del matriz[indice]
    del periodos[indice]
    print("Matriz exterminada correctamenlte")

#ORIGINAL
import random
if __name__ == "__main__":
    menu()
    
#EJERCICIO 11

"""Hacer un módulo denominado transpuesta(m), el parámetro m es una matriz de números enteros y devuelve la
matriz transpuesta (las filas serán las columnas y viceversa)."""

def transpuesta(m):
    
    matriz_transpuesta = []
    
    for j in range(len(m[0])):
        fila_transpuesta = []
        
        for i in range(len(m)):
            fila_transpuesta.append(m[i][j])
        
        matriz_transpuesta.append(fila_transpuesta)
    
    return matriz_transpuesta

# Ejemplo de uso
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [0, 0, 0]]
matriz_transpuesta = transpuesta(matriz)

print("Matriz original:")
for fila in matriz:
    print(fila)

print("\nMatriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)

#EJERCICIO 12
"""Realizar un módulo denominado eliminar_x(m, x) cuyos parámetros sean el primero m una matriz de números
enteros, el segundo parámetro x de tipo entero. El módulo elimina todas las filas y todas las columnas donde
se encuentren valores iguales a x"""

def generar_matriz(matriz):
    
    fila = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))
    
    for _ in range(fila):
        lista = []
        for _ in range(columnas):
            valor = random.randint(0, 100)
            lista.append(valor)
        matriz.append(lista)

def eliminar_x(matriz, x):
    filas = len(matriz)
    columnas = len(matriz[0])
    filas_eliminar = []
    columnas_eliminar = []
    
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == x:
                filas_eliminar.append(i)
                columnas_eliminar.append(j)
    
    for fila in filas_eliminar:
        del matriz[fila] #EXCEPCION. DE TODAS FORMAS, SI SE ELIMINAN LAS FILAS SE ESTARIA ELIMINANDO LAS COLUMNAS XD
    
    if columnas_eliminar:
        for fila in matriz:
            for columna in columnas_eliminar:
                del fila[columna]
    
def mostrar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print()
        
#ORIGINAL
matriz = []
import random
generar_matriz(matriz)
x = int(input("Ingresar x: "))
eliminar_x(matriz, x)
print()
mostrar(matriz)

# f, c = buscar_x_matriz(m, x) #f es la fila y c es la columna de x
# while f != -1 and c != -1:
#     eliminar_fila_matriz(m, f)
#     eliminar_columna_matriz(m, c)
#     f, c = buscar_x_matriz(m, x)

# # m = cargar_matriz()
# # x = int(input(‘x:’))
# # eliminar_x (m, x)
# # mostrar_matriz(m)

#EJERCICIO 13
"""Cargar en forma aleatoria tres listas paralelas lst1 con valores enteros, lst2 con valores flotantes y lst3 con los
caracteres ‘A’, ‘B’. Se desea hacer un algoritmo que cargue las listas lst4, lst5 y lst6 con los respectivos valores
de las tres listas iniciales pero ordenadas de acuerdo al orden de las letras ‘A’, ‘B’. Ejemplo:"""

#Inicial
# lst1 = [5, 9, 7, 1, 0, 4]
# lst2 = [6.0, 7.1, 4.2, 0.3, 1.5, 2.8]
# lst3 = ['B', 'A', 'B', 'A', 'B', 'B']

# #Final
# lst4 = [1, 9, 0, 4, 5, 7]
# lst5 = [0.3, 7.1, 1.5, 2.8, 4.2, 6.0]
# lst6 = ['A', 'A', 'B', 'B', 'B', 'B']

import random

lst1 = []
lst2 = []
lst3 = []

# Generar valores aleatorios para las tres listas iniciales
for _ in range(6):
    lst1.append(random.randint(0, 9))
    lst2.append(random.uniform(0.0, 9.9))
    lst3.append(random.choice(['A', 'B']))

# Imprimir listas iniciales
print("Inicial")
print("lst1 =", lst1)
print("lst2 =", lst2)
print("lst3 =", lst3)

# Crear listas ordenadas según el orden de las letras 'A' y 'B'
lst4 = [x for _, x in sorted(zip(lst3, lst1))]
lst5 = [x for _, x in sorted(zip(lst3, lst2))]
lst6 = sorted(lst3)

# Imprimir listas finales
print("\nFinal")
print("lst4 =", lst4)
print("lst5 =", lst5)
print("lst6 =", lst6)