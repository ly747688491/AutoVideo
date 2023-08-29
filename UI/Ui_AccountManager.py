# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AccountManager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import CheckBox
from qfluentwidgets import EditableComboBox
from qfluentwidgets import PushButton
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import PillPushButton
from qfluentwidgets import ToolButton
from qfluentwidgets import TransparentToolButton
from qfluentwidgets import ToggleButton
from qfluentwidgets import CaptionLabel
from qfluentwidgets import BodyLabel
from qfluentwidgets import LineEdit
from qfluentwidgets import SearchLineEdit


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1124, 785)
        palette = QPalette()
        brush = QBrush(QColor(34, 34, 34, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        Form.setPalette(palette)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 1091, 771))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.CaptionLabel_4 = CaptionLabel(self.layoutWidget)
        self.CaptionLabel_4.setObjectName(u"CaptionLabel_4")

        self.horizontalLayout_4.addWidget(self.CaptionLabel_4)

        self.CaptionLabel_2 = CaptionLabel(self.layoutWidget)
        self.CaptionLabel_2.setObjectName(u"CaptionLabel_2")

        self.horizontalLayout_4.addWidget(self.CaptionLabel_2)

        self.CaptionLabel = CaptionLabel(self.layoutWidget)
        self.CaptionLabel.setObjectName(u"CaptionLabel")

        self.horizontalLayout_4.addWidget(self.CaptionLabel)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.AddAccounButton = PrimaryPushButton(self.layoutWidget)
        self.AddAccounButton.setObjectName(u"AddAccounButton")

        self.horizontalLayout_2.addWidget(self.AddAccounButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.SetOperatorButton = PrimaryPushButton(self.layoutWidget)
        self.SetOperatorButton.setObjectName(u"SetOperatorButton")

        self.horizontalLayout.addWidget(self.SetOperatorButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.SetGroupButton = PushButton(self.layoutWidget)
        self.SetGroupButton.setObjectName(u"SetGroupButton")

        self.horizontalLayout.addWidget(self.SetGroupButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.GroupManagerButton = PushButton(self.layoutWidget)
        self.GroupManagerButton.setObjectName(u"GroupManagerButton")

        self.horizontalLayout.addWidget(self.GroupManagerButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.DetectionButon = PillPushButton(self.layoutWidget)
        self.DetectionButon.setObjectName(u"DetectionButon")

        self.horizontalLayout.addWidget(self.DetectionButon)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)

        self.PlatformComboBox = EditableComboBox(self.layoutWidget)
        self.PlatformComboBox.setObjectName(u"PlatformComboBox")

        self.horizontalLayout_3.addWidget(self.PlatformComboBox)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.OperatorComboBox = EditableComboBox(self.layoutWidget)
        self.OperatorComboBox.setObjectName(u"OperatorComboBox")

        self.horizontalLayout_3.addWidget(self.OperatorComboBox)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.StatusComboBox = EditableComboBox(self.layoutWidget)
        self.StatusComboBox.setObjectName(u"StatusComboBox")

        self.horizontalLayout_3.addWidget(self.StatusComboBox)

        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.KeywordEdit = SearchLineEdit(self.layoutWidget)
        self.KeywordEdit.setObjectName(u"KeywordEdit")

        self.horizontalLayout_3.addWidget(self.KeywordEdit)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.GroupComboBox = EditableComboBox(self.layoutWidget)
        self.GroupComboBox.setObjectName(u"GroupComboBox")

        self.horizontalLayout_3.addWidget(self.GroupComboBox)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.ResetButton = PushButton(self.layoutWidget)
        self.ResetButton.setObjectName(u"ResetButton")

        self.horizontalLayout_3.addWidget(self.ResetButton)

        self.horizontalSpacer_13 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.TableWidget = QWidget(self.layoutWidget)
        self.TableWidget.setObjectName(u"TableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableWidget.sizePolicy().hasHeightForWidth())
        self.TableWidget.setSizePolicy(sizePolicy)
        self.widget = QWidget(self.TableWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 1041, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.SelectAll = CheckBox(self.widget)
        self.SelectAll.setObjectName(u"SelectAll")
        self.SelectAll.setMaximumSize(QSize(100, 20))

        self.horizontalLayout_5.addWidget(self.SelectAll)

        self.SerialNumber = BodyLabel(self.widget)
        self.SerialNumber.setObjectName(u"SerialNumber")
        self.SerialNumber.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.SerialNumber)

        self.horizontalSpacer_16 = QSpacerItem(10, 10, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_16)

        self.Account = BodyLabel(self.widget)
        self.Account.setObjectName(u"Account")
        self.Account.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.Account)

        self.Platform = BodyLabel(self.widget)
        self.Platform.setObjectName(u"Platform")
        self.Platform.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.Platform)

        self.Operator = BodyLabel(self.widget)
        self.Operator.setObjectName(u"Operator")
        self.Operator.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.Operator)

        self.Groups = BodyLabel(self.widget)
        self.Groups.setObjectName(u"Groups")
        self.Groups.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.Groups)

        self.State = BodyLabel(self.widget)
        self.State.setObjectName(u"State")

        self.horizontalLayout_5.addWidget(self.State)

        self.Operation = BodyLabel(self.widget)
        self.Operation.setObjectName(u"Operation")

        self.horizontalLayout_5.addWidget(self.Operation)

        self.widget1 = QWidget(self.TableWidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 60, 1041, 481))
        self.verticalLayout_2 = QVBoxLayout(self.widget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Datawidget = QWidget(self.widget1)
        self.Datawidget.setObjectName(u"Datawidget")
        self.verticalLayoutWidget = QWidget(self.Datawidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 1041, 401))
        self.DataverticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.DataverticalLayout.setObjectName(u"DataverticalLayout")
        self.DataverticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.Datawidget)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.LeftPageButton = TransparentToolButton(self.widget1)
        self.LeftPageButton.setObjectName(u"LeftPageButton")

        self.horizontalLayout_7.addWidget(self.LeftPageButton)

        self.CurrentPageLabel = CaptionLabel(self.widget1)
        self.CurrentPageLabel.setObjectName(u"CurrentPageLabel")

        self.horizontalLayout_7.addWidget(self.CurrentPageLabel)

        self.PageCountLabel = CaptionLabel(self.widget1)
        self.PageCountLabel.setObjectName(u"PageCountLabel")

        self.horizontalLayout_7.addWidget(self.PageCountLabel)

        self.RightPageButton = TransparentToolButton(self.widget1)
        self.RightPageButton.setObjectName(u"RightPageButton")

        self.horizontalLayout_7.addWidget(self.RightPageButton)

        self.PageCountComboBox = EditableComboBox(self.widget1)
        self.PageCountComboBox.setObjectName(u"PageCountComboBox")

        self.horizontalLayout_7.addWidget(self.PageCountComboBox)

        self.horizontalSpacer_15 = QSpacerItem(900, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout_6.addWidget(self.TableWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.CaptionLabel_4.setText(QCoreApplication.translate("Form", u"\u9996\u9875", None))
        self.CaptionLabel_2.setText(QCoreApplication.translate("Form", u">", None))
        self.CaptionLabel.setText(QCoreApplication.translate("Form", u"\u8d26\u53f7\u7ba1\u7406", None))
        self.AddAccounButton.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u8d26\u53f7", None))
        self.SetOperatorButton.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u8fd0\u8425\u4eba", None))
        self.SetGroupButton.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\u5206\u7ec4", None))
        self.GroupManagerButton.setText(QCoreApplication.translate("Form", u"\u5206\u7ec4\u7ba1\u7406", None))
        self.DetectionButon.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u68c0\u6d4b\u8d26\u6237\u72b6\u6001", None))
        self.PlatformComboBox.setText("")
        self.PlatformComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u5e73\u53f0", None))
        self.OperatorComboBox.setText("")
        self.OperatorComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u8fd0\u8425\u4eba", None))
        self.StatusComboBox.setText("")
        self.StatusComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u8d26\u53f7\u72b6\u6001", None))
        self.KeywordEdit.setText("")
        self.KeywordEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5173\u952e\u8bcd", None))
        self.GroupComboBox.setText("")
        self.GroupComboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u5206\u7ec4", None))
        self.ResetButton.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.SelectAll.setText("")
        self.SerialNumber.setText(QCoreApplication.translate("Form", u"\u5e8f\u53f7", None))
        self.Account.setText(QCoreApplication.translate("Form", u"\u8d26\u6237", None))
        self.Platform.setText(QCoreApplication.translate("Form", u"\u5e73\u53f0", None))
        self.Operator.setText(QCoreApplication.translate("Form", u"\u8fd0\u8425\u4eba", None))
        self.Groups.setText(QCoreApplication.translate("Form", u"\u5206\u7ec4", None))
        self.State.setText(QCoreApplication.translate("Form", u"\u72b6\u6001", None))
        self.Operation.setText(QCoreApplication.translate("Form", u"\u64cd\u4f5c", None))
        self.CurrentPageLabel.setText(QCoreApplication.translate("Form", u"1", None))
        self.PageCountLabel.setText(QCoreApplication.translate("Form", u"/1", None))
    # retranslateUi

