'''
uso de la BARRA DE DESPLAZAMIENTO

 aquí para obtener el valor de la barra, donde el usuario la ha dejado parada
 se usa:
 
 .valueChanged
 
 hay que tener en cuenta, que éste método devuelve el valor, que se optine. 
 Automáticamente, si tener que programar nada. Por ello, ucnado definamos la función
 que mostrará el valor elegido por pantalla, sólo necesitaremos pasar ese valor
 como parámentro en la función: (de esta manera)
 
 def mostrar_azucar(self, valor):  
        self.ui.txt_resultado.setText("Nivel de azucar: {}".format(valor)) 
        
        #el "valor" lo recoge del parámetro que viene de entrada
        
Es decir, es como si .valueChanged() hiciera un return del punto (Valor) en el que
ha quedado la selección.

 
 
 
'''

from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import sys
from niveles_dialog import NivelesDialog

class NivelesApp(QDialog):
    
    def __init__(self):  #todos estos valores se cargan sólo por iniciar la ventana
        super().__init__()
        self.ui = NivelesDialog()
        self.ui.setupUi(self)


        self.ui.scroll_azucar.valueChanged.connect(self.mostrar_azucar)
        self.ui.scrollPulso.valueChanged.connect(self.mostrar_pulso)
        self.ui.sliderColesterol.valueChanged.connect(self.mostrar_colesterol)
        self.ui.sliderPresion.valueChanged.connect(self.mostrar_presion)

        self.show()  #mostramos la interfaz
        
    def mostrar_azucar(self, valor):  #este parámetro va a corresponder el el valor de la barra de desplazamiento
        self.ui.txt_resultado.setText("Nivel de azucar: {}".format(valor)) #el valor lo recoge del parámetro que viene de entrada

    def mostrar_pulso(self, valor):
        self.ui.txt_resultado.setText("Pulso: {}".format(valor))
    
    def mostrar_colesterol(self, valor):
        self.ui.txt_resultado.setText("Nivel colesterol: {}".format(valor))
    
    def mostrar_presion(self, valor):
        self.ui.txt_resultado.setText("Presión: {}".format(valor))
    
    


###############
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_inicio = NivelesApp() 
    ventana_inicio.show()  
    sys.exit(app.exec_())