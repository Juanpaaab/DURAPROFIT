# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Interfaz1(object):
    def setupUi(self, Interfaz1):
        Interfaz1.setObjectName("Interfaz1")
        Interfaz1.resize(1366, 768)
        Interfaz1.setMinimumSize(QtCore.QSize(1366, 768))
        Interfaz1.setMaximumSize(QtCore.QSize(1366, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../duraprov.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Interfaz1.setWindowIcon(icon)
        Interfaz1.setStyleSheet("background-color:rgb(5, 51, 74);")
        self.centralwidget = QtWidgets.QWidget(Interfaz1)
        self.centralwidget.setObjectName("centralwidget")
        self.ConectarTrex = QtWidgets.QPushButton(self.centralwidget)
        self.ConectarTrex.setGeometry(QtCore.QRect(440, 280, 431, 301))
        self.ConectarTrex.setStyleSheet("background:rgb(47, 168, 170); color:white;\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
" border-radius: 15;")
        self.ConectarTrex.setObjectName("ConectarTrex")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 80, 761, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("DURAPROFIT INVI.png"))
        self.label.setObjectName("label")
        self.Warning0 = QtWidgets.QLabel(self.centralwidget)
        self.Warning0.setGeometry(QtCore.QRect(290, 610, 771, 51))
        self.Warning0.setStyleSheet("background: none;\n"
"font: 19.5pt \"MS Shell Dlg 2\";\n"
"color: RED;\n"
"")
        self.Warning0.setObjectName("Warning0")
        self.label.raise_()
        self.ConectarTrex.raise_()
        self.Warning0.raise_()
        Interfaz1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Interfaz1)
        QtCore.QMetaObject.connectSlotsByName(Interfaz1)

    def retranslateUi(self, Interfaz1):
        _translate = QtCore.QCoreApplication.translate
        Interfaz1.setWindowTitle(_translate("Interfaz1", "DURAPROFIT"))
        self.ConectarTrex.setText(_translate("Interfaz1", "Conectar al minero T-Rex"))
        self.Warning0.setText(_translate("Interfaz1", "RECUERDE ENCENDER PRIMERO EL MINERO T-REX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Interfaz1 = QtWidgets.QMainWindow()
    ui = Ui_Interfaz1()
    ui.setupUi(Interfaz1)
    Interfaz1.show()
    sys.exit(app.exec_())
