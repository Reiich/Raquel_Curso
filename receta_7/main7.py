'''
Aplicacion 7 - Elegir tipo de Vuelo.

usar RadioButton y actuar cuando uno u otro se seleccione
'''
from PyQt5.QtWidgets import QApplication, QDialog
import sys
from ventana_clase_vuelo import DialogoClaseVuelo

#creo una variable sólo para iniciar el programa gráfico
class tipoVueloApp(QDialog):   #hereda de QDialog
    def __init__(self): 
        super().__init__()
        self.ui_principal = DialogoClaseVuelo() #así llame al objeto ventana en Desginer a su creación allí
        self.ui_principal.setupUi(self)
        
        # de la ventana principal, el radio buttom...si está seleccionado (toggle)
        self.ui_principal.rbt_primera.toggled.connect(self.mostrar_precio)
        self.ui_principal.rbt_negocio.toggled.connect(self.mostrar_precio)
        self.ui_principal.rbt_economica.toggled.connect(self.mostrar_precio)
        self.show() #hace todo lo anterior y se muestra a sí misma (tipoVueloApp)
        
        
    def mostrar_precio(self):    #digo usando self, porque estoy dentro de una clase POO
        coste = ""
        if self.ui_principal.rbt_primera.isChecked() == True:
            coste= "230 euros"
        if self.ui_principal.rbt_negocio.isChecked() == True:
            coste= "180 euros"           
        if self.ui_principal.rbt_economica.isChecked() == True:
            coste= "120 euros"
            
        self.ui_principal.mostrar_clase.setText("Debe pagar {}".format(coste))
 ########################3       
        
        
        
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) #linea obligatoria
    ui = tipoVueloApp()   #linea obligatoria con la variable que quiera ponerle
    
    ui.show()  #ejecuta, la var UI, que tiene toda la clase tipoVueloApp()
    sys.exit(app.exec_()) #cierro app
        