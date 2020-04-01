'''
EJERCICIO CON CHECK BOX. QUE AÑADIRÁ UN PRECIO EXTRA AL PRECIO BASE DE LA PIZZA
SE ESTUVIERAN SELECCIONADOS.


'''

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QWidget
import sys
from ventana_pizza import Ui_Pizza
####### 


class pizzaApp(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ventana = Ui_Pizza()
        self.ventana.setupUi(self) #invocamos el método setupUi
         
        self.ventana.cb_atun.stateChanged.connect(self.anadir_ingrediente)
        self.ventana.cb_pimiento.stateChanged.connect(self.anadir_ingrediente)
        self.ventana.checkBox_3.stateChanged.connect(self.anadir_ingrediente)

    def anadir_ingrediente(self):
        precio_base = 15
        
        if self.ventana.cb_atun.isChecked() == True:
            precio_base += 1
        
        if self.ventana.cb_pimiento.isChecked() == True:
            precio_base += 1
            
        if self.ventana.checkBox_3.isChecked() == True:
            precio_base += 1.5
            
        self.ventana.lbl_resultado.setText("El precio a pagar es de {} euros".format(precio_base))
        
        


################
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v_pizza = pizzaApp() # asigna clase pizzaApp a v_pizza
    v_pizza.show()  #arranca esta ventana pizzaApp
    sys.exit(app.exec_())