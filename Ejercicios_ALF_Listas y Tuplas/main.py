'''
Created on 20 mar. 2020

@author: Raquel
'''
# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
# Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = ["Matemáticas", "Física", "Química", "Historia","Lengua"]

print(asignaturas)

# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y 
# la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

asignaturas = ["Matemáticas", "Física", "Química", "Historia","Lengua"]

for i in asignaturas:
   print("Yo estudio:", i )
   
# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
#  pregunte al usuario la nota que ha sacado en cada asignatura, y después las 
#  muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde 
#  <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de
#   las correspondientes notas introducidas por el usuario.

asignaturas = ["Matemáticas", "Física", "Química", "Historia","Lengua"]
notas = []
for i in asignaturas:
    valor_nota = input("¿Qué nota has sacado en " + i + "?")
    notas.append(valor_nota) #¿cómo guardo cada nota? haciendo un ARRAY donde añado cada nota obtenida
for i in range(len(asignaturas)): #equivaldría a poner un 5, pero lo que hace es contar los elementos que contiene ASGINATURAS
    #es decir, que se va a repetir ese número de veces:
    print(" Has sacado " + notas[i] + " en " + asignaturas[i])
    #imprimiento por orden, cada nota y asignatura con su valor 
    

# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería 
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros = []

for i in range(6):
    valores = int(input("introduce el numero ganador: ")) #tengo que convertir a número para que sea capaz de ordenarlo
    numeros.append(valores)
    # numeros.append(int(input"introduce el numero ganador: "))  #podría sintetizarse en sólo esto
    
numeros.sort()
print(" Los números son : " + str(numeros) ) #tengo que pasarlo a STR para que sea capaz de imprimirlo

# # Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre 
# por pantalla en orden inverso separados por comas.


numeros = []

for i in range(1, 11): 
    numeros.append(i)
       
numeros.reverse()
print(numeros)

# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
# Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha
#  sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
#   Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene
#    que repetir.

asignaturas = ["Matemáticas", "Física", "Química", "Historia","Lengua"]
aprobadas= []
for a in asignaturas:
    valor_nota = float(input("¿Qué nota has sacado en " + a + "?"))
    if valor_nota >= 5: #sólo va a recoger las asignaturas aprobadas
        aprobadas.append(a) #las añade a la lista(ASIGNATURA). Es decir, no recoge los suspensos. 
for a in aprobadas: #por cada asignatura que hay en la lista APROBADAS
        asignaturas.remove(a) #vas a eliminar, el mismo valor exacto, de la otra lista.
        #es decir, lo elimina de la de ASIGNATURAS.
print("Tienes que recuperar : " + str(asignaturas)) #Muestra la lista inicial con los borrados.


# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista
# las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
# resultante.

abc =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for l in range(len(abc), 1 , -1 ): # en sentido inverso, desde el último al primero.
    #restando de una en una las letras
    if l % 3 == 0: #si el número de elemento, su resto es igual a 0
        abc.pop(l-1) #si cumple la condición, lo vas a eliminar. El num. de elemnto del array -1
print(abc)
#vuelve a mostrar la lista, ya con las eliminaciones realizadas

# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es
#  un palíndromo.

palabra = input("Introduce una palabra: ")
p_inversa = palabra

palabra= list(palabra)
p_inversa = list(p_inversa)
p_inversa.reverse() #una vez separada letra a letra. LAs coloca a la inversa
#ahora la variable p_inversa ha quedado con el valor invertido.
#hacemos la comprobación. Deberían coincidir como la palabra "ojo"
if palabra == p_inversa :
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    
# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el
# número de veces que contiene cada vocal.

vocales = ["a", "e","i","o","u"] #¿qué es lo que quiero comprobaR?
palabra = input("Introduce una palabra : ")


for vocal in vocales: #todo el proceso se repetirá 5 veces. (el mismo número de vocales)
    cuenta = 0          #establezco un contador a 0
    for letra in palabra:
        if letra == vocal: #cuando recorro una palabra letra a letra. Compruebo si es la vocal A, luego la E...
            cuenta += 1
    print("La vocal " + vocal + " aparece " + str(cuenta) + " veces") 
    #imprime primero el contador para la A
    # después el contador para la E...y así sucesivamente.

#ejercicio 10 #
# Escribir un programa que almacene en una lista los siguientes precios,
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [50,75,46,22,80,65,8]

precios.sort()

print("El menor número de la lista es : " + str(precios[0]))
m = len(precios)-1
print("El mayor de la lista es : " + str(precios[m]))


# Ejercicio 11 ## de este he copiado TO-DO
# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas/tuplas
# y muestre por pantalla su producto escalar.

a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))

# Ejercicio 12
#DE ESTE PASO TOTALMENTE PORQUE NO ENTIENDO LO QUE PIDE

# Ejercicio 13
# Escribir un programa que pregunte por una muestra de números, separados por comas, 
# los guarde en una lista y muestre por pantalla su media y desviación típica.



valores = input("Escribe varios números separados por comas:")
valores = valores.split(",") # split extrae de un string entero, los valores separados uno a uno como separador la coma
n = len(valores) # calculo la longitud de la variable valores. Es decir, la cantidad de números que el usuario ha introducido.

for i in range(n):                  #por cada uno de los valores, del total de la cantidad
    valores[i] = int(valores[i])    # voy a ir cogiendo cada valor y lo convierto a entero
    

valores = tuple(valores)            #lo convierto a tupla/array
suma = 0

for i in valores:
    suma += i


media = suma/n
print('La media es : ', media)





