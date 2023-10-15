import sys
from Qt.QtWidgets import QApplication, QDockWidget


class UniToolShelf(QDockWidget):
    def __init__(self, parent=None):
        super(UniToolShelf, self).__init__(parent)

        self.widget_init()
        self.layout_init()
        self.connect_init()

    def widget_init(self):
        pass

    def layout_init(self):
        pass

    def connect_init(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    uni_tool_shelf = UniToolShelf()
    uni_tool_shelf.show()
    app.exec_()
