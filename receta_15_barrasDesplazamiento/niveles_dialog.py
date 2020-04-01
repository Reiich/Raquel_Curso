# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'niveles_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class NivelesDialog(object):
    def setupUi(self, NivelesDialog):
        NivelesDialog.setObjectName("NivelesDialog")
        NivelesDialog.resize(380, 353)
        self.lbl_nivelAzucar = QtWidgets.QLabel(NivelesDialog)
        self.lbl_nivelAzucar.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.lbl_nivelAzucar.setObjectName("lbl_nivelAzucar")
        self.lbl_arterial = QtWidgets.QLabel(NivelesDialog)
        self.lbl_arterial.setGeometry(QtCore.QRect(10, 70, 121, 41))
        self.lbl_arterial.setObjectName("lbl_arterial")
        self.scroll_azucar = QtWidgets.QScrollBar(NivelesDialog)
        self.scroll_azucar.setGeometry(QtCore.QRect(120, 30, 231, 16))
        self.scroll_azucar.setOrientation(QtCore.Qt.Horizontal)
        self.scroll_azucar.setObjectName("scroll_azucar")
        self.sliderPresion = QtWidgets.QSlider(NivelesDialog)
        self.sliderPresion.setGeometry(QtCore.QRect(120, 80, 231, 22))
        self.sliderPresion.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPresion.setObjectName("sliderPresion")
        self.lbl_pulso = QtWidgets.QLabel(NivelesDialog)
        self.lbl_pulso.setGeometry(QtCore.QRect(10, 120, 121, 41))
        self.lbl_pulso.setObjectName("lbl_pulso")
        self.scrollPulso = QtWidgets.QScrollBar(NivelesDialog)
        self.scrollPulso.setGeometry(QtCore.QRect(80, 110, 16, 160))
        self.scrollPulso.setOrientation(QtCore.Qt.Vertical)
        self.scrollPulso.setObjectName("scrollPulso")
        self.lbl_colesterol = QtWidgets.QLabel(NivelesDialog)
        self.lbl_colesterol.setGeometry(QtCore.QRect(210, 120, 121, 41))
        self.lbl_colesterol.setObjectName("lbl_colesterol")
        self.sliderColesterol = QtWidgets.QSlider(NivelesDialog)
        self.sliderColesterol.setGeometry(QtCore.QRect(290, 120, 22, 160))
        self.sliderColesterol.setOrientation(QtCore.Qt.Vertical)
        self.sliderColesterol.setObjectName("sliderColesterol")
        self.txt_resultado = QtWidgets.QLineEdit(NivelesDialog)
        self.txt_resultado.setGeometry(QtCore.QRect(10, 320, 361, 20))
        self.txt_resultado.setReadOnly(True)
        self.txt_resultado.setObjectName("txt_resultado")

        self.retranslateUi(NivelesDialog)
        QtCore.QMetaObject.connectSlotsByName(NivelesDialog)

    def retranslateUi(self, NivelesDialog):
        _translate = QtCore.QCoreApplication.translate
        NivelesDialog.setWindowTitle(_translate("NivelesDialog", "Niveles"))
        self.lbl_nivelAzucar.setText(_translate("NivelesDialog", "Nivel de Azúcar"))
        self.lbl_arterial.setText(_translate("NivelesDialog", "Presión Arterial"))
        self.lbl_pulso.setText(_translate("NivelesDialog", "Pulso"))
        self.lbl_colesterol.setText(_translate("NivelesDialog", "Colesterol"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NivelesDialog = QtWidgets.QDialog()
    ui = Ui_NivelesDialog()
    ui.setupUi(NivelesDialog)
    NivelesDialog.show()
    sys.exit(app.exec_())
