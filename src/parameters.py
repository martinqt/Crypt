from PySide.QtCore import *
from PySide.QtGui import *

class Parameters(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Options - Crypt')
        self.resize(300, 150)

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
        pixmap.fill(QColorDialog.getColor())
        self.convertedToolButton.setIcon(QIcon(pixmap))

    def originalColorClicked(self):
        pixmap = QPixmap(16, 16)
        pixmap.fill(QColorDialog.getColor())
        self.originalToolButton.setIcon(QIcon(pixmap))
