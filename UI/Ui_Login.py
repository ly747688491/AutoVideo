from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QStackedWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 900)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.loginWidget = CardWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginWidget.sizePolicy().hasHeightForWidth())
        self.loginWidget.setSizePolicy(sizePolicy)
        self.loginWidget.setMinimumSize(QtCore.QSize(400, 700))
        self.loginWidget.setMaximumSize(QtCore.QSize(400, 700))
        self.loginWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.loginWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.loginWidget.setBorderRadius(50)
        self.loginWidget.setObjectName("loginWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.loginWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BackgroundPixmap = PixmapLabel(self.loginWidget)
        self.BackgroundPixmap.setObjectName("BackgroundPixmap")
        self.verticalLayout.addWidget(self.BackgroundPixmap)
        self.FormWidget = CardWidget(self.loginWidget)
        self.FormWidget.setObjectName("FormWidget")
        self.layoutWidget = QtWidgets.QWidget(self.FormWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 441))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Pivot = Pivot(self.layoutWidget)
        self.Pivot.setObjectName("Pivot")
        self.verticalLayout_2.addWidget(self.Pivot)
        self.PopUpAniStackedWidget = QStackedWidget(self.layoutWidget)
        self.PopUpAniStackedWidget.setObjectName("PopUpAniStackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.layoutWidget1 = QtWidgets.QWidget(self.page)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 100, 341, 129))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.userNameLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.userNameLayout.setContentsMargins(0, 0, 0, 0)
        self.userNameLayout.setObjectName("userNameLayout")
        self.userNameEdit = LineEdit(self.layoutWidget1)
        self.userNameEdit.setObjectName("userNameEdit")
        self.userNameLayout.addWidget(self.userNameEdit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.passWordEdit = LineEdit(self.layoutWidget1)
        self.passWordEdit.setObjectName("passWordEdit")
        self.passWordEdit.setEchoMode(self.passWordEdit.Password)
        self.userNameLayout.addWidget(self.passWordEdit)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.PopUpAniStackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 95, 341, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.PhoneFormLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.PhoneFormLayout.setContentsMargins(0, 0, 0, 0)
        self.PhoneFormLayout.setObjectName("PhoneFormLayout")
        self.phoneNumEdit = LineEdit(self.layoutWidget2)
        self.phoneNumEdit.setObjectName("phoneNumEdit")
        self.PhoneFormLayout.addWidget(self.phoneNumEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.PhoneFormLayout.addItem(spacerItem)
        self.captchaLayout = QtWidgets.QHBoxLayout()
        self.captchaLayout.setObjectName("captchaLayout")
        self.captchaEdit = LineEdit(self.layoutWidget2)
        self.captchaEdit.setObjectName("captchaEdit")
        self.captchaLayout.addWidget(self.captchaEdit)
        self.getCodeButton = HyperlinkButton(self.layoutWidget2)
        self.getCodeButton.setObjectName("getCodeButton")
        self.captchaLayout.addWidget(self.getCodeButton)
        self.PhoneFormLayout.addLayout(self.captchaLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.PhoneFormLayout.addItem(spacerItem1)
        self.PopUpAniStackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.PopUpAniStackedWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoginButton = PushButton(self.layoutWidget)
        self.LoginButton.setObjectName("LoginButton")
        self.horizontalLayout.addWidget(self.LoginButton)
        self.RegisterButton = PushButton(self.layoutWidget)
        self.RegisterButton.setObjectName("RegisterButton")
        self.horizontalLayout.addWidget(self.RegisterButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.ForgotPassword = CaptionLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 159, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 159, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ForgotPassword.setPalette(palette)
        self.ForgotPassword.setAlignment(QtCore.Qt.AlignCenter)
        self.ForgotPassword.setObjectName("ForgotPassword")
        self.verticalLayout_2.addWidget(self.ForgotPassword)
        self.userAgreeLayout = QtWidgets.QHBoxLayout()
        self.userAgreeLayout.setObjectName("userAgreeLayout")
        self.CheckBox = CheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CheckBox.sizePolicy().hasHeightForWidth())
        self.CheckBox.setSizePolicy(sizePolicy)
        self.CheckBox.setMinimumSize(QtCore.QSize(29, 22))
        self.CheckBox.setMaximumSize(QtCore.QSize(22, 16777215))
        self.CheckBox.setText("")
        self.CheckBox.setObjectName("CheckBox")
        self.userAgreeLayout.addWidget(self.CheckBox)
        self.BodyLabel = BodyLabel(self.layoutWidget)
        self.BodyLabel.setObjectName("BodyLabel")
        self.userAgreeLayout.addWidget(self.BodyLabel)
        self.UserAgree = BodyLabel(self.layoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 154, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 154, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.UserAgree.setPalette(palette)
        self.UserAgree.setObjectName("UserAgree")
        self.userAgreeLayout.addWidget(self.UserAgree)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.userAgreeLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.userAgreeLayout)
        self.verticalLayout.addWidget(self.FormWidget)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 4)
        self.gridLayout.addWidget(self.loginWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.PopUpAniStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userNameEdit.setPlaceholderText(_translate("Form", "请输入用户名"))
        self.passWordEdit.setPlaceholderText(_translate("Form", "请输入密码"))
        self.phoneNumEdit.setPlaceholderText(_translate("Form", "手机号"))
        self.captchaEdit.setPlaceholderText(_translate("Form", "请输入验证码"))
        self.getCodeButton.setText(_translate("Form", "获取验证码"))
        self.LoginButton.setText(_translate("Form", "登录"))
        self.RegisterButton.setText(_translate("Form", "注册"))
        self.ForgotPassword.setText(_translate("Form", "忘记密码"))
        self.BodyLabel.setText(_translate("Form", "我已阅读并同意"))
        self.UserAgree.setText(_translate("Form", "用户协议"))


from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, CheckBox, HyperlinkButton, LineEdit, Pivot, PixmapLabel, PushButton
