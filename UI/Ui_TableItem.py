# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableItem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import CheckBox
from qfluentwidgets import ToolButton
from qfluentwidgets import TransparentToolButton
from qfluentwidgets import BodyLabel
from qfluentwidgets import ImageLabel
from qfluentwidgets import AvatarWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1049, 66)
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CheckBox = CheckBox(self.widget_3)
        self.CheckBox.setObjectName(u"CheckBox")

        self.verticalLayout.addWidget(self.CheckBox)


        self.horizontalLayout_4.addWidget(self.widget_3)

        self.NumberLabel = BodyLabel(Form)
        self.NumberLabel.setObjectName(u"NumberLabel")

        self.horizontalLayout_4.addWidget(self.NumberLabel)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.AccountAvatar = AvatarWidget(self.widget_2)
        self.AccountAvatar.setObjectName(u"AccountAvatar")
        self.AccountAvatar.setRadius(15)

        self.horizontalLayout_2.addWidget(self.AccountAvatar)

        self.UserName = BodyLabel(self.widget_2)
        self.UserName.setObjectName(u"UserName")

        self.horizontalLayout_2.addWidget(self.UserName)


        self.horizontalLayout_4.addWidget(self.widget_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.PlatformAvatar = AvatarWidget(self.widget)
        self.PlatformAvatar.setObjectName(u"PlatformAvatar")
        self.PlatformAvatar.setMinimumSize(QSize(30, 30))
        self.PlatformAvatar.setMaximumSize(QSize(30, 30))
        self.PlatformAvatar.setRadius(15)

        self.horizontalLayout_3.addWidget(self.PlatformAvatar)

        self.PlatformName = BodyLabel(self.widget)
        self.PlatformName.setObjectName(u"PlatformName")

        self.horizontalLayout_3.addWidget(self.PlatformName)


        self.horizontalLayout_4.addWidget(self.widget)

        self.Operator = BodyLabel(Form)
        self.Operator.setObjectName(u"Operator")

        self.horizontalLayout_4.addWidget(self.Operator)

        self.Groups = BodyLabel(Form)
        self.Groups.setObjectName(u"Groups")

        self.horizontalLayout_4.addWidget(self.Groups)

        self.status = BodyLabel(Form)
        self.status.setObjectName(u"status")

        self.horizontalLayout_4.addWidget(self.status)

        self.Operation = QWidget(Form)
        self.Operation.setObjectName(u"Operation")
        self.horizontalLayout = QHBoxLayout(self.Operation)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Topping = TransparentToolButton(self.Operation)
        self.Topping.setObjectName(u"Topping")

        self.horizontalLayout.addWidget(self.Topping)

        self.Edit = TransparentToolButton(self.Operation)
        self.Edit.setObjectName(u"Edit")

        self.horizontalLayout.addWidget(self.Edit)

        self.Delete = TransparentToolButton(self.Operation)
        self.Delete.setObjectName(u"Delete")

        self.horizontalLayout.addWidget(self.Delete)


        self.horizontalLayout_4.addWidget(self.Operation)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.CheckBox.setText("")
        self.NumberLabel.setText(QCoreApplication.translate("Form", u"\u5e8f\u53f7", None))
        self.UserName.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.PlatformName.setText(QCoreApplication.translate("Form", u"\u5e73\u53f0\u540d", None))
        self.Operator.setText(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u8005", None))
        self.Groups.setText(QCoreApplication.translate("Form", u"\u5206\u7ec4", None))
        self.status.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
    # retranslateUi

