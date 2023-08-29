import typing
import PySide2.QtCore
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from Controllers.AccountController import GetAccount
import PySide2.QtWidgets
from UI.Ui_AccountManager import Ui_Form
from views.Components.GetSelection import GetSelection


def pop_up():
    get_selection = GetSelection()
    get_selection.exec_()


class AccountPage(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.AddAccounButton.clicked.connect(pop_up)
        
        # self.table_refresh()
        
        # self.table_Setup()

    # def table_refresh(self):
    #     self.AccountTable.clear()
    #     account_list = GetAccount()
    #     for account in account_list:
    #         print(account)