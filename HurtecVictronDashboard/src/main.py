import sys
from PyQt5.QtWidgets import QApplication

from dashboard.main_window import MainWindow
from remote.server import start_server


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    start_server(window)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
