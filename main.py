import sys
from PySide6.QtWidgets import QApplication

from mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    mainWindow = MainWindow(app)
    mainWindow.show()

    sys.exit(app.exec())