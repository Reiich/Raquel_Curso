'''
uso de QListWidget

Vamos a diseñar agragando un List Widget en el que se permitirá escoger
varias opciones. Para ello hay que ir a las propiedades del objeto y
en QAbstratItemView ir a Selection Mode y escoger "Multi selection".

haciendo dobleClick sobre el List Widget vacío, nos permite + añadir
las opciones a elegir. (Permitirá que sean varias)

debajo de el anterior, ponemos otro List Widget,
 
El método para detectar, dentro de un List Widget, cuáles fueron seleccionados es:

.itemSelectionChanged   (para la lista donde ya hay items disponibles) que llamará al método a realizar
.selectedItems()   (que se queda con los items seleccionados en la lista de disponibles)
.addItem(i.text())      
    (que irá añadiendo en la lista de seleccionados (inicialmente en blanco)
     y se crea mediante un bucle FOR. ADemás de añadirlo, 
con .text() hace que se muestre, en el espacio de List Widget de seleccionados.
 
'''

from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import sys
from ventana_diagnostico import Ui_diagnosticosDIalog

class DiagnosticoApp(QDialog):
    
    def __init__(self):  #todos estos valores se cargan sólo por iniciar la ventana
        super().__init__()
        self.ui = Ui_diagnosticosDIalog() # me traigo todo lo configurado con QtDESIGNER
        self.ui.setupUi(self)
    
#diseñamos eventos manuales.
        self.ui.lst_disponibles.itemSelectionChanged.connect(self.mostrar_seleccion)
        #cuando elija alguno de los items se pone en marcha el método mostrar
        
        self.show() #siempre, después de precargar lo anterior, muestro ventana.


    def mostrar_seleccion(self):
        
       self.ui.lst_seleccionados.clear() #elimino los que hubiera seleccionados de antes. lo dejo limpio
       #indico variable para almacenar aquellos items que han sido elegidos (recuerda q configuré para
       # que fuera posible seleccionar varios).. Si hay varios
       #se convierte en una lista. (llena de items)
       diagnosticos = self.ui.lst_disponibles.selectedItems()
       
       ## ¿cómo paso los seleccionados a la lista de abajo? . Con bucle FOR
       for d in list(diagnosticos):
           self.ui.lst_seleccionados.addItem(d.text())
           # este self, además de añadir cada item, con text()lo recoge y muestra
    


###############
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_inicio = DiagnosticoApp() 
    ventana_inicio.show()  
    sys.exit(app.exec_())