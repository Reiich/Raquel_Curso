'''
EJERCICIO CON CHECK BOX. QUE AÑADIRÁ UN PRECIO EXTRA AL PRECIO BASE DE LA PIZZA
SE ESTUVIERAN SELECCIONADOS.

Las agrupaciones de Helados y bebidas, las he realizado desde QtDesigner, dentro de Containers/Group box

Después seleccionando ese elemento , en las opciones del propio GroupBox, activo "checkable" y ello haga un "checked"
De esta manera consigo que al checkar esa opción se active el resto, y si no, que en gris. Sin activar el resto de casillas.

'''

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QWidget
import sys
from ventana_menu import Ui_lista_menu
####### 

class menuApp(QDialog):
    
    def __init__(self):
        
        super().__init__()
        self.ventana = Ui_lista_menu() #el MenuApp tendrá una "ventana" cuya forma será de la clase Ui_lista_menu
        self.ventana.setupUi(self)
        
        self.ventana.cb_choco.stateChanged.connect(self.configurar_menu)
        self.ventana.cb_fresa.stateChanged.connect(self.configurar_menu)
        self.ventana.cb_frutos.stateChanged.connect(self.configurar_menu)
        self.ventana.cb_kinder.stateChanged.connect(self.configurar_menu)
        self.ventana.cb_refresco.stateChanged.connect(self.configurar_menu)
        self.ventana.cb_agua.stateChanged.connect(self.configurar_menu)
        self.ventana.cb_cerveza.stateChanged.connect(self.configurar_menu)
        
    def configurar_menu(self):
        precio = 0
        
        if self.ventana.cb_choco.isChecked() == True:
            precio += 2
        if self.ventana.cb_fresa.isChecked() == True:
            precio += 2
        if self.ventana.cb_frutos.isChecked() == True:
            precio += 3
        if self.ventana.cb_kinder.isChecked() == True:
            precio += 3
        if self.ventana.cb_refresco.isChecked() == True:
            precio += 2
        if self.ventana.cb_agua.isChecked() == True:
            precio += 1
        if self.ventana.cb_cerveza.isChecked() == True:
            precio += 1.5
            
        self.ventana.lbl_resultado.setText("Precio total {} euros".format(precio))
    
        
        
        
################
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v_menu = menuApp() # asigna clase menuApp 
    v_menu.show()  #arranca esta ventana 
    sys.exit(app.exec_())