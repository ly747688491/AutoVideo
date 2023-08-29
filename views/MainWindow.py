import time

from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import FluentWindow, NavigationAvatarWidget, NavigationItemPosition, SplashScreen

from utils.Tools import center
from views.AccountsPage import AccountPage


def Translator():
    pass


class MainWidget(FluentWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

        self.accountPage = AccountPage(self)

        self.initNavigation()
        self.splashScreen.finish()

    def initWindow(self):
        # 设置窗体信息
        self.resize(1300, 900)
        self.setMinimumWidth(1300)
        self.setWindowIcon(QIcon("resources/images/icon.png"))
        self.setWindowTitle("顺道智数")

        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        center(self)

    def initNavigation(self):
        account_icon = "resources/Icon/accounts_black.svg"
        self.addSubInterface(self.accountPage, QIcon(account_icon), "账户管理")

        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Liy', 'resources/images/avatar.jpg'),
            position=NavigationItemPosition.BOTTOM
        )
        self.navigationInterface.addItem(routeKey="settings", icon=FIF.SETTING, text="设置",
                                         position=NavigationItemPosition.BOTTOM)
