import sys
from PySide.QtCore import *
from PySide.QtGui import *
from key import *
import os, sys
sys.path.insert(0, os.getcwd()+'/src/functions')
from file import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        
        self.resize(600, 500)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Crypt')

        self.quit = QPushButton('Quit', self)
        self.quit.clicked.connect(quit)

        self.keyEdit = QTableView(self)

        widget = QWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.keyEdit)
        layout.addWidget(self.quit)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        header = QHeaderView(Qt.Horizontal)
        header.setResizeMode(QHeaderView.Stretch)
        self.keyEdit.setHorizontalHeader(header)
        
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHorizontalHeaderLabels(['From', 'To'])
        self.keyEdit.setModel(self.model)

        self.statusBar().showMessage('Welcome')

        self.createMenu()
        self.populate()

    def populate(self):
        self.clearModel()
        key = getKey()

        for i in key:
            index = self.model.rowCount()
            self.model.setItem(index, 0, QStandardItem(i))
            self.model.setItem(index, 1, QStandardItem(key[i]))

    def clearModel(self):
        self.model.clear();
        self.model.setHorizontalHeaderLabels(['From', 'To'])

    def createMenu(self):
        self.saveAct = QAction(QIcon(':/images/save.png'), 'Save',
                self, shortcut=QKeySequence.Save,
                statusTip='Save the key', triggered=self.saveFile)

        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(self.saveAct)

    def saveFile(self):
        content = '''def getKey():
    return {\n'''

        i = 0
        while i < self.model.rowCount():
            tmp = '        \''+self.escape(self.model.item(i, 0).text())+'\' : '
            tmp += '\''+self.escape(self.model.item(i, 1).text())+'\',\n'
            content += tmp
            i += 1

        content += '''    }'''

        write('src/key.py', content)

    def escape(self, string):
        if string == '\'':
            return '\\'+string
        else:
            return string

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())