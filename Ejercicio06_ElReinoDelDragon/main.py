'''
El Reino del Dragon
'''

#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Reino del Dragon....
import random
import time

def introduccion():
    print ("Estamos en una tierra llena de dragones. Delante nuestro,")
    print ("se ven dos cuevas. En una cueva, el dragón es amigable")
    print ("y compartirá el tesoro contigo. El otro dragón")
    print ("es codicioso y hambriento, y te va a comer nada más que te vea.")
    print ("...")

def CambiarCueva():
    cueva = "" #la variable cuaeva, en principio es una cadena vacia.
    while cueva != "1" and cueva != "2":
        cueva = input("¿A qué cueva quieres entrar? 1 o 2?") # Permite que el usuario ingrese un valro
        print("...que la fuerza te acompañe...")
    return cueva  #return, solo aparece cuando definimos Funciones. Lo que hace es
    #lleva el valor obtenido a la variable "cueva"

def cheqcueva(CambiarCueva): # Los nombres de las variables que están dentro de los paréntesis son llamadas parámetros. 
                                # cambiarCueva, ya le está dando a cheqCueva el número a comprobar. ( que habrá obtenido con RETURN)
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)                        # 2 son los segundos que el programa "duerme" para ejecutar la siguiente instrucción
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("...")
    time.sleep(2)
    # No va a ser siempre la cueva 1 la buena y la dos la mala.
    friendlyCueva = random.randint (1, 2)      #randint, devuelve enteros.
    #por eso, daremos a la var Friendly (la buena) un valor aleatorio cada vez,
    #entre el 1 y el 2 (ya que es el nº de opciones que tiene el usuario)
   
    global puntos
   
    if CambiarCueva == str(friendlyCueva): #comparamos si el valor elegirdo coincida que la Cueva Buena.
        print ("Te entrega el tesoro...")
        puntos += 100
    else:                #si no es asi, por tanto, el jugador entró en la mala.
        print ("El dragon te come de un bocado....")
        print ("Tus puntos totales han sido: " + str(puntos))
        
#### fin de las funciones


#comienza el JUEGO.   
   
EmpezarNuevo = ("si")  # daremos un valor ya definido como "si" a empezar el juego.
                        # para que comience. Sería equivalente a un True
puntos = 0

while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):   #incluye la posibilidad de que el usuario escriba tan solo una "s"
    # lo siguiente lo hará de manera automática.
    introduccion()                      #presenta la introducción. Llamando a la función.
   
    NumCueva = CambiarCueva()         # da un valor a la VAR NumCueva mediante la función CambiarCueva()
   
    cheqcueva(NumCueva)                 #ejecutará la función cheqCueva con el parámetro de NumCueva
   
    EmpezarNuevo = input("Quieres jugar de nuevo? (si o no)")
    #Por último vuelve a preguntar, si quiere jugar otra vez o salir.
else:
    (" Espero te hayas divertido . ")