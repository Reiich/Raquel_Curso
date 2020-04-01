'''

QspinBox 
(esas cajas que aumentan y decrementan un número si presionamos las flechitas)

El método que va a saber si el usuario a dejado de marcar las flechitas. es
    editingFinished
y ese será el método qye vamos a enlazar (connect) con la fución/método correspondiente.

ojo! para recoger el valor de un SpinBox se usa VALUE
 ...y no text()
 
 El objetivo es crear una App, en la que demos el precio de el producto, las unidades y calcule el subtotal
 y automaticamente vaya realizando tanto el subtotal como la operación del total (muestra abajo a la derecha)
 
 
'''

from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import sys
from ventana_spinbox import Ui_Dialog
#####

class ventasApp(QDialog):
    
    def __init__(self):  #todos estos valores se cargan sólo por iniciar la ventana
        super().__init__()
        self.ui_ventas = Ui_Dialog()
        self.ui_ventas.setupUi(self)
        
        self.ui_ventas.spinBox_mouse.editingFinished.connect(self.calcular_total)
        self.ui_ventas.spinBox_teclado.editingFinished.connect(self.calcular_total)

        self.show() ######

    def calcular_total(self):
        precioMouse= int(self.ui_ventas.txt_val_mouse.text())  
        # text() indica que recoja el valor dado en el spinbox . Cojo las dos canridades del precio      
        precioTeclado= int(self.ui_ventas.txt_val_teclado.text())  
        
        #ahora recojo las unidades mediante VALUE. de Mouse y Teclado
        udMouse= int(self.ui_ventas.spinBox_mouse.value())
        udTeclado= int(self.ui_ventas.spinBox_teclado.value()) 
        
        #ahora CALCULO TOTAL por producto 
        totalMouse=  precioMouse * udMouse
        totalTeclado= precioTeclado * udTeclado
        # y lo muestro, en las cajas de la drecha de la app. txt_mouse y txt_tecldo
        #como debo mostrar uso setText. Lo convierto a str (texto)
        self.ui_ventas.txt_mouse.setText(str(totalMouse))
        self.ui_ventas.txt_teclado.setText(str(totalTeclado))
        
        precio_total = totalMouse + totalTeclado
        
        self.ui_ventas.lbl_resultado.setText(str(precio_total) + "e")
        








###############
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui= ventasApp() 
    ui.show()  
    sys.exit(app.exec_())