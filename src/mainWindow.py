import sys, os
sys.path.insert(0, os.getcwd()+'/src/functions')
from PySide.QtCore import *
from PySide.QtGui import *
from key import *
from file import *
from functions import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        
        self.resize(700, 500)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Crypt')
        self.headers = ['From', 'To', 'Count']
        self.inputPath = 'input.txt'
        self.keyPath = 'src/key.py'

        self.quit = QPushButton('Quit', self)
        self.quit.clicked.connect(quit)
        self.populateButton = QPushButton('Repopulate', self)
        self.populateButton.clicked.connect(self.populate)

        self.frequency = QCheckBox('Frequency', self)
        self.frequency.stateChanged.connect(self.toogleFrequency)

        self.output = QTextBrowser(self)
        self.output.setReadOnly(True)

        self.keyEdit = QTableView(self)
        self.keyEdit.setSortingEnabled(True)

        widget = QWidget(self)
        layout = QVBoxLayout()
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.keyEdit)
        hLayout.addWidget(self.output)
        layout.addLayout(hLayout)

        hLayout = QHBoxLayout()
        hLayout.addWidget(self.frequency)
        hLayout.addWidget(self.populateButton)
        layout.addLayout(hLayout)

        layout.addWidget(self.quit)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        header = QHeaderView(Qt.Horizontal)
        header.setResizeMode(QHeaderView.Stretch)
        self.keyEdit.setHorizontalHeader(header)
        
        self.model = QStandardItemModel(0, 3, self)
        self.model.setHorizontalHeaderLabels(self.headers)
        self.keyEdit.setModel(self.model)

        self.statusBar().showMessage('Welcome')

        self.createMenu()
        self.populate()

    def populate(self):
        try:
            self.model.itemChanged.disconnect(self.convert)
        except RuntimeError:
            pass
        
        self.clearModel()
        key = getKey()
        if self.frequency.checkState() == Qt.Checked:
            charCount = getCharCount(read(self.inputPath), True)
        else:
            charCount = getCharCount(read(self.inputPath))

        for i in key:
            index = self.model.rowCount()
            self.model.setItem(index, 0, QStandardItem(i))
            self.model.setItem(index, 1, QStandardItem(key[i]))
            if charCount[i] < 10:
                charCount[i] = '0'+str(charCount[i])
            self.model.setItem(index, 2, QStandardItem(str(charCount[i])))

        self.keyEdit.sortByColumn(2, Qt.DescendingOrder)
        self.model.itemChanged.connect(self.convert)
        self.convert()

    def clearModel(self):
        self.model.clear();
        self.model.setHorizontalHeaderLabels(self.headers)

    def createMenu(self):
        self.saveAct = QAction(QIcon('src/images/save.png'), 'Save',
                self, shortcut=QKeySequence.Save,
                statusTip='Save the key', triggered=self.saveFile)

        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(self.saveAct)

    def toogleFrequency(self):
        if self.frequency.checkState() == Qt.Checked:
            self.headers[2] = 'Frequency'
        else:
            self.headers[2] = 'Count'

        self.model.setHorizontalHeaderLabels(self.headers)
        self.populate()

    def convert(self):
        self.saveFile()
        input = read(self.inputPath)
        key = self.generateKey()

        self.output.setText(transform(input, key))

    def saveFile(self):
        content = '''def getKey():
    return {\n'''

        key = self.generateKey()
        for i in key:
            tmp = '        \''+self.escape(i)+'\' : '
            tmp += '\''+key[i]+'\',\n'
            content += tmp

        content += '''    }'''

        write('src/key.py', content)

    def generateKey(self):
        key = dict()

        i = 0
        while i < self.model.rowCount():
            key[self.model.item(i, 0).text()] = self.model.item(i, 1).text()
            i += 1

        return key

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