import configparser
from PySide.QtCore import *
from PySide.QtGui import *
from key import *
from functions import *

class CryptWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(500, 350)
        self.setFont(QFont('Verdana')) 
        self.setWindowTitle('Crypt')
        
        self.loadConfig()

        self.textInput = QTextEdit(self)
        self.textOutput = QTextBrowser(self)

        layout = QHBoxLayout()
        layout.addWidget(self.textInput)
        layout.addWidget(self.textOutput)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.textInput.textChanged.connect(self.crypt)

    #load the config file
    def loadConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read('parameters.ini')

    #apply the transformation key
    def crypt(self):
        key = self.invertKey(getKey())
        self.textOutput.setText(transform(self.textInput.toPlainText(), key))

    #invert the key/value of the key
    def invertKey(self, key):
        return {v:k for k, v in key.items()}
