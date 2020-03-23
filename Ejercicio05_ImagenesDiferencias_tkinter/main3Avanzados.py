'''
+ Felicitar al usuario cuando haya adivinado las 3 diferencias. Indicarle cuando ha adivinado una diferencia si aun 
le quedan más por adivinar, e indicarle si no ha adivinado ninguna e indicarle también si pincha en una ya adivinada
+ buscar en internet ejemplos para poder pedir al usuario su nombre cuando arranque la aplicación a través de una
ventana de texto emergente
+ Buscar en internet un ejemplo sobre cómo escribir en un archivo de texto, cuando el usuario haya resuelto la ultima 
diferencia guardaremos en un archivo de texto el nombre del usuario y el tiempo tardado
+ listar al arrancar la aplicación el nombre y el tiempo tardado de cada usuario guardados en el archivo del punto anterior

'''
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#tkinter esta disponible por defecto en python
#otro recurso muy usado es pyQt5

########   VARIABLES GLOBALES #########
x = 0
y = 0
contador = 0
marcado = 0 
marcado2 = 0 
marcado3 = 0
marcado4 = 0
marcado5 = 0

score = open("score.txt", "a") #creo variable con la apertura del archivo, en modo sobreescribrir (A)
scoreL = open("score.txt", "r") #creo otra variable para que el archivo TXT sea leido.
lectura = print(scoreL.readlines())
########   FUNCIONES  #########



def registrar():
    #tengo que decirle que escribe el usuario en un TXT
    alias = nombre.get()
    score.write(str(alias) + " \n")    
    print(" El Usuario es : " + str(alias)) # .get () trae lo introducido en la variable nombre.
    ventana_nombre.destroy()
    #tengo que cerrar la ventana 

# def score():
#     #print(str(score.read()))
#     pass
def tequedan():
    messagebox.showinfo("Pista" , "Te quedan : " + str(5 - contador) + " diferencias más.")

def instrucciones():
    messagebox.showinfo("Léeme", " Debes hacer click en las difencias que encuentras en la foto de la derecha. ") 

def felicita():
    messagebox.showinfo("mensaje", " FELICIDADES LO HAS CONSEGUIDO ") 
    
def yapasaste():
    messagebox.showinfo("mensaje", " ésta ya la habías adivinado ") 
    
def click_raton(evento):
    global x, y, contador, marcado, marcado2, marcado3, marcado4, marcado5
    #se pone global para poder usar las variables. Equivale a importar variables
    #x e y definidas fuera de la funcion. ya que lo que es Fuera es global y lo que es dentro es local
    x = evento.x
    y = evento.y
    print("x: " + str(x)) #ESTO PODRÍA NO ESTAR AQUÍ.SOLO MUESTRA EN CONSOLA LAS CORDENADAS
    print("y: " + str(y)) #ESTO PODRÍA NO ESTAR AQUÍ.
    
    if x >= 496 and x <= 560 and y >= 38 and y <= 85 : # 496x - 38y es una cordenada inicio parche. La 560x-85y es otra cordenada fin del parche.
            if marcado == 0:
                 contador = contador + 1
                 print("FELICIDADES ADIVINASTE LA PRIMERA DIFERENCIA")
                 marcado = marcado + 1
                 tequedan()
            else:
                yapasaste()  
            
    elif x >= 440 and x <= 489 and y >= 148 and y <= 189: #ha de cumplirse todo
            if marcado2 == 0:
                print("FELICIDADES ADIVINASTE LA SEGUNDA DIFERENCIA")
                contador = contador + 1
                marcado2 = marcado2 + 1
                tequedan()
            else:
                yapasaste()
                
    elif x >= 330 and x <= 384 and y >= 157 and y <= 198 :
            if marcado3 == 0:
                 contador = contador + 1
                 print("FELICIDADES ADIVINASTE LA TERCERA DIFERENCIA")
                 marcado3 = marcado3 + 1
                 tequedan()
            else:
                yapasaste() 
    elif x >= 367 and x <= 443 and y >= 3 and y <= 26:
            if marcado4 == 0:
                 contador = contador + 1
                 print("FELICIDADES ADIVINASTE LA CUARTA DIFERENCIA")
                 marcado4 = marcado4 + 1
                 tequedan()
            else:
                yapasaste() 
    elif x >= 402 and x <= 460 and y >= 69 and y <= 112:
            if marcado5 == 0:
                 contador = contador + 1
                 print("FELICIDADES ADIVINASTE LA QUINTA DIFERENCIA")
                 marcado5 = marcado5 + 1
                 tequedan()
            else:
                yapasaste() 
    else:
        print("NO HAS ADIVINADO UNA DIFERENCIA")
        
    
    if contador == 5:
        fin = time.time()
        tiempo_tardado = round((fin - inicio),2)
        print("El tiempo que has tardado es : " + str(tiempo_tardado))
        score.write(str(tiempo_tardado) + "segundos. \n")
        felicita()    
      
        
        
# pongo en primer lugar la lista de ALIAS + Tiempo

listado_score = Tk()
listado_score.geometry("250x500")
listado_score.title("Puntuación")        
etiq_score = Label(listado_score, text = "El jugador con menos segundos gana")
etiq_score.pack()
#lectura = tk.text(listado_score, background="white", width=200, height = 350)
#lectura.config(state="disable")
#lectura.pack()
#lectura.insert(INSERT, str(lectura))
boton_comenzar = Button(listado_score, text = "Comenzar", command = listado_score.quit) #es al presionar el botón cuando se cierra
listado_score.mainloop()


#pido el nombre al usuario en otra ventana a parte
ventana_nombre = Tk()
nombre = StringVar() #en esta caso es StringVar porque es texto. puede ser "boolVAR" o intVar también.
ventana_nombre.geometry("200x80")
ventana_nombre.title("Escribe un ALIAS")
ventana_nombre.attributes("-topmost", True)
etiq_nombre = Label(ventana_nombre, text = " Introduce un Alias ")
etiq_nombre.pack()
entrada_nombre = ttk.Entry(ventana_nombre, textvariable = nombre, justify=CENTER, width=10) 
#con textvariable = nombre. lo que hago es asociar el texto de entrada a la variable ya creada arriba, nombre
# textvariable un parámentro propio de tkinter
entrada_nombre.pack()
entrada_nombre.get()
boton_enviar = Button(ventana_nombre, text = "Registrar", command = registrar) #es al presionar el botón,cuando llama función REGISTRAR
boton_enviar.pack() 
ventana_nombre.mainloop()

        
    
#end click_raton
ventana = Tk()
canvas = Canvas(ventana, width = 500, height = 300) #lienzo donde irá la imagen
canvas.pack(expand = YES, fill = BOTH ) #necesario
imagen = PhotoImage(file="imagen.png") #indico que la variable imagen lleva ese archivo
canvas.create_image(0,0,image = imagen, anchor = NW) # 0.0 es la esquina superior izquierda donde colocar la imagen
#nw es hacia donde estoy orientando la imgen. por defecto es así para que aparezca recta

#aquí empieza el juego
ventana.geometry("660x220")
instrucciones()
inicio = time.time()
ventana.title("Juguemos!")
ventana.bind("<Button 1>",click_raton)
ventana.mainloop() #mailoop deja de hacer cosas y el usuario pasa a manejar la ventana




