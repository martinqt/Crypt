import sys
from PySide.QtGui import *


class Frame(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.resize(600,500)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Crypt')

        self.quit = QPushButton('Quit', self)
        self.quit.clicked.connect(quit)

        layout = QVBoxLayout()
        layout.addWidget(self.quit)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())