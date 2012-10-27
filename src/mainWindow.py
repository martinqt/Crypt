import sys
from PySide.QtCore import *
from PySide.QtGui import *


class Frame(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        
        self.resize(600, 500)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Crypt')

        self.quit = QPushButton('Quit', self)
        self.quit.clicked.connect(quit)

        self.keyEdit = QTableView(self)

        layout = QVBoxLayout()
        layout.addWidget(self.keyEdit)
        layout.addWidget(self.quit)
        self.setLayout(layout)

        header = QHeaderView(Qt.Horizontal)
        header.setResizeMode(QHeaderView.Stretch)
        self.keyEdit.setHorizontalHeader(header)
        
        model = QStandardItemModel(0, 2, self)
        model.setHorizontalHeaderLabels(['From', 'To'])
        self.keyEdit.setModel(model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Frame()
    frame.show()
    sys.exit(app.exec_())