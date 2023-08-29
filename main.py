import sys
from datetime import datetime

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication

from Controllers.UserController import GetLoginUser, logoutUser
from views.LoginWindow import LoginWidget
from views.MainWindow import MainWidget


def get_history_data():
    login_user = GetLoginUser()
    now = datetime.now()
    update_time = datetime.strptime(login_user["update_time"], "%Y-%m-%d %H:%M:%S")
    print(now.date())
    print(update_time.date())
    if now.date() == update_time.date():
        return True
    logoutUser(login_user['user_id'])
    return False


if __name__ == "__main__":
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)
    if get_history_data():
        window = MainWidget()
        window.show()
    else:
        w = LoginWidget()
        w.show()
    sys.exit(app.exec_())
