import re
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from utils.Tools import center
from Controllers.UserController import PhoneLogin, UsernameLogin
from config.setting import ERROR_MESSAGE_DICT
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import InfoBarPosition, InfoBar

from UI import LoginWindow
from views.MainWindow import MainWidget


class LoginWidget(FramelessWindow, LoginWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # 设置标题栏
        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.raise_()

        self.setWindowIcon(QIcon("resources/images/icon.png"))
        self.setWindowTitle("Login")
        self.resize(1400, 900)

        # 设置导航按钮
        self.Pivot.addItem("userWidget", " 用户登录", onClick=self.toUserLogin)
        self.Pivot.addItem("PhoneWidget", "手机号登录", onClick=self.toPhoneLogin)

        # 设置登陆事件
        self.LoginButton.clicked.connect(self.UserLogin)

        center(self)

    def toUserLogin(self):
        self.PopUpAniStackedWidget.setCurrentIndex(0)

    def toPhoneLogin(self):
        self.PopUpAniStackedWidget.setCurrentIndex(1)

    def UserLogin(self):
        current_widget = self.PopUpAniStackedWidget.currentIndex()
        if user_agree := self.CheckBox.isChecked():
            if current_widget == 0:
                username = self.userNameEdit.text()
                password = self.passWordEdit.text()
                if self.user_login_check(username, password) and UsernameLogin(username, password):
                    self.close()
                    main_window = MainWidget()
                    main_window.show()
            elif current_widget == 1:
                phone_num = self.phoneNumEdit.text()
                captcha = self.captchaEdit.text()
                PhoneLogin(phone_num, captcha)
            else:
                print("error")
        else:
            InfoBar.error(
                title=ERROR_MESSAGE_DICT["unread_user_agree"]["title"],
                content=ERROR_MESSAGE_DICT["unread_user_agree"]["content"],
                isClosable=ERROR_MESSAGE_DICT["unread_user_agree"]["isClosable"],
                position=InfoBarPosition.TOP,
                duration=ERROR_MESSAGE_DICT["unread_user_agree"]["duration"],
                parent=self,
            )

    def user_login_check(self, username, password):
        if username and password:
            if validate_password(password):
                return True
            InfoBar.warning(
                title=ERROR_MESSAGE_DICT["password_format_error"]["title"],
                content=ERROR_MESSAGE_DICT["password_format_error"]["content"],
                isClosable=ERROR_MESSAGE_DICT["password_format_error"]["isClosable"],
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self,
            )
            return False
        InfoBar.error(
            title=ERROR_MESSAGE_DICT["missing_username_or_password"]["title"],
            content=ERROR_MESSAGE_DICT["missing_username_or_password"]["content"],
            isClosable=ERROR_MESSAGE_DICT["missing_username_or_password"]["isClosable"],
            position=InfoBarPosition.TOP,
            duration=2000,
            parent=self,
        )
        return False


def validate_password(password):
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$"
    result = re.match(pattern, password)
    return bool(result)
