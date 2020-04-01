'''

UTILIZACION DE EVENTOS, POR DEFECTO, QUE TRAE QTDESIGNER SIN Q TENGAMOS Q PROGRAMAR NADA.

Aquí copiamos el texto escrito en un text line superior y lo pegamos en el textLine de abajo.

PAra ello, al botón copiar, hay dque darle 2 EVENTOS.
 - 1 - Al hacer clic en el boton se selecciona todo (pressed -> selectAll)
 - 2 - Al soltar el botón, se copia el contenido (released -> copy)
 
 

'''

from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import sys
from copiaypegaDialog import Ui_CopiaPegaDialog
######

class CopiaypegaApp(QDialog):
    
    def __init__(self):        
        super().__init__()
        self.ventana = Ui_CopiaPegaDialog() 
        self.ventana.setupUi(self)
        
        
## en esta pantalla es tan simple como hacer esto. Simplemente se llama al objeto.
# pues todo los demás ya está configurado desde eventos.py, (creado fácilmente desde QtDesginer)
# es decir, no hay que programar estos eventos que vienen por defecto.        
        
################
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v_evento = CopiaypegaApp() 
    v_evento.show()  
    sys.exit(app.exec_())