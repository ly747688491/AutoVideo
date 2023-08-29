# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Platform.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import ToolButton
from qfluentwidgets import TransparentToolButton
from qfluentwidgets import CardWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 682)
        Form.setMinimumSize(QSize(800, 682))
        Form.setMaximumSize(QSize(800, 682))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.widget_1 = QWidget(Form)
        self.widget_1.setObjectName(u"widget_1")
        self.imagelabel = QLabel(self.widget_1)
        self.imagelabel.setObjectName(u"imagelabel")
        self.imagelabel.setGeometry(QRect(15, 10, 60, 60))
        self.imagelabel.setPixmap(QPixmap(u"../resources/Icon/baijiahao.jpg"))
        self.imagelabel.setScaledContents(True)
        self.text_label = QLabel(self.widget_1)
        self.text_label.setObjectName(u"text_label")
        self.text_label.setGeometry(QRect(5, 70, 80, 20))
        self.text_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.widget_1, 0, 1, 1, 1)

        self.widget_8 = QWidget(Form)
        self.widget_8.setObjectName(u"widget_8")

        self.gridLayout.addWidget(self.widget_8, 1, 0, 1, 1)

        self.widget_32 = QWidget(Form)
        self.widget_32.setObjectName(u"widget_32")

        self.gridLayout.addWidget(self.widget_32, 4, 0, 1, 1)

        self.widget_40 = QWidget(Form)
        self.widget_40.setObjectName(u"widget_40")

        self.gridLayout.addWidget(self.widget_40, 5, 0, 1, 1)

        self.widget_16 = QWidget(Form)
        self.widget_16.setObjectName(u"widget_16")

        self.gridLayout.addWidget(self.widget_16, 2, 0, 1, 1)

        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout.addWidget(self.widget_4, 0, 4, 1, 1)

        self.widget_5 = QWidget(Form)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout.addWidget(self.widget_5, 0, 5, 1, 1)

        self.widget_6 = QWidget(Form)
        self.widget_6.setObjectName(u"widget_6")

        self.gridLayout.addWidget(self.widget_6, 0, 6, 1, 1)

        self.widget_24 = QWidget(Form)
        self.widget_24.setObjectName(u"widget_24")

        self.gridLayout.addWidget(self.widget_24, 3, 0, 1, 1)

        self.widget_48 = QWidget(Form)
        self.widget_48.setObjectName(u"widget_48")

        self.gridLayout.addWidget(self.widget_48, 6, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)

        self.widget_7 = QWidget(Form)
        self.widget_7.setObjectName(u"widget_7")

        self.gridLayout.addWidget(self.widget_7, 0, 7, 1, 1)

        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout.addWidget(self.widget_3, 0, 3, 1, 1)

        self.baijiahao_Widget = CardWidget(Form)
        self.baijiahao_Widget.setObjectName(u"baijiahao_Widget")
        self.baijiahao_Button = TransparentToolButton(self.baijiahao_Widget)
        self.baijiahao_Button.setObjectName(u"baijiahao_Button")
        self.baijiahao_Button.setGeometry(QRect(5, 5, 80, 80))
        icon = QIcon()
        icon.addFile(u"../resources/Icon/baijiahao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.baijiahao_Button.setIcon(icon)
        self.baijiahao_Button.setIconSize(QSize(80, 80))

        self.gridLayout.addWidget(self.baijiahao_Widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.imagelabel.setText("")
        self.text_label.setText(QCoreApplication.translate("Form", u"\u767e\u5bb6\u53f7", None))
    # retranslateUi

