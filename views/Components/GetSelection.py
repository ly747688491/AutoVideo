import PySide2
from PySide2.QtCore import Qt
from PySide2.QtCore import Signal
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QDialog, QWidget, QLabel, QVBoxLayout, QGridLayout, QMessageBox, QHBoxLayout

from Controllers.PlatformController import GetPlatform
from views.Components.WebEngine import EngineDialog


class GetSelection(QDialog):
    _instance = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("请选择账号所在平台")
        self.layout = QVBoxLayout()
        self.setFixedSize(1000, 800)
        grid_widget = GridWidget()
        grid_widget.setLayout(QGridLayout())
        self.layout.addWidget(grid_widget)
        self.setLayout(self.layout)
        self.setStyleSheet("""
        background-color:#fff;
        """)
        GetSelection._instance = self

    @staticmethod
    def get_instance():  # And this method
        return GetSelection._instance

    def close_dialog(self):  # And this method
        self.close()


class GridWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()

        plat_list = GetPlatform()
        row_layout = QVBoxLayout()
        count = 0
        for item in plat_list:
            params_dict = {
                "label_text": item["platform_title"],
                "platform_name": item["platform_name"],
                "icon_path": item["platform_icon"],
                "login_url": item["login_url"],
                "home_url": item["home_url"],
                "avatar_selector": item["avatar_selector"],
                "name_selector": item["name_selector"]
            }
            Icon = create_icon_widget(params_dict)
            Icon.clicked.connect(on_click_button)
            if item["platform_type"] == "1":
                row_layout.addWidget(Icon)
                count += 1
                if count % 5 == 0:  # 当添加了5个元素，创建一个新的水平布局
                    self.layout.addLayout(row_layout)
                    row_layout = QHBoxLayout()

                # 添加最后一行的布局（如果它有元素的话）
            if row_layout.count() > 0:
                self.layout.addLayout(row_layout)

        self.setLayout(self.layout)


class IconWidget(QWidget):
    clicked = Signal(str, str, str, str, str)

    def __init__(self, params):
        super().__init__()
        self.setFixedSize(60, 80)
        self.name_selector = params["name_selector"]
        self.avatar_selector = params["avatar_selector"]
        self.home_url = params["home_url"]
        self.login_url = params["login_url"]
        self.layout = QVBoxLayout(self)
        icon_label = QLabel()
        icon_name = QLabel()
        icon_label.setPixmap(QPixmap(params["icon_path"]).scaled(40, 40, Qt.KeepAspectRatio))
        self.frame_name = params["label_text"]
        icon_name.setText(params["label_text"])
        icon_name.setFixedHeight(16)
        icon_name.setAlignment(Qt.AlignCenter)
        self.setObjectName(params["platform_name"])
        self.layout.addWidget(icon_label)
        self.layout.addWidget(icon_name)
        self.setLayout(self.layout)

    def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        self.clicked.emit(self.frame_name, self.login_url, self.home_url, self.avatar_selector, self.name_selector)


def on_click_button(frame_name, login_url, home_url, avatar_selector, name_selector):
    params = {
        'frame_name': frame_name,
        'login_url': login_url,
        'home_url': home_url,
        'avatar_selector': avatar_selector,
        'name_selector': name_selector
    }
    GetSelection.get_instance().close_dialog()
    web_view = EngineDialog(params)
    web_view.exec_()


def create_icon_widget(params):
    keys = set(params.keys())
    all_params_list = {"label_text", 'platform_name', 'icon_path', 'login_url', 'home_url', 'avatar_selector',
                       'name_selector',
                       }
    if keys == all_params_list:
        return IconWidget(params)
    elif other_list(params):
        return QLabel(params["platform_title"])
    else:
        QMessageBox.critical(None, "Error", "错误，参数传入错误，请检查参数列表")


def other_list(params):
    return False
