# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(250, 20, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(26)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.res_dol = QtWidgets.QLabel(self.centralwidget)
        self.res_dol.setGeometry(QtCore.QRect(420, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.res_dol.setFont(font)
        self.res_dol.setText("")
        self.res_dol.setObjectName("res_dol")
        self.res_lib = QtWidgets.QLabel(self.centralwidget)
        self.res_lib.setGeometry(QtCore.QRect(420, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.res_lib.setFont(font)
        self.res_lib.setText("")
        self.res_lib.setObjectName("res_lib")
        self.res_pes = QtWidgets.QLabel(self.centralwidget)
        self.res_pes.setGeometry(QtCore.QRect(420, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.res_pes.setFont(font)
        self.res_pes.setText("")
        self.res_pes.setObjectName("res_pes")
        self.bot_dol = QtWidgets.QPushButton(self.centralwidget)
        self.bot_dol.setGeometry(QtCore.QRect(490, 90, 131, 31))
        self.bot_dol.setObjectName("bot_dol")
        self.bot_lib = QtWidgets.QPushButton(self.centralwidget)
        self.bot_lib.setGeometry(QtCore.QRect(490, 130, 131, 31))
        self.bot_lib.setObjectName("bot_lib")
        self.bot_pes = QtWidgets.QPushButton(self.centralwidget)
        self.bot_pes.setGeometry(QtCore.QRect(490, 170, 131, 31))
        self.bot_pes.setObjectName("bot_pes")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 90, 353, 113))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Entrada_dol = QtWidgets.QLineEdit(self.widget)
        self.Entrada_dol.setObjectName("Entrada_dol")
        self.gridLayout.addWidget(self.Entrada_dol, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Entrada_lib = QtWidgets.QLineEdit(self.widget)
        self.Entrada_lib.setObjectName("Entrada_lib")
        self.gridLayout.addWidget(self.Entrada_lib, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.Entrada_pes = QtWidgets.QLineEdit(self.widget)
        self.Entrada_pes.setObjectName("Entrada_pes")
        self.gridLayout.addWidget(self.Entrada_pes, 2, 1, 1, 1)
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
        self.bot_dol.setText(_translate("MainWindow", "Convertir"))
        self.bot_lib.setText(_translate("MainWindow", "Convertir"))
        self.bot_pes.setText(_translate("MainWindow", "Convertir"))
        self.label.setText(_translate("MainWindow", "Introduce Dólares"))
        self.label_2.setText(_translate("MainWindow", "Introduce Libras"))
        self.label_3.setText(_translate("MainWindow", "Introduce Pesos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
