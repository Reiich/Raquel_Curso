# Ejercicio 2
# Escribe un programa que te permita jugar a una versión simplificada del juego
# Master Mind. El juego consistirá en adivinar una cadena de números distintos.
# Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras).
# Después el programa debe ir pidiendo que intentes adivinar la cadena de números.
#  En cada intento, el programa informará de cuántos números han sido acertados
#  (el programa considerará que se ha acertado un número si coincide el valor y la posición).

from random import randrange
import random

def jugar():
    len = int(input("Dime una longitud de cadena de numeros entre 2 y 9 cifras:"))
    probarN = input("Prueba con una cifra : ")
    aleatorio = crearAleatorio(len) # creo una VAR llamada aleatorio que ejecuta la funcion crear aleatorio
    print("prueba trampa " + aleatorio)
    
    while probarN != aleatorio:  #es decir, que no lo adivine COMPLETAMENTE EL NÚM. ALEATORIO
        eval = evaluar(len, aleatorio, probarN) # creo otra variable total, que llama a la función evaluar
        print("Con el número " + probarN + " has tenido " + str(eval) + " aciertos.")
        probarN = input("Intenta adivinar la cadena, dame otro número :")
    print("FELICIDADES, HAS GANADO!")
        
    

def crearAleatorio(cad):
    n_aleat = '' #numero aleatroio debe ser un string para poder concaternar el n1 que resulta. Valor nulo ahora mismo
    for i in range(cad):
        x= random.randint(0,9) #tiene que ser string , me devuelve un número entre 0 y 9. Por cada una de las veces que se indica en len
        x = str(x)
        n_aleat += x
    return n_aleat

 
def evaluar(cad, aleatorio, probarN): # creo esta función para que diga si el string (numero) puesto, tiene algun acierto o no
    cont = 0
    a = 0   #empieza desde el cero comprobando si a = b
    b = 0
    for i in range(cad):  # va a realizar las comprobaciones hasta alcanzar el rengo dado por len
        if aleatorio[a] == probarN[b]:
            cont += 1  #contea el número de veces que sí coinciden los números
            a += 1  #va avanzando de posición en la comprobación
            b += 1 #cambia el valor de aleatorio[A] y b. de uno en uno.
        else:  #si no adivina no contea, si no que avanza al siguiente item de la comparación
            a += 1
            b += 1
    return cont    
    #una vez que ya ha realizado el bucle FOR, el numero de veces de la longitud de cadena. Devuelve el cont. (contador)
# fin de funciones


#arranco juego
jugar()

