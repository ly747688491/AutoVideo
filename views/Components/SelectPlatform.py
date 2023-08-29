from PySide2.QtWidgets import QDialog

from UI.Ui_Platform import Ui_Form


class SelectDialog(QDialog, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("请选择账号所在平台")

    def initUi(self):
        self.baijiahao_Button.clicked.connect(self.button_clicked)
        self.imagelabel.clicked.connect(self.button_clicked)

    def button_clicked(self):
        pass
