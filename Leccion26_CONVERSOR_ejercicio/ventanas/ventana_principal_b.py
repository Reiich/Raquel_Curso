# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal_b.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.cantidad.setGeometry(QtCore.QRect(260, 80, 111, 31))
        self.cantidad.setObjectName("cantidad")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(250, 20, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(26)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.usa_b = QtWidgets.QLabel(self.centralwidget)
        self.usa_b.setGeometry(QtCore.QRect(270, 140, 61, 31))
        self.usa_b.setStyleSheet("border-image: url(:/usa/usa.jpg);")
        self.usa_b.setText("")
        self.usa_b.setObjectName("usa_b")
        self.ru_b = QtWidgets.QLabel(self.centralwidget)
        self.ru_b.setGeometry(QtCore.QRect(360, 140, 61, 31))
        self.ru_b.setStyleSheet("border-image: url(:/ru/reino-unido.png);")
        self.ru_b.setText("")
        self.ru_b.setObjectName("ru_b")
        self.mex_b = QtWidgets.QLabel(self.centralwidget)
        self.mex_b.setGeometry(QtCore.QRect(450, 130, 61, 51))
        self.mex_b.setStyleSheet("border-image: url(:/mex/mex.png);")
        self.mex_b.setText("")
        self.mex_b.setObjectName("mex_b")
        self.resultado = QtWidgets.QLabel(self.centralwidget)
        self.resultado.setGeometry(QtCore.QRect(400, 80, 151, 31))
        self.resultado.setText("")
        self.resultado.setObjectName("resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "v_conversor"))
        self.titulo.setText(_translate("MainWindow", "Conversor a Euros"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
