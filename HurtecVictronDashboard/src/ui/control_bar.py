"""Placeholder for control bar."""

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class ControlBar(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        btn = QPushButton("Setup")
        layout.addWidget(btn)
