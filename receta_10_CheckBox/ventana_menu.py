# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lista_menu(object):
    def setupUi(self, lista_menu):
        lista_menu.setObjectName("lista_menu")
        lista_menu.resize(440, 300)
        self.lbl_menu = QtWidgets.QLabel(lista_menu)
        self.lbl_menu.setGeometry(QtCore.QRect(190, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana Pro Cond Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_menu.setFont(font)
        self.lbl_menu.setObjectName("lbl_menu")
        self.lbl_sele_hel = QtWidgets.QLabel(lista_menu)
        self.lbl_sele_hel.setGeometry(QtCore.QRect(70, 70, 101, 16))
        self.lbl_sele_hel.setObjectName("lbl_sele_hel")
        self.lbl_sele_beb = QtWidgets.QLabel(lista_menu)
        self.lbl_sele_beb.setGeometry(QtCore.QRect(270, 70, 101, 20))
        self.lbl_sele_beb.setObjectName("lbl_sele_beb")
        self.groupBox_helados = QtWidgets.QGroupBox(lista_menu)
        self.groupBox_helados.setGeometry(QtCore.QRect(30, 100, 171, 131))
        self.groupBox_helados.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.groupBox_helados.setCheckable(True)
        self.groupBox_helados.setChecked(True)
        self.groupBox_helados.setObjectName("groupBox_helados")
        self.cb_choco = QtWidgets.QCheckBox(self.groupBox_helados)
        self.cb_choco.setGeometry(QtCore.QRect(20, 30, 101, 17))
        self.cb_choco.setObjectName("cb_choco")
        self.cb_fresa = QtWidgets.QCheckBox(self.groupBox_helados)
        self.cb_fresa.setGeometry(QtCore.QRect(20, 50, 91, 17))
        self.cb_fresa.setObjectName("cb_fresa")
        self.cb_frutos = QtWidgets.QCheckBox(self.groupBox_helados)
        self.cb_frutos.setGeometry(QtCore.QRect(20, 70, 131, 17))
        self.cb_frutos.setObjectName("cb_frutos")
        self.cb_kinder = QtWidgets.QCheckBox(self.groupBox_helados)
        self.cb_kinder.setGeometry(QtCore.QRect(20, 90, 111, 17))
        self.cb_kinder.setObjectName("cb_kinder")
        self.groupBox_bebidas = QtWidgets.QGroupBox(lista_menu)
        self.groupBox_bebidas.setGeometry(QtCore.QRect(230, 100, 181, 131))
        self.groupBox_bebidas.setCheckable(True)
        self.groupBox_bebidas.setObjectName("groupBox_bebidas")
        self.cb_refresco = QtWidgets.QCheckBox(self.groupBox_bebidas)
        self.cb_refresco.setGeometry(QtCore.QRect(40, 30, 91, 17))
        self.cb_refresco.setObjectName("cb_refresco")
        self.cb_agua = QtWidgets.QCheckBox(self.groupBox_bebidas)
        self.cb_agua.setGeometry(QtCore.QRect(40, 50, 70, 17))
        self.cb_agua.setObjectName("cb_agua")
        self.cb_cerveza = QtWidgets.QCheckBox(self.groupBox_bebidas)
        self.cb_cerveza.setGeometry(QtCore.QRect(40, 70, 121, 17))
        self.cb_cerveza.setObjectName("cb_cerveza")
        self.lbl_resultado = QtWidgets.QLabel(lista_menu)
        self.lbl_resultado.setGeometry(QtCore.QRect(100, 250, 241, 21))
        self.lbl_resultado.setObjectName("lbl_resultado")

        self.retranslateUi(lista_menu)
        QtCore.QMetaObject.connectSlotsByName(lista_menu)

    def retranslateUi(self, lista_menu):
        _translate = QtCore.QCoreApplication.translate
        lista_menu.setWindowTitle(_translate("lista_menu", "lista_menu"))
        self.lbl_menu.setText(_translate("lista_menu", "<html><head/><body><p><span style=\" font-size:14pt; color:#005500;\">Menú</span></p></body></html>"))
        self.lbl_sele_hel.setText(_translate("lista_menu", "Seleccione su Helado"))
        self.lbl_sele_beb.setText(_translate("lista_menu", "Seleccione su Bebida"))
        self.groupBox_helados.setTitle(_translate("lista_menu", "HELADOS"))
        self.cb_choco.setText(_translate("lista_menu", "Chocolate 2 €"))
        self.cb_fresa.setText(_translate("lista_menu", "Fresa 2 €"))
        self.cb_frutos.setText(_translate("lista_menu", "Frutos del Bosque 3€"))
        self.cb_kinder.setText(_translate("lista_menu", "Kinder Bueno 3 €"))
        self.groupBox_bebidas.setTitle(_translate("lista_menu", "BEBIDAS"))
        self.cb_refresco.setText(_translate("lista_menu", "Refresco 2€"))
        self.cb_agua.setText(_translate("lista_menu", "Agua 1€"))
        self.cb_cerveza.setText(_translate("lista_menu", "Caña Cerveza 1,50€"))
        self.lbl_resultado.setText(_translate("lista_menu", "<html><head/><body><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lista_menu = QtWidgets.QDialog()
    ui = Ui_lista_menu()
    ui.setupUi(lista_menu)
    lista_menu.show()
    sys.exit(app.exec_())
