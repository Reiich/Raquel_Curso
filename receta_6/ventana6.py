# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '6_ventana.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 200)
        Dialog.setMaximumSize(QtCore.QSize(500, 200))
        self.Escriba = QtWidgets.QLabel(Dialog)
        self.Escriba.setGeometry(QtCore.QRect(20, 30, 201, 31))
        self.Escriba.setObjectName("Escriba")
        self.entrada_texto = QtWidgets.QLineEdit(Dialog)
        self.entrada_texto.setGeometry(QtCore.QRect(220, 39, 171, 21))
        self.entrada_texto.setObjectName("entrada_texto")
        self.saludo = QtWidgets.QLabel(Dialog)
        self.saludo.setGeometry(QtCore.QRect(20, 80, 71, 31))
        self.saludo.setObjectName("saludo")
        self.muestra_saludo = QtWidgets.QLabel(Dialog)
        self.muestra_saludo.setGeometry(QtCore.QRect(120, 80, 271, 31))
        self.muestra_saludo.setText("")
        self.muestra_saludo.setObjectName("muestra_saludo")
        self.bt_saludar = QtWidgets.QPushButton(Dialog)
        self.bt_saludar.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.bt_saludar.setObjectName("bt_saludar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Saludo"))
        self.Escriba.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Escriba su nombre</span></p></body></html>"))
        self.saludo.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Saludo:</span></p></body></html>"))
        self.bt_saludar.setText(_translate("Dialog", "Saludar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
