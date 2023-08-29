import logging
import time
import uuid

from PySide2.QtWidgets import QMessageBox,QDesktopWidget


def generate_dynamic_id():
    return uuid.uuid4()


def timestamp_to_str(timestamp, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.localtime(timestamp))


def str_to_timestamp(date_string, format='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(time.strptime(date_string, format)))


def warning_popup(msg):
    # 创建警告对话框
    msgBox = QMessageBox()
    msgBox.warning(msgBox, "警告", msg)

    # 记录警告到日志
    logging.warning(msg)

    # 显示警告对话框
    msgBox.exec()


def center(self):
    qr = self.frameGeometry()  # 获取主窗口的大小
    cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的中心点
    qr.moveCenter(cp)  # 设置窗口的中心点到显示器的中心点
    self.move(qr.topLeft())  # 移动窗口的左上角到其框架的左上角，实现窗口居中