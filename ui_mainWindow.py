# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionDot = QAction(MainWindow)
        self.actionDot.setObjectName(u"actionDot")
        self.actionLine = QAction(MainWindow)
        self.actionLine.setObjectName(u"actionLine")
        self.actionRectnagle = QAction(MainWindow)
        self.actionRectnagle.setObjectName(u"actionRectnagle")
        self.actionElips = QAction(MainWindow)
        self.actionElips.setObjectName(u"actionElips")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menuObject = QMenu(self.menubar)
        self.menuObject.setObjectName(u"menuObject")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuObject.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuObject.addAction(self.actionDot)
        self.menuObject.addAction(self.actionLine)
        self.menuObject.addAction(self.actionRectnagle)
        self.menuObject.addAction(self.actionElips)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDot.setText(QCoreApplication.translate("MainWindow", u"Dot", None))
        self.actionLine.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.actionRectnagle.setText(QCoreApplication.translate("MainWindow", u"Rectnagle", None))
        self.actionElips.setText(QCoreApplication.translate("MainWindow", u"Elipse", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
        self.menuObject.setTitle(QCoreApplication.translate("MainWindow", u"Object", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

