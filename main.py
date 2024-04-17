import os
import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QListWidgetItem
from pathlib import Path

home = str(Path.home())
from main_window import Ui_MainWindow

from PyQt6.QtWidgets import QMainWindow

state = dict()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        state['current_dir'] = str(Path.home())
        self.set_current_dir(state['current_dir'])

        self.refresh_file_explorer()

        self.ui.file_explorer.currentItemChanged.connect(self.on_file_select)

    @staticmethod
    def current_dir():
        return state.get('current_dir', str(Path.home()))

    @staticmethod
    def is_dir(filename: str):
        return Path(os.path.join(MainWindow.current_dir(), filename)).is_dir()

    def set_current_dir(self, dirpath: str):
        state['current_dir'] = dirpath
        self.refresh_file_explorer()

    def refresh_file_explorer(self):
        self.ui.file_explorer.clear()
        for file in os.listdir(self.current_dir()):
            list_item = QListWidgetItem(file)
            if MainWindow.is_dir(file):
                list_item.setIcon(QIcon.fromTheme("folder"))
            self.ui.file_explorer.addItem(list_item)

    def on_file_select(self):
        selected: str = self.ui.file_explorer.currentItem().text()
        if self.is_dir(selected):
            self.set_current_dir(str(Path(os.path.join(MainWindow.current_dir(), selected))))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
