from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from .auto_login import perform_auto_login


class WebTab(QWidget):
    """Simple web tab with optional auto-login."""

    def __init__(self, url: str, username: str = "", password: str = ""):
        super().__init__()
        self.url = url
        self.username = username
        self.password = password

        layout = QVBoxLayout(self)
        self.view = QWebEngineView()
        layout.addWidget(self.view)
        self.view.load(QUrl(url))
        self.view.loadFinished.connect(self._on_loaded)

    def _on_loaded(self, ok: bool):
        if ok and self.username:
            QTimer.singleShot(1500, lambda: perform_auto_login(self.view, self.username, self.password))
