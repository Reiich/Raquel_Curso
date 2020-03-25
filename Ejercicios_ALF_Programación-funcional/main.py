'''
Created on 25 mar. 2020

@author: Raquel
'''

# Ejercicio 1
# Escribir una función que aplique un descuento a un precio y otra que aplique el
#  IVA a un precio.
# Escribir una tercera función que reciba un diccionario con los
#  precios y porcentajes de una cesta de la compra, y una de las funciones anteriores,
#  y utilice la función pasada para aplicar los descuentos o el IVA a los productos
#  de la cesta y devolver el precio final de la cesta.



def descuento(precio, des):
    precio = precio - precio * des/100 #se resta porque es decuento
    return precio

def iva(precio, des=0.21):
    precio = precio + precio * 0.21
    return precio

def listaCompra(cesta, funcion): 
    total= 0 
    for precio,des in cesta.items():
        total += funcion(precio,des) #aplica la funcion solicitada cogiendo precio y descuento del dicc.cesta. ÑADE CUANDO YA SE OBTIENE EL PRECIO DEFINITIVO
    return total
        
cesta= {8:10, 8:10}
print(descuento(8, 10))
print(iva(2))
###ESTO ULTIMO NO FUNCIONA################################
print('El precio de la compra tras aplicar los descuentos es: ', listaCompra(cesta, descuento))
print('El precio de la compra tras aplicar el IVA es: ', listaCompra({2:0.21, 2:0.21 }, iva))


# Ejercicio 2
# Escribir una función que simule una calculadora científica que permita calcular 
# el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará
#  al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con 
#  los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.

from math import sin, cos, tan, exp, log  #importo el biblioteca math

def aplicar_funcion(f, n):
    '''
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        f: Es una función que recibe un número real y devuelve otro.
        n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    '''
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log} #realizo un diccionario con las 4 operaciones. key y su value (método)
    result = {}  #los resultados los acumulo en otro diccionario
    for i in range(1, n+1):
        result[i] = functions[f](i)  #cada resultado será la funcion escogida por el usuario operando con 1,2,3...hasta el número n+1
    return result

def calculator():
    '''
    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logarítmo)
     a la lista de enteros desde 1 hasta n. 
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
    Parámetros:
        f: Es una cadena con la función a aplicar (sin, cos, tan, exp o log).
        n: Es un entero positivo.
    '''
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in aplicar_funcion(f, n).items():
        print (i, '\t', j)
    return

calculator()

# Ejercicio 3
# Escribir que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.



def conteo():
    dicc = {}
    frase = input("Escribe una frase : ")
    trozo = frase.split()
    for i in trozo:
        dicc[i] = len(i)
        #print("La palabra ", i , " cotiene " ,len(i), " letras .")
    print(dicc)
conteo()
        
#opción mas sencilla
def conteo2(frase):
    return {word:len(word) for word in frase.split()} #hago return del bucle. toodo en una sola linea
print(conteo2('Welcome to Python')) #imprimo la función son su parámentro.

# Ejercicio 4
# Escribir una función reciba una lista de notas y devuelva la lista de
# calificaciones correspondientes a esas notas.


def puntuacion(nota):  #puntiación será la traducción de la puntuación saca a una palabra calificatoria
    if nota < 5:
        return "Suspenso"
    if nota < 6:
        return "Suficiente"
    if nota < 8:
        return "Bien"
    if nota < 9:
        return "Notable"
    if nota < 10:
        return "Sobresaliente"
    if nota == 10:
        return "Perfecto"
    
def calificaciones(notas): # aquí notas, es el listado de puntuaciones numéricas
    for i in notas:
        print(puntuacion(i))
    
notas = [4.3, 5, 5.5, 6, 7.8, 8, 8.7, 9, 9.5, 10]
calificaciones(notas)       
    
    
# Ejercicio 5
# Escribir una función reciba un diccionario con las asignaturas y las notas de
# un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las
# calificaciones correspondientes a las notas.


def puntuacion(nota):  #puntiación será la traducción de la puntuación saca a una palabra calificatoria
    if nota < 5:
        return "Suspenso"
    if nota < 6:
        return "Suficiente"
    if nota < 8:
        return "Bien"
    if nota < 9:
        return "Notable"
    if nota < 10:
        return "Sobresaliente"
    if nota == 10:
        return "Perfecto"
    

asig = { "Mates": 5, "lengua" : 6, "Plastica": 9.3}

def mostrar(asig):
    calif = {}
    for a,n in asig.items():
        a = a.upper()
        n = puntuacion(n)
        calif[a] = n
    print(calif)
    
#ejecuUTO
mostrar(asig)

# Ejercicio 6

# LO MISMO DE ANTES PERO SOLO LAS APROBADAS

def puntuacion(nota):  #puntiación será la traducción de la puntuación saca a una palabra calificatoria
    if nota < 5:
        return "Suspenso"
    if nota < 6:
        return "Suficiente"
    if nota < 8:
        return "Bien"
    if nota < 9:
        return "Notable"
    if nota < 10:
        return "Sobresaliente"
    if nota == 10:
        return "Perfecto"
    

asig = { "Mates": 5, "lengua" : 4.6, "Plastica": 9.3, "Quimica" : 3}

def mostrar(asig):
    calif = {}
    for a,n in asig.items():
        if n >= 5:
            calif[a] = n
    print(calif)
    
mostrar(asig)

# Ejercicio 7
# Escribir una función reciba dos tuplas y devuelva su producto escalar.

def module(v):
    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''
    return sum([x ** 2 for x in v]) ** 0.5

print(module((3, 4)))
print(module((1, 2, 3)))
