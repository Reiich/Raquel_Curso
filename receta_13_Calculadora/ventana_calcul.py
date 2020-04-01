# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_calcul.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculadora(object):
    def setupUi(self, Calculadora):
        Calculadora.setObjectName("Calculadora")
        Calculadora.resize(400, 300)
        Calculadora.setStyleSheet("\n"
"background-color: rgb(170, 0, 0);")
        self.lbl_titlulo = QtWidgets.QLabel(Calculadora)
        self.lbl_titlulo.setGeometry(QtCore.QRect(150, 20, 101, 31))
        self.lbl_titlulo.setObjectName("lbl_titlulo")
        self.txt_numero1 = QtWidgets.QLineEdit(Calculadora)
        self.txt_numero1.setGeometry(QtCore.QRect(210, 70, 61, 20))
        self.txt_numero1.setStyleSheet("background-color: rgb(255, 102, 102);")
        self.txt_numero1.setObjectName("txt_numero1")
        self.txt_numero2 = QtWidgets.QLineEdit(Calculadora)
        self.txt_numero2.setGeometry(QtCore.QRect(210, 100, 61, 20))
        self.txt_numero2.setStyleSheet("\n"
"background-color: rgb(255, 102, 102);")
        self.txt_numero2.setObjectName("txt_numero2")
        self.lbl_n1 = QtWidgets.QLabel(Calculadora)
        self.lbl_n1.setGeometry(QtCore.QRect(70, 70, 121, 21))
        self.lbl_n1.setObjectName("lbl_n1")
        self.lbl_n2 = QtWidgets.QLabel(Calculadora)
        self.lbl_n2.setGeometry(QtCore.QRect(70, 100, 121, 21))
        self.lbl_n2.setObjectName("lbl_n2")
        self.btn_suma = QtWidgets.QPushButton(Calculadora)
        self.btn_suma.setGeometry(QtCore.QRect(30, 170, 75, 23))
        self.btn_suma.setStyleSheet("background-color: rgb(255, 166, 166);\n"
"font: 75 8pt \"Segoe Script\";")
        self.btn_suma.setObjectName("btn_suma")
        self.btn_resta = QtWidgets.QPushButton(Calculadora)
        self.btn_resta.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.btn_resta.setStyleSheet("background-color: rgb(255, 166, 166);\n"
"font: 75 8pt \"Segoe Script\";")
        self.btn_resta.setObjectName("btn_resta")
        self.btn_multiplica = QtWidgets.QPushButton(Calculadora)
        self.btn_multiplica.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.btn_multiplica.setStyleSheet("background-color: rgb(255, 166, 166);\n"
"font: 75 8pt \"Segoe Script\";")
        self.btn_multiplica.setObjectName("btn_multiplica")
        self.btn_divide = QtWidgets.QPushButton(Calculadora)
        self.btn_divide.setGeometry(QtCore.QRect(300, 170, 75, 23))
        self.btn_divide.setStyleSheet("background-color: rgb(255, 166, 166);\n"
"font: 75 8pt \"Segoe Script\";")
        self.btn_divide.setObjectName("btn_divide")
        self.lbl_resultado = QtWidgets.QLabel(Calculadora)
        self.lbl_resultado.setGeometry(QtCore.QRect(150, 240, 111, 21))
        self.lbl_resultado.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"System\";\n"
"background-color: rgb(0, 0, 0);")
        self.lbl_resultado.setObjectName("lbl_resultado")

        self.retranslateUi(Calculadora)
        QtCore.QMetaObject.connectSlotsByName(Calculadora)

    def retranslateUi(self, Calculadora):
        _translate = QtCore.QCoreApplication.translate
        Calculadora.setWindowTitle(_translate("Calculadora", "Calculadora"))
        self.lbl_titlulo.setText(_translate("Calculadora", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Calculadora</span></p></body></html>"))
        self.txt_numero1.setToolTip(_translate("Calculadora", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.txt_numero2.setToolTip(_translate("Calculadora", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lbl_n1.setText(_translate("Calculadora", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Introduce un número</span></p></body></html>"))
        self.lbl_n2.setText(_translate("Calculadora", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Introduce un número</span></p></body></html>"))
        self.btn_suma.setText(_translate("Calculadora", "Sumar"))
        self.btn_resta.setText(_translate("Calculadora", "Restar"))
        self.btn_multiplica.setText(_translate("Calculadora", "Multiplicar"))
        self.btn_divide.setText(_translate("Calculadora", "Dividir"))
        self.lbl_resultado.setText(_translate("Calculadora", "<html><head/><body><p align=\"center\"/></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculadora = QtWidgets.QDialog()
    ui = Ui_Calculadora()
    ui.setupUi(Calculadora)
    Calculadora.show()
    sys.exit(app.exec_())
