'''
Created on 19 mar. 2020

@author: Raquel


'''
    #1# Escribir un programa que muestre por pantalla la cadena
print("Hola Mundo!")

#2# Escribir un programa que almacene la cadena ¡Hola Mundo! en
# una variable y luego muestre por pantalla el contenido de la variable.

saludo = "Hola Mundo!"
print(saludo)

#3# Escribir un programa que pregunte el nombre del usuario en la consola y
#después de que el usuario lo introduzca muestre por pantalla la cadena
#¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

 
nombre = input("Escribe tu nombre")
print("Hola " + str(nombre) + " !")

#4# Escribir un programa que pregunte el nombre del usuario en la consola y
#un número entero e imprima por pantalla en líneas distintas el nombre del
#usuario tantas veces como el número introducido.

nombre = input("¿Cuál es tu nombre?")
num = int(input("Dame un número"))
n=0
while n < num:
    print(nombre)
    n = n + 1

# 5 # Escribir un programa que pregunte el nombre del usuario en la consola y
# después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
# letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número
# de letras que tienen el nombre.

nombre = input("¿Cuál es tu nombre?")
n_letras = len(nombre)
print(nombre + " tiene " + str(n_letras) + " letras.")

# 6 # Escribir un programa que realice la siguiente operación aritmética  (3+22⋅5)2

print(((3+2)/(2*5))**2) # ** significa que es al cuadrado. Multiplica x2x2

# 7 # Escribir un programa que pregunte al usuario por el número de horas trabajadas
# y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = float(input("Cuántas horas trabajas al día?"))
coste = float(input("Cuánto te pagan la hora?"))
total = round((horas*30)*coste)
print(" Tu paga mensual es de " + str(total))

# 8# Escribir un programa que lea un entero positivo, 𝑛, introducido por el usuario
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta 𝑛.
#La suma de los 𝑛 primeros enteros positivos puede ser calculada de la siguiente forma:

num = int(input("Dame un número"))
resultado = (num*(num+1))/2
print("El resultado es " + str(resultado))

# 9 # Escribir un programa que pida al usuario su peso (en kg) y estatura
# (en metros), calcule el índice de masa corporal y lo almacene en una variable,
#  y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc>
#   es el índice de masa corporal calculado redondeado con dos decimales.

peso = input("¿cuánto pesas?")
estatura = input("¿cuánto mides?")
masa = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es : " + str(masa))

# 10 # Escribir un programa que pida al usuario dos números enteros y muestre por
# pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los
# números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la
# división entera respectivamente.
 
n = int(input("Introduce un dividendo : "))
m = int(input(" Introduce un divisor : "))
print(n + " / " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))


#11# Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital
#obtenido en la inversión.

cantidad = float(input("Cantidad a Invertir : "))
interes = float(input(" A qué interés : "))
years = int(input(" A qué años : "))
print(" El capital obtenido es : " + str(round(cantidad * (interes/100+1) ** years)))

# 12 # Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
#  y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


peso_payaso = 112
peso_mun =75
muniecas = int(input("¿cuántas muñecas en este pedido?"))
payasos = int(input("¿cuántos payasos en este pedido?"))
resultado = muniecas * peso_mun + payasos * peso_payaso
print(" El peso total del paquete es : " + str(resultado) )

# 13 # Imagina que acabas de abrir una nueva cuenta de ahorros que
# te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
#que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta 
#de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada
#en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
#Redondear cada cantidad a dos decimales.

cantidad = float(input("¿Qué importe vas a depositar?"))
interes = 4
years = 1
while years <= 3:
    resultado = round(cantidad *(interes/100+1)**years, 2)
    print(" La cantiadad obtenida en " + str(years) + " años, es de : " + str(resultado))
    years += 1


# 14 # Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día
#  tiene un descuento del 60%. Escribir un programa que comience leyendo el número 
#  de barras vendidas que no son del día. Después el programa debe mostrar el precio 
#  habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


precioPan = 3.49
dto = 60
cantidad = int(input("¿Cuántas barras no son del día?"))
resultado =  precioPan * cantidad * (1 - dto/100) # es lo mismo que decir 1 -0.6 (sería sobre el 100%)

print("El precio habitual de una barra de pan es de " + str(precioPan) + " euros. ")
print("Por no ser del día, tiene un " + str(dto) + "% de descuento")
print("El precio total de " + str(cantidad) + " barras es de " + str(round(resultado,2)) + " euros.")



