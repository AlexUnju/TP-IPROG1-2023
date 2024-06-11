#CASOS DE ESTUDIO

"""Diseñe la función recursiva pertenece(elem, lista) que retorne True si elem está en la lista y False en caso
contrario. Se propone el siguiente análisis:

Caso base: Si la lista está vacía, entonces retorna False
Recursión: Si elem es el elemento que está al principio de lista entonces retorna True, en caso contrario
retorna pertenece(elem, lista[1:]) sin el primer elemento"""

def pertenece(elem, lista):
    if not lista:
        return False
    elif elem == lista[0]:
        return True
    else:
        return pertenece(elem, lista[1:]) #El ultimo en entrar es el primero en salir

lista = [1, 2, 3, 4, 5]
print(pertenece(6, lista))
print(pertenece(5, lista))

""" Diseñe la función recursiva potencia(b, n) donde b es la base y n es el exponente de la potencia bn. Se propone el siguiente análisis,
utilizando las propiedades de las potencias de igual base:

Caso base: retorna 1 si el exponente n es igual a 0 | PORQUE CUALQUIER NUMERO ELEVADO A LA 0 DA COMO RESULTADO 1

Recursión: retorna b**(n/2) * b**(n/2) si el exponente n es par, o sino
retorna b**(n-1)/2 * b**(n-1)/2 * b si el exponente n es impar

Nota: Debe utilizar una variable auxiliar, para el cálculo y retorno de la potencia, y hacer uso de la propiedad
de las potencias de igual base, que es una de las ventajas principales de esta implementación. Se aprovecha el
resultado calculado en lugar de tener que calcularlo dos veces, entonces la solución recursiva será más
eficiente que la solución iterativa ¿Puede ud. comprobarlo"""

def potencia(b, n):
    if n == 0:  #Caso base: exponente igual a 0
        return 1
    elif n % 2 == 0:  #Caso recursivo: exponente par
        aux = potencia(b, n // 2)  #Cálculo recursivo de b**(n/2)
        return aux * aux
    else:  # Caso recursivo: exponente impar
        aux = potencia(b, (n - 1) // 2)  #Cálculo recursivo de b**((n-1)/2)
        return aux * aux * b

#Ejemplo de uso
print(potencia(2, 4))  # 8
#print(potencia(5, 2))  # 25

