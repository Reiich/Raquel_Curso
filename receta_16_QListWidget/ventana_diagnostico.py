# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_diagnostico.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_diagnosticosDIalog(object):
    def setupUi(self, diagnosticosDIalog):
        diagnosticosDIalog.setObjectName("diagnosticosDIalog")
        diagnosticosDIalog.resize(442, 315)
        self.lbl1 = QtWidgets.QLabel(diagnosticosDIalog)
        self.lbl1.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.lbl1.setObjectName("lbl1")
        self.lst_disponibles = QtWidgets.QListWidget(diagnosticosDIalog)
        self.lst_disponibles.setGeometry(QtCore.QRect(70, 40, 301, 91))
        self.lst_disponibles.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lst_disponibles.setObjectName("lst_disponibles")
        item = QtWidgets.QListWidgetItem()
        self.lst_disponibles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_disponibles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_disponibles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_disponibles.addItem(item)
        self.lbl2 = QtWidgets.QLabel(diagnosticosDIalog)
        self.lbl2.setGeometry(QtCore.QRect(20, 170, 131, 31))
        self.lbl2.setObjectName("lbl2")
        self.lst_seleccionados = QtWidgets.QListWidget(diagnosticosDIalog)
        self.lst_seleccionados.setGeometry(QtCore.QRect(70, 200, 301, 91))
        self.lst_seleccionados.setObjectName("lst_seleccionados")

        self.retranslateUi(diagnosticosDIalog)
        QtCore.QMetaObject.connectSlotsByName(diagnosticosDIalog)

    def retranslateUi(self, diagnosticosDIalog):
        _translate = QtCore.QCoreApplication.translate
        diagnosticosDIalog.setWindowTitle(_translate("diagnosticosDIalog", "Selección Diagnósticos"))
        self.lbl1.setText(_translate("diagnosticosDIalog", "Diagnósticos disponibles"))
        __sortingEnabled = self.lst_disponibles.isSortingEnabled()
        self.lst_disponibles.setSortingEnabled(False)
        item = self.lst_disponibles.item(0)
        item.setText(_translate("diagnosticosDIalog", "Rayos X - 5$"))
        item = self.lst_disponibles.item(1)
        item.setText(_translate("diagnosticosDIalog", "Nivel de Azúcar - 3$"))
        item = self.lst_disponibles.item(2)
        item.setText(_translate("diagnosticosDIalog", "Prueba de hemoglobina - 2$"))
        item = self.lst_disponibles.item(3)
        item.setText(_translate("diagnosticosDIalog", "Análisis de Orina - 3.25 $"))
        self.lst_disponibles.setSortingEnabled(__sortingEnabled)
        self.lbl2.setText(_translate("diagnosticosDIalog", "Diagnósticos escogidos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    diagnosticosDIalog = QtWidgets.QDialog()
    ui = Ui_diagnosticosDIalog()
    ui.setupUi(diagnosticosDIalog)
    diagnosticosDIalog.show()
    sys.exit(app.exec_())
