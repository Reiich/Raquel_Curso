# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_clase_vuelo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DialogoClaseVuelo(object):
    def setupUi(self, DialogoClaseVuelo):
        DialogoClaseVuelo.setObjectName("DialogoClaseVuelo")
        DialogoClaseVuelo.resize(350, 330)
        DialogoClaseVuelo.setMaximumSize(QtCore.QSize(350, 350))
        DialogoClaseVuelo.setStyleSheet("background-color: rgb(124, 249, 185);")
        self.lbl_elija = QtWidgets.QLabel(DialogoClaseVuelo)
        self.lbl_elija.setGeometry(QtCore.QRect(30, 20, 131, 41))
        self.lbl_elija.setObjectName("lbl_elija")
        self.rbt_primera = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbt_primera.setGeometry(QtCore.QRect(60, 70, 91, 21))
        self.rbt_primera.setObjectName("rbt_primera")
        self.rbt_negocio = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbt_negocio.setGeometry(QtCore.QRect(60, 110, 91, 21))
        self.rbt_negocio.setObjectName("rbt_negocio")
        self.rbt_economica = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbt_economica.setGeometry(QtCore.QRect(60, 150, 91, 21))
        self.rbt_economica.setObjectName("rbt_economica")
        self.mostrar_clase = QtWidgets.QLabel(DialogoClaseVuelo)
        self.mostrar_clase.setGeometry(QtCore.QRect(120, 190, 111, 31))
        self.mostrar_clase.setObjectName("mostrar_clase")

        self.retranslateUi(DialogoClaseVuelo)
        QtCore.QMetaObject.connectSlotsByName(DialogoClaseVuelo)

    def retranslateUi(self, DialogoClaseVuelo):
        _translate = QtCore.QCoreApplication.translate
        DialogoClaseVuelo.setWindowTitle(_translate("DialogoClaseVuelo", "Clase de Vuelo"))
        self.lbl_elija.setText(_translate("DialogoClaseVuelo", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Elija la clase de vuelo</span></p></body></html>"))
        self.rbt_primera.setText(_translate("DialogoClaseVuelo", "Primera Clase"))
        self.rbt_negocio.setText(_translate("DialogoClaseVuelo", "Bussines Class"))
        self.rbt_economica.setText(_translate("DialogoClaseVuelo", "Económica"))
        self.mostrar_clase.setText(_translate("DialogoClaseVuelo", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogoClaseVuelo = QtWidgets.QDialog()
    ui = Ui_DialogoClaseVuelo()
    ui.setupUi(DialogoClaseVuelo)
    DialogoClaseVuelo.show()
    sys.exit(app.exec_())
