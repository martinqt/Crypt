# -*-coding:Utf-8 -*

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
        self.buildUi()

    #build the ui
    def buildUi(self):
        self.tabs = QTabWidget(self)

        self.buildGeneralTab()

        self.saveButton = QPushButton('Save', self)

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        layout.addWidget(self.saveButton)
        self.setLayout(layout)

        self.saveButton.clicked.connect(self.saveConfig)

    #create the general tab
    def buildGeneralTab(self):
        self.generalTab = QWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.buildHtmlColorGroup())
        layout.addWidget(self.buildPathsGroup())

        self.generalTab.setLayout(layout)
        self.tabs.addTab(self.generalTab, 'General')

        self.inputPathFieldTool.clicked.connect(self.inputPathToolClicked)
        self.inputPathField.editingFinished.connect(self.inputPathEdited)

    #build the paths group of the general tab
    def buildPathsGroup(self):
        widget = QWidget(self)
        self.inputPathField = QLineEdit(self.config['PATHS']['input-path'], self)
        self.inputPathFieldTool = QToolButton(self)
        self.inputPathFieldTool.setIcon(QIcon(QPixmap('src/images/folder.png')))

        tmpLayout = QHBoxLayout()
        tmpLayout.setContentsMargins(0, 0, 0, 0)
        tmpLayout.addWidget(self.inputPathField)
        tmpLayout.addWidget(self.inputPathFieldTool)
        widget.setLayout(tmpLayout)
        
        formLayout = QFormLayout()
        formLayout.addRow('Input:', widget)

        group = QGroupBox('Paths', self)
        group.setLayout(formLayout)

        return group

    #build the html color group of the general tab
    def buildHtmlColorGroup(self):
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

        self.convertedToolButton.clicked.connect(self.convertedColorClicked)
        self.originalToolButton.clicked.connect(self.originalColorClicked)

        return group

    #update the config when the line edit content change
    def inputPathEdited(self):
        self.config['PATHS']['input-path'] = self.inputPathField.text()

    #show a dialog to help selecting the input
    def inputPathToolClicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Select input file', '', 'Text (*.txt)')[0]
        self.inputPathField.setText(filename)
        self.config['PATHS']['input-path'] = filename

    #change the converted color option
    def convertedColorClicked(self):
        pixmap = QPixmap(16, 16)
        color = QColorDialog.getColor(self.getColorFromString(self.config['HTML_COLORS']['converted']), self, 'Converted Color')
        if color != QColor():
            pixmap.fill(color)
            self.config['HTML_COLORS']['converted'] = self.getStringFromColor(color)
            self.convertedToolButton.setIcon(QIcon(pixmap))

    #change the original color option
    def originalColorClicked(self):
        pixmap = QPixmap(16, 16)
        color = QColorDialog.getColor(self.getColorFromString(self.config['HTML_COLORS']['original']), self, 'Original Color')
        if color != QColor():
            pixmap.fill(color)
            self.config['HTML_COLORS']['original'] = self.getStringFromColor(color)
            self.originalToolButton.setIcon(QIcon(pixmap))

    #load the config file
    def loadConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read('parameters.ini')

    #convert a string to a color object
    def getColorFromString(self, string):
        return QColor(int(string[:3]), int(string[3:6]), int(string[6:9]))

    #get a string from a color object
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

    #save the config file
    def saveConfig(self):
        configFile = open('parameters.ini', 'w')
        self.config.write(configFile)
        configFile.close()
