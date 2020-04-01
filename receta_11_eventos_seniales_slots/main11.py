'''

UTILIZACION DE EVENTOS, POR DEFECTO, QUE TRAE QTDESIGNER SIN Q TENGAMOS Q PROGRAMAR NADA.

manipulacion de los eventos que generan los widgets de una interfaz gráfica

llamamos SLOT a la acción que se produce cuando se realiza un evento. (por

En este ejemplo, cuando diseñemos en QtDesigner, pondremos una linea de entrada de texto
y un pushButton. Seleccionando este último vamos al menú Edit / edit signals-Slots
ahora su pongo y pincho sobre el boton, me permite enlazar con la linea de texto (aparece una flichita roja)
Una vez que enlazo, suelto y aparece una ventna para configurar.
Elijo "Cliecked" y "clear", es decir que al hacer click en el botón se borra todo el texto.

Es decir, haremos que al presionar el botón, haga un reset del campo introducido


'''

from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import sys
from eventos import Ui_EventoDialog
######

class eventoApp(QDialog):
    
    def __init__(self):        
        super().__init__()
        self.ventana = Ui_EventoDialog() 
        self.ventana.setupUi(self)
        
        
## en esta pantalla es tan simple como hacer esto. Simplemente se llama al objeto.
# pues todo los demás ya está configurado desde eventos.py, (creado fácilmente desde QtDesginer)
# es decir, no hay que programar estos eventos que vienen por defecto.        
        
################
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v_evento = eventoApp() 
    v_evento.show()  
    sys.exit(app.exec_())