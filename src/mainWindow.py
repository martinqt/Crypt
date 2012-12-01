import sys, os
sys.path.insert(0, os.getcwd()+'/src/functions')
from PySide.QtCore import *
from PySide.QtGui import *
from key import *
from file import *
from functions import *
from parameters import *
from cryptWindow import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        
        self.resize(700, 500)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Crypt')
        
        self.loadConfig()

        self.headers = ['From', 'To', 'Count']
        self.inputPath = self.config['PATHS']['input-path']
        self.input = read(self.inputPath)
        self.keyPath = self.config['PATHS']['key-path']

        self.options = Parameters()
        self.crypt = CryptWindow()

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

    #reload the stored input
    def reloadInput(self):
        self.input = read(self.inputPath)

    #populate the key table view
    def populate(self):
        try:
            self.model.itemChanged.disconnect(self.convert)
        except RuntimeError:
            pass
        
        self.clearModel()
        key = getKey()
        if self.headers[2] == 'Frequency':
            charCount = getCharCount(self.input, 'frequency')
        elif self.headers[2] == 'Percent':
            charCount = getCharCount(self.input, 'percent')
        else:
            charCount = getCharCount(self.input)

        for i in key:
            if i in charCount:
                if charCount[i] < 10:
                    charCount[i] = '0'+str(charCount[i])
            else:
                charCount[i] = '00'

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
        self.cryptAct = QAction(QIcon('src/images/lock.png'), 'Crypt',
                self, shortcut=QKeySequence(Qt.Key_C),
                statusTip='Crypt a message with the curent key', triggered=self.showCryptWindow)

        self.fileMenu = self.menuBar().addMenu('File')
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.cryptAct)

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

        self.configAct = QAction(QIcon('src/images/reload.png'), 'Reload configuration',
                self, shortcut=QKeySequence(Qt.Key_F5),
                statusTip='Reload the configuration', triggered=self.loadConfig)
        self.inputAct = QAction(QIcon('src/images/reload.png'), 'Reload input',
                self, shortcut=QKeySequence(Qt.Key_F9),
                statusTip='Reload the input file', triggered=self.reloadInput)
        self.wordAct = QAction(QIcon('src/images/dashboard.png'), 'Word analysis',
                self, shortcut=QKeySequence(Qt.Key_F10),
                statusTip='Perform the word analysis', triggered=self.doWordAnalysis)
        self.optionAct = QAction(QIcon('src/images/options.png'), 'Options',
                self, shortcut=QKeySequence(Qt.Key_F11),
                statusTip='Change the options', triggered=self.showOptions)

        self.toolsMenu = self.menuBar().addMenu('Tools')
        self.toolsMenu.addAction(self.configAct)
        self.toolsMenu.addAction(self.inputAct)
        self.toolsMenu.addAction(self.wordAct)
        self.toolsMenu.addAction(self.optionAct)

        self.rowAct = QAction(QIcon('src/images/add.png'), 'Add row',
                self, shortcut=QKeySequence(Qt.Key_A),
                statusTip='Add a row at the end of the table', triggered=self.addRow)
        self.updateKeyAct = QAction(QIcon('src/images/reload.png'), 'Update key',
                self, shortcut=QKeySequence(Qt.Key_U),
                statusTip='Update the key with the current input', triggered=self.updateKey)

        self.keyMenu = self.menuBar().addMenu('Key')
        self.keyMenu.addAction(self.rowAct)
        self.keyMenu.addAction(self.updateKeyAct)

    #change the output mode by handling the combo box
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

    #update the table header
    def applyHeader(self):
        self.model.setHorizontalHeaderLabels(self.headers)

    #apply the replacement key and display the output
    def convert(self):
        self.saveFile()
        key = self.generateKey()

        self.output.setText(transform(self.input, self.htmlFormatDict(key)))
        self.statusBar().showMessage('Converted')

    #write the key to a python file
    def saveFile(self):
        replace = asort(self.generateKey(), False, True)
        content = '''def getKey():
    return {\n'''

        for key, value in replace:
            tmp = '          \''+self.escape(key)+'\' : '
            tmp += '\''+self.escape(value)+'\',\n'
            content += tmp

        content += '''     }'''

        write(self.keyPath, content)

    #generate the key from the table
    def generateKey(self):
        key = dict()

        i = 0
        while i < self.model.rowCount():
            try:
                keyStr = self.model.item(i, 0).text()
            except AttributeError:
                keyStr = ''
            try:
                valueStr = self.model.item(i, 1).text()
            except AttributeError:
                valueStr = ''

            key[keyStr] = valueStr

            i += 1

        return key

    #escape the ` character for the key file
    def escape(self, string):
        if string == '\'':
            return '\\'+string
        else:
            return string

    #handle the word analysis process
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

        self.dashboardLabel.setToolTip(str(round(score, 1))+'%')
        self.dashboardLabel.setPixmap(QPixmap(path).scaled(20, 20, Qt.KeepAspectRatio))
        self.dashboardLabel.setScaledContents(False)
        self.dashboardLabel.setAlignment(Qt.AlignRight)

        self.statusBar().showMessage('Done')

    #load the word dictionnary
    def loadWords(self):
        words = list()

        for line in fileinput.input(['src/dict/fr.txt']):
            words.append(line[:-1])

        return words

    #generate and write the html output file
    def generateHtmlFile(self):
        replaceDict = self.generateKey()

        htmlResult = self.input+'<hr/>'
        htmlResult += transform(self.input, htmlFormatDict(replaceDict))

        write('output/output.html', htmlResult)

    #write the txt output file
    def generateOutputFile(self):
        write('output/output.txt', transform(self.input, getKey()))

    #write the char analysis
    def generateCharactersFile(self):
        writeCharCount(self.input, self.headers[2].lower())

    #display the option window
    def showOptions(self):
        self.options.show()

    #load the config file
    def loadConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read('parameters.ini')

    #prepare the replacement key fro html display
    def htmlFormatDict(self, dict):
        for i in dict:
            if dict[i] == '-' or dict[i] == '':
                if i == ' ':
                    dict[i] = '<span style="color: '+self.toRgb(self.config['HTML_COLORS']['original'])+';">-</span>'
                else:
                    dict[i] = '<span style="color: '+self.toRgb(self.config['HTML_COLORS']['original'])+';">'+i+'</span>'
            else:
                dict[i] = '<span style="color: '+self.toRgb(self.config['HTML_COLORS']['converted'])+';">'+dict[i]+'</span>'

        return dict

    #transform a color string into a css compliant rgb format
    def toRgb(self, string):
        return 'rgb('+string[:3]+', '+string[3:6]+', '+string[6:9]+')'

    #add a row at the end of the table view
    def addRow(self, char = ''):
        self.model.insertRow(self.model.rowCount(), QStandardItem(char))

    def showCryptWindow(self):
        self.crypt.show()

    def updateKey(self):
        charList = getCharList(self.input)
        curentChars = list()
        i = 0
        rowCount = self.model.rowCount()

        while i < rowCount:
            curentChars.append(self.model.item(i).text())
            i += 1

        diffs = list(set(charList) - set(curentChars))

        for diff in diffs:
            self.addRow(diff)
