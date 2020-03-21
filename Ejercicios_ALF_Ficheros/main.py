'''
Created on 21 mar. 2020

@author: Raquel

EJERCICIOS - FICHEROS

'''
# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
# fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
# done n es el número introducido.

def pideNumero():
    n = int(input("Dame un número entero entre el 1 y el 10 : "))
    f = open("tabla-" + str(n) + ".txt", "a") #debe se (a) para añadir linea a liea el bucle y no se sobrescriba.

    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
        #puede hacerse todo en una sola línea       #la operación tb. Concatenada con STR
        
    f.close() #se cierra el archivo
    
    
### fin de la función

#arranco la función. Programa
pideNumero()

# Ejercicio 2
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt 
# con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre 
# por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os

def muestraTabla():
    
    while True: # este while hará que pida todo el tiempo un número hasta que el archivo SI SEA ENCONTRADO
        n = int(input("Dime qué tabla quieres que muestre 1 y el 10 : "))
        archivo = "tabla-" + str(n) + ".txt"  
        try:                        #intenta abrir el archivo para leer "r"
            archivo = open(archivo, 'r')
        except FileNotFoundError:  # si no encuentra el archivo indicado:
            print('No existe el fichero con la tabla del', n)
            
        else:
            print(archivo.read())  #si no da error, haz esto. Lee el archivo e imprime por consola
            break
    
### fin de la función

#arranco la función. Programa
muestraTabla()


# Ejercicio 3
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt 
# con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. 
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

import os

def muestraTabla():
    
    while True: # este while hará que pida todo el tiempo un número hasta que el archivo SI SEA ENCONTRADO
        n = int(input("Dime qué tabla quieres que muestre 1 y el 10 : "))
        m = int(input("Por qué multiplo? (del 1-10)"))
        archivo = "tabla-" + str(n) + ".txt"  
        try:                        #intenta abrir el archivo para leer "r"
            archivo = open(archivo, 'r')
        except FileNotFoundError:  # si no encuentra el archivo indicado:
            print('No existe el fichero con la tabla del', n)
            
        else:
            lineas =archivo.readlines()      # o convierto en una lista
            print(lineas[m-1])               # imprimo sólo el elemento de esa lista.
            break
### fin de la función

#arranco la función. Programa
muestraTabla()

# Ejercicio 4 #
# Escribir un programa que acceda a un fichero de internet mediante su url y
# muestre por pantalla el número de palabras que contiene.

from urllib import request

f = request.urlopen('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md')
f = f.read()
print(len(f.split()))

