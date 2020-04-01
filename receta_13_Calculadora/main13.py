'''

CALCULADORA
 
 

'''

from PyQt5.QtWidgets import QApplication, QDialog, QWidget
import sys
from ventana_calcul import Ui_Calculadora
#####

class CalculadoraApp(QDialog):
    
    def __init__(self):        
        super().__init__()
        self.ventana = Ui_Calculadora() 
        self.ventana.setupUi(self)
        
        self.ventana.btn_suma.clicked.connect(self.sumar)
        self.ventana.btn_resta.clicked.connect(self.restar)
        self.ventana.btn_multiplica.clicked.connect(self.multiplicar)
        self.ventana.btn_divide.clicked.connect(self.dividir)
        
    def sumar(self):
        num1 = self.ventana.txt_numero1.text()  #asigno a la variable "num1" el texto metido en txt_numero1 (que es un text line)
        num2 = self.ventana.txt_numero2.text()  # a modo de "input"
        resultado = float(num1) + float(num2) #lo convierto a float para que opere, y no concatene.
        self.ventana.lbl_resultado.setText(str(resultado)) # debe establecerse como STR, porque el lineText,es str originariamente
           
    def restar(self):
        num1 = self.ventana.txt_numero1.text()
        num2 = self.ventana.txt_numero2.text() 
        resultado = float(num1) - float(num2)
        self.ventana.lbl_resultado.setText(str(resultado))
        
    def multiplicar(self):
        num1 = self.ventana.txt_numero1.text()
        num2 = self.ventana.txt_numero2.text() 
        resultado = float(num1) * float(num2)
        self.ventana.lbl_resultado.setText(str(resultado))
        
    def dividir(self):
        num1 = self.ventana.txt_numero1.text()
        num2 = self.ventana.txt_numero2.text() 
        resultado = float(num1) / float(num2)
        self.ventana.lbl_resultado.setText(str(resultado))
        
        
################
#inicio aplicacion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    v_calc= CalculadoraApp() 
    v_calc.show()  
    sys.exit(app.exec_())