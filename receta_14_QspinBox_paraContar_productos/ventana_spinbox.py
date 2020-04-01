# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_spinbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(484, 174)
        self.lbl_val_t = QtWidgets.QLabel(Dialog)
        self.lbl_val_t.setGeometry(QtCore.QRect(30, 100, 71, 16))
        self.lbl_val_t.setObjectName("lbl_val_t")
        self.txt_val_mouse = QtWidgets.QLineEdit(Dialog)
        self.txt_val_mouse.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.txt_val_mouse.setObjectName("txt_val_mouse")
        self.spinBox_mouse = QtWidgets.QSpinBox(Dialog)
        self.spinBox_mouse.setGeometry(QtCore.QRect(250, 40, 51, 22))
        self.spinBox_mouse.setProperty("value", 3)
        self.spinBox_mouse.setObjectName("spinBox_mouse")
        self.txt_mouse = QtWidgets.QLineEdit(Dialog)
        self.txt_mouse.setGeometry(QtCore.QRect(330, 40, 113, 21))
        self.txt_mouse.setObjectName("txt_mouse")
        self.lbl_val_m = QtWidgets.QLabel(Dialog)
        self.lbl_val_m.setGeometry(QtCore.QRect(30, 40, 71, 16))
        self.lbl_val_m.setObjectName("lbl_val_m")
        self.spinBox_teclado = QtWidgets.QSpinBox(Dialog)
        self.spinBox_teclado.setGeometry(QtCore.QRect(250, 100, 51, 22))
        self.spinBox_teclado.setProperty("value", 3)
        self.spinBox_teclado.setObjectName("spinBox_teclado")
        self.txt_teclado = QtWidgets.QLineEdit(Dialog)
        self.txt_teclado.setGeometry(QtCore.QRect(330, 100, 113, 21))
        self.txt_teclado.setObjectName("txt_teclado")
        self.txt_val_teclado = QtWidgets.QLineEdit(Dialog)
        self.txt_val_teclado.setGeometry(QtCore.QRect(110, 100, 113, 20))
        self.txt_val_teclado.setObjectName("txt_val_teclado")
        self.lbl_resultado = QtWidgets.QLabel(Dialog)
        self.lbl_resultado.setGeometry(QtCore.QRect(370, 140, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_resultado.setFont(font)
        self.lbl_resultado.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_resultado.setObjectName("lbl_resultado")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_val_t.setText(_translate("Dialog", "Valor Teclado"))
        self.txt_val_mouse.setText(_translate("Dialog", "60"))
        self.txt_mouse.setText(_translate("Dialog", "180"))
        self.lbl_val_m.setText(_translate("Dialog", "Valor Mouse"))
        self.txt_teclado.setText(_translate("Dialog", "270"))
        self.txt_val_teclado.setText(_translate("Dialog", "90"))
        self.lbl_resultado.setText(_translate("Dialog", "450"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
