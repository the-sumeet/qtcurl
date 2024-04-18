import os
import sys
from enum import Enum, auto
from typing import Dict, Optional
from urllib.parse import urlparse
from urllib.parse import parse_qs

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QListWidgetItem, QHBoxLayout, QLineEdit, QWidget, QVBoxLayout
from pathlib import Path

from pyqt6_plugins.examplebutton import QtWidgets

from antlr4_driver import parse_curl
from main_window import Ui_MainWindow

from PyQt6.QtWidgets import QMainWindow

from schema import Method

state = dict()


class NameValueWidget(QWidget):
    def __init__(self, name: Optional[str] = "", value: Optional[str] = ""):
        super().__init__()
        layout = QVBoxLayout(self)

        h_layout = QHBoxLayout()
        checkbox = QtWidgets.QCheckBox(parent=self)
        lineEdit1 = QtWidgets.QLineEdit(parent=self, readOnly=True)
        lineEdit1.setText(name)
        lineEdit2 = QtWidgets.QLineEdit(parent=self, readOnly=True)
        lineEdit2.setText(value)
        toolButton = QtWidgets.QToolButton(parent=self)
        h_layout.addWidget(checkbox)
        h_layout.addWidget(lineEdit1)
        h_layout.addWidget(lineEdit2)
        h_layout.addWidget(toolButton)
        layout.addLayout(h_layout)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        state['current_dir'] = str(Path.home())
        self.set_current_dir(state['current_dir'])

        self.refresh_file_explorer()

        # Init widgets
        for method in Method:
            self.ui.methodsSelect.addItem(method.name)

        # Connect
        self.ui.go_up.clicked.connect(self.go_up)
        self.ui.file_explorer.itemClicked.connect(self.on_file_select)

    @staticmethod
    def current_dir():
        return state.get('current_dir', str(Path.home()))

    @staticmethod
    def is_dir(filename: str):
        return Path(os.path.join(MainWindow.current_dir(), filename)).is_dir()

    def set_current_dir(self, dirpath: str):
        state['current_dir'] = dirpath
        self.refresh_file_explorer()

    def go_up(self):
        current_dir = self.current_dir()
        if current_dir != "/":
            parent = Path(current_dir).parent
            self.set_current_dir(str(parent))

    def refresh_file_explorer(self):
        self.ui.file_explorer.clear()
        for file in sorted(os.listdir(self.current_dir())):
            list_item = QListWidgetItem(file)
            if MainWindow.is_dir(file):
                list_item.setIcon(QIcon.fromTheme("folder"))
            self.ui.file_explorer.addItem(list_item)

    def refresh_request(self):
        self.ui.urlIn.setText(state['uri'])
        self.ui.methodsSelect.setCurrentIndex(state.get("method", Method.GET).index)

        for h in state['headers']:
            item = QListWidgetItem()
            name_value = NameValueWidget(h.name, h.value)
            item.setSizeHint(name_value.sizeHint())

            self.ui.headers_list.addItem(item)
            self.ui.headers_list.setItemWidget(item, name_value)

        parsed_url = urlparse(state['uri'])
        for query in parse_qs(parsed_url.query):
            for query_value in parse_qs(parsed_url.query)[query]:
                item = QListWidgetItem()
                name_value = NameValueWidget(query, query_value)
                item.setSizeHint(name_value.sizeHint())

                self.ui.params_list.addItem(item)
                self.ui.params_list.setItemWidget(item, name_value)

    def on_file_select(self):
        selected: str = self.ui.file_explorer.currentItem().text()
        if self.is_dir(selected):
            self.set_current_dir(str(Path(os.path.join(MainWindow.current_dir(), selected))))
        else:
            if not selected.endswith('.curl'):
                return

            with open(os.path.join(MainWindow.current_dir(), selected)) as file:
                try:
                    result: Dict = parse_curl(file.read())

                    state['uri'] = result.get("uri", "")
                    state['method'] = Method[result.get("method", "GET")]
                    state['headers'] = result.get("headers", [])
                    self.refresh_request()

                except Exception as e:
                    self.ui.statusbar.showMessage(str(e))
                    print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
