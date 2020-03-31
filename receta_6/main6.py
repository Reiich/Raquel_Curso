'''
Aplicacion 6 - Una aplicación que pide un texto de entrada

Y luego lo vuelve a imprimir por pantalla a modo de saludo/respuesta.
'''

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ventana6 import *

class DialogoSaludoAplicacion(QDialog):  #esta clase hereda de Qdialog
    def __init__(self):    # su constructor trae el mismo contructor
        super().__init__() # que la clase padre
        
        #creo objetos o propiedades de la clase
        self.dialogo = Ui_Dialog() # la variable dialogo, es de la clase Ui_Dialog
        self.dialogo.setupUi(self)  # llamo al setup de la clase. 
                                    #Es decir, que va a iniciar la ventana con todos sus componentes
        
        self.dialogo.bt_saludar.clicked.connect(self.mostrar_saludo) 
        # le doy una funcionalidad al boton dentro de la clase dialogo. llamado bt_saludar
        #cuando haga click. se conectará con la función mostrar_saludo
        self.show()
        
    def mostrar_saludo(self):  #creo un metodo para motrar saludo que es lo que hará el boton salludar al clicarse
        
        mensaje = self.dialogo.entrada_texto.text()  #asigno la variable "mensaje" al cuadro de entrada de texto
        self.dialogo.muestra_saludo.setText(mensaje) #setText, hace que en el espacio 
        #(en blanco) que hay para poner un texto, vaya el ("mensaje") capturado desde "entrada texto" 
        
        
### creo la aplicación ###

if __name__ == "__main__": # si se cuple que arranca desde el main. Ejecuta en orden lo siguiente
    app = QApplication(sys.argv)  #requisito propio de Qapplication
    ui = DialogoSaludoAplicacion() #al darle toda una clase. ya lleva implicitos los métidis
    ui.show()
    sys.exit(app.exec_())  #sale de la aplicación, sólo cuando sale de la ventana flotante
    #esta linea indica que la ventana flotante es la que manda.
        
        