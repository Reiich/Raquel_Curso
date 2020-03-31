'''
Aplicacion 8 - seleccionar varios RADIOBUTTON

al fianl juntar los dos resultados en una línea.


'''
from PyQt5.QtWidgets import QApplication, QDialog
import sys
from ventana_talla_pago import Ui_MainWindow


        
class elegirCamisaApp(QDialog):
    
    
    def __init__(self):
        super().__init__()  # lo primero que tendrá el constructor es TODO lo que le venga dado de la clase padre Qdialog
        self.ventana = Ui_MainWindow()  #creo variable ventana con la clase dada en el DEsingner a mi ventana
        self.ventana.setupUi(self)  #se inicia a sí mismo
        
        self.ventana.rbt_s.toggled.connect(self.recibe_dato)
        self.ventana.rbt_m.toggled.connect(self.recibe_dato)
        self.ventana.rbt_l.toggled.connect(self.recibe_dato)
        
        self.ventana.rbt_tarjeta.toggled.connect(self.recibe_dato)
        self.ventana.rbt_paypal.toggled.connect(self.recibe_dato)
        self.ventana.rbt_efectivo.toggled.connect(self.recibe_dato)

        self.show() 
        
    def recibe_dato(self):
        talla = ""
        pago =  ""
        
        if self.ventana.rbt_s.isChecked() == True:
            talla = " S "
        if self.ventana.rbt_m.isChecked() == True:
            talla = " M "
        if self.ventana.rbt_l.isChecked() == True:
            talla = " L "            
        if self.ventana.rbt_tarjeta.isChecked() == True:
            pago = " con tarjeta.  "           
        if self.ventana.rbt_paypal.isChecked() == True:
            pago = " con Paypal.  "            
        if self.ventana.rbt_efectivo.isChecked() == True:
            pago = " en efectivo.  "

        self.ventana.txt_resultado.setText("He elegido la talla {} y el pago {}".format(talla, precio))


### Inicio LA aplicación sólo si se está arrancando desde __main__ #### 

if __name__ == "__main__": 
    app = QApplication(sys.argv) #linea obligatoria
    ui = elegirCamisaApp()
    
    ui.show()
    sys.exit(app.exec_()) #cierro app
             
             