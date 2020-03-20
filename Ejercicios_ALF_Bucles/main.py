'''
Created on 20 mar. 2020

@author: Raquel
'''
#1#Escribir un programa que pida al usuario una palabra y
#la muestre por pantalla 10 veces.

palabra = input("Escribe una palabra: ")
i = 0
 
while i < 10:
    print(palabra)
    i += 1
    
#for i in range(10):   #no sería necesario crear una variable i
#    print(palabra)    
    

 # 2 # Escribir un programa que pregunte al usuario su edad y muestre por 
 #pantalla todos los años que ha cumplido (desde 1 hasta su edad).
 
edad = int(input("Escribe tu edad: "))

for i in range(edad):
    print("Has cumplido", str(i+1), "años") # i+1 es para que el número de empiece sea 1 y no un 0
    
# 3 # Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese número 
# separados por comas.

numero = int(input("Indíque un número : "))
for i in range(1,numero+1,2):
     print( i, end= ", ") # al ponerlo así, con end ="", permite que todo salga en una sola línea

# (1 es el número por el que empieza el rango
# , numero +1 es el valor de entrada +1 para que pueda coger el siguiente impar, si lo hubiere

# done el 2) es los saltos que debe hacer. Desde el uno, sal saltar de dos en dos, coge los impares
 
 
## 4 //  Escribir un programa que pida al usuario un número entero positivo y muestre por
#  pantalla la cuenta atrás desde ese número hasta cero separados por comas.

n = int(input("Indíque un número entero positivo: "))
for i in range(n, -1, -1): #Hasta el valor -1 porque necesito coger el numero 0. Y saltar de -1 en -1.
    print( i , end= ", ") 
    
## 5 ## Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
# anual y el número de años, y muestre por pantalla el capital obtenido 
# en la inversión cada año que dura la inversión.

cantidad= int(input("¿Cuánto quiere invertir?"))
interes = int(input("¿A qué interés?"))
years = int(input("¿A cuántos años?"))

for i in range(years):
    cantidad *= 1 + interes / 100 
    print("Capital después de " + str(i+1) + " años: " + str(round(cantidad, 2)))

# i+1 para que empiece desde el 1, y no desde el cero.
# cantidad redondeada, a dos cifras.
   
 
# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla
# un triángulo rectángulo como el de más abajo, de altura el número introducido.

n = int(input("Indíque un número entero positivo: "))
for i in range(n+1):
        print("*" * i)
        
# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


for i in range(1, 11):
    for j in range(1, 11):
        print(i, " X ", j, " = ", i*j)
        

# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla
# un triángulo rectángulo como el de más abajo.

n = int(input("Indíque un número entero: "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#  pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

c = "contraseña"
valor = input("Dame una contraseña : ")

while c != valor:
    print(" Vuelve a intentarlo")
    valor = input("Dame una contraseña : ")
else:
    print("Perfecto, puedes seguir.")

# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla
#  si es un número primo o no.

n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0: # si el resto del valor i es cero, para prgrama
        break
if (i + 1)  == n: #si ese valor i, no ha dado par. (es decir el resto no es 0), si al sumarle uno da n.
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")
    
# Ejercicio 11
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
#  una a una las letras de la palabra introducida empezando por la última.

palabra = input("Escribe una palabra : ")

for i in range(len(palabra)-1,-1, -1): #cojo la longitud de la palabra y voy hasta el -1(a la inversa) de uno en uno
    print(palabra[i], end=" - ")
    
#como se puede tratar un string como un array, pido que me imprima, los valores de ese array.
#total de la long de la palabra -1, hasta el valor -1 (para que coja el 0)
#no olvidar que el array va del 0 en adelante. Si quiero por ejm, 4 letras será la 0,1,2,3.

# Ejercicio 12
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Escribe una frase : ")
letra = input("Escribe una letra: ")
l = 0
for i in frase.lower():
    if i == letra.lower():
        l += 1
print(" La letra ", letra, " aparece ", str(l), "veces.")

# Ejercicio 13
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta 
# que el usuario escriba “salir” que terminará.

valor = input(" Escribe algo y seré tu ECO, hasta que escribas SALIR")

while valor.lower() != "salir":
    print(valor)
    valor = input(" Vuelve a escribir! : ")
else:
    print("Saliste") 
