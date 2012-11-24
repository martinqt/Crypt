import configparser
from PySide.QtCore import *
from PySide.QtGui import *

class Parameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Options - Crypt')
        self.resize(300, 150)

        self.loadConfig()

        self.tab1 = QWidget(self)
        layout = QVBoxLayout()

        self.convertedToolButton = QToolButton(self)
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColor(0, 0, 255))
        self.convertedToolButton.setIcon(QIcon(pixmap))

        pixmap.fill(QColor(255, 0, 0))
        self.originalToolButton = QToolButton(self)
        self.originalToolButton.setIcon(QIcon(pixmap))

        formLayout = QFormLayout()
        formLayout.addRow('Converted:', self.convertedToolButton)
        formLayout.addRow('Original:', self.originalToolButton)

        group = QGroupBox('HTML color', self)
        group.setLayout(formLayout)

        layout.addWidget(group)
        self.tab1.setLayout(layout)

        self.tabs = QTabWidget(self)
        self.tabs.addTab(self.tab1, 'General')

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        self.convertedToolButton.clicked.connect(self.convertedColorClicked)
        self.originalToolButton.clicked.connect(self.originalColorClicked)

    def convertedColorClicked(self):
        pixmap = QPixmap(16, 16)
        color = QColorDialog.getColor(self.getColorFromString(self.config['HTML_COLORS']['converted']), self, 'Converted Color')
        if color != QColor():
            pixmap.fill(color)
            self.config['HTML_COLORS']['converted'] = self.getStringFromColor(color)
            self.convertedToolButton.setIcon(QIcon(pixmap))

    def originalColorClicked(self):
        pixmap = QPixmap(16, 16)
        color = QColorDialog.getColor(self.getColorFromString(self.config['HTML_COLORS']['original']), self, 'Original Color')
        if color != QColor():
            pixmap.fill(color)
            self.config['HTML_COLORS']['original'] = self.getStringFromColor(color)
            self.originalToolButton.setIcon(QIcon(pixmap))

    def loadConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read('parameters.ini')

    def getColorFromString(self, string):
        return QColor(int(string[:3]), int(string[3:6]), int(string[6:9]))

    def getStringFromColor(self, color):
        r = str(color.red())
        if len(r) == 1:
            r = '00'+r
        elif len(r) == 2:
            r = '0'+r

        g = str(color.green())
        if len(g) == 1:
            g = '00'+g
        elif len(g) == 2:
            g = '0'+g

        b = str(color.blue())
        if len(b) == 1:
            b = '00'+b
        elif len(b) == 2:
            b = '0'+b

        return r+g+b
