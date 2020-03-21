
import os
from urllib import request

    # cómo crear un fichero

    #creo una variable para indicar que hay que abrir el archivo

f = open("texto.txt", "w") #la W significa que sólo permite leerlo al usuario.

    #si el fichero indicado, no existiera, se crearía nuevo desde aquí.
    #si el fichero ya existiera, se sobrescribiría el anterior
    
    #para escribir datos en un fichero hay que escribir

f.write("he machacado lo que había escrito?") #escribiría ésto en el archivo texto.txt. 
    # ojo! Sobrescribe lo que hubiera.


######### AÑADIR DATOS #################

    # Si en lugar de crear un fichero nuevo queremos añadir datos a un fichero existente 
    # se debe utilizar la instrucción

    #Abre el fichero con la ruta en modo añadir 
    
f = open("texto.txt", "a")  
    # la (a) significa append. Por lo tanto, no sobrescribe, si no que AÑADE A LO QUE HUBIERE
    
f.write("\n Vamos a añadir esta frase")    
f.write("\nDe momento todo está funcionando")    


######### leer DATOS de un fichero ################# 

    # leer datos supone que lo que haya escrito en el ficheto, lo va a emplear nuestro
    #programa para hacer algo  
    
f = open("texto.txt", "r")
    # donde (r) es el modo de lectura. READ
    # una vez abierto el archivo puede leerse por COMPLETO o también, LINEA a LINEA
    
print(f.read())
     #  Devuelve todos los datos contenidos en F como una cadena de caracteres.
     
lineas = f.readlines()
print(lineas)
    # readlines() devuelve linea a linea, convirtiéndolo, además, en una lista de elemntos
print(lineas[1]) #Como puede ver, lo trata como una lista
    
######### Cerrar un fichero #################  

   #es importante cerrar SIEMPRE un fichero después de usarlo. sobre todo si se abre 
   #en modo escritura, ya que mientras está abierto en este modo no se puede abrir
   #por otra aplicación. Si no se cierra explícitamente un fichero, Python intentará
   # cerrarlo cuando estime que ya no se va a usar más.
f.close()
  
  
######### Renombrado y borrado de un fichero #################   
    # lo primero es hace en el programa un IMPORT os
    # Para renombrar o borrar un fichero se utilizan funciones del módulo (os)
 


os.rename("texto.txt", "renombrado.txt") 
    # Renombra y mueve el fichero. El lugar 1, es el original. El lugar 2 , es el nombre nuevo.

os.remove("renombrado.txt")
    # Borra el fichero de la ruta
    
    # Antes de borrar o renombra un directorio conviene comprobar que existe para 
    # que no se produzca un error. Para ello se utiliza la función isfile.
    # puedo comprobarlo con un condicional
    
# if os.path.isfile("renombre.txt"):
#     print("Existe!")
# else:
#     print("El archivo no se encuentra")
    
print(os.path.isfile("renombre.txt")) #puedo probarlo con un print. De esta manera
    # devuelve TRUE si existe. En caso contrario devuelve FALSE


######### Creación, cambio y eliminación de directorios(CARPETAS) ################# 

    # Para trabajar con directorios también se utilizan funciones del módulo os.

os.mkdir("carpeta_nueva") # MK Crea un nuevo directorio en la ruta ruta.

os.chdir("carpeta_nueva") # CH (change)Cambia el directorio actual al indicado por la ruta .

print(os.getcwd()) # Devuelve una cadena con la ruta del directorio actual.

os.rmdir("carpeta_nueva") # RM (remove)  Borra el directorio de la ruta, siempre y cuando esté vacío.     


######### Leer un fichero de internet ################# 

    # Para leer un fichero de internet hay que utilizar la función urlopen 
    # del módulo urllib.request (Es decir, hay que hacer otro IMPORT)
    # escribiendo: from urllib import request


    # primero indico la URL
f = request.urlopen('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md')
    #segundo, creo una variable que mande leer la variable anterior F
datos = f.read()
    # la muestro por consola, admeás, codificada a utf-8 universal.
    # UTF -8 evita también que muestre códigos de la web. SUPER ACONSEJABLE
print(datos.decode('utf-8'))









    