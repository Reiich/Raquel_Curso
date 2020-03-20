'''
Aprende con ALF Condicionales
@author: Raquel
'''
#1|# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("¿Cuál es tu edad?"))
if edad >=18:
    print("Perfecto! Eres adulto y aquí hay cosas muuuuuy negras")
else:
    print("Cuando seas padre comerás huevos...")


# 2 # Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#  pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
#  por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = "Petardo"
input = input("¿Cuál es tu contraseña?")

if password.lower() == input.lower():
    print("La contraseña introducida es Correcta.")
else:
    print("La contraseña no coincide.")

# 3 # Escribir un programa que pida al usuario dos números y muestre por pantalla
#su división. Si el divisor es cero el programa debe mostrar un error.

n1 = input("Introduzca el dividendo: ")
n2 = input("Introduzca el divisor: ")
if n2 == 0:
    print(" EL divisor no puede ser cero. ")
else:
    print(n1/n2)

# 4 # Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Dame un número entero : "))

if numero%2 == 0:   # % sirve para calcular el resto. Si es par, el resto es 0 porque no hay decimales
    print("EL número es par.")
else:
    print("El número es impar.")


# 5 # Para tributar un determinado impuesto se debe ser mayor de 16 años y tener
#unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que
#pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el
#usuario tiene que tributar o no.

edad = int(input("Dime tu edad : "))
ingreso = float(input("¿Cuánto ganas al mes?"))
print(" ¿ Debo tributar ? ")
if edad >= 18 and ingreso >= 1000:
    print("Debe usted tributar como el 90 % de españolitos")
else:
    print("Te perdonamos. Y si eres asquerosamente rico, también.")


# 6 # Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
# sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior
#  a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
#  Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
#   pantalla el grupo que le corresponde.

sexo = input(" Si eres hombre pon H y si eres mujer M ")
nombre= input("¿Cuál es tu nombre?")

if nombre.lower() < "m":
    if sexo == "M":
        print("Estás en el grupo A, de atontao!")
    else:
        print("Estás en el grupo B, de bobo! ")
else:
    if nombre.lower() > "n":
        print("Estás en el grupo A, de atontao!")
    else:
        print("Estás en el grupo B.")

#otra opción al ejercicio 6 es:
 
# if (sexo == "M" and name.lower() < 'm') or (sexo == "H" and name.lower() > 'n'):
#     group = "A"
# else:
#     group = "B"
# print("Tu grupo es " + group)


# 7 # Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

renta = float(input("¿cuál es tu renta anual?"))

if renta < 10000:
    tasa = "5%"
elif renta < 20000: #¿es menor de
    tasa = "15%"
elif renta < 35000:
    tasa = "20%" #la variable que recoja, como sólo habrá pasado por esta condición. Es la que imprimirá
elif renta < 60000:
    tasa = "30%"
else:
    tasa = "45%"

print(" Te corresponde abonar un " + tasa + " de tipo impositivo")

# 8 # En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
#traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
#pueden ser 0.0, 0.4, 0.6 o más, pero NO valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
# La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# 
bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación: "))

# Clasifiación por niveles de rendimiento
if puntos == inaceptable:
    nivel = "Inaceptable"
elif puntos == aceptable:
    nivel = "Aceptable"
elif puntos >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""

# Mostrar nivel de rendimiento
# if nivel == "":
#     print("Esta puntuación no es válida")
# else:
#     print("Tu nivel de rendimiento es : " + nivel)
#     print("Te corresponde cobrar : " + str((puntos * bonificacion)))
 
# estas dos ultimas lineas también pueden ser:
#  print("Tu nivel de rendimiento es %s" % nivel)
#   print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))


# 9 #Escribir un programa para una empresa que tiene salas de juegos para todas 
# las edades y quiere calcular de forma automática el precio que debe cobrar a sus 
# clientes por entrar. El programa debe preguntar al usuario la edad del cliente y 
# mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
# si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("¿cuál es tu edad?"))
# 
if edad < 4:
    precio = "GRATIS"
elif edad < 18:
    precio = "5 euros"
else:
    precio = "10 euros"
 
 
print(" Su entrada tiene un precio de ", precio, " Disfrute de su visita!")

# 10 # Escribir un programa que pregunte al usuario si quiere una pizza vegetariana
#  o no, y en función de su respuesta le muestre un menú con los ingredientes 
#  disponibles para que elija. Solo se puede eligir un ingrediente además de la 
#  mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por 
#  pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


respuesta = input("¿Quiere pizza Vegetariana? Escriba: SI o NO")

if respuesta.lower() == "si":
    ingrediente = input("¿La quiere con Pimiento o Tofu?")
    tipo = "Vegetariana"
else:
    ingrediente = input("¿La quiere con Peperoni, Jamón o Salmón.")
    tipo = "Carnívora"
    
    
print(" Ha elegido pizza ",tipo)  
print("Su pizza llevará tomate, mozzarella y", ingrediente)



