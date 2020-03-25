'''
Created on 25 mar. 2020

@author: Raquel
'''
# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

def saludo():
    print("Hola AMIGA!")
    
saludo()

# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

def saluda(nombre):
    print("HOOOOOLA " + nombre)
    
nombre = input("¿Cuál es tu nombre?")
saluda(nombre)

#saluda("Raquel")


# 3
#Escribir una función que reciba un número entero positivo y devuelva su factorial.
# 

def factorial(n):
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp #lo que devuelve es la operación 

print(factorial(4))
print(factorial(20))

# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA.
#  La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
#   y devolver el total de la factura. Si se invoca la función sin pasarle el 
#   porcentaje de IVA, deberá aplicar un 21%.

def calcula_iva(c,i=21):  # con i=21, le estoy dando un valor de entrada si no viene ya dado. Será el usado por defecto
    total = c + c * i/100   # sumo a c (cantidad) el resultado el iva correspondiente. PAra obtener el total definitivo.
    return total

print("El total de la factura con el iva incluido es :")
print(calcula_iva(1000, 10))
print(calcula_iva(100))


# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el 
# volumen de un cilindro usando la primera función.    

def circle_area(radius):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius. 
    """
    pi = 3.1415
    return 2*pi*radius**2

def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high

print(cilinder_volume(3,5))

'''
Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva su media.

'''
def media(listanum):                #listanum será una lista de varios números
    return sum(listanum)/len(listanum) #sum es un método ya existente que aplicará a cada número de la lista
                        # se dividirá entra la longitud de esa misma lista. Cantidad de valores

print(media([1, 2, 3, 4, 5]))
#doy los número en una sola lista, separada por comas

# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.



def cuadrado(numeros):
    lista = []
    for i in numeros:
        lista.append(i**2) #lo va a meter en la lista, pero ya el resultado tras **2
    return lista

print(cuadrado([1, 2, 3, 4, 5]))
print(cuadrado([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva 
# un diccionario con su media, varianza y desviación típica.

def cuadrado(*numero):
     # necesito calcula el cuadrado para poder realizar mas tarde la varianza
    list = []
    for i in numero:
        list.append(i**2)
    return list

def operar(*numero):
    #numero: Es una secuencia de números separados por comas.
    
    #Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    dicc = {}
    dicc['media'] = sum(numero)/len(numero)
    dicc['varianza'] = sum(cuadrado(*numero))/len(numero)-dicc['media']**2
    dicc['desviacion tipica'] = dicc['varianza']**0.5
    return dicc

print(operar(1, 2, 3, 4, 5))
print(operar(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))




# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números 
# y otra que calcule el mínimo común múltiplo.


def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))


# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.


def a_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def a_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a 'n'.
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(a_decimal('10110'))
print(a_binary(22))
print(a_decimal(a_binary(22)))
print(a_binary(a_decimal('10110')))


# Ejercicio 11
# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
# con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
# diccionario generado con la función anterior y devuelva una tupla con la palabra 
# más repetida y su frecuencia.


def count_words(text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    text = text.split()    # en la frase de entrada como parámetro. Va a separar palabra a palabra por espacios
    words = {}             # crea un diccionario vacío
    for i in text:         #por cada palabra que haya en el texto (se ha convertido en lista al realizar split()
        if i in words:
            words[i] += 1     #suma 1 si la palabra se encunetra en el txto. Nunca estará en el dicc, una palabra q sólo aparece una vez
        else:
            words[i] = 1    #si no está. esa palabra valdrá 1 equivale a 'lapalabra' = 1. Porque sólo aparece una vez.
    return words            #devuelve el diccionario



def most_repeated(words):
    max_word = ''  #STRING VACÍO. key 'word'
    max_freq = 0   #INT A CERO   value ' freq'
    for word, freq in words.items():  # por cada key,value en los ítems del diccionario
        if freq > max_freq:  #frecuencia (q es un numero) es mayor que el que ya sea maximos. SI fuera menor, no haría nada.
            max_word = word
            max_freq = freq  #sólo añade si la frecuencia comprobada es MAYOR DE LA QUE YA HUBIERA.
    return max_word, max_freq  #DEVUELVE LA PALABRA QUE MAS se ha repetido. con su número de repeticiones.

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))

print(most_repeated(count_words(text))) 
#realiza la función most_repeated, dandole el diccionario words de la misma frase usarda antes