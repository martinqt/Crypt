import sys, os, csv, fileinput
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
        self.input = read(self.inputPath)
        self.keyPath = 'src/key.py'

        self.quit = QPushButton('Quit', self)
        self.quit.clicked.connect(quit)
        self.populateButton = QPushButton('Repopulate', self)
        self.populateButton.clicked.connect(self.populate)

        self.outputMode = QComboBox(self)
        self.outputMode.addItem('Count')
        self.outputMode.addItem('Frequency')
        self.outputMode.addItem('Percent')
        self.outputMode.currentIndexChanged.connect(self.changeOutputMode)

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
        hLayout.addWidget(self.outputMode)
        hLayout.addWidget(self.populateButton)
        layout.addLayout(hLayout)

        layout.addWidget(self.quit)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        header = QHeaderView(Qt.Horizontal)
        header.setResizeMode(QHeaderView.Stretch)
        self.keyEdit.setHorizontalHeader(header)
        
        self.model = QStandardItemModel(0, 3, self)
        self.applyHeader()
        self.keyEdit.setModel(self.model)

        self.dashboardLabel = QLabel(self)
        self.statusBar().insertPermanentWidget(0, self.dashboardLabel, 0);

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
        if self.headers[2] == 'Frequency':
            charCount = getCharCount(read(self.inputPath), 'frequency')
        elif self.headers[2] == 'Percent':
            charCount = getCharCount(read(self.inputPath), 'percent')
        else:
            charCount = getCharCount(read(self.inputPath))

        for i in key:
            if charCount[i] < 10:
                charCount[i] = '0'+str(charCount[i])
            index = self.model.rowCount()
            self.model.setItem(index, 0, QStandardItem(i))
            self.model.setItem(index, 1, QStandardItem(key[i]))
            self.model.setItem(index, 2, QStandardItem(str(charCount[i])))

        self.keyEdit.sortByColumn(2, Qt.DescendingOrder)
        self.model.itemChanged.connect(self.convert)
        self.convert()

    def clearModel(self):
        self.model.clear();
        self.applyHeader()

    def createMenu(self):
        self.saveAct = QAction(QIcon('src/images/save.png'), 'Save',
                self, shortcut=QKeySequence.Save,
                statusTip='Save the key', triggered=self.saveFile)

        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(self.saveAct)

        self.outputAct = QAction(QIcon('src/images/file.png'), 'TXT output',
                self, shortcut=QKeySequence(Qt.Key_F6),
                statusTip='Generate the text output file', triggered=self.generateOutputFile)
        self.htmlAct = QAction(QIcon('src/images/html.png'), 'HTML output',
                self, shortcut=QKeySequence(Qt.Key_F7),
                statusTip='Generate an HTML output file', triggered=self.generateHtmlFile)
        self.charactersAct = QAction(QIcon('src/images/file.png'), 'Characters statistics',
                self, shortcut=QKeySequence(Qt.Key_F8),
                statusTip='Generate a file with the characters statistics', triggered=self.generateCharactersFile)

        self.generateMenu = self.menuBar().addMenu('Generate')
        self.generateMenu.addAction(self.outputAct)
        self.generateMenu.addAction(self.htmlAct)
        self.generateMenu.addAction(self.charactersAct)

        self.wordAct = QAction(QIcon('src/images/dashboard.png'), 'Word analysis',
                self, shortcut=QKeySequence(Qt.Key_F10),
                statusTip='Perform the word analysis', triggered=self.doWordAnalysis)

        self.toolsMenu = self.menuBar().addMenu('Tools')
        self.toolsMenu.addAction(self.wordAct)

    def changeOutputMode(self):
        index = self.outputMode.currentIndex()

        if index == 0:
            self.headers[2] = 'Count'
        elif index == 1:
            self.headers[2] = 'Frequency'
        else:
            self.headers[2] = 'Percent'

        self.applyHeader()
        self.populate()

    def applyHeader(self):
        self.model.setHorizontalHeaderLabels(self.headers)

    def convert(self):
        self.saveFile()
        key = self.generateKey()

        self.output.setText(transform(self.input, key))
        self.statusBar().showMessage('Converted')

    def saveFile(self):
        replace = asort(self.generateKey(), False, True)
        content = '''def getKey():
     return {\n'''

        for key, value in replace:
            tmp = '          \''+self.escape(key)+'\' : '
            tmp += '\''+value+'\',\n'
            content += tmp

        content += '''     }'''

        write(self.keyPath, content)

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

    def doWordAnalysis(self):
        self.statusBar().showMessage('Analysing...')
        dictWords = self.loadWords()
        words = self.output.toPlainText().split(' ')
        score = total = 0

        for word in words:
            length = len(word)
            total += length
            if word in dictWords:
                score += length


        score = score/total*100

        if score < 34:
            path = 'src/images/dashboard_red.png'
        elif score < 67:
            path = 'src/images/dashboard_orange.png'
        else:
            path = 'src/images/dashboard_green.png'

        self.dashboardLabel.setPixmap(QPixmap(path))
        self.dashboardLabel.setScaledContents(False)
        self.dashboardLabel.setAlignment(Qt.AlignRight)

        self.statusBar().showMessage('Done')

    def loadWords(self):
        words = list()

        for line in fileinput.input(['src/dict/fr.txt']):
            words.append(line[:-1])

        return words

    def generateHtmlFile(self):
        writeHtmlFile()

    def generateOutputFile(self):
        write('output/output.txt', transform(read(self.inputPath), getKey()))

    def generateCharactersFile(self):
        writeCharCount(self.input, self.headers[2].lower())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
