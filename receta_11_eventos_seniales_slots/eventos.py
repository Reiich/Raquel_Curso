# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventos.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventoDialog(object):
    def setupUi(self, EventoDialog):
        EventoDialog.setObjectName("EventoDialog")
        EventoDialog.resize(359, 253)
        self.text = QtWidgets.QLineEdit(EventoDialog)
        self.text.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.text.setObjectName("text")
        self.btn_limpiar = QtWidgets.QPushButton(EventoDialog)
        self.btn_limpiar.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.btn_limpiar.setObjectName("btn_limpiar")

        self.retranslateUi(EventoDialog)
        self.btn_limpiar.clicked.connect(self.text.clear)
        QtCore.QMetaObject.connectSlotsByName(EventoDialog)

    def retranslateUi(self, EventoDialog):
        _translate = QtCore.QCoreApplication.translate
        EventoDialog.setWindowTitle(_translate("EventoDialog", "Señales y Slots"))
        self.btn_limpiar.setText(_translate("EventoDialog", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EventoDialog = QtWidgets.QDialog()
    ui = Ui_EventoDialog()
    ui.setupUi(EventoDialog)
    EventoDialog.show()
    sys.exit(app.exec_())
