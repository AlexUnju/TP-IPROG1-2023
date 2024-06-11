#CASOS DE ESTUDIO
"""Analizar y ejecutar el programa adivina_numero que en menos de 7 intentos el usuario tiene que adivinar un
número generado al azar que se encuentra en el rango de 1 a 100"""
import random
i_max = 7
i = 0
guess = random.randint(1, 100)
print('Adivina el nro en [1, 100]')
while i < i_max:
    print(f'Tienes {i_max - i} intentos')
    nro = int(input('Ingresa número:'))
    i += 1
    if nro < guess:
        print('Demasiado pequeño')
    elif nro > guess:
        print('Demasiado grande')
    else: break
if nro == guess:
    print(f'Acertaste! en {i} intentos')
else:
    print(f'El número es {guess}')

#Raiz_manual
def f(x):
    return x**3 + 6*x**2 - x - 61.8

while True:
    x = float(input('Proponer x:'))
    error_absoluto = f(x)
    print(f'Error: {error_absoluto}')
    op = input('¿Más iteraciones?:')
    if op in ['n', 'N', 'no', 'No']:
        break
    print(f'Raíz aproximada: {x}')
    
#Raiz_automatica
def f(x):
    return x**3 + 6*x**2 - x - 61.8
a = int(input('Límite a: '))
b = int(input('Límite b: '))
err_p = float(input('Error %: '))
m = (a + b) / 2
while True:
    fa = f(a)
    fm = f(m)
    if fa*fm > 0:
        a = m
    else:
        b = m
    m1 = m
    m = (a + b) / 2
    m2 = m
    err_r = abs((m1-m2)/m1)*100
    if err_r < err_p:
        break
    print('Raíz aproximada:', m)
    print('f(x):', f(m))

#EJERCICIO 1    
"""Tres niños fueron a una fiesta de cumpleaños con disfraces de superhéroes

Los nombres de los tres niños son Juan, Pedro y Jorge.
Se disfrazaron de Spiderman, Iron Man y Batman. Los
niños tienen 6, 8 y 10 años.
No sabemos cómo se vistió cada niño o qué edad tiene
cada niño, pero tenemos las siguientes pistas:
● Jorge estaba disfrazado de Spiderman.
● Juan no estaba disfrazado de Batman.
● El niño más pequeño disfrazado de Spiderman.
● El niño de 8 años disfrazado de Batman"""

#Jorge estaba disfrazado de Spiderman (6 años)
#Pedro estaba disfrazado de Batman (8 años)
#Jorge estaba disfrazado de Iron Man (10 años)

#EJERCICIO 2
"""Resolver el siguiente ejercicio, debe formular una estrategia para organizar la información y encontrar todas
las relaciones (utilice papel, lápiz y goma de borrar):

Hay cinco casas están pintadas de un color diferente, y sus habitantes son de diferentes nacionalidades, tienen
diferentes mascotas, beben diferentes bebidas y fuman diferentes marcas de cigarrillos. Otra cosa: en el
enunciado 6, derecha significa tu derecha. — Life International, Diciembre 17, 1962

1. Hay cinco casas.
2. El inglés vive en la casa roja.
3. El español es dueño del perro.
4. El café se bebe en la casa verde.
5. El ucraniano bebe té.
6. La casa verde está inmediatamente a la derecha de la casa de color marfil.
7. El fumador de Old Gold tiene caracoles.
8. Los Kools se fuman en la casa amarilla.
9. La leche se bebe en la casa del medio.
10. El noruego vive en la primera casa.
11. El hombre que fuma Chesterfields vive en la casa de al lado del hombre con el zorro.
12. Los Kools se fuman en la casa contigua a la casa donde se guarda el caballo.
13. El fumador de Lucky Strike bebe jugo de naranja.
14. Los japoneses fuman Parliaments.
15. El noruego vive al lado de la casa azul.
¿Quién bebe agua? ¿Quién es el dueño de la cebra?"""




"""1. Hay cinco casas.
¿Quién bebe agua? ¿Quién es el dueño de la cebra?"""

"""Hacer un programa que calcule el promedio de los valores de las medidas de los aforos, tener en cuenta que el
vacío o null no cuenta para el cálculo. también debe mostrar los aforos con valor vacío"""

#EJERCICIO 3
def calcular_promedio(aforos):
    valores = []
    vacios = []
    
    for aforo, valor in aforos.items():
        if valor != 'vacio':
            valores.append(float(valor))
        else:
            vacios.append(aforo)
    
    if valores:
        promedio = sum(valores) / len(valores)
        print("Promedio de los valores de las medidas de los aforos:", promedio)
    else:
        print("No hay valores válidos para calcular el promedio.")
    
    if vacios:
        print("Aforos con valor vacío:", ", ".join(vacios))

aforos = {
    'aforo 1': '7.5',
    'aforo 2': '0.0',
    'aforo 3': 'vacio',
    'aforo 4': '8.2',
    'aforo 5': '6.9',
    'aforo 6': 'vacio',
    'aforo 7': '8.5'
}

calcular_promedio(aforos)

#EJERCICIO 4
"""Hacer un algoritmo para jugar al juego del NIM simplificado. El juego consiste en que sobre una mesa hay una
cantidad n de fósforos y dos jugadores en turnos alternados van quitando de 1, 2 o 3 a la vez. El objetivo para
ganar es que el jugador contrario tenga que levantar el último fósforo de la mesa"""

def jugar_nim():
    fosforos = int(input("Ingrese la cantidad inicial de fósforos en la mesa: "))
    jugador_actual = 1

    while fosforos > 0:
        print("Fósforos restantes en la mesa:", fosforos)
        
        max_fosforos = min(fosforos, 3) #La función min() toma dos valores como argumentos y devuelve el valor más pequeño de los dos.
        
        print("Turno del jugador", jugador_actual)
        cantidad = int(input("Ingrese la cantidad de fósforos a quitar (1-{}): ".format(max_fosforos)))

        while cantidad < 1 or cantidad > max_fosforos:
            print("Cantidad inválida. Intente nuevamente.")
            cantidad = int(input("Ingrese la cantidad de fósforos a quitar (1-{}): ".format(max_fosforos)))

        fosforos -= cantidad

        jugador_actual = 3 - jugador_actual  # Alternar entre jugador 1 y jugador 2

    jugador_ganador = 3 - jugador_actual
    print("El jugador", jugador_ganador, "ha ganado!")


#ORIGINAL
jugar_nim()

#EJERCICIO 5
"""En una pequeña aldea, cinco personas están sentadas en una fila. Cada una tiene una profesión diferente
(doctor, abogado, maestro, carnicero y panadero) y cada una tiene una mascota diferente (perro, gato, pájaro,
pez y conejo). También tienen diferentes pasatiempos (lectura, deportes, música, cine y jardinería) y
diferentes deportes favoritos (fútbol, baloncesto, tenis, béisbol y natación).
Se sabe lo siguiente:

● La persona del extremo izquierdo de la fila es el carnicero y tiene un gato.
● El abogado tiene un perro.
#● Al maestro le gusta leer y su deporte favorito es el béisbol.
● La persona que tiene un pájaro está sentada al lado de la persona que le gusta la música.
● La persona del extremo derecho de la fila es el panadero y su deporte favorito es la natación.
#● La persona que le gusta el cine está sentada al lado de la persona que tiene un conejo.
● La persona que tiene un pez está sentada en el medio.
¿Qué profesión tiene la persona que le gusta la jardinería"""

#EJERCICIO 6
"""Seis amigos (Alejandro, Bárbara, Carlos, Daniela, Esteban y Fernanda) están sentados alrededor de una mesa
redonda para jugar un juego de cartas. Cada uno de ellos tiene una carta con un número del 1 al 6 en la mano,
pero no pueden ver su propia carta. Los jugadores deben adivinar el número de su propia carta mirando las
cartas de los demás. Si adivinan correctamente, ganan $10 cada uno. Si adivinan incorrectamente, pierden $5
cada uno. ¿Cuál es la estrategia más inteligente que pueden utilizar los jugadores para maximizar sus
ganancias y minimizar sus pérdidas?"""
