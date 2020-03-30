'''
Created on 30 mar. 2020

@author: Raquel
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets 
from ventanas import ventana_principal_b  #del package ventanas, me importas la ventana B

###### funciones #####


def transformar_a_dolares():
    introducido = ui.cantidad.text() #creo una variable. llamada "introducido" cuyo valor le va a venir dado del text introducido por el objeto "entrada_euros"
    introducido_float = float(introducido.replace(",",".")) #lo convierte a FLOAT para ser decimales. Co nel añadido de que si el usuario pone una , lo convierta a un (.) para que no de errores
    dolares = introducido_float * 1.1      #la operación a realizar, consiste en el valor recibido multiplicarlo por 1.1 (valor del dolar ahora mismo)  
    # el resultado lo va a mostrar en el espacio asignado con DESIGNER "res_dol" que no es mas que una etiqueta en blanco para que pueda ir variando.
    ui.resultado.setText(str(round(dolares, 2)).replace(".",",") + " e") 
                                        # también hago que al mostrarse el resultado, 
                                        #si metí una coma, también imprima , y no como por defecto,
                                        # saca punto (por el tema USA)


def transformar_a_libras():
    introducido = ui.cantidad.text() #creo una variable. llamada "introducido" cuyo valor le va a venir dado del text introducido por el objeto "entrada_euros"
    introducido_float = float(introducido.replace(",",".")) #lo convierte a FLOAT para ser decimales. Co nel añadido de que si el usuario pone una , lo convierta a un (.) para que no de errores
    libras = introducido_float * 0.90      #la operación a realizar, consiste en el valor recibido multiplicarlo por 1.1 (valor del dolar ahora mismo)  
    # el resultado lo va a mostrar en el espacio asignado con DESIGNER "res_lib" que no es mas que una etiqueta en blanco para que pueda ir variando.
    ui.resultado.setText(str(round(libras, 2)).replace(".",",") + " e")  
                                      

def transformar_a_pesos():
    introducido = ui.cantidad.text() 
    introducido_float = float(introducido) #convierto a float.
    pesos = introducido_float * 0.038 # un peso ,exicano equivale a 0.038 euros
    ui.resultado.setText(str(round(pesos, 2)) + " e")  
                                    #res_pes es el hueco, dejado en el diseño para mostrar el resultado
                                    #que en principio es transparente o vacío.       


############## fin funciones #####################################

#lineas obligatorias
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
#####################

#las siguientes dos líneas son la asignación de elementos dentro de Variables
ui = ventana_principal_b.Ui_MainWindow() #indico que la variable "ui" será la ventana principal
ui.setupUi(MainWindow) #todo esto viene dado del archivo .py que convertí desde ui. 
#Se configura automáticamente enlazando a través de Import ventanas. Todo ese trabajo que me ahorro.

#configuro (yo manualmente) la funcionalidad para los elementos de la ventana
# en este caso las tres LABEL en las que he puesto una imagen con Pyqt5. 
#Cuando cliquee, realiza función transformar_a

ui.usa_b.clicked.connect(transformar_a_dolares) 
ui.ru_b.clicked.connect(transformar_a_libras) 
ui.mex_b.clicked.connect(transformar_a_pesos) 



# por último, otras líneas obligatorias. La que muestra ventana y la que controla el sys
MainWindow.show()
sys.exit(app.exec_())