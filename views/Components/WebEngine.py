from PySide2.QtCore import QTimer, Slot
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEnginePage, QWebEngineProfile
from PySide2.QtWidgets import QDialog, QVBoxLayout

from Controllers.AccountController import SaveAccount
from config.setting import COOKIE_DELAY


class EngineDialog(QDialog):
    _instance = None

    def __init__(self, params, parent=None):
        super().__init__(parent)
        self.setWindowTitle(params["frame_name"])
        self.layout = QVBoxLayout()
        self.setFixedSize(1500, 900)
        web_engin_view = WebEngineView(params["home_url"], params["avatar_selector"], params["name_selector"])
        # 获取web引擎的全局设置
        settings = QWebEngineSettings.globalSettings()
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)
        web_engin_view.load(params["login_url"])
        self.layout.addWidget(web_engin_view)
        self.setLayout(self.layout)
        self.params = params
        EngineDialog._instance = self

    @staticmethod
    def get_instance():
        return EngineDialog._instance

    def close_dialog(self):
        self.close()


class WebEngineView(QWebEngineView):
    def __init__(self, home_url, avatar_selector, name_selector):
        super(WebEngineView, self).__init__()
        self.home_url = home_url
        self.avatar_selector = avatar_selector
        self.name_selector = name_selector
        self.page = QWebEnginePage(QWebEngineProfile.defaultProfile(), self)
        self.setPage(self.page)
        self.page.urlChanged.connect(self.on_urlChanged)
        self.cookies = {}
        self.data = {}
        self.timer = QTimer()

    def load(self, url):
        self.page.load(QUrl(url))

    def on_urlChanged(self, url):
        try:
            if url.toString() == self.home_url:
                self.page.loadFinished.connect(self.on_loadFinished)
                self.page.profile().cookieStore().cookieAdded.connect(self.on_cookieAdded)
                delay = COOKIE_DELAY
                self.timer.singleShot(delay, self.data_save)
        except Exception as e:
            print(e)

    def on_loadFinished(self, ok):
        if ok:
            self.page.runJavaScript(
                f"document.querySelector('{self.name_selector}').innerText;",
                0,
                self.on_aTextReceived,
            )
            self.page.runJavaScript(
                f"document.querySelector('{self.avatar_selector}').src;",
                0,
                self.on_imgSrcReceived,
            )

    def on_cookieAdded(self, cookie):
        name = cookie.name().data().decode("utf-8")
        value = cookie.value().data().decode("utf-8")
        self.cookies[name] = value

    def on_aTextReceived(self, a_text):
        self.data["name"] = a_text

    def on_imgSrcReceived(self, img_src):
        self.data["img_src"] = img_src

    @Slot()
    def data_save(self):
        from views.AccountsPage import AccountPage

        self.data["cookies"] = self.cookies
        SaveAccount(self.data["name"], self.data["img_src"], self.data["cookies"])
        EngineDialog.get_instance().close_dialog()
        AccountPage.table_refresh()
        self.page.profile().cookieStore().deleteAllCookies()
