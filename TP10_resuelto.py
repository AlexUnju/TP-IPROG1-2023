#CASOS DE ESTUDIO
"""Mediante un menú de opciones realizar el siguiente programa modular para gestionar el listado de notas de un
examen para los estudiantes de una institución educativa:

1. Registrar estudiantes: para cada uno se debe solicitar DNI, nombre y nota. Validar que la nota se
encuentre entre 0 y 10. El proceso finaliza cuando se ingresa un DNI igual a cero.
2. Mostrar el listado de estudiantes con sus respectivas notas.
3. Buscar a un estudiante por su DNI y mostrar su nombre y nota.
4. Modificar los datos de un estudiante buscando por DNI (el DNI no se puede modificar).
5. Eliminar a un estudiante por su DNI. Emitir un mensaje de confirmación.
6. Mostrar los estudiantes que obtuvieron nota mayor o igual a una dada y el promedio correspondiente"""

def menu():
    estudiantes = dict()
    while True:
        print()
        print("\t-MENU-")
        print("1. Registrar estudiantes")   
        print("2. Mostrar listado")
        print("3. Buscar estudiante por su DNI")
        print("4. Modificar los datos de un         estudiante")
        print("5. Eliminar a un estudiante por su DNI")
        print("6. Mostrar estudiantes con mayor nota y el promedio")
        print("7. Salir")
        opcion = input("\nIngrese una opcion [1, 7]: ")
        if opcion == "1":
            registrar_estudiantes(estudiantes)
        elif opcion == "2":
            mostrar_listado(estudiantes)
        elif opcion == "3":
            buscar_estudiante(estudiantes)
        elif opcion == "4":
            modificar_datos(estudiantes)
        elif opcion == "5":
            eliminar_estudiante(estudiantes)
        elif opcion == "6":
            mayor_alpromedio(estudiantes)
        elif opcion == "7":
            print("\nGracias por usar nuestro programa!")
            break
        else:
            print("Error, opcion invalida. Intente nuevamente")
            
def registrar_estudiantes(estudiantes):
    while True:
        dni = int(input("\nIngrese su DNI (0 para salir): "))
        if dni == 0:
            break
        if dni in estudiantes:
            print("Error: El estudiante ya está registrado.")
            continue #-> ignora el resto del codigo y vuelve al inicio del bucle
        nombre = input("Ingrese su nombre: ")
        nota = int(input("Ingrese su nota: "))
        while nota < 0 or nota > 10:
            print("Error: nota fuera de rango [0, 10]")
            nota = int(input("Ingrese su nota: "))
        estudiantes[dni] = {"nombre": nombre, "nota": nota}
        
def mostrar_listado(estudiantes):
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for clave, valor in estudiantes.items():
            print(f'DNI: {clave}')
            print(f'Nombre: {valor["nombre"]}')
            print(f'Nota: {valor["nota"]}')
            print()

def buscar_estudiante(estudiantes):
    dni = int(input("Ingrese el DNI del estudiante para buscarlo: "))
    if dni in estudiantes: #-> dni solo recorre las claves, es decir, el dni
        estudiante = estudiantes[dni] #-> "estudiante" toma los elementos del diccionario, pero no la clave
        print("\nEstudiante encontrado:")
        print(f'\nNombre: {estudiante["nombre"]}')
        print(f'Nota: {estudiante["nota"]}')
    else:
        print("Estudiante no encontrado.")
            
def modificar_datos(estudiantes):
    dni = int(input("Ingrese el DNI del estudiante para modificarlo: "))
    if dni in estudiantes:
        estudiante = estudiantes[dni]
        nombre = input("Ingrese nombre nuevo: ")
        nota = int(input("Ingrese nota nueva: "))
        while nota < 0 or nota > 10:
            print("Error: nota fuera de rango [0, 10]")
            nota = int(input("Ingrese nota nueva: "))
        estudiante["nombre"] = nombre
        estudiante["nota"] = nota
        print("\nEstudiante modificado con éxito!")
    else:
        print("Estudiante no encontrado.")

def eliminar_estudiante(estudiantes):
    dni = int(input("Ingrese el DNI del estudiante para eliminarlo: "))
    for clave in estudiantes.keys():
        if clave == dni:
            del estudiantes[clave]
            break
    print("\nEstudiante eliminado  con exito!")

# def eliminar_estudiante(estudiantes):
#     dni = int(input("Ingrese el DNI del estudiante para eliminarlo: "))
#     if dni in estudiantes:
#         del estudiantes[dni]
#         print("\nEstudiante eliminado con éxito!")
#     else:
#         print("Estudiante no encontrado.")
        
def mayor_alpromedio(estudiantes):
    nota_dada = int(input("Ingrese una nota limite: "))
    suma = 0
    cantidad = 0
    for clave, valor in estudiantes.items():
        if valor["nota"] >= nota_dada:
            print(f'\nDNI: {clave}')
            print(f'Nombre: {valor["nombre"]}')
            print(f'Nota: {valor["nota"]}')
            suma += valor["nota"]
            cantidad += 1

    if cantidad == 0:
        print("No hay estudiantes con una nota mayor o igual a la nota límite.")
    else:
        promedio = suma / cantidad
        print(f'El promedio general es de {promedio}')

        
#ORIGINAL
menu()

#EJERCICIO 1
"""Analizar, realizar la prueba de escritorio para los valores de entrada solicitados y mostrar la salida de los
siguientes códigos:"""

#s1 = abc aac ede eea cba

s1 = input('Ingrese cadena:')
s2 = s1.replace(' ','')
dic = {}
for i in range(len(s2)):
    letra = s2[i]
    if letra in dic:
        dic[letra] += 1
    else:
        dic[letra] = 1
        print('Análisis:','\'',s1,'\'')
        
for key in dic:
    print(key,'->',dic[key])
    
# valores = x y x y x z

valores = input('Ingrese cadena:')
lst_valores = valores.split(' ')
lst_claves = [i for i in range(len(lst_valores))] #-> compresion de lista -> nueva_lista = [expresion for elemento in iterable if condicion]
dic1 = dict(zip(lst_claves, lst_valores)) #crea un diccionario con su calve y valor
dic2 = {}
for key, value in dic1.items():
    if not value in dic2.values(): #->la condicion dice que "si el valor no esta en dic2" que al diccionario 'dic2' le asigle la clave
        dic2[key] = value          #dic2[key] y el valor "value"       

print(dic1)
print(dic2)

#EJERCICIO 2
"""Escribir un programa que implemente una agenda con diccionarios. En la agenda se podrán guardar nombres y
números de teléfono. El programa debe mostrar el siguiente menú:

1. Añadir/modificar: solicita un nombre, si el nombre se encuentra en la agenda, debe mostrar el
teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe
permitir ingresar el teléfono correspondiente.
2. Buscar: solicitando una cadena de caracteres, y muestra todos los contactos cuyos nombres comienzan
por dicha cadena.
3. Borrar: solicita un nombre y si existe nos preguntará si queremos borrarlo de la agenda. Si existe más
de uno debe identificarlos por un número secuencial que permita al usuario identificarlo para realizar
la operación de borrado.
4. Listar: muestra todos los contactos de la agenda."""

def menu():
    agenda = dict()
    while True:
        print("\t-- MENU --")
        print("1. Crear agenda")
        print("2. Añadir/modificar a un estudiante")
        print("3. Buscar por nombre")
        print("4. Borrar estudiante")
        print("5. Mostrar agenda")
        print("6. Salir.")

        opcion = input("\nElija una opcion [1, 5]: ")
        if opcion == "1":
            crear_agenda(agenda)
        if opcion == "2":
            añadir_modificar(agenda)
        elif opcion == "3":
            buscar_solicitando(agenda)
        elif opcion == "4":
            borrar_solicitando(agenda)
        elif opcion == "5":
            mostrar(agenda)
        elif opcion == "6":
            print("\nGracias por usar nuestro programa! Adios")
            break

def crear_agenda(agenda):
    while True:
        nombre = input("Ingrese su nombre (0 para salir): ")
        if nombre == "0":
            break
        telefono = int(input("Ingrese el telefono: "))
        if telefono in agenda:
            print("Error: Telefono en uso")
            break

        agenda[telefono] = {"nombre": nombre}
        
def añadir_modificar(agenda):
    nombre = input("Ingrese el nombre:  ")
    for clave, valor in agenda.items():
        if valor["nombre"] == nombre:
            print(f"Telefono: {clave}")
            modificar = input("\n¿Desea modificar el telefono? s/n: ")

            if modificar.lower() == "si":
                nuevo = int(input("Ingrese nuevo telefono:"))
                value = valor["nombre"]
                del agenda[clave]
                agenda[nuevo] = {"nombre": value}
                print("Estudiante modificado correctamente")
                break
        else:
            print("\nEl nombre no se encontro: ")                
            nuevo = int(input("\nIngrese telefono para añadir:"))
            agenda[nuevo] = {"nombre": nombre}
            print("Usuario añadido correctamente!")
            break

def buscar_solicitando(agenda):
    buscar = input("Ingrese un nombre para ver las coincidencias: ")
    for clave, valor in agenda.items():
        if valor["nombre"].startswith(buscar):
            print(f'Telefono: {clave}')
            print(f'Nombre: {valor["nombre"]}')
            
def borrar_solicitando(agenda):
    nombre = input("Ingrese el nombre del estudiante que desea borrar: ")
    coincidencias = []
    for clave, valor in agenda.items():
        if valor["nombre"] == nombre:
            coincidencias.append(clave)
    if len(coincidencias) == 0:
        print("No se encontró ningún estudiante con ese nombre en la agenda.")
    elif len(coincidencias) == 1:
        confirmacion = input(f"¿Desea borrar al estudiante {nombre}? (s/n): ")
        if confirmacion.lower() == "s":
            del agenda[coincidencias[0]]
            print("Estudiante borrado exitosamente.")
    else:
        print("Se encontraron múltiples coincidencias para el nombre ingresado:")
        for i, clave in enumerate(coincidencias):
            print(f"{i+1}. Telefono: {clave}, Nombre: {agenda[clave]['nombre']}")
        seleccion = input("Ingrese el número correspondiente al estudiante que desea borrar: ")
        if seleccion.isdigit() and int(seleccion) in range(1, len(coincidencias)+1):
            confirmacion = input(f"¿Desea borrar al estudiante {agenda[coincidencias[int(seleccion)-1]]['nombre']}? (s/n): ")
            if confirmacion.lower() == "s":
                del agenda[coincidencias[int(seleccion)-1]]
                print("Estudiante borrado exitosamente.")
        else:
            print("Selección inválida.")

def mostrar(agenda):
    for clave, valor in agenda.items():
        print(f'Nombre: {valor["nombre"]}')
        print(f'Telefono: {clave}')

# def listar(agenda):
#     if agenda:
#         print("Lista de contactos:")
#         for i, contacto in enumerate(agenda.items(), start=1):
#             nombre, telefono = contacto
#             print(f"{i}. Nombre: {nombre}, Teléfono: {telefono}")
#     else:
#         print("La agenda está vacía.")

#original
menu()

#EJERCICIO 3
"""Ingrese un texto y cuente las cantidades de repeticiones para los caracteres que lo componen. Ejemplo de
entrada: INTRODUCCION A LA PROGRAMACION y salida:"""

#FORMA 1 CREANDO UNA VARIABLE DENTRO DEL BUCLE (SIN DEFINIR)
def contar_letras(frase):
    dic = dict()
    nuevo = frase.replace(" ", "")
    for i in range(len(nuevo)):
        letra = nuevo[i]
        if letra in dic:
            dic[letra] += 1
        else:
            dic[letra] = 1
    return dic
        
#ORIGINAL
frase = input("Ingrese una frase: ")
dic = contar_letras(frase)
for key in dic:
    print(f"{key} -> {dic[key]}")

# #FORMA 2 SIN VARIABLE
# def contar_letras(frase):
#     dic = dict()
#     nuevo = frase.replace(" ", "")
#     for i in range(len(nuevo)):
#         if nuevo[i] in dic:
#             dic[nuevo[i]] += 1
#         else:
#             dic[nuevo[i]] = 1
#     return dic
        
# #ORIGINAL
# frase = input("Ingrese una frase: ")
# dic = contar_letras(frase)
# for key in dic:
#     print(f"{key} -> {dic[key]}")

#EJERCICIO 4
"""Escribir un programa que permita gestionar una base de datos de estudiantes de una carrera de la facultad. Los
estudiantes se guardan en un diccionario en el que la clave de cada cliente será su Libreta Universitaria (LU),
los datos del estudiante son nombre, dirección, teléfono, correo, estado), donde el estado tendrá el valor True
si se trata de un estudiante activo. El programa debe preguntar al usuario por una opción del siguiente menú:

1. Añadir estudiante, por defecto estado True
2. Eliminar estudiante,
3. Mostrar estudiante,
4. Listar todos los estudiantes,
5. Listar estudiantes activos o pasivos (permitir la selección)
6. Cambiar de estado a un estudiante solicitando la LU (True a False o False a True)."""

dic = dict()

def menu():
    while True:
        print("\t-Menu-")
        print("1. Añadir estudiante")
        print("2. Eliminar estudiante")
        print("3. Mostrar estudiante")
        print("4. Listar todos los estudiantes")
        print("5. Listar estudiantes activos o posivos")
        print("6. Cambiar estado de estudiante")
        print("7. Salir")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            añadir_estudiantes()
        elif opcion ==  "2":
            eliminar_estudiante()
        elif opcion == "3":
            mostrar_estudiante()
        elif opcion == "4":
            listar_estudiantes()
        elif opcion == "5":
            listar_estados()
        elif opcion == "6":
            cambiar_estado()
        elif opcion == "7":
            print("\nGracias por usar nuestro programa!")
            break
        else:
             print("Opción inválida. Intente nuevamente.")
            
            
#VALIDACIONES
def validar_clave(clave):
    return clave in dic

def validar_tel(telefono):
    pass

def añadir_estudiantes():
    print()
    clave= input("Ingrese LU: ")
    if validar_clave(clave):
        print("Error: Libreta universitaria en uso.")
        return
    nombre = input("Ingrese nombre completo: ")
    direccion = input("Ingrese direccion: ")
    telefono = input("Ingrese telefono: ")
    correo = input("Ingrese correo electronico: ")
    print()
    dic[clave] = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo, 'estado': True}

# def agregar_estudiante():
#     lu = input("Ingrese el número de Libreta Universitaria (LU): ")
#     nombre = input("Ingrese el nombre del estudiante: ")
#     direccion = input("Ingrese la dirección del estudiante: ")
#     telefono = input("Ingrese el número de teléfono del estudiante: ")
#     correo = input("Ingrese el correo del estudiante: ")
#     estado = True  # Estado activo por defecto
    
#     estudiante = {
#         "nombre": nombre,
#         "dirección": direccion,
#         "teléfono": telefono,
#         "correo": correo,
#         "estado": estado
#     }
    
#     dic[lu] = estudiante -> Se puede agregar como valor un diccionario ya creado XD
#     print("Estudiante agregado correctamente.")
    
def eliminar_estudiante():
    if dic:
        clave = input("Ingrese LU del estudiante a eliminar: ")
        if clave in dic: #antes buscaba la clave con un for pero no es necesario
            del dic[clave]
            print("\nEstudiante eliminado exitosamente!")
        
    else:
        print("Error: No hay estudiantes cargados")

    
def mostrar_estudiante():
    lu = input("Ingrese el número de Libreta Universitaria (LU) del estudiante a mostrar: ")
    
    if lu in dic:
        estudiante = dic[lu] #-> "estudiante" toma todo el valor de la clave
        print("Datos del estudiante:")
        print("LU:", lu)
        print("Nombre:", estudiante["nombre"])
        print("Dirección:", estudiante["dirección"])
        print("Teléfono:", estudiante["teléfono"])
        print("Correo:", estudiante["correo"])
        print("Estado:", "Activo" if estudiante["estado"] else "Pasivo") #-> expresion condicional o operador ternario, estructura: valor_verdadero if condición else valor_falso

    else:
        print("No se encontró un estudiante con ese LU.")

# def mostrar_estudiante():
#     clave = input("Ingrese LU del estudiante a mostrar: ")
#     if dic:
#         for lu, valor in dic.items():
#             if lu == clave:
#                 print(f"\nNombre: {valor['nombre']}")
#                 print(f"Direccion: {valor['direccion']}")
#                 print(f"Telefono: {valor['telefono']}")
#                 print(f"Correo: {valor['correo']}")
#                 print(f"Estado: {valor['estado']}")
#         print()
#     else:
#         print("Error: No hay estudiantes cargados")
            
def listar_estudiantes():
    if dic:
        print("\nLista de estudiantes: ")
        for lu, valor in dic.items():
                print(f"\nLU: {lu}")
                print(f"Nombre: {valor['nombre']}")
                print(f"Direccion: {valor['direccion']}")
                print(f"Telefono: {valor['telefono']}")
                print(f"Correo: {valor['correo']}")
                print(f"Estado: {valor['estado']}")
        print()
    else:
        print("Error: No hay estudiantes cargados")
        
# def listar_estudiantes():
#     print("Listado de todos los estudiantes:")
#     for lu, estudiante in dic.items():
#         print("LU:", lu)
#         print("Nombre:", estudiante["nombre"])
#         print("Dirección:", estudiante["dirección"])
#         print("Teléfono:", estudiante["teléfono"])
#         print("Correo:", estudiante["correo"])
#         print("Estado:", "Activo" if estudiante["estado"] else "Pasivo")

def listar_estados():
    listar = input("¿Qué tipo de estudiantes quiere listar? (True or False): ")
    if dic:
        for lu, valor in dic.items():
            if str(valor['estado']) == listar:
                print(f"\nLU: {lu}")
                print(f"Nombre: {valor['nombre']}")
                print(f"Direccion: {valor['direccion']}")
                print(f"Telefono: {valor['telefono']}")
                print(f"Correo: {valor['correo']}")
                print(f"Estado: {valor['estado']}")
    else:
        print("\nError: No hay estudiantes cargados")

# def listar_estudiantes_estado():
#     estado = input("Ingrese el estado de los estudiantes a listar (activo/pasivo): ")
#     estado = estado.lower()
    
#     if estado == "activo" or estado == "pasivo":
#         print(f"Listado de estudiantes {estado}s:")
#         for lu, estudiante in dic.items():
#             if estudiante["estado"] == (estado == "activo"):
#                 print("LU:", lu)
#                 print("Nombre:", estudiante["nombre"])
#                 print("Dirección:", estudiante["dirección"])
#                 print("Teléfono:", estudiante["teléfono"])
#                 print("Correo:", estudiante["correo"])
#                 print("-----------------------")
#     else:
#         print("Estado inválido. Debe ingresar 'activo' o 'pasivo'.")
        
def cambiar_estado():
    if dic:
        clave = input("Ingrese la LU del estudiante que desea cambiar de estado: ")
        for lu, valor in dic.items():
            if lu == clave:
                cambiar = input(f"¿Quiere cambiar el estado del estudiante {valor['nombre']}? si/no: ")
                if cambiar.lower() == "si":
                    valor['estado'] = not valor['estado']
                    print("\nEstudiante cambiado con exito!\n")
                    break   
    else:
        print("Error: No hay estudiantes cargados")

# def cambiar_estado_estudiante():
#     lu = input("Ingrese el número de Libreta Universitaria (LU) del estudiante a cambiar el estado: ")
    
#     if lu in dic: 
#         estudiante = dic[lu]
#         estudiante["estado"] = not estudiante["estado"]
#         print("Estado del estudiante cambiado correctamente.")
#     else:
#         print("No se encontró un estudiante con ese LU.")
    
#ORIGINAL
menu()

#EJERCICIO 5
"""Utilizando diccionarios diseñar un programa modular que permita gestionar los productos de un comercio, las
funcionalidades solicitadas son:

a. Registrar productos: para cada uno se debe solicitar, código, descripción, precio y stock. Agregar las
siguientes validaciones:
i. El código no se puede repetir
ii. Todos los valores son obligatorios
iii. El precio y el stock no pueden ser negativos
b. Mostrar el listado de productos
c. Mostrar los productos cuyo stock se encuentre en el intervalo [desde, hasta]
d. Diseñar un proceso que le sume X al stock de todos los productos cuyo valor actual de stock sea menor
al valor Y.
e. Eliminar todos los productos cuyo stock sea igual a cero.
f. Salir"""

def menu():
    while True:
        print()
        print("\t-MENU-")
        print("a. Registrar productos")
        print("b. Mostrar el listado de productos")
        print("c. Mostrar los productos dentro de un intervalo")
        print("d. Sumar stock a los productos")
        print("e. Eliminar los productos con stock 0")
        print("f. Salir")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "a":
            registrar_productos()
        elif opcion == "b":
            mostrar_listado()
        elif opcion == "c":
            mostrar_por_intervalo()
        elif opcion == "d":
            sumar_stock()
        elif opcion == "e":
            eliminar_stock_cero()
        elif opcion == "f":
            print("\nGracias por usar nuestro programa!")
            break
            
def registrar_productos():
    codigo = input("Ingrese el codigo de producto: ")
    if validar_codigo(codigo):
        print("Error: El codigo no puede repetirse")
        return
    descripcion = input("Ingrese la descripcion del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    if precio < 0 or stock < 0:
        print("Error: El precio y stock no pueden ser negativos")
        return
    
    productos[codigo] = {'descripcion': descripcion, "precio": precio, "stock": stock}

def mostrar_listado():
    if productos:
        print("\nLista de productos:")
        for clave, valor in productos.items():
            print(f"\nCodigo: {clave}")
            print(f"Descripcion: {valor['descripcion']}")
            print(f"Precio: {valor['precio']}")
            print(f"Stock: {valor['stock']}")
    else:
        print("\nError: El diccionario esta vacio")

def mostrar_por_intervalo():
    if productos:
        desde = float(input("Desde: "))
        hasta = float(input("Hasta: "))
        print(f"\nLista de productos en el intervalo [{desde}, {hasta}]")
        for clave, valor in productos.items():
            if valor['stock'] >= desde and valor['stock'] <= hasta:
                print(f"\nCodigo: {clave}")
                print(f"Descripcion: {valor['descripcion']}")
                print(f"Precio: {valor['precio']}")
                print(f"Stock: {valor['stock']}")
    else:
        print("Error: El diccionario esta vacio")
        
def sumar_stock():
    if productos:
        y = int(input("\nAñadir stock a los producotos menores que: "))
        x = int(input("¿Cuanto stock quieres añadir?: "))
        for stock in productos.values():
            if stock['stock'] < y:
                stock['stock'] += x
        print("\n¡Stock añadido con exito!")
    else:
        print("Error: El diccionario esta vacio")

def eliminar_stock_cero():
    if productos:
        productos_del = []
        for clave, valor in productos.items():
            if valor['stock'] == 0:
                productos_del.append(clave)
                
        for clave in productos_del:
            del productos[clave]
        print("\nProductos eliminados correctamente")
    else:
        print("Error: El diccionario esta vacio")
        

#VALIDACIONES
def validar_codigo(codigo):
    return codigo in productos
    
#ORIGINAL
productos = {"01": {'descripcion': "rico", 'precio': 750, 'stock': 20},
             "02": {'descripcion': "bueno", 'precio': 500, 'stock': 10},
             "03": {'descripcion': "delicioso", 'precio': 300, 'stock': 0}}

menu()

#EJERCICIO 6
""" Diseñar un programa que, mediante un menú de opciones, permite realizar lo siguiente:
a. Cargar dos listas (lista01 y lista02) de contactos de una agenda digital, donde cada contacto tiene
número de celular, nombre y correo electrónico.
b. Mostrar las listas generadas
c. Generar la lista03 que contenga la fusión de las dos primeras, considerar lo siguiente:
i. Pueden existir contactos que tengan el mismo número de celular en lista01 y lista02
ii. Lista03 puede generarse agregando primero lista01 y luego lista02, pero debe validar que el
número de celular no se haya agregado previamente. De ser así debe mostrar un mensaje
informando que ya existe el contacto y pedir al usuario que elija cuál de los dos contactos
corresponde que se guarde en lista03.
d. Salir"""

def menu():
    while True:
        print("\t-MENU-")
        print("a. Cargar listas (lista01 y lista02)")
        print("b. Mostrar las listas generadas")
        print("c. Generar lista 03")
        print("d. Salir")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "a":
            cargar_listas()
        elif opcion == "b":
            mostrar_listas()
        elif opcion == "c":
            generar_lista03()
        elif opcion == "d":
            print("\nGracias por usar nuestro programa. ¡Hasta luego!")
            break
            
def cargar_listas():
    cargar1 = int(input("¿Cuantos contactos quiere cargar a la lista01?: "))
    cargar2 = int(input("¿Cuantos contactos quiere cargar a la lista02?: "))

    if cargar1 >= 0 and cargar2 >= 0:
        for _ in range(cargar1):
            nombre = input("\nIngrese nombre: ")
            celular = input("Ingrese numero de celular: ")
            correo = input("Ingrese correo electronico: ")
            lista01.append({'nombre': nombre, 'celular': celular, 'correo': correo})
            
        for _ in range(cargar2):
            nombre = input("\nIngrese nombre: ")
            celular = input("Ingrese numero de celular: ")
            correo = input("Ingrese correo electronico: ")
            lista02.append({'nombre': nombre, 'celular': celular, 'correo': correo})
        print("\nListas cargadas exitosamente!\n")
    else:
        print("\nError: No pueden ser numeros negativos")
    
def mostrar_listas():
    if len(lista01) > 0:
        print("\nLista 01:")
        for lst1 in lista01:
            print(f"\nNombre: {lst1['nombre']}")
            print(f"Celular: {lst1['celular']}")
            print(f"Correo: {lst1['correo']}")
    else:
        print("\nError: No hay contactos en la lista01")
        
    if len(lista02) > 0:
        print("\nLista 02:")
        for lst2 in lista02:
            print(f"\nNombre: {lst2['nombre']}")
            print(f"Celular: {lst2['celular']}")
            print(f"Correo: {lst2['correo']}")
        print()
    else:
        print("\nError: No hay contactos en la lista02\n")

def generar_lista03():
    
    lista03 = lista01.copy() #una forma mas facil de agregar todos los elementos a la lista03
    
    # for lst1 in lista01:
    #     lista03.append(lst1)
    
    for lst2 in lista02:
        for lst3 in lista03:
            if lst2['celular'] == lst3['celular']:
                elegir = input(f"El numero {lst2['celular']} esta repetido. ¿Cual contacto desea conservar: 1. list01 o 2. list01?: ")
                if elegir == "1":
                    continue
                
                elif elegir == "2":
                    lst3['celular'] = lst2['celular']
                    
# def generar_lista03(lista01, lista02, lista03):
#     print("\n-- Generar Lista03 --")
    
#     lista03 = lista01.copy()
    
#     for contacto in lista02:
#         celular = contacto["celular"] #Para cada numero de celular de lista02 se guarda en "celular"
#         if celular in [c["celular"] for c in lista03]: #Se realiza una verificación para determinar si el celular ya existe en lista03
#             print(f"Ya existe un contacto con el número de celular {celular}")
#             opcion = input("¿Cuál de los dos contactos desea conservar? (1 - lista01, 2 - lista02): ")
#             if opcion == "1": #Si el usuario eleje "1" se ejecuta "continue" para pasar el siguiente contacto (se conserva el contacto existente)
#                 continue 
#             elif opcion == "2":
#                 lista03 = [c for c in lista03 if c["celular"] != celular] #se actualiza lista03 para eliminar los contactos duplicados, o sea elimina lo de lista01
#         lista03.append(contacto) #se le agrega "contacto" que seria un diccionario de lista02
        
    if len(lista03) > 0:
        print("\nLista generada:")
        for lst3 in lista03:
            print(f"\nNombre: {lst3['nombre']}")
            print(f"Celular: {lst3['celular']}")
            print(f"Correo: {lst3['correo']}")
        print()
                    
    
#ORIGINAL
lista01 = list()
lista02 = list()
lista03 = list()
menu()

#EJERCICIO 7
"""Realizar un programa para realizar un conjunto de préstamos realizados por una biblioteca. Cada libro en
una biblioteca puede ser prestado sólo a un usuario de la biblioteca a la vez. Sin embargo, un usuario
puede sacar varios libros. Por lo tanto, la información sobre qué libros se prestan a qué usuarios puede
representarse mediante un diccionario, en la que los libros son las claves y los usuarios son los valores. Un
ejemplo usando la estructura de datos sería:

{ "Orgullo y prejuicio" : "Alicia" , "Cumbres Borrascosas" : "Alicia" , "Grandes esperanzas" : "Juan" }

Una operación de búsqueda en la clave "Grandes esperanzas" devolvería "Juan". Si Juan devuelve su
libro, eso causaría una operación de eliminación, y si Pat saca un libro, eso causaría una operación de
inserción, lo que llevaría a un estado diferente:

{ "Orgullo y prejuicio" : "Alicia" , "Los hermanos Karamazov" : "Pat" , "Cumbres Borrascosas" : "Alicia" }"""

def menu():
    while True:
        print()
        print("\tBIBLIOTECA")
        print("1. Prestar libros")
        print("2. Devolver libros")
        print("3. Salir")
        opcion = input("Elija una opcion [1-3]: ")
        
        if opcion == "1":
            prestar_libros()
        elif opcion == "2":
            devolver_libros()
        elif opcion == "3":
            print("\nGracias por usar nuestro programa. ¡Hasta luego!")
            break
    
def prestar_libros():
    cantidad = int(input("\n¿Cuantos libros quiere cargar?: "))
    for i in range(cantidad):
        nombre = input("\nIngrese nombre de la persona: ")
        libros = input(f"Ingrese el nombre del libro {i+1}: ")
        if libros not in prestamos:
            prestamos[libros] = nombre
        else:
            print("\nError: El libro se encuentra prestado.")

            
def devolver_libros():
        devolver = input("\nIngrese nombre del libro a devolver: ")
        if devolver in prestamos:
            print(f"Persona a cargo del libro: {prestamos[devolver]}")
            confirmar = input("\n¿Confirma la devolución? si/no: ")
            if confirmar.lower() != "si":
                return
            else:
                del prestamos[devolver]
                print("\nLibro devuelto correctamente!")
        
#ORIGINAL
prestamos = dict()
menu()