# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_talla_pago.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        MainWindow.setStyleSheet("\n"
"background-color: rgb(255, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_talla = QtWidgets.QLabel(self.centralwidget)
        self.lbl_talla.setGeometry(QtCore.QRect(50, 40, 91, 16))
        self.lbl_talla.setObjectName("lbl_talla")
        self.lbl_pago = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pago.setGeometry(QtCore.QRect(50, 170, 161, 16))
        self.lbl_pago.setObjectName("lbl_pago")
        self.txt_resultado = QtWidgets.QLabel(self.centralwidget)
        self.txt_resultado.setGeometry(QtCore.QRect(20, 280, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        self.txt_resultado.setFont(font)
        self.txt_resultado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txt_resultado.setObjectName("txt_resultado")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.capaSuperor = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.capaSuperor.setContentsMargins(0, 0, 0, 0)
        self.capaSuperor.setObjectName("capaSuperor")
        self.rbt_s = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbt_s.setObjectName("rbt_s")
        self.capaSuperor.addWidget(self.rbt_s)
        self.rbt_m = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbt_m.setObjectName("rbt_m")
        self.capaSuperor.addWidget(self.rbt_m)
        self.rbt_l = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbt_l.setObjectName("rbt_l")
        self.capaSuperor.addWidget(self.rbt_l)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 200, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.capaInferior = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.capaInferior.setContentsMargins(0, 0, 0, 0)
        self.capaInferior.setObjectName("capaInferior")
        self.rbt_tarjeta = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbt_tarjeta.setObjectName("rbt_tarjeta")
        self.capaInferior.addWidget(self.rbt_tarjeta)
        self.rbt_paypal = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbt_paypal.setObjectName("rbt_paypal")
        self.capaInferior.addWidget(self.rbt_paypal)
        self.rbt_efectivo = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbt_efectivo.setObjectName("rbt_efectivo")
        self.capaInferior.addWidget(self.rbt_efectivo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_talla.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Elija su talla</span></p></body></html>"))
        self.lbl_pago.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Elija el método de pago</span></p><p><br/></p></body></html>"))
        self.txt_resultado.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.rbt_s.setText(_translate("MainWindow", "S"))
        self.rbt_m.setText(_translate("MainWindow", "M"))
        self.rbt_l.setText(_translate("MainWindow", "L"))
        self.rbt_tarjeta.setText(_translate("MainWindow", " Tarjeta Crédito / Débito"))
        self.rbt_paypal.setText(_translate("MainWindow", " Paypal"))
        self.rbt_efectivo.setText(_translate("MainWindow", "Efectivo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
