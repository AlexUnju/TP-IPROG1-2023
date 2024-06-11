#CASOS DE ESTUDIO

"""Analice, diseñe y codifique los siguientes enunciados en Python
1. Una institución bancaria tiene una aplicación que recibe una lista con los movimientos de las cuentas bancarias
de sus clientes mediante un servicio externo. Para cada cuenta se recibe el número de cuenta, nombre y
apellido del cliente, importe, fecha del movimiento y el tipo de movimiento (E=Extracción, D=Depósito). El
formato de cada cuenta está dado por una cadena de caracteres donde cada atributo de una cuenta se
encuentra separado por comas.
Por ejemplo:
27200123456,MARIA FERNANDEZ,0000500000,30-05-2021,E
27200321654,CARLOS TORRES,0000400045,31-05-2021,D
27200987125,LAURA AQUINO,0000230000,30-05-2021,D
27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E  
27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E
27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D
Tenga en cuenta que:
- Los 2 últimos dígitos del importe corresponden a los centavos, o sea que el valor 0000500000 es
equivalente a 5000 pesos.
- La fecha solo tiene carácter informativo por lo que debe guardarse como un string.
Se solicita lo siguiente:
1. Procesar la lista recibida y guardar los datos recibidos en una lista.
2. Mostrar la lista con las cuentas obtenidas.
3. Mostrar los movimientos correspondientes a depósitos y el total acumulado.
4. Mostrar los movimientos de una cuenta.
Nota: utilice los datos del ejemplo para validar el programa"""

def movimiento(lista_externa):
    lst = list()
    for item in lista_externa:
        movimiento = item.split(",")
        importe = movimiento[2]
        importe = float(importe[:-2] + "." + importe[-2:])
        movimiento[2] = importe
        lst.append(movimiento)
    return lst

def mostrar(lista_externa):
    print('Lista de todos los movimientos')
    for i, item in enumerate(lista_externa):
        print(i, item)

def mostrar_debito(lista_externa):
    suma = 0
    print()
    for i, item in enumerate(lista_externa):
        if item[4] == "D":
            print(i, item)
            suma += item[2]
    print()
    print("\nDebito, total acomulado: {}".format(suma))

def mostrar_movimiento(lista_externa):
    existe = False
    codigo = input("\nIngrese el codigo de la cuenta: ")
    for i, item in enumerate(lista_externa):
        if item[0] == codigo:
            print(i, item)
            existe = True
            break
    if not existe:
        print("El codigo de la cuenta no existe")
     

#ORIGINAL
lista_externa = ["27200123456,MARIA FERNANDEZ,0000500000,30-05-2021,E",
            "27200321654,CARLOS TORRES,0000400045,31-05-2021,D",
            "27200987125,LAURA AQUINO,0000230000,30-05-2021,D",
            "27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E",
            "27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E",
            "27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D"]

lst = movimiento(lista_externa)
mostrar(lst)
mostrar_debito(lst)
mostrar_movimiento(lst)

#EJERCICIO 1
"""Analizar, realizar la prueba de escritorio y mostrar la salida de los siguientes programas:"""

#Texto: '192.168.0.1' separador = '.' 

def s_sep(cadena, car):
    lpalabras = list()
    if car in cadena:
        lpalabras = cadena.split(car)
    else:
        print('Ingreso inválido')
    return lpalabras
          
mensaje = '''
Ingrese un texto y luego
un caracter separador por ejm:
Texto: 1-2-3-4
Separador: -
'''      
print(mensaje)
txt = input('Texto:')
separador = input('Separador:')
lista = s_sep(txt, separador)
print(lista)

#edad = 'uno' , -10, 0

def lee_edad():
    edad = ""
    i = 0
    while i < 3:
        i += 1
        valor = input(f'Intento {i}, edad:')
        try:
            edad = float(valor)
            if edad <= 0.0:
                print('La edad debe ser > 0')
            else:
                return edad
        except ValueError:
            print('Dato inválido')
    print(f'Incorrecto! {i} intentos')

edad = lee_edad()
print(edad)

#EJERCICIO 2
"""Analizar y ejecutar el siguiente código que tiene tres funciones que realizan la misma tarea: contar la cantidad
de vocales que tiene una frase. Investigar en internet las instrucciones que no conozca."""

def contar_vocales1(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in 'aeiouáéíóúü':
            contador += 1
    return contador

def contar_vocales2(texto):
    return sum(map(texto.lower().count, 'aeiouáéíóúü'))
               #map(función, secuencia)
import re

def contar_vocales3(texto):
    return len(re.findall('[aeiouáéíóíúü]', texto, re.IGNORECASE))

cad = input('Ingrese una frase:') #'Pájaro de mal agüero'
print(contar_vocales1(cad))
print(contar_vocales2(cad))
print(contar_vocales3(cad))

#EJERCICIO 3
"""Analizar, ejecutar y mejorar el siguiente código."""
import random

def bienvenida(mensaje):
    bienv_inp = ['hola', 'buenas','que tal','hi', 'buenos','buen','todo']
    bienv_out = ['Hola, ¿cómo estás?','Hola, ¿qué tal?', 'Hola, ¿te puedo ayudar?', 'Hola, encantado de comunicarme contigo', 'Hola, espero que estés bien!']
    
    for palabra in mensaje.split():
        if palabra.lower() in bienv_inp:
            return random.choice(bienv_out)
        else:
            return 'Tu mensaje no está en mi base de datos'
        
cad = input('Soy un robot, salúdame por favor: ')
print(bienvenida(cad))

#EJERCICIO 4
"""Ingresar una dirección de email por teclado. Verificar que la cadena ingresada contiene un solo caracter '@'"""
#FORMA 1
email = input("Ingrese su email: ")

cont = email.count("@")

if cont == 1:
    print("Email valido")
else:
    print("Email invalido")

#FORMA 2
email = input("Ingrese una dirección de email: ")

if email.count('@') == 1:
    print("La dirección de email es válida.")
else:
    print("La dirección de email no es válida.")
    
#EJERCICIO 5
"""Ingresar una frase por teclado, se desea modificar todos los espacios en blanco dobles y dejar solo un espacioen blanco."""
frase = input("Ingrese una frase: ")

nueva_frase = frase.replace("  ", " ")
print(nueva_frase)

#EJERCICIO 6
"""Solicitar el ingreso de una palabra clave por teclado. Controlar que la cadena ingresada tenga más de 6
caracteres y al menos un número y un caracter en mayúsculas para que sea válido, en caso contrario mostrar
un mensaje de error."""

palabra_clave = input("Ingrese una palabra clave: ")

#Verificar la longitud
if len(palabra_clave) <= 6:
    print("Error: La palabra clave debe tener más de 6 caracteres.")
    exit()

#Verificar la presencia de al menos un número
if not any(char.isdigit() for char in palabra_clave):
    print("Error: La palabra clave debe contener al menos un número.")
    exit()

#Verificar la presencia de al menos una mayúscula
if not any(char.isupper() for char in palabra_clave):
    print("Error: La palabra clave debe contener al menos una letra mayúscula.")
    exit() #-> Para detener el programa en caso de error, se le puede agregar un texto como argumento

#Si se llega a este punto, la palabra clave es válida
print("La palabra clave es válida.")

#EJERCICIO 7
"""Escribir un módulo que tiene un parámetro que es una cadena de caracteres devuelve: La primera letra de
cada palabra de la cadena en mayúsculas. Por ejemplo, si recibe “universal serial bus” debe devolver “USB”."""

def obtener_iniciales(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    iniciales = [palabra[0].upper() for palabra in palabras]  # Obtener la primera letra de cada palabra en mayúsculas
    return ''.join(iniciales)  # Unir las iniciales en una sola cadena

cadena = "universal serial bus"
iniciales = obtener_iniciales(cadena)
print(iniciales)  # Output: "USB"

#EJERCICIO 8
"""Escribir un módulo que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y
devuelva el valor decimal correspondiente"""

def binario_a_decimal(cadena_binaria):
    decimal = int(cadena_binaria, 2)
    return decimal

cadena = "1101"
decimal = binario_a_decimal(cadena)
print(decimal)  # Output: 13

#EJERCICIO 9
"""Escribir un módulo denominado ins_car_xd(cadena, car, x, d), devuelve una cadena que inserta un caracter en
la cadena cada x cantidad de caracteres de la cadena, siendo el parámetro d la dirección desde dónde se
comienza la inserción, d puede ser “i” o “f”, si d es “i” es desde el inicio y si d es “f” es desde el fin, por
defecto d = “i” si no se especifica este parámetro . Ejemplo: cadena = “2552552550” car = “.” y x = 3 el
módulo debería devolver “255.255.255.0” otro ejemplo cadena = “1234567890” car = “,” x = 3 y d = “f” el
módulo debería devolver “1,234,567,890”"""

def ins_car_xd(cadena, car, x, d="i"):
    if d == "i":
        return car.join([cadena[i:i+x] for i in range(0, len(cadena), x)])
    elif d == "f":
        return car.join([cadena[i:i+x] for i in range(len(cadena)-x, -x, -x)])

# Ejemplos de uso
cadena1 = "2552552550"
resultado1 = ins_car_xd(cadena1, ".", 3)
print(resultado1)  # Salida: 255.255.255.0

cadena2 = "1234567890"
resultado2 = ins_car_xd(cadena2, ",", 3, "f")
print(resultado2)  # Salida: 1,234,567,890

#forma 2
def ins_car_xd(cadena, car, x, d="i"):
    if d == "f":
        cadena = cadena[::-1]
    partes = [cadena[i:i+x] for i in range(0, len(cadena), x)]
    return car.join(partes[::-1] if d == "f" else partes)

# Ejemplos de uso
cadena1 = "2552552550"
resultado1 = ins_car_xd(cadena1, ".", 3)
print(resultado1)  # Salida: 255.255.255.0

cadena2 = "1234567890"
resultado2 = ins_car_xd(cadena2, ",", 3, "f")
print(resultado2)  # Salida: 1,234,567,890

#EJERCICIO 10
"""Hacer un módulo que acepte una cadena original y devuelve otra cadena que es el geringoso de la cadena original.
Utilizar una iteración sobre la cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda
luego de cada vocal de la cadena original"""

def geringoso(cadena):
    vocales = "aeiou"
    geringoso_cadena = ""
    for caracter in cadena:
        geringoso_cadena += caracter
        if caracter.lower() in vocales:
            geringoso_cadena += "p" + caracter.lower()
    return geringoso_cadena

# Ejemplo de uso
cadena_original = "Hola, cómo estás?"
resultado = geringoso(cadena_original)
print(resultado)  # Salida: Hopolapa, copómopo epestáspá?

#EJERCICIO 11
""" Diseñar un programa que permita realizar el registro a una aplicación de estudiantes de una universidad, cada
estudiante cuenta con los siguientes atributos: dni, clave, nombre, eMail y número de celular. Se solicita
desarrollar las siguientes funcionalidades:

a. Registrarse en la aplicación: Se solicitan los datos del estudiante con las siguientes validaciones:
dni: es de tipo string debe tener 8 dígitos numéricos, luego de ingresar este valor se debe verificar que
no exista actualmente.
- clave: debe tener como mínimo una longitud de 6 caracteres, al menos una mayúscula y un número
- nombre: no puede tener números ni caracteres especiales y al menos 3 caracteres
- eMail: debe verificar que tenga el @ y que no se encuentre al inicio ni al final de la cadena ingresada.
- Número de Celular: debe incluir el código de área más el número sin el 15 (por ejemplo 388-4800123),
es decir:
    ■ Los primeros dígitos corresponden al código de área y los valores solo pueden ser 388, 3886,
3887 y 3888
    ■ El guión es obligatorio
    ■ Los restantes números corresponden al número de celular y su longitud debe ser de 7 dígitos.
    
El registro de estudiantes debe realizarse utilizando una estructura de tipo lista de listas que estará
inicializada con 10 estudiantes para facilitar las pruebas.

b. Buscar un estudiante: el programa solicitará el nombre y en función de ello mostrará lo siguiente:
● Si se ingresa un vacío (enter), el programa mostrará la lista completa de estudiantes registrados
● Si se ingresa un nombre, el programa mostrará los estudiantes cuyos nombres contengan al valor
ingresado, por ejemplo si ingresa ana, mostrará Mariana, Analía, etc.

c. Ingresar (Login): debe solicitar el dni y la clave y verificar que coincida con algún estudiante registrado, si no
existe emitirá el mensaje “Usuario o Clave incorrectos”. Si los datos son correctos mostrará el mensaje
“Ingreso exitoso” y también mostrará el nombre y correo electrónico del estudiante."""

def registro(estudiantes):
    
    dni = input("Ingrese DNI: ")
    if not validar_dni(dni):
        print("El DNI debe ser solo numerico y de una longitud de 8")
        return
    
    for estudiante in estudiantes:
        if estudiante[0] == dni:
            print("El estudiante  ya esta registrado")
            return
        
    clave = input("Ingrese clave: ")
    if not validar_clave(clave):
        print("Error: Clave invalida. Debe contener almenos una letra y un valor numerico, clave > 6")
        return
    
    nombre = input("Ingrese nombre: ")
    if not validar_nombre(nombre):
        print("Error: El nombre debe ser >= 3 y debe contener solo letras")
        return
    
    email= input("Ingrese email: ")
    if not validar_email(email):
        print("Error: No debe contener '@' al principio ni al final, solo al medio")
        return
        
    celular = input("Ingrese numero de celular: ")
    if not validar_celular(celular):
        print("Error: número de celular inválido. Debe tener el formato '388-1234567'.")
        return
         
    estudiantes.append([dni, clave, nombre, email, celular])
    print("Registro exitoso")
    
    
#VALIDACIONES
def validar_dni(dni):
    valor = dni.isdigit() and len(dni) == 8
    return valor

def validar_clave(clave):
    return len(clave) >= 6 and any(caracter.isupper() for caracter in clave) and any(caracter.isdigit() for caracter in clave) 

    # if len(clave) < 6:
    #     print("La clave debe tener mas de 6 caracteres")
    #     return
    #     #exit("La clave debe tener mas de 6 caracteres")
        
    # if not any(caracter.isupper() for caracter in clave):
    #     print("La clave debe tener almenos una mayuscula")
    #     return
    #     #exit("La clave debe tener almenos una mayuscula")
        
    # if not any(caracter.isdigit()for caracter in  clave):
    #     print("La clave debe tener almenos un numero")
    #     return    
    #     #exit("La clave debe tener almenos un numero")
    
    # return clave

def validar_nombre(nombre):
    return len(nombre) >= 3 and nombre.isalpha()
        
def validar_email(email):
    return "@" in email and not email.startswith("@") and not email.endswith("@")

def validar_celular(celular):
    if "-" not in celular:
        return False
    codigo_area, numero = celular.split("-")
    return codigo_area in ["388", "3886", "3887", "3888"] and len(numero) == 7 and numero.isdigit()

def buscar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre == "":
        for valor in estudiantes:
            print()
            print(f"DNI: {valor[0]}")
            print(f"Clave: {valor[1]}")
            print(f"Nombre: {valor[2]}")
            print(f"Email: {valor[3]}")
            print(f"Celular: {valor[4]}")
            print()
    else:
        resultados = [estudiante for estudiante in estudiantes if nombre.lower() in estudiante[2].lower()]
        if resultados:
            for valor in resultados:
                print()
                print(f"DNI: {valor[0]}")
                print(f"Clave: {valor[1]}")
                print(f"Nombre: {valor[2]}")
                print(f"Email: {valor[3]}")
                print(f"Celular: {valor[4]}")
                print()
        else:
            print("No se encontraron estudiantes con ese nombre.")
            
"""def buscar_estudiante():
    nombre_buscar = input("Ingrese el nombre del estudiante a buscar (deje vacío para mostrar todos): ")
    if nombre_buscar == "":
        for estudiante in estudiantes:
            print(f"DNI: {estudiante[0]}, Nombre: {estudiante[2]}, Email: {estudiante[3]}")
    else:
        resultados = [estudiante for estudiante in estudiantes if nombre_buscar.lower() in estudiante[2].lower()]
        if resultados:
            for estudiante in resultados:
                print(f"DNI: {estudiante[0]}, Nombre: {estudiante[2]}, Email: {estudiante[3]}")
        else:
            print("No se encontraron estudiantes con ese nombre.")"""

def login(estudiantes):
    dni = input("Ingresar DNI: ")
    clave = input("Ingresar clave: ")
    for estudiante in estudiantes:
        if estudiante[0] == dni and estudiante[1] == clave:
                print("\nIngreso exitoso!\n")
                print(f"Nombre: {estudiante[2]}")
                print(f"Email: {estudiante[3]}")
                print()
        else:
            print("Usuario o clave incorrectos")

#ORIGINAL
estudiantes = [] #En realidad, como la lista es global, no hace falta pasar argumentos ni parametros para trabajar con ella

"""estudiantes = [
    ["12345678", "Clave123", "Juan Pérez", "juan@example.com", "388-1234567"],
    ["87654321", "Prueba456", "María López", "maria@example.com", "388-9876543"]]"""
    
while True:
    print("\t**MENU**")
    print("1. Registrar estudiantes")
    print("2. Buscar estudiante")
    print("3. Login")
    print("4. Salir")
    opcion = input("Ingrese una opcion [1, 4]: ")
    
    if opcion == "1":
        registro(estudiantes)
    elif opcion == "2":
        buscar_estudiante(estudiantes)
    elif opcion == "3":
        login(estudiantes)
    elif opcion == "4":
        print("\nGracias por usar nuestro programa!")
        break