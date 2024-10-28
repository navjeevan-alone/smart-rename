import sys
from PyQt5.QtWidgets import QApplication
from gui import FileRenamerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileRenamerApp()
    window.show()
    sys.exit(app.exec_())
