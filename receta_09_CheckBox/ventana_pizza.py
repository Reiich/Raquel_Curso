# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_pizza.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pizza(object):
    def setupUi(self, Pizza):
        Pizza.setObjectName("Pizza")
        Pizza.resize(400, 300)
        self.lbl_titulo = QtWidgets.QLabel(Pizza)
        self.lbl_titulo.setGeometry(QtCore.QRect(50, 0, 301, 61))
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.cb_atun = QtWidgets.QCheckBox(Pizza)
        self.cb_atun.setGeometry(QtCore.QRect(100, 80, 71, 31))
        self.cb_atun.setObjectName("cb_atun")
        self.cb_pimiento = QtWidgets.QCheckBox(Pizza)
        self.cb_pimiento.setGeometry(QtCore.QRect(100, 110, 71, 31))
        self.cb_pimiento.setObjectName("cb_pimiento")
        self.checkBox_3 = QtWidgets.QCheckBox(Pizza)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 140, 71, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.lbl_resultado = QtWidgets.QLabel(Pizza)
        self.lbl_resultado.setGeometry(QtCore.QRect(10, 210, 381, 61))
        self.lbl_resultado.setText("")
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.lbl_selecc = QtWidgets.QLabel(Pizza)
        self.lbl_selecc.setGeometry(QtCore.QRect(80, 50, 121, 21))
        self.lbl_selecc.setObjectName("lbl_selecc")

        self.retranslateUi(Pizza)
        QtCore.QMetaObject.connectSlotsByName(Pizza)

    def retranslateUi(self, Pizza):
        _translate = QtCore.QCoreApplication.translate
        Pizza.setWindowTitle(_translate("Pizza", "Pizza"))
        self.lbl_titulo.setText(_translate("Pizza", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">El precio base de la pizza es de 15 euros</span></p></body></html>"))
        self.cb_atun.setText(_translate("Pizza", "Atún"))
        self.cb_pimiento.setText(_translate("Pizza", "Pimiento"))
        self.checkBox_3.setText(_translate("Pizza", "Setas"))
        self.lbl_selecc.setText(_translate("Pizza", "Seleccione extras:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pizza = QtWidgets.QDialog()
    ui = Ui_Pizza()
    ui.setupUi(Pizza)
    Pizza.show()
    sys.exit(app.exec_())
