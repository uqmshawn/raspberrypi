from PyQt5.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QAction,
)

from ui.setup_dialog import SetupDialog

from .config_manager import load_config, save_config

from .web_tabs import WebTab


class MainWindow(QMainWindow):
    """Main dashboard window with tabbed interface."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hurtec & Victron Dashboard")
        self.resize(800, 600)
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self._build_menus()

        config = load_config() or {}
        for tab in config.get("tabs", []):
            self.add_tab(
                tab.get("url"),
                tab.get("name", tab.get("url")),
                tab.get("username", ""),
                tab.get("password", ""),
            )

    def add_tab(self, url: str, name: str, username: str = "", password: str = ""):
        tab = WebTab(url, username=username, password=password)
        self.tabs.addTab(tab, name)

    def _build_menus(self):
        menu = self.menuBar().addMenu("Tabs")

        add_action = QAction("Add Tab", self)
        add_action.triggered.connect(self.prompt_add_tab)
        menu.addAction(add_action)

        remove_action = QAction("Remove Current Tab", self)
        remove_action.triggered.connect(self.remove_current_tab)
        menu.addAction(remove_action)

    def prompt_add_tab(self):
        dialog = SetupDialog(self)
        if dialog.exec_() == dialog.Accepted:
            data = dialog.get_data()
            if data["url"]:
                self.add_tab(data["url"], data.get("name") or data["url"], data.get("username", ""), data.get("password", ""))

    def remove_current_tab(self):
        index = self.tabs.currentIndex()
        if index >= 0:
            self.tabs.removeTab(index)

    def closeEvent(self, event):
        config = {"tabs": []}
        for i in range(self.tabs.count()):
            widget = self.tabs.widget(i)
            url = widget.view.url().toString()
            name = self.tabs.tabText(i)
            entry = {"url": url, "name": name}
            if getattr(widget, "username", ""):
                entry["username"] = widget.username
            if getattr(widget, "password", ""):
                entry["password"] = widget.password
            config["tabs"].append(entry)
        save_config(config)
        super().closeEvent(event)
