# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(532, 480)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        vtnPrincipal.setFont(font)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblNombre = QLabel(self.centralwidget)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setGeometry(QRect(60, 90, 91, 51))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblNombre.setFont(font1)
        self.lblApellido = QLabel(self.centralwidget)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setGeometry(QRect(50, 150, 101, 41))
        self.lblApellido.setFont(font1)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(150, 150, 281, 31))
        self.txtApellido.setMaxLength(20)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(150, 100, 281, 31))
        self.txtNombre.setMaxLength(20)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(210, 280, 91, 31))
        self.btnGuardar.setFont(font1)
        self.lblcedula = QLabel(self.centralwidget)
        self.lblcedula.setObjectName(u"lblcedula")
        self.lblcedula.setGeometry(QRect(40, 190, 101, 41))
        self.lblcedula.setFont(font1)
        self.txtcedula = QLineEdit(self.centralwidget)
        self.txtcedula.setObjectName(u"txtcedula")
        self.txtcedula.setGeometry(QRect(150, 200, 101, 31))
        self.txtcedula.setMaxLength(20)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 532, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtNombre, self.txtApellido)
        QWidget.setTabOrder(self.txtApellido, self.txtcedula)
        QWidget.setTabOrder(self.txtcedula, self.btnGuardar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"sistema administrativo de persona", None))
        self.lblNombre.setText(QCoreApplication.translate("vtnPrincipal", u"NOMBRE :", None))
        self.lblApellido.setText(QCoreApplication.translate("vtnPrincipal", u"APELLIDO :", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.lblcedula.setText(QCoreApplication.translate("vtnPrincipal", u"       cedula:", None))
    # retranslateUi

