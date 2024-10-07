import sys
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QBrush
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QSize, Qt, QPoint


from shape import Shape
from ui_mainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.setFixedSize(400, 400)
        self.setWindowTitle("Lab2")

        self.label = QLabel()

        self.canvasMask = QPixmap(QSize(400, 400))
        self.canvasMask.fill(QColor('#fff'))

        self.pen = QPen()
        self.pen.setWidth(3)
        self.pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        self.brush = QBrush()
        self.brush.setStyle(Qt.BrushStyle.SolidPattern)


        self.label.setPixmap(self.canvasMask)
        self.setCentralWidget(self.label)

        self.previousPoint = None
        self.shapes = []
        self.paintMode = 'dot'

        self.actionDot.triggered.connect(lambda: self.changePaintMode('dot'))
        self.actionElips.triggered.connect(lambda: self.changePaintMode('elipse'))
        self.actionLine.triggered.connect(lambda: self.changePaintMode('line'))
        self.actionRectnagle.triggered.connect(lambda: self.changePaintMode('rectangle'))

    def closeEvent(self, event):
        event.accept()
        sys.exit()

    def mousePressEvent(self, event):
        position = event.pos()

        painter = QPainter(self.canvasMask)
        painter.setPen(self.pen)
        match self.paintMode:
            case 'dot':
                painter.drawPoint(position.x(), position.y())
                self.shapes.append(Shape('dot', position.x(), position.y()))
            case 'elipse':
                self.brush.setColor(QColor('#bdfccb'))

        painter.end()

        self.label.setPixmap(self.canvasMask)

        self.previousPoint = position

    def mouseReleaseEvent(self, event):
        position = event.pos()

        painter = QPainter(self.canvasMask)
        painter.setPen(self.pen)

        match self.paintMode:
            case 'rectangle':
                painter.drawRect(self.previousPoint.x(), self.previousPoint.y(), position.x() - self.previousPoint.x(), position.y() - self.previousPoint.y())
                self.shapes.append(Shape('rectangle', self.previousPoint.x(), self.previousPoint.y(), position.x() - self.previousPoint.x(), position.y() - self.previousPoint.y()))
            case 'line':
                painter.drawLine(self.previousPoint.x(), self.previousPoint.y(), position.x(), position.y())
                self.shapes.append(Shape('line', self.previousPoint.x(), self.previousPoint.y(), position.x(), position.y()))
            case 'elipse':
                painter.setBrush(self.brush)
                center = QPoint(self.previousPoint.x(), self.previousPoint.y())
                painter.drawEllipse(center , (position.x() - self.previousPoint.x()), (position.y() - self.previousPoint.y()))
                self.shapes.append(Shape('elipse', center, (position.x() - self.previousPoint.x()), (position.y() - self.previousPoint.y())))

        painter.end()

        self.label.setPixmap(self.canvasMask)



    def changePaintMode(self, mode):
        self.paintMode = mode
        self.menuObject.setTitle('Object: ' + mode)