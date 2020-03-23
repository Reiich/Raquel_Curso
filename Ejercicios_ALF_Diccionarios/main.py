'''
Created on 23 mar. 2020

@author: Raquel
'''
# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre 
# su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

#diccionario DIVISA
divisa = {'Euro':'€', 
          'Dollar':'$', 
          'Yen':'¥'}

consulta = input("Dime qué divisa desea consultar: ")
print(divisa.get(consulta.title(), "La divisa no está.")) #get devuelve el valor dado (variable Consulta), ó si no lo encuentra
                                    # devuelve la frase indicada. No está esta divisa.

# gracias a añadir ese .title(), no distinque el diccionario entre caracteres en Mayus o Minusc.


# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#  y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje

nombre = input("Dime tu nombre : ")
edad = input("Dime tu edad : ")
direc = input("Dime tu dirección : ")
telf = input("Dime tu teléfono : ")

dicc = {
    "Nombre" : nombre,
    "Edad" : edad,
    "Dirección" : direc,
    "Teléfono" : telf
    }


print(dicc["Nombre"],"tiene", dicc["Edad"], "años, vive en ", dicc["Dirección"],
       "y su número de teléfono es ", dicc["Teléfono"])



# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
#  ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar
#   un mensaje informando de ello.

#RECUERTA QUE EN EL DICCIONARIO PUEDES PONER Tipos de dato STRING - INT -FLOAT. 
frutas = {
    "platano" : 1.35,
    "manzana" : 0.80,
    "pera" : 0.85,
    "naranja" : 0.70,    
    }

fruta = input("¿Qué fruta quiere?").lower()
kilos = float(input("¿cuántos kilos de " + fruta + " quiere?"))

if fruta in frutas:
    print(kilos, 'kilos de', fruta, 'valen', frutas[fruta]*kilos, ' EUROS.') # saca el value,valor,  frutas[fruta]
else:                                                       # y lo multiplica por los kilos
    print(fruta, " no está disponible.")

# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
#  pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

from datetime import datetime

def fechaActual(date):
    meses = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dia = date.day     #extrae el día
    mes = meses[date.month - 1]   #extrae el mes, que es un número. Al que le resta uno y le da el valor en el ARRAY (meses)
    year = date.year   #extrae el año
    mensaje = "{} de {} del {}".format(dia, mes, year)   #es un string, cuyo formato es las variable, dia,mes,year
    return mensaje  #lo que se devuelve cuando la función fechaActual, es llamada

ahora = datetime.now()   #pido al sistema que me devuelva la fecha ACTUAL
print(fechaActual(ahora))


# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas 
# de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por
#  pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos>
#   créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> 
#   son sus créditos. Al final debe mostrar también el número total de créditos del curso.


creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5} 
total_creditos = 0

for a, c in creditos.items():
    print( " La asignatura {} tiene {} créditos".format(a, c) )
    total_creditos += c
    
print("EL número total de créditos es: " + str(total_creditos))

# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información 
# sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
#  que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

persona = {}

nombre = input("Dime tu nombre: ")
persona["Nombre"] = nombre
print(persona.items())

edad = input("Dime tu edad: ")
persona["Edad"] = edad
print(persona.items())

sexo = input("Dime tu sexo, M o F: ")
persona["Sexo"] = sexo
print(persona.items())

phone = input("Dime tu teléfono: ")
persona["Teléfono"] = phone
print(persona.items())

# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
#  hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista
#   de la compra y el coste total, con el siguiente formato


cesta = {}
iniciar = True
total_compra = 0 


while iniciar == True:
    articulo = input("¿qué producto añades a la cesta?")
    precio = float(input("¿qué precio tiene?"))
    cesta[articulo] = precio   #se añade en pares de esta manera TAN SIMPLE.
    total_compra += precio
    continuar = input("¿quiere añadir más productos? SI o NO.").upper()
    if continuar == "NO" or continuar == "N":
        print("Lista compra")
        print("_____________________________")
        print("")
        for articulo, precio in cesta.items():
            print(articulo, '\t', precio)
        print("El total a abonar es : " + str(total_compra))
        iniciar = False

# Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés.
#  El usuario introducirá las palabras en español e inglés separadas por dos puntos,
#   y cada par <palabra>:<traducción> separados por comas. El programa debe crear un 
#   diccionario con las palabras y sus traducciones. Después pedirá una frase en
#    español y utilizará el diccionario para traducirla palabra a palabra. Si una 
#    palabra no está en el diccionario debe dejarla sin traducir.
        
traductor = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas cada par: ")

for par in palabras.split(','):   #primero creo el traductor, separando cada par,cuando encuentre (,)
    key, value = par.split(':')   # segundo: separando la key y su value por los (:)  # he creado dos variables a la vez
    traductor[key] = value          # añado al diccionario "traductor" la key y su correspondiente value.

frase = input('Introduce una frase en español: ')

for par in frase.split():    #por cada palabra separada de espacios ()
    if par in traductor:     # busca cada palabra , si se encuentra en el diccionario "llamado traductor)
        print(traductor[par], end=' ')    #imprime el valor correspondiente.
    else:
        print(par, end=' ') # la imprime como viene dada, sin traducir, la deja en español
        

# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
# el número de factura y el valor el coste de la factura. El programa debe preguntar 
# al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste
#  y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número
#   de factura y se eliminará del diccionario. Después de cada operación el programa debe
#    mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


facturas = {}
pagado = 0
adeber = 0
continuar = "SI"


while continuar != "T":  # MIENTRAS QUE SEA DISTINTO DE T. REPETIRÁ LA OPCION A O LA P.
    if continuar == "A":
        numero = input("¿qué número de factura?")
        coste = float(input("¿De cuánto importe?"))
        facturas[numero] = coste
        print("Facturas pendientes de cobro:")
        print(facturas)
        adeber += coste

        
    if continuar == "P":
        numero = input("Diga el número de factura:")
        coste = facturas.pop(numero, 0)  #elimina el coste que tenga de la factura y la variable coste. pasa a operar.
        pagado += coste
        adeber -= coste  
    #una vez realizada la opc SI o la opc NO...sigue el programa con lo siguiente
        
    print("Pagado : " + str(pagado))
    print("Pendiente de pago : " + str (adeber))
    continuar = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ').upper()
    if continuar == "T":
        print("Hasta la próxima")
