from PyQt6.QtWidgets import *
from launcher_gui import *

class Controller(QMainWindow, Ui_startscr):
    def __init__(self, app: QApplication):
        super().__init__()
        self.setupUi(self)
        self.app = app
