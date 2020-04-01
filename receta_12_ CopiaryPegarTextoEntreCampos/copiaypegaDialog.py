# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'copiaypegaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CopiaPegaDialog(object):
    def setupUi(self, CopiaPegaDialog):
        CopiaPegaDialog.setObjectName("CopiaPegaDialog")
        CopiaPegaDialog.resize(397, 300)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        CopiaPegaDialog.setFont(font)
        CopiaPegaDialog.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text_1 = QtWidgets.QLineEdit(CopiaPegaDialog)
        self.text_1.setGeometry(QtCore.QRect(20, 50, 361, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.text_1.setFont(font)
        self.text_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QLineEdit(CopiaPegaDialog)
        self.text_2.setGeometry(QtCore.QRect(20, 240, 361, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.text_2.setFont(font)
        self.text_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.text_2.setObjectName("text_2")
        self.btn_copy = QtWidgets.QPushButton(CopiaPegaDialog)
        self.btn_copy.setGeometry(QtCore.QRect(160, 100, 75, 23))
        self.btn_copy.setObjectName("btn_copy")
        self.btn_paste = QtWidgets.QPushButton(CopiaPegaDialog)
        self.btn_paste.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.btn_paste.setObjectName("btn_paste")

        self.retranslateUi(CopiaPegaDialog)
        self.btn_copy.pressed.connect(self.text_1.selectAll)
        self.btn_paste.clicked.connect(self.text_2.paste)
        self.btn_copy.released.connect(self.text_1.copy)
        QtCore.QMetaObject.connectSlotsByName(CopiaPegaDialog)

    def retranslateUi(self, CopiaPegaDialog):
        _translate = QtCore.QCoreApplication.translate
        CopiaPegaDialog.setWindowTitle(_translate("CopiaPegaDialog", "Copia y Pega"))
        self.btn_copy.setText(_translate("CopiaPegaDialog", "Copiar"))
        self.btn_paste.setText(_translate("CopiaPegaDialog", "Pegar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CopiaPegaDialog = QtWidgets.QDialog()
    ui = Ui_CopiaPegaDialog()
    ui.setupUi(CopiaPegaDialog)
    CopiaPegaDialog.show()
    sys.exit(app.exec_())
