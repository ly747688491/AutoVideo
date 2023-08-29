import sys

from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout
from qfluentwidgets import FluentIcon

from Controllers.AccountController import GetAccount
from UI.Ui_TableItem import Ui_Form
from UI.Ui_AccountManager import Ui_Form as Ui_AccountManager


class TableWidget(QWidget, Ui_AccountManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        data = init_data()
        self.LeftPageButton.setIcon(FluentIcon.LEFT_ARROW)
        self.RightPageButton.setIcon(FluentIcon.RIGHT_ARROW)
        for data_item in data:
            Item_widget = ItemWidget()
            Item_widget.dataRender(data_item)
            self.DataverticalLayout.addWidget(Item_widget)


class ItemWidget(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setMinimumWidth(1000)

    def dataRender(self, data_item):
        self.UserName.setText(data_item[0])
        account_pixmap = QPixmap(data_item[1])
        self.PlatformName.setText(data_item[2])
        platform_pixmap = QPixmap(data_item[3])
        scaled_account_pixmap = account_pixmap.scaled(self.AccountAvatar.size(), Qt.KeepAspectRatio)
        scaled_platform_pixmap = platform_pixmap.scaled(self.PlatformAvatar.size(), Qt.KeepAspectRatio)
        self.AccountAvatar.setPixmap(scaled_account_pixmap)
        self.Operator.setText(data_item[4])
        self.PlatformAvatar.setPixmap(scaled_platform_pixmap)
        self.Groups.setText("")
        if data_item[5]:
            success_text = f"登陆成功\n登陆时间：{data_item[6]}"
            self.status.setText(success_text)
        else:
            self.status.setText("登录失效")
        self.Topping.setIcon(FluentIcon.UP)
        self.Edit.setIcon(FluentIcon.EDIT)
        self.Delete.setIcon(FluentIcon.DELETE)


def init_data():
    account_list = GetAccount()
    account_model = []
    for data in account_list:
        status = data["account_status"]
        login_time = data["update_time"]
        account_from = data["platform_name"]
        platform_icon = data["platform_avatar"]
        data_list = [data["username"], data["account_avatar"], account_from, platform_icon, data['account_operator'],
                     status, login_time]
        account_model.extend((data_list, data_list, data_list, data_list, data_list))
    return account_model


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())
